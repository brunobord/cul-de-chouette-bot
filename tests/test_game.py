import unittest
from game import Game


class GameTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.game.gamers = {'a': 0, 'b': 0, 'c': 0}
        self.game.turns = ['a', 'b', 'c']
        self.game.current = 1

    def test_remove_player_x(self):
        self.assertFalse(self.game.remove_player('x'))
        self.assertEquals(self.game.turns, ['a', 'b', 'c'])
        self.assertEquals(self.game.current, 1)

    def test_remove_player_a(self):
        self.game.remove_player('a')
        self.assertEquals(self.game.turns, ['b', 'c'])
        self.assertEquals(self.game.current, 0)
        self.assertFalse('a' in self.game.gamers)

    def test_remove_player_b(self):
        self.game.remove_player('b')
        self.assertEquals(self.game.turns, ['a', 'c'])
        self.assertEquals(self.game.current, 1)
        self.assertFalse('b' in self.game.gamers)

    def test_remove_player_c(self):
        self.game.remove_player('c')
        self.assertEquals(self.game.turns, ['a', 'b'])
        self.assertEquals(self.game.current, 1)
        self.assertFalse('c' in self.game.gamers)
