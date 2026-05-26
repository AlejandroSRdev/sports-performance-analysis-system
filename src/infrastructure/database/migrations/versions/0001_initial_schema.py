"""initial schema

Revision ID: 0001_initial_schema
Revises:
Create Date: 2026-05-26

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision: str = "0001_initial_schema"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. players — no dependencies
    op.create_table(
        "players",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("team", sa.String(100), nullable=True),
        sa.Column("name", sa.String(200), nullable=False),
        sa.Column("jersey_number", sa.Integer(), nullable=True),
        sa.Column("active", sa.Boolean(), nullable=False, server_default=sa.text("true")),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.PrimaryKeyConstraint("id"),
    )

    # 2. player_statistics_snapshots — depends on players
    op.create_table(
        "player_statistics_snapshots",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("player_id", sa.UUID(), nullable=False),
        sa.Column("snapshot_date", sa.Date(), nullable=False),
        sa.Column("source_url", sa.String(500), nullable=True),
        # General
        sa.Column("games_played", sa.Integer(), nullable=True),
        sa.Column("at_bats", sa.Integer(), nullable=True),
        # Batting
        sa.Column("batting_average", sa.Numeric(5, 3), nullable=True),
        sa.Column("on_base_percentage", sa.Numeric(5, 3), nullable=True),
        sa.Column("slugging_percentage", sa.Numeric(5, 3), nullable=True),
        sa.Column("ops", sa.Numeric(5, 3), nullable=True),
        sa.Column("runs", sa.Integer(), nullable=True),
        sa.Column("hits", sa.Integer(), nullable=True),
        sa.Column("doubles", sa.Integer(), nullable=True),
        sa.Column("triples", sa.Integer(), nullable=True),
        sa.Column("home_runs", sa.Integer(), nullable=True),
        sa.Column("runs_batted_in", sa.Integer(), nullable=True),
        sa.Column("walks", sa.Integer(), nullable=True),
        sa.Column("strikeouts", sa.Integer(), nullable=True),
        sa.Column("stolen_bases", sa.Integer(), nullable=True),
        # Fielding
        sa.Column("fielding_percentage", sa.Numeric(5, 3), nullable=True),
        sa.Column("putouts", sa.Integer(), nullable=True),
        sa.Column("assists", sa.Integer(), nullable=True),
        sa.Column("errors", sa.Integer(), nullable=True),
        # Pitching
        sa.Column("earned_run_average", sa.Numeric(5, 2), nullable=True),
        sa.Column("innings_pitched", sa.Numeric(6, 1), nullable=True),
        sa.Column("wins", sa.Integer(), nullable=True),
        sa.Column("losses", sa.Integer(), nullable=True),
        sa.Column("earned_runs", sa.Integer(), nullable=True),
        sa.Column("pitching_strikeouts", sa.Integer(), nullable=True),
        sa.Column("walks_allowed", sa.Integer(), nullable=True),
        sa.Column("hits_allowed", sa.Integer(), nullable=True),
        # Per-game averages
        sa.Column("hits_per_game", sa.Numeric(5, 3), nullable=True),
        sa.Column("runs_per_game", sa.Numeric(5, 3), nullable=True),
        sa.Column("rbi_per_game", sa.Numeric(5, 3), nullable=True),
        sa.Column("strikeouts_per_game", sa.Numeric(5, 3), nullable=True),
        sa.Column("walks_per_game", sa.Numeric(5, 3), nullable=True),
        # Metadata
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.ForeignKeyConstraint(["player_id"], ["players.id"], ondelete="RESTRICT"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("player_id", "snapshot_date", name="uq_player_snapshot_date"),
    )
    op.create_index(
        "ix_player_statistics_snapshots_player_id",
        "player_statistics_snapshots",
        ["player_id"],
    )
    op.create_index(
        "ix_player_statistics_snapshots_snapshot_date",
        "player_statistics_snapshots",
        ["snapshot_date"],
    )

    # 3. coach_context_notes — depends on players
    op.create_table(
        "coach_context_notes",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("player_id", sa.UUID(), nullable=False),
        sa.Column("note", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.ForeignKeyConstraint(["player_id"], ["players.id"], ondelete="RESTRICT"),
        sa.PrimaryKeyConstraint("id"),
    )

    # 4. player_performance_analyses — depends on players
    op.create_table(
        "player_performance_analyses",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("player_id", sa.UUID(), nullable=False),
        sa.Column("analysis_period_start", sa.Date(), nullable=False),
        sa.Column("analysis_period_end", sa.Date(), nullable=False),
        sa.Column("batting_trend", sa.String(20), nullable=True),
        sa.Column("discipline_trend", sa.String(20), nullable=True),
        sa.Column("contact_trend", sa.String(20), nullable=True),
        sa.Column("fielding_trend", sa.String(20), nullable=True),
        sa.Column("pitching_trend", sa.String(20), nullable=True),
        sa.Column("overall_trend", sa.String(20), nullable=True),
        sa.Column("priority_area", sa.String(100), nullable=True),
        sa.Column("consistency_score", sa.Numeric(4, 3), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.ForeignKeyConstraint(["player_id"], ["players.id"], ondelete="RESTRICT"),
        sa.PrimaryKeyConstraint("id"),
    )

    # 5. player_insight_reports — depends on players and player_performance_analyses
    op.create_table(
        "player_insight_reports",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("player_id", sa.UUID(), nullable=False),
        sa.Column("analysis_id", sa.UUID(), nullable=False),
        sa.Column("summary", sa.Text(), nullable=True),
        sa.Column("key_observations", postgresql.ARRAY(sa.Text()), nullable=True),
        sa.Column("recommended_focus", postgresql.ARRAY(sa.Text()), nullable=True),
        sa.Column("limitations", postgresql.ARRAY(sa.Text()), nullable=True),
        sa.Column("ai_model_used", sa.String(100), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.ForeignKeyConstraint(["player_id"], ["players.id"], ondelete="RESTRICT"),
        sa.ForeignKeyConstraint(
            ["analysis_id"],
            ["player_performance_analyses.id"],
            ondelete="RESTRICT",
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("analysis_id", name="uq_player_insight_reports_analysis_id"),
    )


def downgrade() -> None:
    op.drop_table("player_insight_reports")
    op.drop_table("player_performance_analyses")
    op.drop_table("coach_context_notes")
    op.drop_index(
        "ix_player_statistics_snapshots_snapshot_date",
        table_name="player_statistics_snapshots",
    )
    op.drop_index(
        "ix_player_statistics_snapshots_player_id",
        table_name="player_statistics_snapshots",
    )
    op.drop_table("player_statistics_snapshots")
    op.drop_table("players")
