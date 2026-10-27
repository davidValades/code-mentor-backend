# Biblioteca personal de conocimientos

## Acceso y organización

Mantén esta biblioteca fuera del paquete de la skill y de su repositorio público, bajo una ubicación persistente acordada. Si no existe una ubicación acordada, pregunta una sola vez por ella con opciones. No crees fichas reales dentro de assets/templates. Un .md no abre otros archivos: el asistente los consulta con herramientas disponibles.

En cada raíz autorizada utiliza `conocimientos/index.md`, `conocimientos/fichas/<id>.md` y `conocimientos/historial/<id>/r0001.md`, r0002.md, etc. El ámbito general contiene conceptos y ejemplos sintéticos, sin nombres, rutas, código o peticiones de la empresa. El conocimiento específico del equipo permanece en la raíz local del proyecto. Compartirlo exige autorización del resumen exacto.

El índice es un catálogo derivado: ID, título, ruta relativa de ficha, revisión, temas/topic, prerrequisitos por ID, fecha de actualización y repaso pendiente. Consulta primero el índice y después solo las fichas pertinentes y sus prerrequisitos. Las evidencias y los contadores siguen en state.json; las fichas resumen su significado, no crean una segunda fuente de calificaciones. Un plan de estudio se puede resumir en el perfil o tarea vigente; no necesita otro contador.

## Identidad y contenido

Usa la plantilla assets/templates/knowledge-card.md. El ID es estable, legible y sin datos privados, por ejemplo `csharp.operadores.igualdad`; permite solo letras minúsculas, números, puntos y guiones. Las fechas no forman parte del ID. Antes de crear busca por ID, título y sinónimos en el índice; si existe, actualiza su ficha. Conserva IDs y fecha de creación existentes aunque no sigan la convención nueva; valida cualquier nombre de archivo, no uses un ID inseguro como ruta. Un cambio de título no crea otro concepto.

Cada ficha incluye created_at y updated_at ISO 8601 con zona horaria, revisión entera empezando en 1, ámbito, topic(s) del registro, fuentes con URL/sección/fecha de consulta/versión aplicable, relaciones y prerrequisitos, explicación propia breve, ejemplo mínimo sintético, dudas, próxima práctica y repaso orientativo. Las fuentes explican el concepto; no prueban aprendizaje del alumno.

Separa contenido técnico verificado, comprensión declarada, comprensión conceptual demostrada, práctica guiada y autonomía práctica. Para cada avance cita IDs de evidencia realmente existentes, fecha, actividad, modalidad y grado de ayuda. Si no hay registro accesible, indica observación conversacional o declaración pendiente de registrar y no inventes IDs. Leer una ficha, elegir una opción o copiar código no acredita dominio. Conserva dudas y resultados incorrectos relevantes; no presentes el historial como una subida obligatoria de nivel.

## Cuándo proponer y cuándo guardar

Aplica el sistema combinado: al cerrar un tema o tarea con algo útil que conservar; en cada revisión de tres sesiones nuevas desde la última revisión; antes si la misma dificultad aparece en dos sesiones distintas, o a petición del alumno. Usa review_due según memory.md, no cuentes mensajes. Agrupa los motivos que coincidan en una sola propuesta. Sin novedades relevantes, informa «sin cambios» y no generes revisiones vacías.

Presenta una propuesta breve con ID, motivo, cambios exactos y estado de aprendizaje sustentado. Para una ficha nueva muestra el contenido completo; para actualizar muestra los cambios, manteniendo accesible el contenido previo. Pide aceptación de esa propuesta antes de escribir la ficha y su índice. Un rechazo o aplazamiento conserva la ficha vigente. Esta autorización específica no sustituye ni interrumpe el guardado ya autorizado de evidencias y checkpoints. Crear fichas no es modificar las instrucciones del profesor.

Si el alumno pospone, conserva en el checkpoint autorizado los IDs y cambios pendientes, sin guardarlos como ficha aprobada. Una revisión de aprendizaje se registra aunque no se acepten sus fichas; en la siguiente sesión consulta también pendientes, no dependas solo de review_due. No vuelvas a preguntar por una propuesta ya aceptada y aún no guardada; reintenta su contenido exacto tras comprobar versiones.

## Escritura y recuperación

Las fichas y el índice se escriben con herramientas de archivos; mentor_store.py no tiene una operación para guardarlos. No envíes `kind=knowledge` ni cambies el esquema existente. No atribuyas a escrituras manuales sus garantías de bloqueo, recibos o atomicidad.

Después de la aceptación:
1. Relee la ficha y su revisión. Si cambiaron desde la propuesta, reconcilia y presenta los cambios nuevos antes de sobrescribir. Comprueba que rutas y destino están dentro de la raíz acordada y no atraviesan enlaces simbólicos hacia otros ámbitos.
2. Para una actualización, conserva el contenido vigente exacto en historial/<id>/rNNNN.md antes de reemplazarlo. No sobrescribas un archivo de historial con contenido distinto. Incrementa revision una vez, conserva created_at y registra updated_at real.
3. Escribe la ficha vigente y después actualiza la fila del índice con su revisión y relaciones. No modifiques fichas ajenas a la propuesta.
4. Lee los resultados guardados y comprueba ID, revisión, fechas, enlaces relativos e historial antes de afirmar éxito. Si un paso falla, informa qué quedó guardado y qué queda pendiente; un reintento no crea otra revisión si la ficha ya coincide.

Si la ficha y el índice discrepan tras una interrupción, comprueba ficha e historial y repara solo la fila derivada tras verificarla; no inventes avances desde el índice. Si hay escritores simultáneos, detén la escritura ante el conflicto y coordina, sin prometer bloqueo seguro con herramientas manuales.

Sin acceso o persistencia, entrega la propuesta en conversación como borrador pendiente. No afirmes haber guardado, leído toda la biblioteca o sincronizado entornos. Esta biblioteca se actualiza durante sesiones activas; no se entrena el modelo ni se trabaja en segundo plano.
