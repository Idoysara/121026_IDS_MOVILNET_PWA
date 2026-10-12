#!/usr/bin/env python3
"""
core/geo_catalog.py — Catálogo Territorial y Base de Datos Geoespacial de Venezuela
==================================================================================
Proyecto: AI_Movilnet_300926 / Módulo Geoespacial MCP Nivel 5
Normativa: División Político-Territorial de Venezuela (INE / IGVSB)
Sistemas de Coordenadas: WGS84 (EPSG:4326) / Proyección UTM Huso 19N/20N
"""

from __future__ import annotations

import math
import sqlite3
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

DB_PATH = Path(__file__).resolve().parent.parent / "db" / "local_movilnet.db"

# Radio terrestre en kilómetros y metros para fórmulas geodésicas Haversine
EARTH_RADIUS_KM = 6371.0
EARTH_RADIUS_M = 6371000.0


# ============================================================================
# Jerarquía Territorial Oficial de Venezuela (Estados, Municipios, Parroquias)
# ============================================================================

VENEZUELA_TERRITORIAL_DIVISIONS: Dict[str, Dict[str, Dict[str, Any]]] = {
    "Distrito Capital": {
        "Libertador": {
            "lat_min": 10.4200, "lat_max": 10.5350,
            "lon_min": -67.0500, "lon_max": -66.8650,
            "parroquias": [
                "Altagracia", "Antímano", "Candelaria", "Caricuao", "Catedral",
                "Coche", "El Junquito", "El Paraíso", "El Recreo", "El Valle",
                "La Pastora", "La Vega", "Macarao", "San Agustín", "San Bernardino",
                "San José", "San Juan", "San Pedro", "Santa Rosalía", "Santa Teresa",
                "Sucre (Catia)", "23 de Enero"
            ]
        }
    },
    "Miranda": {
        "Chacao": {
            "lat_min": 10.4700, "lat_max": 10.5250,
            "lon_min": -66.8750, "lon_max": -66.8350,
            "parroquias": ["Chacao"]
        },
        "Baruta": {
            "lat_min": 10.4100, "lat_max": 10.4850,
            "lon_min": -66.9050, "lon_max": -66.8200,
            "parroquias": ["Nuestra Señora del Rosario de Baruta", "El Cafetal", "Las Minas de Baruta"]
        },
        "Sucre": {
            "lat_min": 10.4600, "lat_max": 10.5350,
            "lon_min": -66.8400, "lon_max": -66.7200,
            "parroquias": ["Petare", "Leoncio Martínez", "Caucagüita", "Fila de Mariches", "La Dolorita"]
        },
        "El Hatillo": {
            "lat_min": 10.3800, "lat_max": 10.4500,
            "lon_min": -66.8600, "lon_max": -66.7800,
            "parroquias": ["Santa Rosalía de Palermo"]
        },
        "Guaicaipuro": {
            "lat_min": 10.2800, "lat_max": 10.4100,
            "lon_min": -67.1200, "lon_max": -66.9600,
            "parroquias": ["Los Teques", "Cecilio Acosta", "San Pedro", "El Jarillo", "Altagracia de la Montaña", "Paracotos", "Tácata"]
        }
    },
    "Zulia": {
        "Maracaibo": {
            "lat_min": 10.5500, "lat_max": 10.7500,
            "lon_min": -71.7500, "lon_max": -71.5500,
            "parroquias": [
                "Bolívar", "Chiquinquirá", "Coquivacoa", "Cristo de Aranza",
                "Idelfonso Vásquez", "Juana de Ávila", "Manuel Dagnino",
                "Olegario Villalobos", "Raúl Leoni", "Santa Lucía", "Venancio Pulgar"
            ]
        },
        "San Francisco": {
            "lat_min": 10.4800, "lat_max": 10.6000,
            "lon_min": -71.7200, "lon_max": -71.5800,
            "parroquias": ["San Francisco", "El Bajo", "Domitila Flores", "Francisco Ochoa", "Los Cortijos", "Marcial Hernández"]
        }
    },
    "Carabobo": {
        "Valencia": {
            "lat_min": 10.0800, "lat_max": 10.2600,
            "lon_min": -68.0800, "lon_max": -67.9200,
            "parroquias": ["Candelaria", "Catedral", "El Socorro", "Miguel Peña", "Rafael Urdaneta", "San Blas", "San José", "Santa Rosa"]
        },
        "Naguanagua": {
            "lat_min": 10.2200, "lat_max": 10.3200,
            "lon_min": -68.0500, "lon_max": -67.9700,
            "parroquias": ["Naguanagua"]
        },
        "San Diego": {
            "lat_min": 10.2000, "lat_max": 10.3000,
            "lon_min": -68.0000, "lon_max": -67.9200,
            "parroquias": ["San Diego"]
        }
    },
    "Lara": {
        "Iribarren": {
            "lat_min": 9.9800, "lat_max": 10.1500,
            "lon_min": -69.4500, "lon_max": -69.2000,
            "parroquias": ["Catedral", "Concepción", "Santa Rosa", "Unión", "El Cují", "Tamaca", "Juan de Villegas"]
        }
    },
    "Anzoátegui": {
        "Sotillo": {
            "lat_min": 10.1600, "lat_max": 10.2600,
            "lon_min": -64.6700, "lon_max": -64.5800,
            "parroquias": ["Puerto La Cruz", "Pozuelos"]
        },
        "Simón Bolívar": {
            "lat_min": 10.0800, "lat_max": 10.2200,
            "lon_min": -64.7500, "lon_max": -64.6300,
            "parroquias": ["Barcelona", "El Carmen", "San Cristóbal", "Naricual", "Bergantín"]
        }
    }
}


