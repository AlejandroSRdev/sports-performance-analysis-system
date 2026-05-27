STACK DEFINITION — V1
Backend
Python 3.12
FastAPI
SQLAlchemy 2.x
Alembic
Pydantic

Database
PostgreSQL
The database is responsible for:
historical snapshot persistence;
analytical continuity;
deterministic analytical storage;
coach contextual persistence;
and AI insight historical traceability.

Frontend
Vite
Vanilla JavaScript
HTML
CSS
The frontend is intentionally minimal and operationally focused.
The frontend is responsible only for:
triggering workflows;
displaying analytical results;
and enabling simple coach interaction.
The frontend is NOT designed as:
a complex dashboard system;
a rich frontend application;
or a frontend-centered architecture.

AI Layer
OpenAI API
AI is treated as:
a non-deterministic contextualization dependency governed by backend workflows.
The AI layer is responsible only for:
summarization;
contextualization;
prioritization;
and communication support.
The AI layer is NOT responsible for:
deterministic analytics;
statistical calculations;
causal inference;
or analytical authority.

Ingestion Layer
BeautifulSoup
pandas.read_html()
The ingestion layer is responsible for:
controlled scraping;
table parsing;
statistical normalization;
and DTO generation.

Infrastructure
Docker
Fly.io (backend deployment)
Vercel (frontend deployment)
The infrastructure intentionally prioritizes:
simplicity;
deployment speed;
operational reliability;
and low-friction iteration.

Observability
Structured logging
Logging covers:
ingestion execution;
parsing failures;
AI execution;
analytical generation;
and persistence workflows.

Explicitly Excluded From V1
React
TypeScript
LangChain / LangGraph
Machine Learning Pipelines
Microservices
Event-Driven Architecture
Complex Workflow Engines
Advanced Observability Stacks
Autonomous AI Systems
Premature Infrastructure Complexity

Strategic Infrastructure Objective
The stack is intentionally designed to support:
deterministic backend governance;
longitudinal analytical persistence;
controlled AI-assisted workflows;
operational reliability;
and progressive real-world validation.
The objective is NOT technological sophistication.
The objective is:
building a reliable operational sports analytics system under real organizational conditions.