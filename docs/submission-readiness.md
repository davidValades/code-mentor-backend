# Preparación para revisión de OpenAI — 2.3.0

Comprobaciones del 27 de octubre de 2026. Este documento distingue preparación técnica de presentación y aprobación. No es una certificación de OpenAI ni una garantía de aprobación o eficacia educativa.

## Material preparado

| Elemento | Resultado |
| --- | --- |
| Identidad prevista | David Valadés, persona individual; el usuario confirmó que aparece Verified. Pendiente comprobar la identidad importada en el portal. |
| Nombre y categoría | Code Mentor Backend; Education & Research. |
| Alcance | Una skill de tutoría C#/.NET en español; sin MCP, servidor propio ni recogida automática por el creador. |
| Países y pagos | Todos los disponibles; gratuito, sin compras. |
| Ficha | Campos base en inglés, traducción es-ES incluida y tres prompts de inicio. |
| Políticas y soporte | Páginas públicas del mismo repositorio; correo de privacidad davidvaladesnavarro@gmail.com, recepción confirmada por el usuario. |
| Icono | PNG propio de libro y bombilla, sin símbolo C#; cuadrado 1254×1254, menos de 5 MiB. |
| Licencia | MIT, incluida en el ZIP. |
| Paquete | Portable plugin.json, skills/ y assets/; sin app bindings, hooks, credenciales ni registros reales del alumno. |
| Pruebas | 47 pruebas del registro principal + 15 de adaptación = 62 aprobadas. |
| Formato | Validación contra el esquema portable 1.0.0 y validación básica de SKILL.md aprobadas; límites de ficha, enlaces internos y contenido del ZIP comprobados. |
| Docencia | Escenarios con ayuda/dificultad diferentes, conducción y registro inaccesible revisados; no se inventaron rankings, aprendizaje ni guardados. |
| Gráfico | Renderizado e inspeccionado con datos sintéticos de QA; esos datos no se incluyen como progreso del alumno. |
| Revisión independiente | Detectó tres problemas de frescura/etiquetas/contadores; reproducidos mediante pruebas que fallaban y corregidos con suite completa aprobada. |
| Vídeo y credenciales de prueba | No aplicables a un complemento solo de skills, según la documentación de envío vigente. |

## Archivos para preparar el envío

[Descargar el ZIP 2.3.0](../dist/code-mentor-backend-2.3.0.zip).

SHA-256 del ZIP: 42eced50894f0a710990204ec41404acbf2ff6d884210df550c3430b55bb6b5b.

Los tests se ejecutan con MENTOR_SKILL apuntando a la carpeta instalada o a una copia de revisión: python -m unittest discover -s tests -q. Las pruebas de utilidades no demuestran resultados educativos del alumno.

## Comprobaciones del portal aún pendientes

1. Acceder a OpenAI Platform con la cuenta y organización verificadas y subir el ZIP como borrador.
2. Comprobar inventario (una skill, cero MCP), identidad pública, ficha, icono, países, traducciones y versión importada.
3. Esperar los análisis de metadatos y skills, revisar hallazgos y corregir errores requeridos para esa versión exacta.
4. El desarrollador debe revisar y completar personalmente las declaraciones legales y de políticas que solicite el portal. No se han aceptado en su nombre.
5. Enviar el borrador a revisión solo cuando lo anterior esté completado. Publicar tras aprobación es una acción separada.

No se ha presentado esta versión a revisión ni se han ejecutado los análisis privados de OpenAI. El acceso al portal no se ha completado, por lo que no se ha podido verificar el estado de su organización ni crear un borrador online. Los cuatro enlaces públicos se comprobaron sin autenticación y el ZIP descargado del repositorio coincide con el SHA-256 indicado.

## Fuentes oficiales consultadas

- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/plugin-guidelines

Las condiciones del portal prevalecen sobre este listado cuando cambien. El paquete contiene cuatro enlaces públicos aunque la validación de metadatos para skills-only no exige los cuatro.
