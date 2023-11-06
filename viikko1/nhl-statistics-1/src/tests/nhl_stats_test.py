import unittest
from statistics_service import StatisticsService
from player import Player
from statistics_service import SortBy

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_search(self):
        search = self.stats.search("Semenko")
        self.assertEqual(search.name, "Semenko")

    def test_search_none(self):
        search = self.stats.search("A")
        self.assertEqual(search, None)
    
    def test_team(self):
        team = self.stats.team("PIT")
        self.assertEqual(team,[self.stats._players[1]])
    
    def test_top(self):
        top = self.stats.top(2, SortBy.POINTS)
        players = self.stats._players
        actual_top = [players[4], players[1], players[3]]
        self.assertEqual(top, actual_top)

        top = self.stats.top(2, SortBy.GOALS)
        players = self.stats._players
        actual_top = [players[1], players[3], players[2]]
        self.assertEqual(top, actual_top)

        top = self.stats.top(2, SortBy.ASSISTS)
        players = self.stats._players
        actual_top = [players[4], players[3], players[1]]
        self.assertEqual(top, actual_top)