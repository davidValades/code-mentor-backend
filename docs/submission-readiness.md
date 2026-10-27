# Estado de distribución y revisión — 2.4.0

Actualizado el 27 de octubre de 2026. Preparación, instalación privada, envío y publicación son estados distintos. No se garantiza aprobación ni eficacia educativa.

## Estado comprobado

- La skill personal declara v2.4 y añade cierre de sesión, preferencias y actualización de memoria por lotes.
- El complemento privado existente se ha actualizado a 2.4.0, conservando identidad y visibilidad. La lectura posterior confirma las nuevas instrucciones y plantilla.
- La organización prevista figura verificada y admite acceso desde la cuenta elegida por el autor.
- Existe un borrador público 2.3.0, no enviado ni publicado. El portal muestra el bloqueo «We are not accepting more skills-only submissions at this time». No se ha comprobado una fecha de reapertura.
- La ingestión portable descartaba la skill por policy.products incompatible. Se ha eliminado del paquete actualizado; la copia privada reconoce sus archivos. El borrador antiguo no acredita que 2.4.0 haya pasado análisis públicos.
- Esta versión no se ha subido al portal público. No se han aceptado declaraciones legales en nombre del desarrollador.

## Material y validación

| Elemento | Resultado |
| --- | --- |
| Nombre y categoría | Code Mentor Backend; Education & Research. |
| Alcance | Tutor C#/.NET en español; sin MCP, servidor propio ni recogida automática por el creador. |
| Países, pagos y licencia | Todos los disponibles; sin compras; MIT. |
| Ficha | Base en inglés, traducción es-ES y tres prompts; límites de persistencia y Work explicados. |
| Soporte y privacidad | Cuatro enlaces públicos del repositorio; privacidad por davidvaladesnavarro@gmail.com. |
| Icono | Libro y bombilla propios, sin símbolo C#; PNG cuadrado dentro de límites. |
| Paquete | Portable plugin.json, skills/ y assets/; sin credenciales, app bindings, hooks ni memoria real. |
| Utilidades | 62 pruebas aprobadas; scripts existentes sin cambios. |
| Formato | Skill, esquema portable, versión, política, límites de ficha y enlaces internos validados. |
| Flujo nuevo | Cierre sin escritura y recuperación tras interrupción probados con escenarios sintéticos. Revisión independiente detectó la necesidad de diario previo por operación; incorporada. |
| Recuperación | Reintento exacto en raíz temporal sintética conserva la actualización de otro escritor sin nueva versión duplicada. |
| Archivos reales | En Work se creó, reemplazó y leyó un documento de prueba. En el chat normal del usuario no se logró escritura y se solicitó Work. No demuestra compatibilidad de todos los chats o de voz. |
| Privacidad | QA no se considera progreso real. Datos laborales no se transfieren por cerrar una sesión. |

## Paquete

[ZIP 2.4.0](../dist/code-mentor-backend-2.4.0.zip).

SHA-256: de3a994ca59c41c4a5e07bcec3d8d223118cb3cc319540f0cc812ae90c43dce8.

Pruebas: `MENTOR_SKILL=/ruta/a/la/skill python -m unittest discover -s tests -q`. Las pruebas no garantizan eficacia educativa ni escrituras futuras.

## Pendientes públicos

1. Confirmar que el portal acepta este tipo de solicitudes o consultar elegibilidad a soporte. No añadir MCP ajeno al objetivo para sortear el bloqueo.
2. Actualizar el borrador existente con el paquete corregido cuando proceda y revisar inventario y hallazgos reales.
3. Comprobar nombre público frente a identidad verificada, ficha, icono, países y versión; esperar análisis requeridos.
4. El desarrollador completa personalmente las declaraciones legales y de políticas.
5. Enviar a revisión; publicar tras aprobación como acción separada.

Cada alumno todavía debe acordar destino y comprobar acceso. Actualizar el profesor no configura su carpeta ni habilita escritura en Chat o voz. No hay trabajo de fondo.

## Referencias oficiales

- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/plugin-guidelines
- https://learn.chatgpt.com/docs/build-skills
- https://learn.chatgpt.com/docs/get-started-with-work

La disponibilidad y los requisitos efectivos del portal prevalecen sobre esta lista; no hay plazo prometido.
