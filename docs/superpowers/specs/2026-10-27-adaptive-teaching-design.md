# Diseño propuesto: adaptación docente por evidencias

Estado: propuesta para revisión; todavía no implementada. Fecha: 2026-10-27.
Enfoque elegido: combinar preferencias del alumno, necesidades del concepto y resultados observados.

## Objetivo y enfoques considerados

Orientar al profesor hacia ayudas útiles en situaciones parecidas, sin clasificar al alumno con un estilo fijo.
Se consideraron preferencias únicamente (fáciles pero no miden aprendizaje), resultados únicamente (mejor evidencia pero pueden ignorar comodidad y accesibilidad), y enfoque combinado (seleccionado). Las observaciones personales apoyan decisiones provisionales; no son un experimento causal ni una prueba de eficacia general.

## Cómo decide el profesor

1. Recuperar preferencias, evidencias recientes, checkpoint y contexto permitido; abrir solo los resultados pertinentes.
2. Ante dificultad, comprobar primero si falta un prerrequisito, si hay sobrecarga o si el enunciado es ambiguo.
3. Elegir una ayuda apropiada para el concepto y el entorno: esquema, analogía con límites, trazado, ejemplo resuelto seguido de práctica, comparación de casos, explicación propia, predicción o depuración guiada.
4. Si hay antecedentes comparables, priorizar una estrategia prometedora. Sin ellos, aplicar una opción razonable al contenido y marcar que falta evidencia personal.
5. Observar la respuesta y ayuda necesaria; preparar una comprobación en un ejemplo distinto y una recuperación posterior cuando proceda.
6. Si no funciona, reducir el paso, revisar prerrequisitos o cambiar una ayuda. No insistir por una clasificación previa.

Se mantienen práctica de recuperación y repasos. Por voz durante conducción no se requieren pantallas, escritura ni manipulación del dispositivo; no se acredita autonomía de programación con una respuesta oral.

## Memoria privada

Dentro de la raíz persistente ya acordada, una carpeta adaptacion/ separada de las fichas:
- preferencias.md: preferencias y restricciones declaradas, fecha y alcance.
- observaciones.jsonl: registros con ID estable y referencia a evidencia existente, sesión, fecha, concepto, tarea, modalidad, ayudas usadas, grado de ayuda, criterio y resultado observable. Puede registrar una combinación de estrategias sin atribuir el efecto a una sola.
- balance.md: síntesis derivada por concepto/tipo de tarea/modalidad, número de observaciones, límites, recencia y recomendaciones provisionales.
- graficos/: representaciones derivadas del mismo registro y fecha de generación.

El formato concreto se validará en la implementación. No se inventan campos o comandos de mentor_store.py; el esquema 2 existente sigue siendo fuente de evidencias y contadores. Si la evidencia no se guardó, una observación no inventa su ID ni se considera confirmada. Se conserva la separación general/proyecto y no se publican los registros personales en el repositorio público.

## Qué significa éxito

Registrar por separado:
- comprensión inmediata observada;
- aplicación a un caso nuevo;
- recuperación en una sesión posterior y demora real;
- grado de ayuda;
- claridad/esfuerzo/preferencia declarados por el alumno.

No usar rapidez como criterio principal ni convertir satisfacción en dominio. Conservar errores y ausencias de evaluación; distinguir cero aciertos de una comprobación pendiente. No mezclar pruebas orales e IDE, tareas muy diferentes o niveles de ayuda distintos en una tasa global.

## Gráficos

Tabla o gráfico por contexto y estrategia, con resultados como aciertos/intentos comparables, ayuda y retención diferida, siempre mostrando denominador y datos pendientes. Con pocos datos mostrar observaciones y estado «evidencia insuficiente», no porcentajes aparentando precisión ni un ranking global del alumno. No habrá datos ficticios ni perfiles «80 % visual».

Generar Markdown y un gráfico estático exportable cuando haya observaciones útiles; sin app ni panel nuevo. El gráfico no es la memoria: se reconstruye a partir de registros. Se actualiza al revisar, durante una sesión activa.

## Frecuencia y autonomía

Las adaptaciones del siguiente paso se eligen sin interrumpir cada explicación, dentro del modo tutor y los permisos existentes. Ocasionalmente puede proponerse una variante breve en una práctica normal, sin convertir las clases en experimentos continuos.

Revisar cada tres sesiones, antes si se repite una dificultad o el alumno lo pide. Señalar confusores como experiencia previa, dificultad, secuencia o varias ayudas simultáneas; no proclamar causalidad. Reutilizar review_due y el ciclo de improvement-loop.md, sin segundo contador.

Guardar observaciones operativas solo en el ámbito autorizado. Pedir configuración si no existe y distinguirla de aceptar fichas de conocimiento. Una preferencia docente permanente nueva se propone, evalúa y acepta mediante el ciclo existente; probar una explicación no modifica el paquete ni activa una regla general.

## Verificación prevista

Comprobar escasez de datos, preferencia sin éxito, múltiples ayudas simultáneas, éxitos solo con pistas, retención pendiente, voz sin IDE, registros sin acceso, datos antiguos y preferencia empresarial específica. Los gráficos y balances deben ser trazables a evidencias reales; las revisiones no garantizan eficacia educativa.

## Base investigadora y límites

La investigación informa el diseño general; no valida este profesor personalizado:
- Clinton-Lisell y Litzinger (2024), revisión de estilos: https://doi.org/10.3389/fpsyg.2024.1428732
- Dunlosky et al. (2013), técnicas de aprendizaje: https://doi.org/10.1177/1529100612453266
- Karpicke y Blunt (2011), recuperación y aprendizaje conceptual: https://doi.org/10.1126/science.1199327
- Kalyuga et al. (2003), interacción con experiencia: https://doi.org/10.1207/S15326985EP3801_4

No hay diagnóstico, estilo fijo, proceso en segundo plano, entrenamiento de pesos ni sincronización automática.