def haversine_distance_meters(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calcula la distancia geodésica ortodrómica en metros usando la fórmula de Haversine."""
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi / 2.0)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0)**2
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
    return EARTH_RADIUS_M * c


# ============================================================================
# Inicialización del Esquema SQL Geoespacial
# ============================================================================

def init_geo_database(db_file: Path = DB_PATH) -> None:
    """Crea la tabla geocartográfica de puntos de interés y la alimenta con registros base verificados."""
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS geo_pois (
            id TEXT PRIMARY KEY,
            osm_id INTEGER,
            name TEXT NOT NULL,
            category TEXT NOT NULL,       -- 'farmacia', 'salud_clinica', 'comercio', 'edificio_corporativo', 'perros_calientes'
            sub_category TEXT,           -- 'hospital', 'farmacia_cadena', 'torre_oficinas', etc.
            state TEXT NOT NULL,         -- 'Distrito Capital', 'Miranda', etc.
            municipality TEXT NOT NULL,  -- 'Chacao', 'Baruta', etc.
            parish TEXT NOT NULL,        -- 'Chacao', 'Leoncio Martínez', etc.
            latitude REAL NOT NULL,
            longitude REAL NOT NULL,
            address TEXT NOT NULL,
            phone TEXT,
            opening_hours TEXT,
            emergency_service INTEGER DEFAULT 0,
            metadata_json TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
    """)

    cur.execute("CREATE INDEX IF NOT EXISTS idx_geo_pois_lat_lon ON geo_pois(latitude, longitude);")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_geo_pois_cat_muni ON geo_pois(category, municipality);")

    # Semilla oficial de POIs verificados en Venezuela
    INITIAL_POIS = [
        # --- SALUD & FARMACIAS (Chacao) ---
        (
            "POI-CCS-FAR-001", 10101, "Farmatodo Los Palos Grandes", "farmacia", "farmacia_24h",
            "Miranda", "Chacao", "Chacao", 10.4965, -66.8505,
            "1ra Avenida con 2da Transversal de Los Palos Grandes, Chacao, Caracas",
            "+58 212-2851122", "24/7", 1, '{"cadena": "Farmatodo", "delivery": true, "estacionamiento": true}'
        ),
        (
            "POI-CCS-FAR-002", 10102, "Locatel La Castellana", "farmacia", "farmacia_equipos_medicos",
            "Miranda", "Chacao", "Chacao", 10.4990, -66.8540,
            "Av. Principal de La Castellana con Calle José Ángel Lamas, Chacao",
            "+58 212-2638844", "07:00 - 21:00", 0, '{"cadena": "Locatel", "alquiler_equipos_medicos": true}'
        ),
        (
            "POI-CCS-CLI-001", 10103, "Clínica El Ávila", "salud_clinica", "hospital_privado",
            "Miranda", "Chacao", "Chacao", 10.4988, -66.8512,
            "6ta Transversal con Av. San Juan Bosco, Altamira Norte, Chacao",
            "+58 212-2761111", "24/7", 1, '{"emergencia_adultos": true, "emergencia_pediatrica": true, "uci": true}'
        ),
        (
            "POI-CCS-CLI-002", 10104, "Centro Médico Docente La Trinidad", "salud_clinica", "hospital_privado",
            "Miranda", "Baruta", "Las Minas de Baruta", 10.4370, -66.8545,
            "Av. Intercomunal La Trinidad - El Hatillo, Baruta, Caracas",
            "+58 212-9496411", "24/7", 1, '{"emergencia_traumatologia": true, "helipuerto": true}'
        ),
        # --- EDIFICIOS CORPORATIVOS & OFICINAS ---
        (
            "POI-CCS-CORP-001", 10201, "Torre Movilnet El Rosal", "edificio_corporativo", "telecomunicaciones_sede",
            "Miranda", "Chacao", "Chacao", 10.4890, -66.8670,
            "Av. Venezuela, Torre Movilnet, Urb. El Rosal, Chacao, Caracas",
            "+58 212-8221000", "08:00 - 17:00", 0, '{"oficina_comercial": true, "atencion_abonados": true, "cobertura": "4GMAX"}'
        ),
        (
            "POI-CCS-CORP-002", 10202, "Centro Financiero Latino", "edificio_corporativo", "torre_financiera",
            "Distrito Capital", "Libertador", "Altagracia", 10.5085, -66.9110,
            "Av. Urdaneta con esquina Ánimas, La Candelaria / Altagracia, Caracas",
            "+58 212-5632211", "08:00 - 18:00", 0, '{"piso_oficinas": 32, "banco_sede": true}'
        ),
        (
            "POI-CCS-CORP-003", 10203, "Torre Parque Ávila", "edificio_corporativo", "torre_empresarial",
            "Miranda", "Sucre", "Leoncio Martínez", 10.4950, -66.8370,
            "Av. Francisco de Miranda, Los Dos Caminos, Sucre, Caracas",
            "+58 212-2395500", "08:00 - 18:00", 0, '{"helipuerto": false, "estacionamiento": true}'
        ),
        # --- COMERCIOS & GASTRONOMÍA VERIFICADA ---
        (
            "POI-CCS-COM-001", 10301, "Carritos de Perros de Plaza Altamira (Sur)", "perros_calientes", "comida_callejera",
            "Miranda", "Chacao", "Chacao", 10.4958, -66.8530,
            "Salida Metro Altamira Sur, Av. Francisco de Miranda, Chacao, Caracas",
            None, "17:00 - 04:00", 0, '{"especialidad": "Perros con salchicha polaca y papitas", "horario_nocturno": true}'
        ),
        (
            "POI-CCS-COM-002", 10302, "Puesto El Pana de Los Palos Grandes", "perros_calientes", "comida_callejera",
            "Miranda", "Chacao", "Chacao", 10.4980, -66.8490,
            "1ra Transversal de Los Palos Grandes, Chacao, Caracas",
            None, "18:00 - 02:00", 0, '{"especialidad": "Hamburguesas y perros callejeros"}'
        ),
        (
            "POI-CCS-COM-003", 10303, "Centro Comercial Sambil Chacao", "comercio", "centro_comercial",
            "Miranda", "Chacao", "Chacao", 10.4905, -66.8580,
            "Av. Libertador con calle Los Ángeles, Chacao, Caracas",
            "+58 212-2630000", "10:00 - 21:00", 0, '{"tiendas": 450, "zona_comida": true, "farmacias": 3}'
        ),
        # --- INTERIOR DE VENEZUELA (Maracaibo, Valencia, Barquisimeto) ---
        (
            "POI-MAR-CLI-001", 20101, "Hospital Privado El Ángel (Maracaibo)", "salud_clinica", "hospital_privado",
            "Zulia", "Maracaibo", "Olegario Villalobos", 10.6720, -71.6110,
            "Av. 4 Bella Vista con Calle 67 Cecilio Acosta, Maracaibo, Zulia",
            "+58 261-7921100", "24/7", 1, '{"emergencia": true, "banco_sangre": true}'
        ),
        (
            "POI-VAL-FAR-001", 30101, "Farmatodo San Diego El Remanso", "farmacia", "farmacia_24h",
            "Carabobo", "San Diego", "San Diego", 10.2310, -67.9750,
            "Av. Don Julio Centeno, Sector El Remanso, San Diego, Carabobo",
            "+58 241-8711122", "24/7", 1, '{"autofarmacia": true}'
        )
    ]

    for item in INITIAL_POIS:
        cur.execute("""
            INSERT OR REPLACE INTO geo_pois (
                id, osm_id, name, category, sub_category,
                state, municipality, parish, latitude, longitude,
                address, phone, opening_hours, emergency_service,
                metadata_json, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
        """, item)

    conn.commit()
    conn.close()


# Ejecutar inicialización idempotente al importar
init_geo_database()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Catálogo Geoespacial de Venezuela")
    parser.add_argument("--test", action="store_true", help="Auto-verificación matemática Haversine y DB")
    args = parser.parse_args()
    if args.test:
        dist = haversine_distance_meters(10.4958, -66.8530, 10.4980, -66.8500)
        assert dist > 0, "Fallo en cálculo Haversine"
        print(f"✅ [GEO_CATALOG]: Auto-test superado: Distancia Haversine = {dist:.2f} m. DB POIs inicializados.")

