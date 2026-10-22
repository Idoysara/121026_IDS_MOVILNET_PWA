"""
services/cazador_ofertas/src/domain/zones.py — Catálogo Canónico de Zonas y Polígonos de Cobertura
================================================================================================
Define los sectores y centroides comerciales para el Modelo Espacial de Cero Fricción (Escenario 1).
El comerciante selecciona su sector y el sistema fija los límites y centroide automáticamente,
sin exigirle ingresar ningún radio en metros ni coordenadas técnicas.
"""
from typing import Dict, Any, List, Optional, Tuple
import unicodedata

def normalizar_texto(texto: str) -> str:
    """Normaliza texto eliminando acentos y convirtiendo a minúsculas para comparaciones robustas."""
    if not texto:
        return ""
    nfkd = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in nfkd if not unicodedata.combining(c)).lower().strip()

# Catálogo oficial de Zonas Urbanas Canónicas (Caracas + Referencia Internacional DOOH)
CANONICAL_ZONES: Dict[str, Dict[str, Any]] = {
    "las mercedes": {
        "slug": "las-mercedes",
        "nombre": "Las Mercedes",
        "municipio": "Baruta",
        "ciudad": "Caracas",
        "centroide": {"lat": 10.4794, "lon": -66.8569},
        "radio_zona_m": 1500.0,
        "descripcion": "Zona comercial, gastronómica y financiera Las Mercedes",
        "tags": ["mercedes", "tolon", "jalisco", "rio de janeiro"]
    },
    "chacao": {
        "slug": "chacao",
        "nombre": "Chacao",
        "municipio": "Chacao",
        "ciudad": "Caracas",
        "centroide": {"lat": 10.4925, "lon": -66.8550},
        "radio_zona_m": 1200.0,
        "descripcion": "Casco histórico y eje comercial Avenida Francisco de Miranda",
        "tags": ["chacao", "plaza el indio", "san ignacio", "mercado de chacao"]
    },
    "altamira": {
        "slug": "altamira",
        "nombre": "Altamira",
        "municipio": "Chacao",
        "ciudad": "Caracas",
        "centroide": {"lat": 10.4965, "lon": -66.8490},
        "radio_zona_m": 1200.0,
        "descripcion": "Plaza Francia, Sur y Norte de Altamira",
        "tags": ["altamira", "plaza francia", "luis roche", "san juan bosco"]
    },
    "los palos grandes": {
        "slug": "los-palos-grandes",
        "nombre": "Los Palos Grandes",
        "municipio": "Chacao",
        "ciudad": "Caracas",
        "centroide": {"lat": 10.4985, "lon": -66.8415},
        "radio_zona_m": 1100.0,
        "descripcion": "Distrito gastronómico, cultural y residencial Los Palos Grandes",
        "tags": ["palos grandes", "parque cristal", "cuadra gastronomica"]
    },
    "sabana grande": {
        "slug": "sabana-grande",
        "nombre": "Sabana Grande",
        "municipio": "Libertador",
        "ciudad": "Caracas",
        "centroide": {"lat": 10.4930, "lon": -66.8770},
        "radio_zona_m": 1200.0,
        "descripcion": "Bulevar peatonal de Sabana Grande y centros comerciales adyacentes",
        "tags": ["sabana grande", "bulevar", "city market", "el recreo", "chacaito"]
    },
    "la candelaria": {
        "slug": "la-candelaria",
        "nombre": "La Candelaria",
        "municipio": "Libertador",
        "ciudad": "Caracas",
        "centroide": {"lat": 10.5050, "lon": -66.9070},
        "radio_zona_m": 1200.0,
        "descripcion": "Sector comercial tradicional y epicentro gastronómico La Candelaria",
        "tags": ["candelaria", "plaza candelaria", "sambil candelaria", "urdaneta"]
    },
    "el rosal": {
        "slug": "el-rosal",
        "nombre": "El Rosal",
        "municipio": "Chacao",
        "ciudad": "Caracas",
        "centroide": {"lat": 10.4880, "lon": -66.8650},
        "radio_zona_m": 1000.0,
        "descripcion": "Distrito corporativo y financiero El Rosal",
        "tags": ["rosal", "tamanaco", "torre bnc", "avenida venezuela"]
    },
    "plaza venezuela": {
        "slug": "plaza-venezuela",
        "nombre": "Plaza Venezuela",
        "municipio": "Libertador",
        "ciudad": "Caracas",
        "centroide": {"lat": 10.4965, "lon": -66.8858},
        "radio_zona_m": 1200.0,
        "descripcion": "Nodo neurálgico metropolitano y comercial Plaza Venezuela",
        "tags": ["plaza venezuela", "previsora", "sabana grande oeste", "ucv"]
    },
    "colinas de bello monte": {
        "slug": "bello-monte",
        "nombre": "Colinas de Bello Monte",
        "municipio": "Baruta",
        "ciudad": "Caracas",
        "centroide": {"lat": 10.4820, "lon": -66.8750},
        "radio_zona_m": 1200.0,
        "descripcion": "Eje comercial y residencial Bello Monte",
        "tags": ["bello monte", "ciudad banesco", "avenida principal bello monte"]
    },
    "brickell": {
        "slug": "brickell",
        "nombre": "Brickell (Miami)",
        "municipio": "Miami-Dade",
        "ciudad": "Miami",
        "centroide": {"lat": 25.7617, "lon": -80.1918},
        "radio_zona_m": 1500.0,
        "descripcion": "Distrito financiero internacional Brickell (DOOH Multi-Región)",
        "tags": ["brickell", "brickell city centre", "biscayne"]
    }
}

def resolver_zona(nombre_o_consulta: str) -> Optional[Dict[str, Any]]:
    """
    Busca y resuelve una zona canónica por nombre exacto, alias o coincidencia en tags.
    Retorna la metadata de la zona (centroide, radio_zona_m, municipio, etc.) o None.
    """
    if not nombre_o_consulta:
        return None
    query_norm = normalizar_texto(nombre_o_consulta)
    
    # 1. Búsqueda directa por clave normalizada
    if query_norm in CANONICAL_ZONES:
        return CANONICAL_ZONES[query_norm]
    
    # 2. Búsqueda por coincidencia de subcadena o tags
    for key, data in CANONICAL_ZONES.items():
        if query_norm in key or key in query_norm:
            return data
        for tag in data.get("tags", []):
            tag_norm = normalizar_texto(tag)
            if tag_norm in query_norm or query_norm in tag_norm:
                return data
    
    return None

def listar_zonas_disponibles() -> List[Dict[str, Any]]:
    """Retorna la lista de todas las zonas disponibles para selectores UI de Cero Fricción."""
    zonas = []
    for key, data in CANONICAL_ZONES.items():
        zonas.append({
            "key": key,
            "slug": data["slug"],
            "nombre": data["nombre"],
            "ciudad": data["ciudad"],
            "municipio": data["municipio"],
            "radio_sugerido_m": data["radio_zona_m"],
            "descripcion": data["descripcion"]
        })
    return sorted(zonas, key=lambda z: z["nombre"])
