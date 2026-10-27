# Biblioteca de conocimientos — Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans for this small, authorized update.

**Goal:** Incorporar fichas personales y estudio de documentación al profesor existente.
**Architecture:** Referencias y plantillas Markdown externas a los registros personales; el script de memoria y su esquema 2 se mantienen.
**Tech Stack:** Markdown, YAML, Python para comprobaciones existentes y empaquetado.
**Spec:** ../specs/2026-10-27-knowledge-library-design.md

## Global Constraints

Conservar separación general/proyecto, guardar fichas solo tras aceptación, consultar solo contexto pertinente y no afirmar persistencia o ejecución sin evidencia.

## Review Focus

Registro inexistente; fuentes sin acceso o de otra versión; ficha duplicada bajo otro título; comprensión oral sin autonomía práctica; propuesta pendiente tras revisión de tres sesiones.

## Task 1: Guía y plantillas

- [x] Ejecutar escenario de referencia con la skill anterior y registrar carencias observadas.
- [x] Añadir references/documentation-study.md y references/knowledge-library.md; plantillas knowledge-card.md y knowledge-index.md.
- [x] Conectar referencias desde SKILL.md, curriculum.md, memory.md y storage-contract.md.
- [x] Resolver acceso, IDs, aprobación, historial, recuperación tras guardado parcial y separación empresarial sin nuevos comandos CLI.
- [x] Ejecutar escenario con la skill actualizada y uno alternativo sin acceso al registro; revisar resultados.

## Task 2: Documentación y distribución

- [x] Ampliar README y docs/knowledge-library.md; aclarar datos externos y privados.
- [x] Subir versión del paquete a 2.2.0, conservar enlaces e icono propio y actualizar descripción/prompts.
- [x] Validar la skill instalada, enlaces locales, ausencia de datos personales de aprendizaje, ZIP y 47 pruebas de la utilidad.
- [x] Guardar y verificar actualización de la skill personal y del repositorio GitHub; comparar archivos publicados con el contenido validado.

## Validación realizada

Skill instalada validada; enlaces locales comprobados; 47/47 pruebas de almacenamiento aprobadas. Escenario inicial: faltaban contrato de fichas, índice y recuperación definidos. Dos escenarios con la ampliación comprobaron actualización sin duplicar, conservación de ID/fecha, aceptación antes de guardar, y borrador pendiente sin archivos ni dominio inventado. Revisión independiente estática sin fallos importantes. Los 34 archivos publicados se compararon por hash con la fuente validada. Estas comprobaciones no garantizan todas las respuestas futuras ni constituyen aprobación de OpenAI.
