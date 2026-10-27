# Adaptación de la enseñanza por resultados

Code Mentor Backend 2.3 combina preferencias declaradas, necesidades del concepto y evidencias reales. No clasifica al alumno en estilos fijos ni garantiza que un método sea la causa de una mejora.

## Funcionamiento

El profesor recupera las fichas pertinentes y las observaciones disponibles. Ante dificultad comprueba primero prerrequisitos, tamaño del paso y claridad del enunciado; después elige una ayuda: esquema, analogía, trazado, ejemplo resuelto, comparación, explicación propia, recuperación o depuración guiada.

Registra qué se ha podido explicar o aplicar, con qué ayuda y si se recuerda después. La modalidad del aprendizaje y de la comprobación, dificultad, actividad y concepto se conservan por separado. Un acierto con pistas no demuestra autonomía. Una valoración positiva no es un resultado de aprendizaje.

La revisión aprovecha las tres sesiones del ciclo existente; se anticipa ante dificultades reiteradas o a petición del alumno. Las adaptaciones del siguiente paso respetan el modo tutor. Cambios permanentes siguen la evaluación y aceptación del ciclo de mejora.

## Archivos privados

Dentro de la raíz persistente acordada:

- adaptacion/preferencias.md: preferencias/restricciones declaradas y su alcance.
- adaptacion/observaciones.jsonl: observaciones con ID estable y referencia a evidencias existentes.
- adaptacion/balance.md: resultados derivados con fecha, revisión del registro y huella de observaciones.
- adaptacion/graficos/resultados.svg: gráfico estático de esos resultados.

Estos archivos se crean durante uso autorizado, no al instalar la skill. El repositorio público contiene la utilidad y plantillas vacías, no datos del alumno. Los detalles laborales se mantienen en su ámbito local. No hay transmisión al creador, sincronización automática ni proceso de fondo.

## Utilidad

Con Python 3.11+ y un state.json ya configurado, se puede ejecutar:

- python scripts/mentor_adaptation.py --root /ruta/absoluta record (JSON por stdin).
- python scripts/mentor_adaptation.py --root /ruta/absoluta read.
- python scripts/mentor_adaptation.py --root /ruta/absoluta report.

Consulta [el contrato exacto](../skills/code-mentor-backend/references/adaptation-contract.md) y la [guía docente](../skills/code-mentor-backend/references/adaptive-teaching.md) antes de usarla. La utilidad no cambia el esquema 2 principal. Valida evidencias, evita duplicados y deriva los resultados desde el estado vigente. Las fichas de conocimiento siguen un proceso aparte de propuesta y aceptación.

## Interpretación del gráfico

Muestra aciertos/intentos, pendientes y número de sesiones en cada contexto. No ofrece un porcentaje de estilo ni un ganador global. El aviso «Evidencia insuficiente» se usa si hay menos de tres intentos evaluados o de dos sesiones con intentos evaluados; es un criterio orientativo de presentación, no un umbral científico. Superarlo tampoco demuestra eficacia.

Los resultados de recuperación diferida requieren una evidencia anterior del mismo tema, otra sesión y al menos 24 horas. Los relatos sin comprobar, soluciones copiadas y evaluaciones pendientes no se cuentan como aciertos. Las ayudas combinadas se presentan juntas.

Antes de decidir, el profesor revisa recencia, dificultad y posibles diferencias entre ejercicios; la agrupación no elimina esos factores. Sin acceso al registro, informa del límite y prepara un borrador, sin afirmar guardado.
