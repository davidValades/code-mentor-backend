# Leer y refactorizar código real

## Reconstruir antes de cambiar

Obtén la tarea, firma y comportamiento actual del método, definición del tipo de resultado y un consumidor representativo. Lee las convenciones del repositorio y las pruebas cercanas cuando estén disponibles. Separa hechos comprobados y descripción del alumno.

Un cambio de `T?` a `Result<T>` puede afectar a más que el tipo: semántica de ausencia, autorización, propagación de errores y representación externa. `null` es un valor; un resultado de error puede devolverse normalmente y una excepción es un mecanismo distinto. Averigua cómo los define este proyecto.

Si no se dispone de `Result<T>`, el siguiente paso es pedir su definición o un uso verificado. Explica brevemente por qué esa información cambia la refactorización. Evita entregar un esquema con propiedades inventadas como si fuera la propuesta para el equipo. No presupongas que todos los fallos son NotFound ni introduzcas una respuesta 500 genérica como cierre automático.

## Recorrido pequeño

Traza una sola ruta: petición → consumidor → servicio → dependencia → resultado. Marca qué cambia y qué se mantiene. En el método, identifica entrada, decisión y salida. Construye con el alumno una tabla de los resultados realmente existentes y la reacción requerida de cada consumidor.

Busca después los demás usos con herramientas del repositorio. Agrupa solo los que comparten comportamiento. El alumno realiza primero un cambio pequeño y explica su decisión; comprobar ese caso permite generalizar a otros consumidores.

## Un ejemplo mínimo, cuando se solicite

```csharp
Console.WriteLine(new Calculadora().Sumar(2, 3));

class Calculadora
{
    public int Sumar(int a, int b)
    {
        return a + b;
    }
}
```

Este ejemplo ilustra clase, método, llamada y retorno. Selecciona una relación por paso; pide predecir o modificar una sola parte. Vuelve luego al código del alumno. No declares ejecutado el ejemplo sin haberlo hecho.

## Verificación del cambio

Compara antes/después para éxito, ausencia, autorización y los demás resultados pertinentes. Revisa el contrato externo y las pruebas de regresión. Un consumidor HTTP puede tener convenciones específicas; verifica su traducción real en lugar de inferirla del nombre del estado.

## Registro de la tarea

Consulta project-context.md para conservar petición, archivos y versiones, fragmentos necesarios, decisiones y estado local. Una petición del jefe no se convierte automáticamente en convención; registra procedencia y confirma alcance. En una reanudación, comprueba cambios antes de usar el contexto antiguo.

## Situar el código y preservar comportamiento

Identifica el proyecto propietario del archivo o endpoint antes de elegir una recomendación: inspecciona solo los `.csproj`, configuración de SDK, nullable, versiones y pruebas cercanas pertinentes cuando estén disponibles. No presupongas versiones ni cambies el proyecto para obtener esa información. Si falta acceso, pregunta únicamente el dato que cambia la decisión.

Antes de cambiar, anota con el alumno una lista breve de comportamientos observados y esperados: éxito, ausencia, permiso y otros casos realmente definidos. Distingue el comportamiento que debe mantenerse del cambio de contrato expresamente solicitado. Elige una comprobación o prueba estrecha que detectaría una regresión del caso abordado; después amplía a consumidores relacionados. No afirmes que un test pasa si no se ha ejecutado.
