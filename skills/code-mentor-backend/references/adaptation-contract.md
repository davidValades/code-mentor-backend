# Contrato de observaciones y gráficos

## Ubicación y autorización

Usa la misma raíz general o de proyecto ya acordada y su state.json esquema 2. Esta ampliación no crea ni migra el registro principal. Sin ubicación acordada, configura una vez el almacenamiento con el alumno; un directorio temporal no garantiza persistencia. La autorización operativa permite registrar observaciones de enseñanza sin preguntar cada vez; las fichas siguen requiriendo aceptación de contenido. No guardar preferencias de equipo o código de empresa en el ámbito general.

## CLI disponible

Ejecuta con Python 3.11+: `python scripts/mentor_adaptation.py --root /ruta/absoluta record`, `read` o `report`. record recibe un JSON por stdin; read solo lee; report escribe balance y SVG locales. No existen otros comandos. No interpolar entradas ni secretos en comandos shell.

| Campo de record | Valor |
| --- | --- |
| id | ID de observación estable: minúsculas, números, puntos o guiones, máximo 128 caracteres. |
| evidence_id | ID realmente existente en events de esta raíz. |
| concept_id | ID estable y genérico del concepto, mismo al retomar, con la misma convención segura. |
| task_kind | read / trace / explain / implement / debug. |
| difficulty | introductory / standard / complex; estimación contextual explícita. |
| check_kind | immediate / transfer / delayed. |
| strategies | Lista no vacía sin duplicados de IDs de adaptive-teaching.md; todas las ayudas usadas, sin atribuir éxitos de una combinación a cada una. |
| learned_evidence_id | null en una comprobación inmediata, o ID previo del aprendizaje; obligatorio para transfer y delayed. |

Los demás campos se rechazan. La utilidad deriva resultado, actividad, modalidad, ayuda, sesión y fecha de la evidencia real, sin copiarlos en otro registro mutable. Conserva la modalidad del aprendizaje y de la comprobación por separado. Para transfer, el profesor verifica que se trata de un caso nuevo; la utilidad no puede juzgar el contenido semántico del ejercicio. Para delayed exige otra sesión, mismo tema y al menos 24 horas desde la evidencia previa; la demora real se muestra en el balance.

strategies describe las ayudas del episodio de aprendizaje que se evalúa; al vincular una comprobación posterior conserva el mismo conjunto y comprueba el historial. La ayuda recibida durante la comprobación queda separada por el campo assistance del evento. No cambies el conjunto para atribuir un repaso a otro método.

Reutiliza id y contenido exactos al reintentar. El orden de strategies se normaliza. Repetir la misma observación es idempotente; reutilizar su ID con otros datos se rechaza, igual que contar dos veces una evidencia con IDs de observación distintos. Una corrección requiere revisar el registro y sus derivados; no inventes una nueva observación del mismo intento. La utilidad no automatiza edición ni borrado del historial de observaciones.

## Garantías y límites

El archivo adaptacion/observaciones.jsonl se reescribe de forma atómica bajo el mismo bloqueo de la raíz que usa mentor_store.py. No rompe bloqueos existentes y rechaza rutas inseguras o destinos a través de enlaces simbólicos. Conserva permisos privados POSIX cuando están disponibles. Estas medidas no sustituyen la seguridad del entorno ni garantizan exclusión frente a otras herramientas que ignoren el bloqueo.

read revalida los vínculos contra el estado actual. Evidencias eliminadas se excluyen como huérfanas; vínculos que ya no cumplan el contrato se excluyen como incompatibles. No se alteran las evidencias principales ni sus contadores. Una solicitud de eliminación también debe revisar observaciones, preferencias, balances, gráficos y copias afectadas, sin prometer borrar sistemas externos.

Una declaración, resultado unverified o respuesta con ayuda solution se muestra como pendiente y no como intento evaluado ni acierto. Los demás intentos se separan en correct, partial e incorrect; un acierto con pista nunca equivale a autonomía.

report genera adaptacion/balance.md y adaptacion/graficos/resultados.svg con fecha, source_revision y observation_digest. Son derivados reconstruibles, no fuente de memoria. Si una escritura falla, no afirmes actualización completa; vuelve a ejecutar report y verifica ambos archivos. Una revisión distinta del registro hace que el balance deba revisarse/regenerarse antes de decidir. Las preferencias están en un Markdown aparte, no en este JSONL.

No ejecutes la utilidad para fabricar observaciones a partir de ejemplos docentes o salidas de agentes de prueba. Un gráfico vacío es un resultado válido, no una orden de generar datos del alumno.

Para comprobar vigencia contrasta tanto source_revision como observation_digest con read: añadir observaciones no incrementa la revisión de state.json. Si cualquiera difiere, regenera el balance antes de usarlo.

## Variantes y valoraciones narrativas

Conserva los ocho IDs existentes de strategies. Los mapas, tablas, ejercicios parciales y demás variantes se describen según [exploración gradual](teaching-exploration.md) en adaptacion/exploracion.md del mismo ámbito, junto a su feedback y vínculos a evidencias. No envíes variant, feedback, coverage, clarity ni otros campos nuevos a record, ni añadas variantes a candidate o state.json.

Este Markdown complementa al registro principal; no crea eventos ni contadores y no modifica observaciones.jsonl. report no lo ingiere: balance.md y resultados.svg continúan agrupando por los IDs existentes, sin calcular estados narrativos ni eficacia por subformato. Conservar el análisis cualitativo fuera de esos derivados evita perderlo al regenerarlos.

Antes de actualizar exploracion.md, leer identidad/versión actual y conservar aportaciones ajenas e historial. Verificar después. Los detalles laborales permanecen en el ámbito local autorizado. Una solicitud de eliminación debe revisar también este documento y sus copias autorizadas. Sin acceso, mantener sus cambios en el mismo lote pendiente, sin afirmar que están guardados.
