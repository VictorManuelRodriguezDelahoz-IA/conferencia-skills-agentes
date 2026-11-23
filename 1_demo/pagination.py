"""Helpers de paginación (ficticios) que una API podría usar."""


def parse_limit(value):
    if value is None:
        return 20
    return int(value)


def parse_page(value):
    if value is None:
        return 1
    return int(value)
