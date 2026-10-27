# Cierres, memoria y continuidad — 2.4.0

La skill prepara las notas; el alumno no tiene que redactar el registro manualmente. Escribir y recuperar esas notas exige almacenamiento persistente accesible y autorización. Una skill o un complemento privado no crean carpetas ni permisos, y no garantizan las herramientas del modo de voz.

## Cuándo lo propone

- Tras cada bloque significativo: evidencia y punto para retomar, si hay acceso autorizado.
- Al cerrar cada sesión: nota breve de lo trabajado y pendientes.
- Al cerrar tarea, tras tres sesiones completas nuevas desde la revisión anterior, ante dificultad en dos sesiones distintas o por petición: una actualización agrupada. No se cuentan mensajes.
- Sin novedades: sin cambios. Si el alumno aplaza Work, no se repite la invitación en cada turno.

Una pausa conserva la sesión abierta. Cerrar la aplicación no provoca un guardado automático. No hay procesos de fondo, sincronización implícita ni recordatorios programados por este flujo.

## Qué se conserva

Objetivo, alcance, conceptos/prerrequisitos, ejercicios, cambios y pruebas realmente realizados, respuestas, grado de ayuda y modalidad, errores y términos corregidos, decisiones con procedencia, dificultades, dudas, siguiente acción y repaso orientativo. Distingue lectura, comprensión declarada, comprensión demostrada, práctica guiada, aplicación autónoma y recuperación posterior. Copiar o decir «entendido» no acredita dominio.

También conserva cómo se enseñó: preferencias declaradas, esquemas/analogías/trazas/ejemplos o combinaciones usadas, contexto y resultados, incluidas ayudas que no funcionaron. Al retomar una dificultad consulta estos antecedentes; no clasifica al alumno por estilos fijos ni infiere eficacia de una sola preferencia. Los gráficos requieren evidencias reales y las utilidades compatibles; un resumen Markdown no produce por sí solo estadísticas de aprendizaje.

## Chat sin escritura y Work

El profesor deja un único paquete visible, con ID y revisión, sesiones incluidas, destino o «sin configurar», nota y lista de cambios pendientes. Propone al usuario activar Work y adjuntar o pegar el paquete si el contexto no está disponible allí. Preparar el paquete no demuestra que se haya guardado fuera de esa conversación. No exige Work para seguir aprendiendo.

Work debe comprobar sus herramientas, el destino, la última versión y los lotes ya aplicados. Actualiza solo lo autorizado, conserva historial y lee el resultado. No crea otra copia para fingir que modificó un adjunto de solo lectura. Un reintento conserva IDs y aplica únicamente lo pendiente; si hubo un fallo parcial, muestra qué se guardó y qué no.

El usuario decide cuándo activar Work; se aplica el uso de su plan. No hay un coste fijo prometido ni compra automática de créditos. En conducción no se pide cambiar de modo, tocar pantalla ni adjuntar documentos.

## Ubicaciones y permisos

- Perfil general: conceptos, dificultades y logros sin información empresarial.
- Proyecto laboral: contexto y referencias permitidas en la raíz local acordada; no se exportan automáticamente.
- Documentos remotos: solo cuando exista herramienta con escritura sobre sus identidades reales. No se pasan sus IDs como rutas a la CLI local.
- Sin destino: el cierre permanece pendiente. Configurar ubicación y comprobar escritura/lectura se realiza una vez; la compatibilidad de un modo no demuestra la de otro.

Las notas operativas se guardan dentro de la autorización existente. Las fichas por concepto siguen requiriendo aceptar su contenido exacto. Compartir contexto laboral con otro entorno exige aprobar el resumen exacto. La memoria del profesor son estos registros, no una garantía de memoria general de ChatGPT.

## Comprobación de versión

La skill declara v2.4; el paquete usa 2.4.0. Para comprobar una instalación, pedir al agente leer su SKILL.md disponible y la referencia session-close.md. Leer esas páginas en GitHub verifica la fuente pública, pero no acredita que estén instaladas en ese chat. Después probar un cierre con contenido ficticio y verificar el documento original desde una lectura independiente.
