# Estudiar documentación y conservar conocimientos

Code Mentor Backend 2.2 amplía el profesor existente con estudio guiado de documentación y fichas personales de conceptos. No requiere una app o servidor propio.

## Cómo se consulta la información

SKILL.md contiene las reglas y la tabla para elegir referencias. Para estudiar una fuente, el asistente consulta documentation-study.md; para buscar o mantener fichas, knowledge-library.md. El asistente abre esos archivos con las herramientas del entorno: los Markdown no ejecutan búsquedas por sí mismos.

Al empezar, recupera el registro accesible, el checkpoint y el índice de conocimientos. Después abre solo las fichas relacionadas y sus prerrequisitos. Contrasta sus resúmenes con las evidencias del registro y la documentación aplicable. Una ficha no es prueba de dominio por sí sola.

## Biblioteca privada externa

Dentro de la ubicación persistente acordada con el usuario se organiza:

- conocimientos/index.md: catálogo por ID, relaciones, revisión y repaso.
- conocimientos/fichas/<id>.md: ficha vigente de cada concepto.
- conocimientos/historial/<id>/r0001.md: revisiones previas conservadas antes de actualizar.

Esta estructura se crea cuando se configura y autoriza su uso, fuera del paquete de la skill. El repositorio público contiene instrucciones y plantillas vacías, nunca la biblioteca real del alumno. El perfil general contiene conceptos y ejemplos sintéticos; las tareas, nombres y código de empresa permanecen en su contexto de proyecto autorizado.

La biblioteca puede estar junto al registro general acordado. No se debe crear automáticamente dentro de un repositorio laboral o publicarla en GitHub. Si ChatGPT y Codex no tienen acceso a la misma ubicación, no comparten los cambios por sí solos; se prepara un resumen de continuidad permitido.

## Qué incluye una ficha

ID estable como csharp.operadores.igualdad, título, ámbito, revisión incremental, fechas ISO con zona, temas, prerrequisitos, fuentes consultadas y versión aplicable, explicación breve, ejemplo sintético, evidencias y ayuda recibida, dudas, próxima práctica y repaso orientativo. La fecha de creación y el ID se conservan aunque cambie el título. La documentación consultada no acredita aprendizaje; se distingue comprensión declarada, conceptual, práctica guiada y autonomía.

## Cuándo se propone guardar

El profesor aplica un sistema combinado: al cerrar un tema o tarea con novedades relevantes, cada tres sesiones desde la revisión anterior y antes si una dificultad se repite en dos sesiones distintas, o a petición del alumno. Agrupa motivos coincidentes y no crea revisiones vacías.

Muestra la propuesta y pide aceptación de su contenido antes de escribir fichas o índice. El registro de evidencias y checkpoints previamente autorizado continúa sin pedir permiso en cada bloque. Si se aplaza una propuesta, queda pendiente en el checkpoint; no se presenta como conocimiento ya guardado.

## Ejemplo de estudio

«Usa Code Mentor Backend. Me han pedido revisar los operadores de C#. Consulta lo que he demostrado saber y propón por dónde empezar».

El profesor revisa conocimientos previos accesibles, consulta fuentes primarias, comprueba la versión cuando afecte al proyecto y prepara una ruta breve. Explica una idea, propone una predicción o práctica y espera la respuesta. Al cerrar el bloque puede proponer una ficha; no marca dominado todo el tema porque el alumno haya leído la documentación.

## Límites técnicos

mentor_store.py sigue usando el esquema 2 para evidencias y contadores. Las fichas y el índice se gestionan con herramientas de archivos; no existe un comando save_knowledge ni kind=knowledge. Las escrituras manuales no tienen las garantías de bloqueo y recibos de la utilidad. Sin acceso o persistencia se muestra un borrador pendiente, sin afirmar que se ha guardado. No hay trabajo en segundo plano, sincronización automática ni entrenamiento de pesos del modelo.
