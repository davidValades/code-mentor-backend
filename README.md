# Code Mentor Backend

**Un profesor en español para aprender C# y .NET backend mientras trabajas con código real.**

Code Mentor Backend es una skill de tutoría: guía la lectura, escritura, refactorización y depuración de código, y te ayuda a entender las decisiones de arquitectura. Adapta la ayuda a tus conocimientos y al contexto de la tarea, con explicaciones pequeñas y comprobaciones de comprensión.

## Qué puedes aprender y practicar

- **Leer código complejo:** seguir llamadas entre métodos y clases, identificar responsabilidades y entender cómo circulan los datos.
- **Refactorizar con criterio:** comprender el contrato de un método y revisar los casos afectados por un cambio, como sustituir un resultado nulo por un tipo de resultado con varios estados.
- **Depurar paso a paso:** plantear hipótesis, elegir puntos de interrupción, observar valores y comprobar qué ocurre antes de proponer una solución.
- **Estudiar documentación:** partir de lo que ya sabes, detectar las bases necesarias y convertir la lectura en ejemplos y ejercicios.
- **Hablar de programación con precisión:** aprender vocabulario técnico y recibir correcciones respetuosas cuando un término o una explicación no sean correctos.
- **Repasar y ganar autonomía:** practicar con preguntas breves y retomar conceptos que necesitan refuerzo.

El profesor puede utilizar ejemplos, analogías, esquemas o trazas. Ajusta sus propuestas según tus preferencias y las evidencias disponibles, sin etiquetarte con un estilo de aprendizaje fijo. También puede preparar una clase oral para un trayecto si la plataforma y el dispositivo admiten voz.

## Empieza con una petición

En un entorno compatible donde tengas disponible Code Mentor Backend, prueba alguna de estas frases:

> «Usa Code Mentor Backend para explicarme este método. Un concepto cada vez y comprueba si lo entiendo».

> «Tengo que refactorizar una llamada que antes esperaba null. Ayúdame a identificar los casos y a entender el contrato del resultado».

> «Quiero aprender a depurar este fallo. Guíame paso a paso y explícame qué debo observar».

> «Rubén me ha pedido estudiar los operadores de C#. Ayúdame a abordarlos según mis conocimientos previos».

> «¿Qué formas de explicación me están ayudando más, según las evidencias que tienes? Dime también qué información te falta».

Puedes pedir ayuda directa cuando la necesites. Revisa las explicaciones y los cambios antes de aplicarlos: el profesor puede equivocarse y debe basarse en el código y las evidencias disponibles.

## Atajos del profesor

Cuando Code Mentor Backend esté activa, puedes escribir estos atajos como texto, seguidos de los detalles que quieras. También puedes hablar con el profesor con normalidad. No son comandos nativos de ChatGPT o Codex y no activan la skill por sí solos.

| Atajo | Para qué sirve |
| --- | --- |
| `/instrucciones` | Ver los atajos más usados; pide la lista completa cuando la necesites. |
| `/aprender` · `/estudiar` · `/repaso` | Aprender un concepto, estudiar documentación o practicar lo ya visto. |
| `/tarea` · `/leer` · `/refactorizar` | Organizar una tarea, comprender código o guiar una refactorización. |
| `/depurar` · `/corregir` | Investigar un fallo o revisar tu explicación o código. |
| `/pista` · `/solución` · `/vocabulario` | Pedir una ayuda breve, una solución directa o una definición. |
| `/progreso` · `/guardar` · `/continuar` | Consultar evidencias, guardar lo autorizado o retomar donde sea posible. |
| `/voz` | Preparar una clase oral adaptada al tiempo disponible. |

Ejemplo: `/estudiar operadores de C#`. El guardado sigue dependiendo de un destino accesible, permisos y aceptación cuando corresponda.

## Usar la skill en ChatGPT o Codex

El código de la skill está en [skills/code-mentor-backend](skills/code-mentor-backend/). Para utilizarla, necesitas que esté instalada o disponible en una superficie compatible y que la conversación pueda acceder a sus instrucciones y recursos. La disponibilidad de skills, voz y herramientas de archivos depende del entorno.

