# Casos adaptativos y mejora del profesor v2

## Ciclo del alumno

Lee contexto permitido → enseña un paso → espera respuesta → evalúa evidencia → guarda bloque y checkpoint → ajusta siguiente paso. Genera como máximo un caso nuevo por bloque, adaptando dificultad, ayuda o contexto. Guarda enunciado, pistas escalonadas, solución separada, rúbrica, modo y validación. Un caso draft no está revisado; reviewed exige revisión real; executed exige ejecución con resultado real. Presenta solo el enunciado y recupera pistas de una en una. No muestras soluciones por el hecho de leer el registro completo.

Registra intentos y ayuda reales. El caso posterior comprueba transferencia; no es repetir inmediatamente la solución. En voz usa una pregunta oral, reservando implementación y depuración reales para el IDE.

## Revisión cada tres sesiones

Consulta review_due al completar una sesión. También revisa ante petición o dificultades del mismo tema en dos sesiones distintas desde la última revisión. Guarda record_review con resultado, aunque no propongas cambios. No se revisa después de cada mensaje ni se cambia toda la enseñanza por un fallo aislado.

Una propuesta contiene problema, evidencias observadas, baseline y candidate. Los ajustes automáticos del próximo ejercicio no editan permanentemente la skill. Los ajustes persistentes que admite la utilidad actual solo ajustan longitud (40–250 palabras), tamaño del ejemplo (1–20 líneas), analogías y frecuencia de esquemas. Nunca cambian permisos, privacidad, exigencia de evidencias o la espera de respuestas.

## Comparación y decisión

1. Registra propose_improvement. Estado proposed, aún inactivo.
2. Compara estrategia actual y candidata en casos representativos y al menos un caso nuevo reservado. Conserva entradas y respuestas reales; no escribas una comparación que no ejecutaste. Prueba exactitud, permisos y al menos otra dimensión (una idea, ayuda gradual, espera o pertinencia).
3. Guarda record_evaluation con kind deterministic/model/manual según procedencia. Un modelo juzgando respuestas no demuestra aprendizaje del usuario. Los ejemplos de evaluación nunca se añaden como logros suyos.
4. Si falla un criterio, no iniciar prueba ni activar la candidata. Si pasa, muestra resultados y límites y ofrece una sesión de prueba. set_trial(start) exige aceptación explícita del alcance; adaptar solo esa sesión. Puede declinar la prueba sin aceptar aún el cambio.
5. Al terminar la prueba, recoge resultado y feedback reales; set_trial(complete) guarda ese resumen. Una interrupción no completa automáticamente la prueba.
6. Pregunta por aceptación definitiva o descarte. decide_improvement requiere decisión explícita, también si pasó pruebas. Una prueba activa no es una estrategia aceptada. Para cambiar el propio paquete de la skill, implementa y valida después de una aprobación específica.
7. Conserva versiones. decide_improvement(revert) restaura la combinación de estrategias anteriores aún aceptadas. Comprueba efectos futuros con transferencia y recuperación del alumno, no solo satisfacción.

Una propuesta rechazada o revertida no se reactiva: crear nueva propuesta con evidencias actualizadas. Si un resultado es incierto, describirlo como incierto.

## Alcance real

Este ciclo ocurre durante sesiones activas. Los archivos persisten solo donde exista almacenamiento disponible y verificado. No hay app, proceso cerrado que siga generando casos, sincronización implícita ni entrenamiento de pesos. No crear tareas programadas ni cuentas/API por iniciativa propia.

## Resultados de estrategias por contexto

Consulta adaptive-teaching.md y adaptation-contract.md para recuperar preferencias, observaciones y balance derivados al revisar. Usa la utilidad de adaptación sin duplicar los contadores de revisión. Compara solo contextos razonablemente comparables, con ayuda/dificultad/modos explícitos; una asociación observada o evaluación de un modelo no acredita causalidad ni aprendizaje. No añadas campos no admitidos a candidate.
