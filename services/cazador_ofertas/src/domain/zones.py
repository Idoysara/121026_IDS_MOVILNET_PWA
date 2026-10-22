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
    "caracas": {
        "slug": "caracas-metropolitana",
        "nombre": "Caracas (Área Metropolitana)",
        "municipio": "Metropolitano",
        "ciudad": "Caracas",
        "centroide": {"lat": 10.4910, "lon": -66.8650},
        "radio_zona_m": 4500.0,
        "descripcion": "Valle de Caracas y ejes comerciales de la Gran Caracas",
        "tags": ["caracas", "ccs", "distrito capital", "gran caracas"]
    },
    # CIUDADES PILOTO NACIONALES
    "maracay": {
        "slug": "maracay-centro-delicias",
        "nombre": "Maracay (Las Delicias / Centro)",
        "municipio": "Girardot",
        "ciudad": "Maracay",
        "centroide": {"lat": 10.2550, "lon": -67.5920},
        "radio_zona_m": 3500.0,
        "descripcion": "Eje comercial Las Delicias, Centro y Parque Los Aviadores",
        "tags": ["maracay", "aragua", "las delicias", "los aviadores", "san jacinto", "el limon"]
    },
    "valencia": {
        "slug": "valencia-vinedo-naguanagua",
        "nombre": "Valencia (El Viñedo / Sambil)",
        "municipio": "Valencia",
        "ciudad": "Valencia",
        "centroide": {"lat": 10.2300, "lon": -68.0080},
        "radio_zona_m": 4000.0,
        "descripcion": "Eje gastronómico El Viñedo, Naguanagua, Sambil y Metrópolis",
        "tags": ["valencia", "carabobo", "el vinedo", "naguanagua", "sambil valencia", "san diego", "metropolis valencia"]
    },
    "la guaira": {
        "slug": "la-guaira-caribe-catia",
        "nombre": "La Guaira (Caribe / Catia La Mar)",
        "municipio": "Vargas",
        "ciudad": "La Guaira",
        "centroide": {"lat": 10.6050, "lon": -66.9500},
        "radio_zona_m": 5000.0,
        "descripcion": "Litoral central, Catia La Mar, Maiquetía, Macuto y Caribe",
        "tags": ["la guaira", "vargas", "litoral", "caribe", "catia la mar", "maiquetia", "macuto", "playa grande"]
    },
    "barquisimeto": {
        "slug": "barquisimeto-este-sambil",
        "nombre": "Barquisimeto (Zona Este / Sambil)",
        "municipio": "Iribarren",
        "ciudad": "Barquisimeto",
        "centroide": {"lat": 10.0710, "lon": -69.3050},
        "radio_zona_m": 4000.0,
        "descripcion": "Epicentro comercial Este, Sambil Barquisimeto, Av. Lara y Cabudare",
        "tags": ["barquisimeto", "lara", "sambil barquisimeto", "cabudare", "nueva segovia", "zona este"]
    },
    "maracaibo": {
        "slug": "maracaibo-5dejulio-lago",
        "nombre": "Maracaibo (5 de Julio / Lago Mall)",
        "municipio": "Maracaibo",
        "ciudad": "Maracaibo",
        "centroide": {"lat": 10.6650, "lon": -71.6100},
        "radio_zona_m": 4500.0,
        "descripcion": "Corredor 5 de Julio, Bella Vista, El Milagro, Lago Mall y Sambil Maracaibo",
        "tags": ["maracaibo", "zulia", "5 de julio", "bella vista", "lago mall", "sambil maracaibo", "el milagro"]
    },
    "lecheria": {
        "slug": "lecheria-plaza-mayor",
        "nombre": "Lechería (Plaza Mayor / Playa Mansa)",
        "municipio": "Diego Bautista Urbaneja",
        "ciudad": "Lechería",
        "centroide": {"lat": 10.1940, "lon": -64.6950},
        "radio_zona_m": 3000.0,
        "descripcion": "Bulevar costero, Plaza Mayor, Playa Mansa y Av. Principal de Lechería",
        "tags": ["lecheria", "anzoategui", "plaza mayor", "playa mansa", "puerto la cruz", "morro", "barcelona anzoategui"]
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
