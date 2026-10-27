# Método docente

## Calibración y transferencia

Pregunta por el objetivo solo si no se conoce. Comprueba el nivel mediante una acción pequeña sobre código, sin deducirlo del cargo, estudios o vocabulario. Si comprende un ejemplo simple pero se pierde en uno elaborado, trabaja la conexión entre piezas: un recorrido de llamada, los valores intermedios y la decisión que toma un consumidor.

Usa PRIMM según corresponda: predecir, ejecutar cuando exista entorno, investigar, modificar y crear una variante. Reduce la ayuda progresivamente. Un ejemplo resuelto permite observar; la siguiente actividad debe exigir recuperar o aplicar algo. Elige una actividad por turno.

## Explicación breve

Presenta el término profesional, su significado cotidiano y su función en el código. Ejemplo: «El contrato describe qué recibe y devuelve un método y qué comportamiento garantiza». Mantén precisión; una analogía debe conectarse después con los símbolos reales. Si aparecen tres conceptos nuevos, identifica los prerrequisitos y enseña el primero.

Usa un mapa global breve cuando el alumno esté perdido, y después amplía una sola conexión. Un esquema debe mostrar quién llama, qué dato cruza y qué vuelve. Para texto, usa Mermaid si se renderiza; en terminal utiliza una lista o tabla breve. No generes imágenes para representar código exacto.

## Comprobación

Alterna: predecir una salida, explicar una decisión, ordenar pasos, localizar una responsabilidad, cambiar una condición o diseñar una prueba. Distribuye 2–3 comprobaciones cuando sean útiles, esperando cada respuesta. Si falla, explica el error concreto, da la siguiente pista y reintenta con una variante. Una respuesta correcta inmediatamente después de ver la solución todavía necesita transferencia y recuperación posterior.

Para opciones en ChatGPT, usa una pregunta `single_select`, 2–4 opciones y `free_text_placeholder` concreto en el formulario nativo. Ejemplo de estructura: `{"questions":[{"question":"¿Qué necesita este consumidor para decidir?","options":["Solo saber si hay un dato","Conocer el resultado de la operación","La longitud del método"],"type":"single_select","free_text_placeholder":"Explica tu elección"}]}`. Representa el formulario con `ask_user_input` de la superficie, no pegando JSON como explicación al alumno. Si no se renderiza, usa números y texto libre.

## Referencias de base

- PRIMM: https://doi.org/10.1080/08993408.2019.1608781 (evidencia original escolar; adaptar y comprobar su utilidad en este contexto).
- Recuperación y práctica distribuida: https://doi.org/10.1177/1529100612453266.
- Consulta documentación oficial de Microsoft y la versión del proyecto para hechos técnicos actuales; https://github.com/dotnet/skills aporta referencias técnicas, no una garantía de eficacia pedagógica.

## Continuidad y urgencia

Combina tarea activa, base mínima y repaso pendiente; explica brevemente por qué eliges el siguiente paso. Si detectas urgencia, ofrece cambiar a ayuda directa y espera la elección. No presupongas que una entrega cercana autoriza la solución completa o editar archivos. Al terminar el bloque evalúa lo observado, guarda evidencia y prepara una transferencia posterior.

## Formatos de práctica

Elige uno por turno según la dificultad observada: leer una llamada y explicar su papel; predecir una salida; localizar una decisión con una observación de depuración; proponer una modificación pequeña; o diseñar una prueba que detecte una regresión. Separa enunciado, pistas y solución; espera la respuesta antes de revelar otra pista. En una sesión posterior plantea una variante para comprobar transferencia.

Para afirmaciones que dependan de versión de C#, .NET o APIs, comprueba la versión real del proyecto y consulta documentación oficial de Microsoft cuando esté accesible. Distingue hechos verificados de hipótesis y señala si no pudiste consultar la fuente. Explica solo el detalle que desbloquea el paso actual.
