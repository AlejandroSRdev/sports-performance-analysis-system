# Sports Performance Analysis System

Backend-centered operational sports analytics system designed for real baseball club environments.

The system transforms federative player statistics and coach contextual input into structured analytical workflows, longitudinal performance tracking, and AI-assisted operational insights under deterministic backend governance.

---

# Core Objective

The objective of this project is not to build a generic sports SaaS platform or an AI-first product.

The objective is to build a production-oriented backend system capable of:

- ingesting federative statistical data;
- preserving longitudinal historical continuity;
- executing deterministic performance analysis;
- contextualizing results with explicit coach observations;
- and generating controlled AI-assisted operational summaries.

The backend remains analytically authoritative at all times.

AI is treated as a constrained contextualization dependency, never as a source of analytical truth.

---

# System Philosophy

The system follows several core engineering principles:

- deterministic backend governance;
- explicit workflow orchestration;
- structured persistence;
- immutable historical snapshots;
- controlled AI integration;
- operational observability;
- progressive extensibility without premature complexity.

The system is intentionally designed around real organizational workflows and operational usefulness rather than technological sophistication.

---

# Main Capabilities

## Federative Statistics Ingestion

- Controlled ingestion of federative baseball statistics
- HTML parsing and normalization
- Structured DTO generation
- Historical snapshot persistence

## Longitudinal Performance Tracking

- Immutable player statistical snapshots
- Historical analytical continuity
- Progression and trend detection

## Deterministic Analytics

Backend-generated analytical outputs:

- trend classification
- consistency scoring
- progression analysis
- priority area detection

No AI involvement in deterministic calculations.

## Coach Context Layer

Manual contextual observations:

- reduced workload
- positional changes
- technical adjustments
- recovery periods

Human context remains explicit and non-inferred.

## AI-Assisted Insight Generation

Optional AI contextualization layer for:

- summarization
- communication support
- operational prioritization

AI outputs are validated and persisted separately from deterministic analysis.

---

# Architecture

The system follows a:

> Layered Modular Monolith with Hexagonal-Inspired Boundaries

Structure:

```text
src/
├── presentation/
├── application/
├── domain/
├── infrastructure/
├── shared/
├── config/
└── main.py
```

The architecture prioritizes:

- operational clarity;
- infrastructure isolation;
- deterministic workflows;
- and progressive evolution under real-world pressure.

---

# Stack

## Backend

- Python 3.12
- FastAPI
- SQLAlchemy 2.x
- Alembic
- PostgreSQL
- Pydantic

## Ingestion

- BeautifulSoup
- pandas.read_html()

## AI

- OpenAI API

## Infrastructure

- Docker
- Fly.io

## Frontend (Minimal V1)

- Vite
- Vanilla JavaScript
- HTML/CSS

---

# Domain Model

Core entities:

- Player
- PlayerStatisticsSnapshot
- CoachContextNote
- PlayerPerformanceAnalysis
- PlayerInsightReport

The analytical center of the system is the Player and its longitudinal historical continuity.

---

# Engineering Principles

## Backend Authority

The backend is responsible for:

- calculations;
- validation;
- persistence;
- workflow orchestration;
- analytical integrity.

## AI Governance

AI is never responsible for:

- determining analytical truth;
- calculating metrics;
- inferring injuries or emotions;
- diagnosing performance;
- modifying deterministic outputs.

## Historical Traceability

Statistical snapshots are immutable historical records.

The system preserves analytical continuity across time.

---

# Current Scope (V1)

Included:

- federative data ingestion
- historical persistence
- deterministic analysis
- coach contextualization
- AI-assisted summaries
- operational retrieval endpoints

Explicitly excluded:

- machine learning
- autonomous AI coaching
- biomechanics
- computer vision
- advanced scouting
- distributed systems
- event-driven architecture
- microservices

---

# Strategic Outcome

This project is designed to validate a real operational backend system under organizational conditions.

The objective is not to demonstrate AI usage.

The objective is:

 Transforming real sports data into operationally useful analytical workflows through reliable backend engineering.