# Skills y agentes para mejorar el desarrollo

Material de práctica de la conferencia: **de un issue a un cambio de código que podemos probar y revisar.**

Todo es ficticio y usa solo Python y su biblioteca estándar: no hay nada que instalar.

## Estructura

```
conferencia-skills-agentes/
├── 1_demo/                      Parte 2 · Demostración (15–27 min)
│   ├── ISSUE.md                 Issue de limit (1–100, default 20)
│   ├── pagination.py            Código inicial con el bug
│   ├── test_pagination.py       Tests: fallan 0 y 101
│   ├── PROMPT_AGENTE.md         Encargo para el agente (Caso 2)
│   └── .claude/skills/revisar-pr/SKILL.md   Skill de revisión (Caso 1)
├── 2_reto/                      Parte 3 · Reto por parejas (27–50 min)
│   ├── ISSUE.md                 Issue de page (>= 1, default 1)
│   ├── pagination.py            parse_limit ya corregido, parse_page original
│   ├── test_pagination.py       Tests de limit (pasan) + hueco para los de page
│   └── .claude/skills/revisar-pr/SKILL.md   Skill base para adaptar
└── 3_soluciones/                Solo para el presentador / al final
    ├── demo/pagination.py
    └── reto/pagination.py, test_pagination.py, SKILL_adaptada.md
```

## Cómo usarlo

### Demostración

```bash
cd 1_demo
python -m unittest -v        # Deben fallar test_zero_invalid y test_above_max_invalid
```

1. **Caso 1 · Skill.** Abre Claude Code dentro de `1_demo/` y ejecuta `/revisar-pr`
   pasándole `ISSUE.md`, `pagination.py` y `test_pagination.py`.
   Hallazgo esperado: `parse_limit` hace `int(value)` pero no valida el rango 1–100.
2. **Caso 2 · Agente.** Pega el contenido de `PROMPT_AGENTE.md`. El agente debe:
   leer, ejecutar los tests, explicar los fallos, **esperar tu aprobación**,
   cambiar solo `parse_limit`, volver a ejecutar los tests y mostrar el diff.
3. Compara con [3_soluciones/demo/pagination.py](3_soluciones/demo/pagination.py).

> Si quieres repetir la demo, restaura el archivo: `git checkout -- 1_demo/pagination.py`
> (o vuelve a copiarlo desde este repositorio).

### Reto por parejas

```bash
cd 2_reto
python -m unittest -v        # Los tests de limit pasan; los de page aún no existen
```

1. Leer `ISSUE.md` y planear las entradas/salidas (3 min).
2. Adaptar `.claude/skills/revisar-pr/SKILL.md` (5 min).
3. Escribir los tests de `parse_page`, pedir plan al agente, autorizar el cambio (10 min).
4. Revisar diff y que sigan pasando los tests de `limit` (3 min).
5. Compartir (2 min).

Sin agente o terminal: escribir el plan y los tests esperados, indicando que **no se ejecutaron**.

## Ideas clave para explicar

| Pieza | En esta carpeta |
| --- | --- |
| Prompt | `PROMPT_AGENTE.md`: una petición concreta para esta tarea |
| Skill | `SKILL.md`: la receta reutilizable para revisar cualquier PR |
| Agente | Claude Code / Codex leyendo archivos y ejecutando tests |
| Herramientas | Lectura de archivos y terminal (`python -m unittest`) |
| Contexto | `ISSUE.md`, el código y los tests |

Una skill es una guía, **no una barrera de seguridad**: los permisos reales se configuran en la herramienta.

> Mensaje de cierre: una skill nos ayuda a expresar el proceso; las pruebas y la revisión humana
> nos ayudan a decidir si el resultado es confiable.