Tener este repositorio o leer el archivo en GitHub **no demuestra que la skill esté activa** en una conversación. Para comprobarlo, puedes preguntar:

> «Comprueba si tienes disponible Code Mentor Backend. Lee sus instrucciones cargadas y dime la versión y desde dónde las has leído. Si no puedes acceder, dímelo».

Si solo puede leer GitHub, la respuesta confirma la versión del repositorio, no la de una instalación activa.

## Memoria y progreso

La skill puede preparar registros de lo trabajado: conceptos, dificultades, logros demostrados, ayuda recibida, preguntas pendientes y próximos pasos. También puede registrar qué explicaciones o ejercicios se utilizaron y sus resultados, para orientar las siguientes sesiones.

La actualización se propone tras bloques significativos y al cerrar una sesión. Se agrupa al terminar una tarea, tras tres sesiones completas desde la revisión anterior, cuando se repite una dificultad o cuando la solicitas. **No depende de un número fijo de mensajes.** Las fichas de conocimiento se proponen con identificador, fechas e historial; su contenido requiere tu aceptación antes de guardarse.

Para conservar esta información entre sesiones necesitas acordar un **destino persistente** y darle acceso de escritura al entorno que uses. La skill puede guardar y verificar los cambios cuando cuenta con las herramientas y los permisos necesarios. Si no puede escribir, prepara un paquete pendiente y puede ofrecerte continuar en Work; tú decides cuándo hacerlo. Si un chat dispone de otra herramienta con escritura autorizada, puede utilizarla sin pasar a Work.

La skill no crea permisos por sí sola, no trabaja en segundo plano ni garantiza sincronización automática. Sin un destino accesible, una nota visible en el chat no equivale a una memoria guardada. Puedes pedir: «¿Qué has guardado, dónde y qué queda pendiente?».

Separa el perfil general de aprendizaje del contexto laboral. No publiques código confidencial, credenciales ni datos privados; compartir información de trabajo entre entornos requiere autorización. Consulta la [guía de memoria](docs/session-memory.md) para conocer los detalles.

## Cómo se organiza el repositorio

| Recurso | Contenido |
| --- | --- |
| [SKILL.md](skills/code-mentor-backend/SKILL.md) | Instrucciones principales del profesor y recursos que consulta según la tarea. |
| [Flujos prácticos](skills/code-mentor-backend/references/practical-workflows.md) | Guías para trabajar con tareas, revisión de código, ejecución y depuración. |
| [Biblioteca de conocimientos](docs/knowledge-library.md) | Estudio, fichas personales, fuentes e historial. |
| [Adaptación docente](docs/adaptive-teaching.md) | Preferencias, observaciones y uso prudente de evidencias y gráficos. |
| [Cierre y memoria](docs/session-memory.md) | Cuándo guardar, permisos, continuidad y alternativa cuando no hay escritura. |
| [Pruebas](tests/) | Comprobaciones de las utilidades de registro y adaptación. |

La skill combina instrucciones, referencias, plantillas y utilidades locales. Los registros reales de cada alumno se mantienen fuera del paquete y del repositorio público. Las plantillas no son, por sí mismas, un historial de aprendizaje.

## Versiones y publicación

La **skill en el código fuente declara la versión 2.6**. El último [paquete descargable preparado](dist/code-mentor-backend-2.4.0.zip) y el manifiesto portable corresponden a **2.4.0**; no incluyen las mejoras posteriores de la fuente. Consulta la versión de tu instalación para saber qué funciones tienes disponibles.

Existe un borrador de publicación 2.3.0 que **no se ha enviado ni aprobado**. En la última comprobación, el portal indicaba que no aceptaba nuevas solicitudes de complementos que solo contienen skills. La [guía de preparación](docs/submission-readiness.md) recoge el estado de la revisión y sus comprobaciones para 2.4.0.

## Soporte, privacidad y licencia

- [Soporte](docs/support.md) · [Política de privacidad](docs/privacy.md) · [Condiciones de uso](docs/terms.md).
- Código disponible bajo [licencia MIT](LICENSE).
- Autor: David Valadés.
