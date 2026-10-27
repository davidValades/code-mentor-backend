# Adaptación de la enseñanza por resultados — 2.7

Code Mentor Backend combina preferencias declaradas, necesidades del concepto y evidencias reales. Explora ayudas desde el inicio, gradualmente dentro de tareas y repasos normales. No clasifica al alumno en estilos fijos ni garantiza que un método sea la causa de una mejora.

## Funcionamiento

Usa una ayuda principal por bloque y una acción del alumno por turno. Si faltan antecedentes, elige por contenido y entorno y declara ese límite. Introduce variantes pertinentes aún no probadas sin exigir completar un catálogo antes de avanzar. Ante dificultad comprueba primero prerrequisitos, tamaño del paso y claridad del enunciado.

Las ocho ayudas existentes son esquemas, analogías, trazas, ejemplos resueltos, comparaciones, explicación propia, recuperación y depuración guiada. Sus variantes incluyen mapas mentales o conceptuales, secuencias de llamadas, dibujos funcionales de objetos y referencias, tablas de decisiones, ejemplos parciales y fragmentos para ordenar. Consulta el [catálogo y protocolo](../skills/code-mentor-backend/references/teaching-exploration.md).

## Cuándo pide tu opinión

Pregunta brevemente por claridad o esfuerzo al estrenar una ayuda en ese concepto/contexto o detectar un atasco. Ofrece opciones y espacio de detalles si el entorno lo permite. Si ya lo comentaste, utiliza esa declaración sin repetir la pregunta. No pregunta tras cada explicación ni al cerrar por rutina; puedes omitir la valoración.

La valoración se separa de la comprobación de aprendizaje, esperando tu respuesta antes del siguiente ejercicio. «Me ha aclarado la idea» es una declaración. Explicar una decisión, resolver una variante y recuperarla después aportan evidencias distintas, que se registran con modalidad y ayuda recibida.

## Cómo usa los resultados

Prioriza provisionalmente ayudas prometedoras en contextos comparables; considera concepto, tarea, dificultad, bases previas, orden y práctica acumulada. Una explicación posterior puede aprovechar lo aprendido con otra anterior. Mantiene también resultados contradictorios, recuperación activa y oportunidades pertinentes de explorar otras ayudas.

La cobertura narrativa distingue «sin probar», «evidencia insuficiente», «prometedora en este contexto» y «necesita revisión». Una valoración positiva o un único acierto no bastan para considerar una ayuda prometedora. La conclusión exige revisar varios intentos en más de una sesión y sigue siendo provisional, sin umbral de eficacia científica.

La revisión aprovecha las tres sesiones del ciclo existente; se anticipa ante dificultad en dos sesiones distintas o petición. Los apoyos se retiran progresivamente para practicar autonomía. Los cambios permanentes del profesor siguen la evaluación y aceptación de su ciclo de mejora.

## Archivos privados

Dentro de la raíz persistente acordada:

| Archivo | Función |
| --- | --- |
| adaptacion/preferencias.md | Preferencias/restricciones declaradas y su alcance. |
| adaptacion/exploracion.md | Variantes, motivos, feedback, cobertura y revisión cualitativa con fechas y evidencias enlazadas. |
| adaptacion/observaciones.jsonl | Observaciones con ID estable y referencia a evidencias existentes. |
| adaptacion/balance.md | Resultados derivados con fecha, revisión del registro y huella de observaciones. |
| adaptacion/graficos/resultados.svg | Gráfico estático de esos resultados. |

Estos archivos se crean durante uso autorizado, no al instalar la skill. El repositorio público contiene utilidades y plantillas vacías, no datos del alumno. El registro principal conserva la autoridad del progreso; exploracion.md no duplica eventos ni contadores. Los detalles laborales permanecen en su ámbito local. No hay transmisión al creador, sincronización automática ni proceso de fondo.

Sin escritura, las notas se incorporan al mismo lote pendiente de cierre. Prepararlas no demuestra que se hayan guardado. Durante conducción la interacción es oral y las acciones de pantalla o IDE se posponen.

## Utilidad y gráficos

Con Python 3.11+ y un state.json ya configurado, la utilidad mantiene record, read y report según [el contrato exacto](../skills/code-mentor-backend/references/adaptation-contract.md). No cambia el esquema 2 ni admite nuevos campos o IDs por esta ampliación. Las fichas de conocimiento siguen requiriendo aceptación.

report genera balance.md y resultados.svg desde observaciones.jsonl, agrupando por los ocho IDs existentes y sus combinaciones, concepto y contexto. No ingiere exploracion.md ni calcula sus estados, cobertura o eficacia por variante. La valoración cualitativa se conserva por separado para que regenerar los derivados no la sobrescriba.

El gráfico muestra aciertos/intentos, pendientes y sesiones, no porcentajes de estilos ni un ganador global. «Evidencia insuficiente» aparece por debajo de tres intentos evaluados o de dos sesiones con intentos evaluados; es una señal orientativa de presentación, no validación estadística. Superarla tampoco demuestra eficacia.

La recuperación diferida registrada exige otra sesión y al menos 24 horas desde la evidencia previa del mismo tema. Los relatos sin comprobar, soluciones copiadas y evaluaciones pendientes no se cuentan como aciertos. Las combinaciones se presentan juntas.

Antes de decidir, el profesor revisa fuentes, recencia y diferencias entre ejercicios. Sin acceso, informa del límite y prepara un borrador; no inventa gráficas ni logros.
