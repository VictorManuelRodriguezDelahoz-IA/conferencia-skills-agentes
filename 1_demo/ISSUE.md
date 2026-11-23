# Issue #1 · `parse_limit` acepta valores fuera del contrato

**Contexto:** helper ficticio de paginación que una API podría usar. No es un endpoint real.

**Comportamiento actual:** `parse_limit('0')` devuelve `0` y `parse_limit('101')` devuelve `101`.

**Contrato esperado para `limit`:**

| Entrada | Resultado |
| --- | --- |
| `None` | `20` (valor por defecto) |
| `'1'` … `'100'` | el entero correspondiente |
| `'0'`, `'101'`, otro número fuera de rango | `ValueError` |
| `'abc'` (texto no numérico) | `ValueError` |

**Fuera de alcance:**
- No cambiar la interfaz (`parse_limit(value)` sigue igual).
- No implementar respuestas HTTP.
- No tocar `parse_page` (tiene su propio issue).

**Cómo comprobarlo:** `python -m unittest -v`
