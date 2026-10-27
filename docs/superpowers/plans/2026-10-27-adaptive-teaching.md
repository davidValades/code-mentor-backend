# Adaptación docente y preparación de envío — Implementation Plan

> **For agentic workers:** Ejecutar en esta sesión; diseño aprobado al pedir terminar todo.

**Goal:** Completar adaptación por evidencias y paquete 2.3.0 comprobable.
**Architecture:** Referencias docentes y utilidad local de observaciones/representación derivada, conservando mentor_store esquema 2 como fuente de evidencias.
**Tech Stack:** Python 3.11 estándar, Markdown, JSONL, SVG; sin red ni proceso de fondo en las utilidades.
**Spec:** ../specs/2026-10-27-adaptive-teaching-design.md

## Global Constraints

Respetar ámbitos y permisos existentes; no inventar dominio, causalidad, datos ni aprobación. No guardar aprendizaje personal en el repositorio público.

## Review Focus

Escasez de datos; evidencias ausentes/corregidas; combinación de estrategias; pruebas de retención aún pendientes; voz y ayuda distinta no comparables.

## Tasks

- [x] Base de comparación con profesor anterior y pruebas RED de la nueva utilidad.
- [x] Implementar registro por ID de evidencia, agrupación por contexto/ayuda/tipo de comprobación y gráficos derivados; proteger reintentos, rutas y datos pendientes.
- [x] Actualizar guía, plantillas, memoria y ciclo de mejora; probar escenarios y revisar de forma independiente.
- [x] Validar almacenamiento anterior, nueva utilidad, paquete y privacidad de su contenido; publicar fuentes y registrar comprobaciones.
- [x] Verificar enlaces públicos y metadatos, comprobar guía oficial actual y preparar ZIP 2.3.0.
- [ ] Inspeccionar el portal si hay acceso; distinguir borrador, escaneos y declaraciones pendientes de una presentación a revisión.
