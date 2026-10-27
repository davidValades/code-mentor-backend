# Cierre de sesión y memoria por lotes — 2.4.0

## Objetivo y autorización

El usuario pide implementar en esta sesión el cierre del profesor, con resumen de lo trabajado, aprendizajes demostrados y pendientes, y propuesta periódica de actualizar memoria con Work cuando Chat no puede escribir. Mantener la skill existente; no crear app, servidor ni tarea programada. Se reutilizan las preferencias ya acordadas de privacidad, fichas aprobadas y revisión cada tres sesiones. Las elecciones rutinarias siguientes son decisiones de implementación, no nuevas preferencias atribuidas al usuario.

## Enfoques

- Guardar con Work cada mensaje: interrumpe y consume uso sin aportar una unidad de aprendizaje; descartado.
- Guardar por lotes al cerrar tarea, cada tres sesiones completas, ante dificultad repetida o petición: implementado sobre la revisión existente. Preparar una nota breve al cerrar cada sesión y acumular lo pendiente.
- Solo copiar manualmente toda la conversación: no ofrece el registro verificable solicitado; conservar únicamente como salida cuando faltan herramientas.

## Diseño

Una referencia de cierre y una plantilla definen un paquete con identidad estable, sesiones incluidas, ámbito/destino, hechos con procedencia, cambios propuestos y recibo de persistencia. Separar nota operativa autorizada de fichas pendientes de aceptación. No inventar evidencia, dominio ni sesiones. Preparar el paquete en la conversación no acredita persistencia ni transferencia entre modos.

Con escritura persistente comprobada, aplicar cambios autorizados al mismo registro y leer los resultados. Sin ella, dejar un único paquete visible y un texto breve para que el usuario active Work o lo lleve al entorno con acceso. Work no tiene permisos por su nombre: descubrir capacidad real, comprobar destino y revisión, conciliar pendientes, evitar duplicados y verificar escritura. En Biblioteca reemplazar la misma identidad; un adjunto de solo lectura no se modifica con shell. Sin registro JSON accesible, el Markdown es narrativo y no acredita contadores calculados ni gráficos.

## Restricciones

No pasar a Work, gastar créditos comprados, conceder permisos ni crear sincronización automáticamente. Las fichas requieren aceptación exacta. Mantener datos laborales en proyecto local y pedir autorización del resumen exacto antes de trasladarlo. En conducción no pedir interacción con pantalla. No registrar esta conversación de diseño ni los datos sintéticos de prueba como aprendizaje.

## Verificación

Escenario inicial con skill 2.3: ofrece resumen sin guardado ficticio, pero sin paquete de aplicación con identidad/estado ni instrucción de actualización por lotes. Prueba posterior con el cierre nuevo; caso adicional con paquete repetido, escritura parcial y estado concurrente. Validar el paquete privado con su ingestión real y comprobar los archivos de la versión guardada. El portal público sigue siendo un canal distinto y su restricción de skills-only no se resuelve con esta actualización.
