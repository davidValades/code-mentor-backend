# Session Memory Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Cerrar sesiones con continuidad y actualizar memoria por lotes verificables.

**Architecture:** Extender instrucciones y plantillas existentes, sin añadir ejecutores ni esquema. Mantener la skill personal, el complemento privado y la fuente pública coherentes.

**Tech Stack:** Markdown, YAML, JSON; utilidades Python existentes sin cambios.

**Spec:** ../specs/2026-10-27-session-memory-design.md

## Global Constraints

- Revisión cada tres sesiones; agrupar desencadenantes y no contar mensajes.
- Cero sincronización o transición de modo implícita; comprobar escritura real.
- Datos de empresa solo en ámbito autorizado; fichas aceptadas antes de escribir.

## Review Focus

- Chat sin escritura: paquete pendiente, sin éxito ficticio.
- Evidencia relatada o copiada: no convertir en autonomía.
- Reintentos y escritura parcial: aplicar solo lo pendiente tras lectura actual.
- Cambio de modo o voz: no presumir contexto transferido ni pedir pantalla al conducir.
- Complemento portable: no incluir policy.products incompatible; preservar identidad y prompts.

### Task 1: Cierre y contrato de persistencia

**Files:** SKILL.md, references/session-close.md, references/memory.md, references/storage-contract.md, references/voice.md, assets/templates/session-close.md, agents/openai.yaml.

- [x] Leer fuente y ejecutar escenario inicial con versión 2.3.
- [x] Añadir referencia/plantilla, enlazar y aclarar almacenamiento por capacidades.
- [x] Probar cierre sin escritura y aplicación repetida/parcial; validar la skill y ejecutar suite existente.
- [x] Guardar y verificar la actualización personal.

### Task 2: Distribución coherente

**Files:** plugin.json y overlay privado, README.md, docs/session-memory.md, docs/submission-readiness.md, fuente de skill y ZIP 2.4.0.

- [x] Actualizar complemento privado conservando identidad y comprobar lectura posterior.
- [x] Renovar documentación y paquete público, corrigiendo estado real de publicación.
- [x] Verificar publicación de archivos y equivalencia del paquete; documentar pruebas y límites.

## Resultado de verificación

62 pruebas de utilidades, validación básica de skill, esquema portable, enlaces y metadatos: aprobados. Cierre sin escritura conserva preferencias y procedencia; recuperación respeta replay exacto y estado concurrente. Revisión independiente detectó diario previo insuficiente; se añadió a referencia y plantilla. Prueba sintética de CLI: replay no duplica versión ni sobreescribe el perfil posterior. Actualización privada 2.4.0 guardada y releída; publicación de fuente y paquete pendiente de la verificación final de distribución.
