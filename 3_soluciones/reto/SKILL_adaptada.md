---
name: revisar-pr
description: Revisa código frente a un issue y sus tests sin modificar archivos.
---
# Revisar un cambio

Lee el issue, el código y los tests autorizados.
Compara la implementación con cada criterio y revisa casos límite.
Para cada hallazgo, indica archivo, evidencia, riesgo y prueba sugerida.
Separa hechos observados de hipótesis. No inventes resultados de tests.
No modifiques archivos, instales paquetes, publiques ni accedas a secretos.
Si falta información, dilo. La persona decide qué aceptar o corregir.

## Paginación
Si el cambio toca parámetros de paginación (limit, page, offset):
- Verifica el valor por defecto, el mínimo y el máximo que pide el issue.
- Comprueba que existan tests para cada borde: el valor justo dentro y justo fuera
  (p. ej. 0 y 1, 100 y 101), negativos y texto no numérico.
- Cita la línea exacta del archivo y del test que sirve como evidencia.
- Confirma que los tests de los otros parámetros siguen pasando.
