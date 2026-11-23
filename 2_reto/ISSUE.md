# Issue #2 · Validar el número de página

**Punto de partida:** `parse_limit` ya está corregido; `parse_page` sigue como el original.

**Contrato esperado para `page`:**

| Entrada | Resultado |
| --- | --- |
| `None` | `1` (valor por defecto) |
| `'1'` | `1` |
| `'5'` | `5` |
| `'0'` | `ValueError` |
| `'-1'` | `ValueError` |
| `'abc'` | `ValueError` |

No hay máximo: se aceptan enteros desde 1 en adelante.

**Fuera de alcance:**
- No cambiar la interfaz (`parse_page(value)` sigue igual).
- No definir respuestas HTTP.
- No romper los tests de `limit`.

## Pasos · 23 minutos

1. **Leer y planear · 3 min.** Anoten entradas y resultados (tabla de arriba).
2. **Adaptar la skill · 5 min.** En `.claude/skills/revisar-pr/SKILL.md`, añadan una
   instrucción para revisar límites de paginación y señalar evidencia por archivo.
3. **Pedir ayuda al agente · 10 min.** Añadan los tests de página en `test_pagination.py`,
   pidan un plan, autoricen el cambio acotado y ejecuten `python -m unittest -v`.
4. **Revisar · 3 min.** Diff, nuevos tests y que sigan pasando los de `limit`.
5. **Compartir · 2 min.** Una mejora de la skill, un caso borde y lo que realmente ocurrió.

**Entrega por pareja:** skill adaptada, tests, cambio propuesto y resultados reales.
Sin agente o terminal: el plan y los tests esperados, indicando que no se ejecutaron.
