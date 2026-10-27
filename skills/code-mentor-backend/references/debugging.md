# Depurar para encontrar la causa

Empieza por un caso reproducible: entrada, resultado esperado, resultado observado y mensaje exacto del fallo. Si no hay error visible, delimita el primer punto donde un dato deja de tener el valor esperado.

En Visual Studio 2022, guía una operación cada vez y explica su propósito:

1. Colocar un punto de interrupción antes de la decisión sospechosa.
2. Reproducir el caso y comprobar que la ejecución se detiene en el recorrido esperado.
3. Inspeccionar parámetros y valores en Variables locales o Inspección. Predecir el valor antes de observarlo.
4. Usar paso por instrucciones o paso a procedimientos según necesitemos entrar en una llamada. Explicar qué opción corresponde al botón mostrado; no depender de atajos que puedan variar.
5. Consultar la pila de llamadas para conocer cómo se llegó al punto.
6. Contrastar una hipótesis concreta y elegir la siguiente observación según el resultado.

«Mira el resultado de esta llamada para comprobar si la ausencia se produce aquí» es una instrucción útil. «Pon breakpoints por todas partes» no delimita una hipótesis.

Lee tipos y valores reales. Una variable llamada result puede contener error, ausencia o dato válido según su contrato. Una excepción debe leerse con su mensaje, tipo, pila y excepción interna pertinentes.

Cuando la evidencia señale la causa, pide al alumno proponer el cambio más pequeño. Comprueba reproducción original, caso normal y regresión relacionada. Si solo se revisó código, informa de revisión estática; si se compiló o ejecutó, conserva la salida real. No sugieras cambiar arquitectura, agregar capturas de excepción o devolver valores por defecto antes de entender la causa.

En voz durante un trayecto, utiliza un caso oral corto sobre cómo elegir la siguiente observación. La ejecución en el IDE queda para una sesión frente al ordenador y no se acredita como realizada.

## Elegir el primer punto de observación

Clasifica provisionalmente por evidencia: fallo de compilación → diagnóstico y ubicación exactos; excepción → tipo, mensaje y pila; prueba fallida → aserción y resultado esperado/observado; respuesta HTTP inesperada → petición, ruta y punto donde se decide la respuesta. Un 404 no demuestra por sí solo si falló el enrutamiento o la búsqueda. Pregunta por una pieza cada vez y cambia de hipótesis si la observación la contradice. Para defectos del proyecto, comprueba primero el componente propietario y su configuración pertinente.
