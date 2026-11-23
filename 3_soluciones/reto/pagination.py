"""Solución del reto: parse_limit (demo) + parse_page validado."""

MIN_LIMIT = 1
MAX_LIMIT = 100
DEFAULT_LIMIT = 20

MIN_PAGE = 1
DEFAULT_PAGE = 1


def parse_limit(value):
    if value is None:
        return DEFAULT_LIMIT
    limit = int(value)
    if not MIN_LIMIT <= limit <= MAX_LIMIT:
        raise ValueError(f"limit debe estar entre {MIN_LIMIT} y {MAX_LIMIT}; se recibió {limit}")
    return limit


def parse_page(value):
    if value is None:
        return DEFAULT_PAGE
    page = int(value)
    if page < MIN_PAGE:
        raise ValueError(f"page debe ser {MIN_PAGE} o mayor; se recibió {page}")
    return page
