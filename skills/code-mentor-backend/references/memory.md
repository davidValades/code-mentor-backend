# Memoria y evidencias v2

## Recuperar antes de enseñar

Lee [el contrato](storage-contract.md) antes de la primera escritura. Localiza el registro general y, en el entorno laboral, el del proyecto acordado. Usa read para conocer revisión, documentos vigentes, tareas activas y checkpoint; carga solo lo pertinente. No busques el código empresarial desde ChatGPT si solo se ha autorizado un resumen. Si falta acceso, usa ese resumen y declara su fecha y límites.

Si se ha configurado una biblioteca, consulta su índice y las fichas pertinentes según [biblioteca de conocimientos](knowledge-library.md). Incluye propuestas pendientes del checkpoint, aunque review_due ya sea false.

Mantén dos ámbitos: general (conceptos, dificultades transferibles y logros demostrados) y proyecto (tareas, contexto, archivos/versiones y fragmentos necesarios). No copies contenido laboral al perfil general. En el primer uso sin ubicaciones acordadas, pregunta dónde guardar mediante opciones; no confundas un directorio temporal con persistencia garantizada.

## Guardado durante el uso

Para cierres, cambios de modo y lotes pendientes aplica [cierre de sesión](session-close.md). Prepara una nota al terminar cada sesión; agrupa la actualización con Work solo en los desencadenantes allí definidos cuando Chat carezca de escritura. La plantilla session-close.md conserva identidad del lote, procedencia, destino, pendientes, ayudas docentes y recibo. No guardar sesiones de diseño ni datos sintéticos como aprendizaje.

Después de cada bloque significativo, registra lo observado y el checkpoint. Al cerrar, guarda el checkpoint y completa la sesión una sola vez. Una pausa conserva el mismo session_id; una desconexión que no se procesó no acredita guardado. No preguntar permiso en cada bloque para guardar lo ya autorizado dentro del ámbito acordado.

Utiliza IDs estables y la última revisión. Reintentos de una escritura incierta conservan ID, revisión original y contenido exactos. Ante conflicto vuelve a leer y reconcilia; no inventes una nueva evidencia para el mismo hecho. Comprueba el resultado real y la revisión guardada. Si falla, di que queda pendiente y prepara continuidad; no registres éxito ficticio.

Para narrativa usa las plantillas de assets/templates y save_document: perfil general o proyecto/tarea local. Mantén versiones anteriores de decisiones y contexto. El historial no obliga a copiar conversaciones completas. Permite rectificar evidencias: conserva una corrección explícita y explica su efecto; una petición de eliminación requiere retirar también los recibos/documentos que conserven ese contenido y verificarlo, sin afirmar borrado de copias externas. La utilidad actual no automatiza eliminación ni migraciones: no uses apply para operaciones no soportadas.

## Evidencia y progreso

Registra actividad, modalidad, ayuda, resultado y evidencia específica de la respuesta o acción. Un autoinforme usa activity=declared, outcome=unverified. «Lo entiendo» y copiar una solución no acreditan dominio. Una explicación correcta puede acreditar comprensión conceptual; autonomía práctica requiere implementación o depuración en IDE, sin ayuda y con resultado observado. Para consolidar exige recuperación independiente en otra sesión al menos un día después de esa práctica. No conviertas un concepto puramente oral en logro de programación.

La función learning_status calcula el estado desde evidencias; conceptual es una distinción de comprensión, no un nivel práctico superior a guided. Un intento de caso no crea automáticamente evidencia: evalúa la respuesta primero. Si corriges un registro, vuelve a calcular el estado.

Tras una comprobación breve durante la tarea, prepara un reto pequeño en otra sesión. En voz será oral; si el objetivo es práctico, reserva un ejercicio IDE. Usa intervalos orientativos 1/3/7/14 días y reajusta según recuperación real; no son predicción individual ni recordatorios creados. Un «sí» no pospone un repaso ganado por práctica real.

## Revisión del profesor

Tras cada sesión completada consulta review_due. Revisar cada tres sesiones nuevas desde la revisión anterior; anticipar si el usuario lo pide o aparece dificultad del mismo tema en dos sesiones distintas. Revisar no obliga a cambiar nada: guarda motivo, evidencias y resultado, incluso «sin cambios». El contador vive en sesiones y revisiones, no en un número editado a mano.

Muestra progreso en conversación mediante tabla pequeña de competencias, evidencias y próximo paso; no crear un panel o app. En ChatGPT sin acceso al mismo registro, no afirmes compartir memoria con Codex.

Sin registro accesible, una tercera sesión relatada permite ofrecer revisión provisional y un lote pendiente, pero no afirmar que review_due fue calculado. No dependas de cierres de app ni supongas que tres mensajes o tres chats equivalen a tres sesiones.

## Documento de aprendizaje y revisión

Al finalizar una tarea, al completar una revisión de tres sesiones, ante una dificultad reiterada o cuando lo pida el alumno, prepara una nota Markdown breve y útil para futuras sesiones. Incluye fecha, conceptos abordados, hechos demostrados con referencia a evidencia y grado de ayuda, comprensión declarada sin verificar, dificultades, términos corregidos, dudas, siguiente ejercicio y fecha de repaso orientativa. Distingue observación de hipótesis; nunca conviertas una respuesta copiada u oral en autonomía práctica.

Actualiza el documento de perfil general sin nombres, código o detalles de la empresa, usando save_document kind=profile e ID lógico estable; conserva versiones anteriores y comprueba el resultado. Para una tarea laboral, guarda detalles y referencias únicamente en el registro de proyecto autorizado con kind=task y un ID lógico estable, siguiendo project-context.md. Solo comparte un resumen laboral después de la autorización del texto exacto. No vuelques el contenido profesional al perfil general.

Compara esta nota con la anterior: señala avances con evidencia, conceptos que requieren refuerzo y lo que aún no se ha comprobado. Reutiliza lo pertinente al iniciar la siguiente sesión, y decide con el alumno una práctica breve adaptada. No alteres las instrucciones de la skill por este registro: proponer un cambio docente y aceptarlo sigue otro proceso. Si no hay almacenamiento persistente, ofrece la nota en la conversación como resumen para guardar y aclara que no se ha guardado. Esto se realiza durante sesiones activas, no en segundo plano.

## Fichas y estudio de documentación

Las notas de aprendizaje y las evidencias operativas se guardan dentro del ámbito ya autorizado. Las fichas por concepto y sus actualizaciones requieren aceptación específica de la propuesta según knowledge-library.md; no conviertas una nota automática en ficha aprobada. Propón las novedades al cerrar tema/tarea, en cada revisión de tres sesiones o ante dificultad del mismo tema en dos sesiones distintas. Deduplica motivos y conserva aplazamientos en el checkpoint.

Usa documentation-study.md al preparar una ruta desde una fuente o una petición de estudio. El perfil/tarea puede conservar esa ruta y las relaciones con IDs de fichas, sin duplicar los contadores ni dar dominio por leer.

## Observaciones de enseñanza

Si existe autorización de registro operativo, vincula las ayudas usadas a las evidencias reales según adaptation-contract.md, sin convertir declaraciones en aciertos. Recupera preferencias.md y solo el balance pertinente para adaptar el siguiente paso. En la revisión de tres sesiones puedes generar balance/gráfico, conservando datos pendientes y referencias. Si el registro cambia, revalida los derivados. Los registros de adaptación y sus copias también se revisan en correcciones o solicitudes de eliminación.
