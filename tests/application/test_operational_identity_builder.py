import pytest

from src.application.services.operational_identity_builder import OperationalIdentityBuilder


class TestNormalizeText:

    def test_removes_accents(self) -> None:
        assert OperationalIdentityBuilder.normalize_text("Sáavedra") == "saavedra"

    def test_removes_accents_on_full_example(self) -> None:
        assert OperationalIdentityBuilder.normalize_text(" Alejandro  Sáavedra ") == "alejandro_saavedra"

    def test_collapses_multiple_spaces(self) -> None:
        assert OperationalIdentityBuilder.normalize_text("Juan  Carlos") == "juan_carlos"

    def test_lowercases(self) -> None:
        assert OperationalIdentityBuilder.normalize_text("CB Vallès") == "cb_valles"

    def test_trims_leading_trailing_spaces(self) -> None:
        assert OperationalIdentityBuilder.normalize_text("  pedro  ") == "pedro"

    def test_replaces_spaces_with_underscores(self) -> None:
        assert OperationalIdentityBuilder.normalize_text("Carlos Lopez") == "carlos_lopez"


class TestBuild:

    def test_deterministic_key_generation(self) -> None:
        key1 = OperationalIdentityBuilder.build(name="Alejandro Sáavedra", jersey_number=17, team="CB Vallès")
        key2 = OperationalIdentityBuilder.build(name="Alejandro Sáavedra", jersey_number=17, team="CB Vallès")
        assert key1 == key2

    def test_full_key_format(self) -> None:
        key = OperationalIdentityBuilder.build(name="Alejandro Sáavedra", jersey_number=17, team="CB Vallès")
        assert key == "alejandro_saavedra:17:cb_valles"

    def test_missing_jersey_fallback(self) -> None:
        key = OperationalIdentityBuilder.build(name="Pedro Garcia", jersey_number=None, team="CB Vallès")
        assert key == "pedro_garcia:unknown:cb_valles"

    def test_missing_team_fallback(self) -> None:
        key = OperationalIdentityBuilder.build(name="Pedro Garcia", jersey_number=7, team=None)
        assert key == "pedro_garcia:7:unknown"

    def test_missing_both_fallbacks(self) -> None:
        key = OperationalIdentityBuilder.build(name="Pedro Garcia", jersey_number=None, team=None)
        assert key == "pedro_garcia:unknown:unknown"
