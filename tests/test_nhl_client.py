"""
Simple unit tests for NHLDataClient
Run with: pytest tests/test_nhl_client.py
"""
import pytest
import json
from src.api.nhl_client import NHLDataClient


def test_search_player_mcdavid():
    """Test searching for Connor McDavid"""
    client = NHLDataClient()
    player_id = client.search_player("Connor", "McDavid", "EDM")

    assert player_id is not None
    assert player_id == 8478402


def test_search_player_bedard():
    """Test searching for Connor Bedard"""
    client = NHLDataClient()
    player_id = client.search_player("Connor", "Bedard", "CHI")

    assert player_id is not None
    assert player_id == 8484144


def test_search_player_not_found():
    """Test searching for a player that doesn't exist"""
    client = NHLDataClient()
    player_id = client.search_player("Fake", "Player", "EDM")

    assert player_id is None


def test_get_player_stats_mcdavid():
    """Test getting career stats for Connor McDavid"""
    client = NHLDataClient()
    stats = client.get_player_stats(8478402)

    assert stats is not None
    assert len(stats) > 0


def test_get_player_stats_bedard():
    """Test getting career stats for Connor Bedard"""
    client = NHLDataClient()
    stats = client.get_player_stats(8484144)

    assert stats is not None
    assert len(stats) > 0


def test_full_workflow_mcdavid():
    """Test full workflow: search then get stats for McDavid"""
    client = NHLDataClient()

    # Search for player
    player_id = client.search_player("Connor", "McDavid", "EDM")
    assert player_id is not None

    # Get stats
    stats = client.get_player_stats(player_id)
    assert stats is not None
    assert len(stats) > 0


def test_full_workflow_bedard():
    """Test full workflow: search then get stats for Bedard"""
    client = NHLDataClient()

    # Search for player
    player_id = client.search_player("Connor", "Bedard", "CHI")
    assert player_id is not None

    # Get stats
    stats = client.get_player_stats(player_id)
    assert stats is not None
    assert len(stats) > 0


def test_inspect_stats_structure():
    """Inspect the structure of stats data returned by get_player_stats"""
    client = NHLDataClient()
    stats = client.get_player_stats(8484144)  # Connor Bedard

    print("\n" + "="*80)
    print("CONNOR BEDARD STATS")
    print("STATS DATA TYPE:", type(stats))
    print("="*80)

    if isinstance(stats, dict):
        print("\nTop-level keys:", list(stats.keys()))
        print("\nFull stats structure (pretty printed):")
        print(json.dumps(stats, indent=2, default=str))
    elif isinstance(stats, list):
        print("\nList length:", len(stats))
        if len(stats) > 0:
            print("\nFirst item type:", type(stats[0]))
            print("\nFirst few items:")
            print(json.dumps(stats[:3], indent=2, default=str))
    else:
        print("\nRaw stats:")
        print(stats)

    print("="*80)

    # This test always passes - it's just for inspection
    assert stats is not None
