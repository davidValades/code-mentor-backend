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

- [ ] Crear references/teaching-exploration.md y assets/templates/teaching-exploration.md en skills/code-mentor-backend.
- [ ] Conectar SKILL.md, teaching.md, adaptive-teaching.md y adaptation-contract.md.
- [ ] Integrar episodios/pendientes en referencia y plantilla de cierre y plantilla de preferencias.
- [ ] Revisar vínculos, IDs, separación entre declaración y evidencia y cinco condiciones de Review Focus.

## Tarea 2 — Documentación y verificación

- [ ] Actualizar README.md y docs/adaptive-teaching.md; declarar fuente 2.7 y paquete portable 2.4.0.
- [ ] Verificar enlaces y preservación de atajos/contratos; releer todos los archivos guardados.
- [ ] Comprobar con un escenario sintético sin registrar progreso del alumno.
- [ ] Informar por separado fuente actualizada e instalación/ejecución no verificadas.

## Entorno de ejecución

El entorno local está desconectado. No se ejecutan ni modifican scripts Python, no se prepara un ZIP y no se afirma actualizar la instalación personal o el complemento privado. Las modificaciones del repositorio se guardan mediante el conector de GitHub.
