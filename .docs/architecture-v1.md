Sports Performance Analysis System — Architecture Definition V1
Architectural Objective
The system architecture is designed to support:
Deterministic sports analytics
Longitudinal performance tracking
Controlled AI-assisted operational insights
Historical persistence continuity
Explicit workflow orchestration
Backend-governed analytical reliability
The architecture intentionally prioritizes:
Operational clarity
Structured persistence
Analytical traceability
Controlled AI integration
Progressive extensibility
Real organizational usability
The system is not designed as:
A sports SaaS platform
A distributed analytics platform
A machine learning system
An autonomous AI coaching system
A frontend-heavy product
It is designed as:
A backend-centered operational sports analysis system that transforms federative statistics and human contextual input into structured analytical workflows.


Architectural Style
Layered Modular Monolith
 with Hexagonal-Inspired Boundaries
The architecture prioritizes:
explicit operational responsibility separation;
deterministic governance;
infrastructure isolation;
and progressive evolution under real operational conditions.
The objective is not architectural purity, but:
reliable analytical workflows with controllable system behavior.

System Structure
src/
│
├── presentation/
│   ├── routes/
│   ├── schemas/
│   └── dependencies/
│
├── application/
│   ├── use_cases/
│   ├── services/
│   ├── orchestrators/
│   └── dto/
│
├── domain/
│   ├── entities/
│   ├── analytics/
│   ├── rules/
│   ├── value_objects/
│   └── repositories/
│
├── infrastructure/
│   ├── database/
│   ├── ai/
│   ├── ingestion/
│   ├── repositories/
│   └── observability/
│
├── shared/
├── config/
└── main.py
The system follows a layer-first modular monolith structure.
The architecture prioritizes:
operational clarity;
deterministic analytical workflows;
infrastructure isolation;
and controlled backend governance.
The system is intentionally organized around:
analytics;
persistence;
workflow orchestration;
and historical continuity,
rather than early module fragmentation.
Each layer owns a distinct responsibility:
presentation/
HTTP exposure and request handling
application/
workflow orchestration and use-case execution
domain/
entities, rules, and deterministic analytics
infrastructure/
database, AI adapters, ingestion, and external integrations
The architecture follows hexagonal-inspired dependency boundaries, meaning:
the domain layer remains isolated from infrastructure and external dependencies.


1. DOMAIN LAYER
Responsibility
Defines:
operational entities;
analytical rules;
deterministic calculations;
workflow invariants;
and domain semantics.
The domain layer must remain:
deterministic;
infrastructure-independent;
analytically focused;
operationally coherent.
The domain does NOT know:
FastAPI
PostgreSQL
SQLAlchemy
OpenAI
HTML scraping
HTTP requests
external APIs

Core Domain Concepts
Player
Represents player identity and organizational continuity.
Game
Represents official federative matches.
PlayerGameStats
Represents structured player statistics for a specific game.
PlayerSeasonSnapshot
Represents aggregated longitudinal statistical states.
CoachContextNote
Represents manually introduced contextual observations.
DeterministicAnalysis
Represents backend-generated analytical conclusions.
AIInsightReport
Represents AI-generated contextual summaries derived from deterministic analytics.

Valid Domain Responsibilities
Examples:
calculate_trend()
compute_rolling_average()
detect_performance_decline()
classify_consistency()
Invalid responsibilities:
call_openai()
save_to_database()
scrape_federation_html()



2. APPLICATION LAYER
Responsibility
Orchestrates:
use-case execution;
workflow coordination;
validation pipelines;
dependency interaction;
analytical execution flow.
This layer represents:
the operational orchestration center of the system.

Main Use Cases
ImportFederationStats
Imports and normalizes federative statistical data.
GeneratePlayerAnalysis
Executes deterministic analytical calculations.
AddCoachContext
Persists contextual coach observations.
GenerateAIInsight
Generates AI-assisted operational summaries under backend governance.
GetPlayerPerformanceOverview
Builds player-level analytical overviews.
GetTeamPerformanceSummary
Builds aggregated team-level analytical summaries.

Application Workflow Example
1. Load player statistics
2. Execute deterministic analytics
3. Load contextual coach notes
4. Build AI context DTO
5. Execute AI generation
6. Validate AI output
7. Persist analytical report
The application layer coordinates workflows but does not own:
infrastructure implementation;
or analytical formulas themselves.

3. INFRASTRUCTURE LAYER
Responsibility
Implements:
persistence;
external integrations;
scraping;
AI providers;
technical adapters;
observability tooling.
All external dependencies are isolated here.

Key Infrastructure Components
Database Infrastructure
PostgreSQL
SQLAlchemy
Alembic
Ingestion Infrastructure
Federation HTML parsers
CSV importers
Data normalization adapters
AI Infrastructure
OpenAI Adapter
Prompt builders
Response validation pipeline
Observability Infrastructure
Structured logging
Error tracing
Import monitoring
AI execution monitoring

4. PRESENTATION LAYER
Responsibility
Exposes:
HTTP endpoints;
request validation;
response serialization;
external API contracts.
This layer must remain intentionally thin.
The presentation layer does not contain:
analytical logic;
persistence logic;
AI orchestration;
or domain calculations.

Dependency Direction
Dependencies follow strict directional flow:
presentation
   ↓
application
   ↓
domain
Infrastructure is consumed through controlled boundaries:
application → infrastructure
The domain layer never depends on infrastructure.

AI Governance Architecture
AI is treated as:
a non-deterministic contextualization dependency.
The AI layer is never responsible for:
calculating metrics;
determining analytical truth;
inferring causality;
diagnosing performance;
or modifying deterministic results.
The backend preserves authority over:
analytics;
validation;
persistence;
calculations;
historical continuity;
and workflow execution.

Analytical Flow Architecture
Raw Federative Data
       ↓
Normalization
       ↓
Structured Persistence
       ↓
Deterministic Analytics
       ↓
Context Aggregation
       ↓
AI Contextualization
       ↓
Validated Insight Persistence
This guarantees:
traceability;
analytical consistency;
controlled AI usage;
and reproducible workflows.

Strategic Architectural Outcome
The architecture is designed to produce:
a real operational sports analysis system;
under real organizational conditions;
with controllable analytical workflows;
longitudinal analytical continuity;
replaceable external dependencies;
observable execution;
and progressively extensible operational capabilities.
The system is intentionally designed to evolve through:
real operational pressure and organizational feedback,
not speculative architectural complexity.