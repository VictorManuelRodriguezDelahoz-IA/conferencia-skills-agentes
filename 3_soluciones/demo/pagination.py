"""Solución de la demo: solo cambia parse_limit; la interfaz se mantiene."""

MIN_LIMIT = 1
MAX_LIMIT = 100
DEFAULT_LIMIT = 20


def parse_limit(value):
    if value is None:
        return DEFAULT_LIMIT
    limit = int(value)  # 'abc' ya lanza ValueError aquí
    if not MIN_LIMIT <= limit <= MAX_LIMIT:
        raise ValueError(f"limit debe estar entre {MIN_LIMIT} y {MAX_LIMIT}; se recibió {limit}")
    return limit


def parse_page(value):  # sin cambios: está fuera del alcance del issue #1
    if value is None:
        return 1
    return int(value)
