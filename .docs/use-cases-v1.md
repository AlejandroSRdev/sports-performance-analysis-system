Sports Performance Analysis System — Use Cases Definition V1
Core Operational Flow
1. Federative data ingestion
2. Statistical normalization
3. Historical snapshot persistence
4. Deterministic analytical execution
5. Optional coach contextualization
6. AI-assisted insight generation
7. Analytical retrieval and visualization
The backend remains authoritative during all workflow stages.

1. Import Federative Statistics
Objective
Import federative statistical tables and normalize them into structured internal persistence.

Pipeline Position
STEP 1 — Ingestion Layer
Executed:
manually by coach/admin;
or through controlled scraping execution.

Endpoint
POST /imports/federation-stats

Request
{
 "source_url": "https://www.fcbs.cat/campionat/2026/b_sub14/stats/val.htm#team.gms"
}

Responsibilities
fetch HTML;
parse statistical tables;
normalize values;
validate required structure;
generate normalized DTOs;
persist player snapshots.

Response
{
 "imported_players": 14,
 "snapshots_created": 14,
 "source_url": "...",
 "imported_at": "2026-05-23T18:00:00Z"
}

Basic Errors
{
 "error": "INVALID_SOURCE_URL"
}
{
 "error": "TABLE_STRUCTURE_NOT_SUPPORTED"
}
{
 "error": "IMPORT_FAILED"
}

2. Generate Deterministic Player Analysis
Objective
Generate deterministic analytical conclusions from historical player snapshots.

Pipeline Position
STEP 3 — Deterministic Analytics Layer
Executed:
after snapshots exist;
optionally multiple times over different periods.

Endpoint
POST /players/{player_id}/analysis

Request
{
 "analysis_period_start": "2026-04-01",
 "analysis_period_end": "2026-05-23"
}

Responsibilities
load player snapshots;
compare historical progression;
calculate trends;
calculate consistency;
determine priority areas;
persist analysis result.

Response
{
 "analysis_id": 42,
 "player_id": 7,

 "batting_trend": "improving",
 "discipline_trend": "stable",
 "fielding_trend": "declining",

 "overall_trend": "positive",

 "priority_area": "plate discipline",

 "consistency_score": 0.74,

 "created_at": "2026-05-23T18:15:00Z"
}

Basic Errors
{
 "error": "PLAYER_NOT_FOUND"
}
{
 "error": "INSUFFICIENT_SNAPSHOT_HISTORY"
}
{
 "error": "ANALYSIS_GENERATION_FAILED"
}

3. Register Coach Context
Objective
Persist contextual coach observations associated with a player.

Pipeline Position
STEP 4 — Human Context Layer
Executed:
optionally;
before AI insight generation.

Endpoint
POST /players/{player_id}/context-notes

Request
{
 "note": "Reduced training load during last two weeks."
}

Responsibilities
validate player existence;
persist contextual note;
preserve historical context continuity.

Response
{
 "context_note_id": 12,
 "player_id": 7,
 "created_at": "2026-05-23T18:22:00Z"
}

Basic Errors
{
 "error": "PLAYER_NOT_FOUND"
}
{
 "error": "EMPTY_NOTE"
}

4. Generate AI Insight Report
Objective
Generate AI-assisted contextual summaries from deterministic analytical outputs.

Pipeline Position
STEP 5 — AI Contextualization Layer
Executed:
after deterministic analysis;
optionally after coach notes exist.

Endpoint
POST /players/{player_id}/insights

Request
{
 "analysis_id": 42
}

Responsibilities
load deterministic analysis;
load coach context notes;
build structured AI context DTO;
execute AI generation;
validate output structure;
persist AI insight report.

Response
{
 "report_id": 9,

 "summary": "Player has shown stable offensive progression with improving consistency at bat.",

 "key_observations": [
   "Improved batting average",
   "Reduced strikeout growth"
 ],

 "recommended_focus": [
   "Plate discipline",
   "Fielding consistency"
 ],

 "limitations": [
   "No game-level event data available"
 ],

 "created_at": "2026-05-23T18:30:00Z"
}

Basic Errors
{
 "error": "ANALYSIS_NOT_FOUND"
}
{
 "error": "AI_GENERATION_FAILED"
}
{
 "error": "INVALID_AI_OUTPUT"
}

5. Retrieve Player Performance Overview
Objective
Retrieve consolidated player analytical information.

Pipeline Position
STEP 6 — Retrieval / Visualization Layer
Executed:
when coach requests player overview.

Endpoint
GET /players/{player_id}/overview

Responsibilities
load player information;
load historical snapshots;
load analyses;
load AI reports;
aggregate structured overview response.

Response
{
 "player": {
   "id": 7,
   "name": "Luis Dominguez"
 },

 "latest_snapshot": {
   "batting_average": 0.287,
   "ops": 0.812
 },

 "latest_analysis": {
   "overall_trend": "positive",
   "priority_area": "fielding"
 },

 "latest_ai_report": {
   "summary": "Player has shown consistent offensive progression."
 }
}

Basic Errors
{
 "error": "PLAYER_NOT_FOUND"
}

6. Retrieve Historical Analyses
Objective
Retrieve previous analytical executions for longitudinal review.

Pipeline Position
STEP 6 — Historical Analytical Retrieval
Executed:
when coach wants historical analytical continuity.

Endpoint
GET /players/{player_id}/analyses

Responsibilities
retrieve historical analyses;
retrieve associated AI reports;
preserve analytical continuity.

Response
{
 "player_id": 7,

 "analyses": [
   {
     "analysis_id": 42,
     "overall_trend": "positive",
     "created_at": "2026-05-23T18:15:00Z"
   },
   {
     "analysis_id": 31,
     "overall_trend": "stable",
     "created_at": "2026-05-10T17:00:00Z"
   }
 ]
}

Basic Errors
{
 "error": "PLAYER_NOT_FOUND"
}

Strategic Operational Outcome
The use cases are intentionally designed to support:
deterministic analytical workflows;
structured longitudinal persistence;
coach-assisted contextualization;
and controlled AI-assisted communication.
The backend preserves authority over:
persistence;
calculations;
validation;
workflow orchestration;
and analytical integrity.

