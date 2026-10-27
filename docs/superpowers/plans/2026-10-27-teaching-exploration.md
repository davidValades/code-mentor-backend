# Exploración gradual de ayudas — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox syntax for tracking.

**Goal:** Incorporar la exploración gradual y el feedback acordados a la skill y al README.

**Architecture:** Mantener CLI, IDs y esquema existentes. Añadir protocolo y plantilla narrativa con vínculos a evidencias; conectar enseñanza, cierre y documentación.

**Tech Stack:** Markdown; utilidades Python existentes sin modificaciones.

**Spec:** ../specs/2026-10-27-teaching-exploration-design.md

## Global Constraints

- Una ayuda principal por bloque; tareas y repasos normales.
- Feedback al estrenar una ayuda en ese contexto o ante atasco, separado de evaluación.
- Sin nuevos campos, IDs, operaciones o contadores en la CLI.
- Sin datos del alumno en el paquete ni promesas de instalación.

## Review Focus

- Sin memoria accesible: declarar límite y conservar pendientes.
- Valoración positiva sin práctica: no acreditar dominio.
- Conducción: interacción oral y práctica de pantalla pendiente.
- Ayudas combinadas: no atribuir el resultado a componentes aislados.
- Regenerar report: conservar análisis narrativo fuera del balance derivado.

## Tarea 1 — Protocolo y registro

- [x] Crear references/teaching-exploration.md y assets/templates/teaching-exploration.md en skills/code-mentor-backend.
- [x] Conectar SKILL.md, teaching.md, adaptive-teaching.md y adaptation-contract.md.
- [x] Integrar episodios/pendientes en referencia y plantilla de cierre y plantilla de preferencias.
- [x] Revisar vínculos, IDs, separación entre declaración y evidencia y cinco condiciones de Review Focus.

## Tarea 2 — Documentación y verificación

- [x] Actualizar README.md y docs/adaptive-teaching.md; declarar fuente 2.7 y paquete portable 2.4.0.
- [x] Verificar enlaces y preservación de atajos/contratos; releer todos los archivos guardados.
- [x] Comprobar con un escenario sintético sin registrar progreso del alumno.
- [x] Informar por separado fuente actualizada e instalación/ejecución no verificadas.

## Entorno de ejecución

El entorno local está desconectado. No se ejecutan ni modifican scripts Python, no se prepara un ZIP y no se afirma actualizar la instalación personal o el complemento privado. Las modificaciones del repositorio se guardan mediante el conector de GitHub.

## Verificación realizada

- Snapshot de entrada: 12b68e23f3e36e05c948d76789c90913e6a72d4f.
- Fuente candidata revisada: b5681ca8a68f9fcf525459472c8f62491574c009.
- Nueve comprobaciones estáticas: 16 atajos conservados; versiones explícitas; 14 variantes con IDs admitidos; frontmatter conservado; scripts/estado/manifiesto intactos; feedback separado de evaluación; demora compatible; 42 enlaces relativos resueltos; lecturas de entrada coincidentes con el snapshot.
- Los 13 archivos de la candidata se releyeron y coincidieron exactamente con el contenido propuesto.
- Comparación de árboles: ningún archivo eliminado y ningún cambio fuera de los 13 previstos.
- Revisión independiente de fuente, enseñanza, adaptación, memoria y cierre: sin errores importantes identificados.
- Escenario sintético: alumno que conoce true/false, se pierde al seguir llamadas y carece de carpeta de memoria. La respuesta introdujo una traza con un ejemplo C# pequeño, distinguió llamada y cuerpo del if, pidió solo claridad al final y declaró que no había progreso guardado.
- La prueba fue una respuesta de modelo sobre la fuente candidata, no uso de una instalación activa ni evidencia de eficacia o progreso de un alumno real.
- Sin ejecución Python ni quick_validate por ausencia de entorno local. No se modificaron scripts. La actualización de la instalación personal y del complemento privado permanece pendiente.
