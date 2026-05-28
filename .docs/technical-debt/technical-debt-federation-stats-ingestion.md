# TECHNICAL DEBT — FEDERATION STATS INGESTION WORKFLOW V1

## Context

This document tracks intentionally deferred technical concerns for the federation statistics ingestion workflow implemented in V1.

The objective of V1 is:

* reliable ingestion;
* longitudinal persistence;
* deterministic normalization;
* operational continuity.

The objective is NOT production-hardening every edge case prematurely.

---

# 1. IMPORT TRANSACTION SEMANTICS

## Current State

The route handler performs:

```python
db.commit()
```

only after:

```python
use_case.execute()
```

completes successfully.

Per-row mapping failures are recoverable and skipped.

Fatal import errors rollback the entire transaction implicitly.

---

## Current Semantics

V1 behaves effectively as:

```text
global transactional import
+
recoverable row-level parsing failures
```

Meaning:

* malformed rows are skipped;
* fatal infrastructure/use-case failures rollback all persisted changes.

---

## Risk

This behavior is currently implicit.

Future maintainers may:

* introduce intermediate commits;
* assume partial persistence;
* misunderstand rollback guarantees.

---

## Future Improvement

Explicitly formalize import transactional semantics.

Potential future directions:

### Option A — Fully atomic import

Entire import succeeds or fails as one transaction.

### Option B — Partial persistence import

Persist valid rows incrementally even if later rows fail.

Requires:

* explicit transaction boundaries;
* import execution tracking;
* reconciliation semantics.

---

# 2. CONCURRENT PLAYER DUPLICATION RISK

## Current State

Player resolution currently follows:

```text
find_by_operational_identity_key()
↓
if missing:
    create Player
```

---

## Risk

Under concurrent imports:

* two executions may not find the same player;
* both may create duplicated Players.

This is currently possible because:

* there is no database UNIQUE constraint;
* no row locking strategy exists.

---

## Current Justification

V1 assumes:

* low concurrency;
* manually triggered imports;
* operational simplicity.

This risk is acceptable temporarily.

---

## Future Improvement

Add database-level protection:

```sql
UNIQUE (operational_identity_key)
```

Potentially combined with:

* retry handling;
* integrity error recovery;
* upsert semantics.

---

# 3. URL VALIDATION SEMANTICS

## Current State

`InvalidSourceUrlError` exists conceptually but federation URL validation is not explicit.

Invalid URLs currently collapse into:

```text
HtmlFetchFailedError
```

---

## Risk

Error semantics are slightly ambiguous:

* malformed URL;
* unreachable host;
* timeout;
* 404 response;
  all become infrastructure fetch failures.

---

## Current Justification

Operational impact is low for V1.

The system still fails safely.

---

## Future Improvement

Introduce explicit URL validation before fetch execution.

Possible checks:

* valid scheme;
* federation domain whitelist;
* URL normalization;
* federation-specific pattern validation.

---

# 4. IMPORT ORCHESTRATION RESPONSIBILITY GROWTH

## Current State

`ImportFederationStatsUseCase` currently coordinates:

* HTML fetching;
* table selection;
* row mapping;
* identity resolution;
* player persistence;
* snapshot persistence;
* import metrics;
* logging.

---

## Risk

As federation ingestion evolves, the use case may become:

* too orchestration-heavy;
* harder to test;
* semantically overloaded.

---

## Current Justification

Current workflow complexity remains acceptable for V1.

Avoiding premature orchestration abstraction is intentional.

---

## Future Improvement

Potential extraction candidates:

```text
FederationImportOrchestrator
PlayerIdentityResolver
SnapshotCreationService
ImportExecutionReporter
```

Only if:

* federation ingestion expands significantly;
* multiple federation sources appear;
* import complexity grows materially.

---

# 5. FEDERATION SCHEMA FRAGILITY

## Current State

Table detection relies on federation column signatures.

The system assumes:

* relatively stable federation table structure;
* recognizable column naming.

---

## Risk

Federation HTML changes may:

* break ingestion;
* change column names;
* reorder tables;
* introduce localization changes.

---

## Current Justification

The selector already applies defensive matching.

This is sufficient for V1 operational validation.

---

## Future Improvement

Introduce:

* federation schema versioning;
* richer signature matching;
* parser monitoring;
* import diagnostics;
* snapshot schema evolution handling.

---

# 6. IMPORT OBSERVABILITY DEPTH

## Current State

Structured logging exists for:

* import start;
* player reuse/creation;
* snapshot creation/skipping;
* row failures;
* import completion.

---

## Risk

Operational observability remains shallow.

The system currently lacks:

* execution duration metrics;
* import IDs;
* per-phase timing;
* persistence latency tracking;
* structured import reports.

---

## Current Justification

V1 prioritizes workflow correctness over observability sophistication.

---

## Future Improvement

Potential additions:

```text
import_execution_id
phase duration metrics
row-level diagnostics
import audit persistence
structured execution summaries
```

Only after:

* real operational usage;
* repeated imports;
* actual debugging pressure.

---

# FINAL NOTE

The current ingestion workflow already satisfies the core V1 operational objectives:

* deterministic external normalization;
* clean domain boundaries;
* player identity continuity;
* append-only historical persistence;
* recoverable row-level failures.

The technical debt documented here is intentionally deferred to preserve:

* implementation focus;
* architectural simplicity;
* operational validation speed;
* controlled system evolution.