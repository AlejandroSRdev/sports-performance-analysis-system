Documento Estratégico — V1
Sports Performance Analysis System
Club Baseball Vallès

1. Objetivo Estratégico
Diseñar un sistema backend operacional capaz de transformar estadísticas federativas reales y contexto proporcionado por entrenadores en análisis útiles para la toma de decisiones deportivas.
El objetivo principal NO es construir una plataforma deportiva genérica ni un SaaS complejo, sino crear una herramienta operativa utilizada en un entorno real para:
analizar progresión de jugadores;
detectar tendencias;
identificar áreas prioritarias de trabajo;
reducir carga analítica manual del entrenador;
y generar insights deportivos contextualizados mediante workflows gobernados por backend.

2. Posicionamiento Estratégico
El sistema se alinea con el posicionamiento actual:
Backend Systems
AI Systems
Operational Automation
Sports & Performance Systems
Applied Operational Workflows
La IA se trata como:
dependencia probabilística gobernada por backend.
El backend conserva autoridad sobre:
persistencia;
validación;
estructura;
reglas;
cálculos;
y límites de interpretación.

3. Problema Operacional Detectado
Actualmente:
las estadísticas federativas existen;
pero están dispersas;
son difíciles de interpretar longitudinalmente;
y requieren análisis manual por parte del entrenador.
El sistema busca convertir:
datos deportivos dispersos
 en
decisiones operativas concretas.

4. Objetivo Funcional de la V1
La V1 debe permitir que un entrenador pueda:
Ver evolución individual de jugadores.
Detectar tendencias positivas o negativas.
Identificar áreas prioritarias de mejora.
Obtener recomendaciones operativas simples.
Contextualizar el análisis con observaciones humanas reales.

5. Alcance Correcto de la V1
Incluir
Persistencia histórica de estadísticas.
Ingesta inicial manual o scraping simple.
Visualización básica de evolución.
Análisis determinista de tendencias.
Recomendaciones operativas asistidas por IA.
Contexto libre introducido por entrenador.

Excluir
Machine learning.
Predicción de rendimiento.
Scouting avanzado.
Biomecánica.
Visión artificial.
Frontend complejo.
Automatización completa del scraping.
Comparativas avanzadas entre múltiples equipos.
Diagnósticos físicos o psicológicos automáticos.

6. Fuentes de Datos
La V1 utilizará principalmente:
Overall Stats
Per-game Stats
Games Summary
Extraídos desde:
scraping controlado;
exportación manual;
o carga estructurada.

7. Arquitectura Conceptual
CAPA 1 — Ingesta
Obtención de datos federativos.
Responsabilidades:
scraping;
importación;
parsing;
normalización.

CAPA 2 — Persistencia
Base histórica estructurada.
Responsabilidades:
snapshots por jugador;
persistencia temporal;
continuidad histórica.

CAPA 3 — Analytics Determinista
Motor principal del sistema.
Responsabilidades:
tendencias;
rolling averages;
evolución;
consistencia;
alertas;
rankings;
comparación temporal.
La IA NO participa aquí.

CAPA 4 — Contexto Humano
Observaciones libres del entrenador.
Ejemplos:
cambios técnicos;
molestias;
adaptación táctica;
reducción de entrenamientos;
cambios de rol.
El sistema NO interpreta automáticamente estas observaciones.

CAPA 5 — IA Asistida
La IA:
resume;
contextualiza;
verbaliza;
prioriza.
La IA NO:
calcula;
diagnostica;
inventa causas;
infiere información no proporcionada.

8. Flujo Operacional
Paso 1
Ingesta de estadísticas.

Paso 2
Persistencia histórica.

Paso 3
Cálculo determinista de evolución y tendencias.

Paso 4
Entrada opcional de contexto por parte del entrenador.

Paso 5
Generación de resumen operacional mediante IA.

Paso 6
Visualización simple de resultados.

9. Filosofía del Sistema
El sistema NO intenta reemplazar criterio humano.
El sistema:
aumenta capacidad analítica;
reduce fricción operacional;
y estructura información útil.
La IA funciona como:
capa contextualizadora y comunicativa.
No como autoridad deportiva.

10. Restricciones Fundamentales
La IA NO puede:
inferir lesiones;
inferir estados emocionales;
inferir fatiga;
diagnosticar técnica;
inventar causalidad;
generar recomendaciones biomecánicas;
actuar fuera del contexto explícito proporcionado.

11. Stack Inicial
Backend:
Python
FastAPI
Persistencia:
PostgreSQL
Infraestructura:
Docker
Vercel/Fly.io según necesidad
IA:
OpenAI API
Frontend:
visualización mínima y funcional

12. Objetivo de Validación
La V1 se considerará validada si:
un entrenador utiliza el sistema repetidamente;
el análisis reduce tiempo manual;
las recomendaciones son percibidas como útiles;
y el sistema genera valor operativo observable.

13. Narrativa Profesional Resultante
“Diseñé un sistema backend de análisis deportivo para un club real que transforma estadísticas federativas y contexto del entrenador en insights operativos mediante análisis determinista y workflows asistidos por IA bajo gobernanza backend.”

14. Principio Rector Final
El objetivo NO es demostrar uso de IA.
El objetivo es:
transformar datos deportivos reales en decisiones útiles mediante sistemas backend fiables, observables y operacionalmente coherentes.