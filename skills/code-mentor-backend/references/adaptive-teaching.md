# Adaptación docente por evidencias

Combina preferencias declaradas, exigencias del concepto y resultados observados. No clasifiques al alumno como visual/auditivo/cinestésico ni atribuyas un resultado a una estrategia por aparecer antes. Una preferencia o satisfacción no demuestra aprendizaje. Las fuentes generales orientan la enseñanza, no validan este profesor individual.

## Elegir el siguiente paso

1. Lee preferencias y restricciones accesibles, checkpoint, evidencias recientes, índice y fichas pertinentes. Consulta el balance solo si conoces su fecha y revisión de origen; vuelve al registro si quedó antiguo.
2. Ante dificultad, comprueba primero prerrequisitos, tamaño del paso y claridad del enunciado. Una explicación distinta no resuelve por sí sola una base ausente.
3. Elige la ayuda adecuada al contenido y entorno. Con antecedentes comparables, prioriza provisionalmente ayudas prometedoras; sin ellos, explica que falta evidencia personal. Una preferencia de accesibilidad se respeta aunque no haya puntuaciones; no exige diagnóstico.
4. Usa una idea y una comprobación por turno. Registra ayuda, resultado y límites reales; prepara transferencia a un caso distinto y recuperación posterior. Reduce ayuda progresivamente sin ocultar los errores.
5. Si no funciona, modifica una ayuda o reduce el paso. No insistas por un supuesto estilo fijo. Conserva recuperación activa y repasos aunque resulte más cómodo releer.

| Ayuda | Uso orientativo y límite |
| --- | --- |
| diagram | Relaciones y recorrido entre componentes; esquema funcional, sin decoración innecesaria. |
| analogy | Introducción de una idea con un referente familiar; explicitar dónde deja de servir y regresar al código. |
| trace | Seguir evaluación, llamadas y valores; no entregar toda la solución del ejercicio. |
| worked-example | Razonar sobre otro ejemplo y retirar pasos en la práctica posterior. |
| comparison | Contrastar casos para identificar la diferencia relevante. |
| self-explanation | Pedir justificar una predicción con palabras propias. |
| retrieval | Recuperar sin consultar y comprobar después; un fallo puede orientar el repaso. |
| guided-debugging | Hipótesis, breakpoint/log y experimento verificable; sin inventar ejecución. |

Estos IDs pueden combinarse en una observación, pero una combinación no se acredita a un componente aislado. El resultado depende también del contenido, dificultad, experiencia previa y orden. No uses velocidad como medida principal.

## Registro y preferencias

Utiliza la carpeta adaptacion/ en la raíz persistente autorizada, fuera de la skill y de su repositorio público. preferencias.md, basado en la plantilla, conserva lo que el alumno declara y su alcance; balance.md y graficos/resultados.svg son derivados. observaciones.jsonl vincula las estrategias a IDs de evidencias existentes del mismo ámbito. Lee [el contrato de adaptación](adaptation-contract.md) antes de ejecutar la utilidad.

El alumno puede decir que algo le resulta más claro; registra esa preferencia como declaración, no como éxito. La utilidad de observaciones no almacena feedback libre: usa el perfil o documento del proyecto autorizado para claridad/esfuerzo/preferencias. No inventes modalidad o ayuda para completar campos de un evento; si faltan, la observación queda pendiente.

El balance separa concepto, tema, tipo de tarea, dificultad, modalidad de aprendizaje y de comprobación, actividad, ayuda, tipo de comprobación y combinación de estrategias. Su agrupación no hace idénticos los ejercicios: consulta las evidencias y contexto antes de comparar. Describe aciertos/intentos, parciales, errores, pendientes y demora real. No produzcas rankings globales ni porcentajes de estilos. El umbral de 3 intentos y 2 sesiones con intentos evaluados es una señal conservadora de interfaz, no validación estadística ni prueba de eficacia.

## Revisión y autonomía

Adapta el siguiente paso dentro del modo tutor y permisos existentes, sin pedir aceptación de cada explicación. Ocasionalmente ofrece una variante en una práctica normal; no conviertas las clases en experimentos continuos. En voz durante conducción no pidas pantallas, lectura, escritura o manipulación del dispositivo. Una explicación oral no acredita programación autónoma.

Revisa con review_due cada tres sesiones, antes ante dificultad repetida en dos sesiones distintas o petición del alumno. Genera el balance/gráfico durante la revisión si hay acceso; con pocos datos muestra la insuficiencia. Con cero observaciones, no rellenes ejemplos como si fueran datos. La observación de una revisión no cuenta como nueva sesión.

Los cambios permanentes siguen improvement-loop.md y requieren aceptación explícita. propose_improvement solo admite los cuatro ajustes de su contrato; no añadas IDs de estrategias a candidate. Para modificar reglas del paquete fuera de ellos, prepara un cambio de skill y valídalo tras autorización. Las preferencias y elecciones contextuales no activan mejoras permanentes por sí solas.

Sin acceso a archivos o Python, ofrece un balance manual trazable o un borrador pendiente y declara sus límites; no atribuyas garantías de la utilidad a escrituras manuales. No hay proceso de fondo, entrenamiento del modelo ni sincronización implícita.

## Base investigadora

Consulta fuentes cuando una afirmación concreta lo requiera: revisión de estilos de Clinton-Lisell y Litzinger (2024), doi:10.3389/fpsyg.2024.1428732; técnicas de Dunlosky et al. (2013), doi:10.1177/1529100612453266; recuperación de Karpicke y Blunt (2011), doi:10.1126/science.1199327; experiencia previa de Kalyuga et al. (2003), doi:10.1207/S15326985EP3801_4. No extrapoles resultados de tareas experimentales a una garantía de aprender C# con un LLM.

Para comprobar vigencia contrasta tanto source_revision como observation_digest con read: añadir observaciones no incrementa la revisión de state.json. Si cualquiera difiere, regenera el balance antes de usarlo.
