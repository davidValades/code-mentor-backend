# Contrato de almacenamiento v2

## Ubicación y límites

Mantén datos fuera del paquete de la skill. Acuerda una raíz personal para el perfil y otra local para cada proyecto. Comprueba acceso, persistencia y normas de la empresa; evita directorios seguidos por Git empresarial o sincronizados externamente sin autorización. No cambies configuración del repositorio por iniciativa propia. Usa raíces absolutas. Un directorio temporal no garantiza continuidad.

Cada raíz tiene `state.json`: esquema 2, revisión, ámbito general/project, eventos, sesiones, revisiones, casos, intentos, observaciones, mejoras, documentos y recibos. JSON es fuente de evidencias y contadores; Markdown conserva narrativa. Lee la última versión referenciada de cada documento; archivos huérfanos tras interrupciones no son vigentes. No edites versiones directamente.

La biblioteca opcional conocimientos/ usa fichas e índice escritos con herramientas de archivos según knowledge-library.md. No está gestionada por la CLI: no existe kind=knowledge ni un comando save_knowledge. State.json conserva evidencias y contadores; el índice es derivado y las fichas resumen el aprendizaje. No cambies el esquema 2 para activar esta ampliación.

La CLI no usa red ni sincroniza dispositivos. Sin Python o persistencia, prepara un resumen de continuidad e indica el guardado pendiente. No atribuyas las garantías del script a escrituras manuales.

## CLI

Ejecuta `python scripts/mentor_store.py --root /ruta/absoluta init --scope general` con Python 3.11+. Otros comandos: read, validate, status, apply, prepare-summary, export-summary. `status` devuelve revisión, review_due, estados derivados por tema, estrategia activa y checkpoint. Entradas JSON por stdin; nunca interpolar contenido o secretos en shell.

`apply` recibe request_id, expected_revision, operation y payload; devuelve revision, record_id y replayed. Reintentar exige ID y contenido idénticos. Ante conflicto vuelve a leer y reconcilia. No rompas bloqueos sin investigar otro escritor.

Operaciones: record_evidence, save_checkpoint, complete_session, record_review, save_case, record_case_attempt, record_observation, confirm_convention, propose_improvement, record_evaluation, set_trial, decide_improvement, save_document. Consulta los campos exactos y ejemplos siguientes. Un user_confirmed=true se envía solo tras aceptación explícita; el script no verifica la conversación.

## Evidencias y privacidad

Evento general: id, session_id, recorded_at ISO con zona, topic, activity (declared/explain/predict/implement/debug/retrieve), modality (oral/text/ide), assistance (none/hint/guided/solution), outcome (correct/partial/incorrect/unverified), evidence_summary, review_due (fecha con zona o null). Evento de proyecto añade task_id y source_refs.

Referencia: path relativa, commit completo o null, branch, dirty booleano, observed_at. Un commit no representa cambios locales: dirty=true cuando corresponda. Nunca guardar remoto autenticado.

El esquema rechaza campos laborales adicionales en eventos generales, pero no anonimiza texto libre. Revisar el contenido antes de guardar: conceptos genéricos y dificultades transferibles sí; nombres, rutas, código, peticiones y decisiones empresariales no. Compartir contexto laboral exige aprobación del resumen exacto.

save_document recibe id, kind (profile/project/task/checkpoint/improvement), title, content Markdown y recorded_at. Solo profile en ámbito general; los demás en proyecto. Conserva versiones inmutables. El script no identifica todos los secretos: revisar el texto antes de persistir.

No sobrescribir esquemas desconocidos ni migrar v1 automáticamente. Preparar y confirmar una migración conserva procedencia y evidencias.

## Entradas concretas de la CLI

`apply` recibe en stdin un objeto `{"request_id":"identificador-estable", "expected_revision":0, "operation":"...", "payload":{...}}`. Obtén siempre la revisión de `read` o de una escritura real. El identificador del evento y el de la solicitud son distintos. Si el guardado falla, conserva la entrada exacta para reintentar.

| Operación | Campos exactos de payload |
| --- | --- |
| record_evidence | Los campos del evento definidos arriba; añade task_id y source_refs solo para project. |
| save_checkpoint | session_id, topic, evidence_id (string o null), pending_question, next_step, recorded_at. |
| complete_session | id, recorded_at. Un id repetido no crea una sesión nueva. |
| record_review | id, recorded_at, reason, result. El script captura automáticamente las sesiones y evidencias revisadas. |
| save_case | id, topic, prompt, hints (lista), solution, criteria (lista), validation (draft/reviewed/executed), validation_evidence (texto), mode (oral/ide). |
| record_case_attempt | id, case_id, session_id, response, assistance, outcome, recorded_at. |
| record_observation | id, task_id, statement, source, recorded_at; solo project. |
| confirm_convention | id de la observación, user_confirmed=true, scope, reason; solo tras confirmación real. |
| save_document | id lógico, kind, title, content Markdown, recorded_at. |
| propose_improvement | id, reason, evidence_ids (lista no vacía), baseline, candidate. candidate admite únicamente explanation_words (40–250), example_lines (1–20), analogies (booleano) y diagrams (when_interaction/on_request/frequent). |
| record_evaluation | id, improvement_id, kind (deterministic/model/manual), results, cases, checks. cases contiene al menos un design y un heldout, cada uno con id, split, baseline_response y candidate_response. checks contiene al menos tres booleanos, incluyendo accuracy y permissions. |
| set_trial | id de mejora, action (start/complete/decline), user_confirmed=true y summary. Solo cuando la elección real exista; complete describe el resultado observado. |
| decide_improvement | id de mejora, decision (accept/reject/revert), user_confirmed=true, reason. Para accept debe haber evaluación favorable y prueba completada o explícitamente rechazada. |

Ejemplo autocontenido de evidencia **hipotética** (no guardar como si fuera una respuesta del alumno):

```json
{"request_id":"req-001","expected_revision":0,"operation":"record_evidence","payload":{"id":"e-001","session_id":"s-001","recorded_at":"2026-10-26T18:00:00+01:00","topic":"methods","activity":"declared","modality":"oral","assistance":"none","outcome":"unverified","evidence_summary":"Dice que entiende el retorno; falta comprobarlo.","review_due":null}}
```

Para preparar una exportación ejecuta `prepare-summary` con stdin `{"selected_ids":["e-001"]}`; para ámbito project añade `curated_text` con el resumen mínimo redactado manualmente. La salida contiene `summary`, `digest` y `approval_pending=true`. Presenta ese summary al usuario completo. Una vez acepte ese contenido exacto, llama `export-summary` con stdin `{"summary":<objeto mostrado>,"approved_digest":"<digest recibido>","destination":"/ruta/absoluta/nueva.json"}`. Nunca interpretes el digest como autorización por sí solo. La exportación rehúsa sobrescribir un archivo existente y usa permisos privados POSIX cuando estén disponibles; revisa igualmente las políticas del destino.

Usa `status` para consultar los estados calculados; no llamas directamente funciones Python desde la conversación. El contador de revisión se basa en sesiones completadas nuevas y en evidencias observadas desde la última revisión. El ajuste por dificultad repetida considera dos sesiones distintas.
