
import unittest
from bowling_game import BowlingGame


class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()

    def roll_many(self, rolls, pins):
        for _ in range(rolls):
            self.game.roll(pins)

    def roll_spare(self):
        self.game.roll(5)
        self.game.roll(5)

    def roll_strike(self):
        self.game.roll(10)

    def test_TC01_open_frame(self):
        self.game.roll(4)
        self.game.roll(3)
        self.roll_many(18, 0)
        self.assertEqual(self.game.score(), 7)

    def test_TC02_spare(self):
        self.roll_spare()       # Frame 1: 5 + 5 = 10 (spare)
        self.game.roll(5)       # Frame 2: first roll = 5
        self.roll_many(17, 0)   # Rest of the game is all zeroes
        self.assertEqual(self.game.score(), 20)

    def test_TC03_strike(self):
        self.roll_strike()
        self.game.roll(4)
        self.game.roll(3)
        self.roll_many(16, 0)
        self.assertEqual(self.game.score(), 24)

    def test_TC04_two_strikes(self):
        self.roll_strike()
        self.roll_strike()
        self.game.roll(4)
        self.game.roll(2)
        self.roll_many(14, 0)
        self.assertEqual(self.game.score(), 46)

    def test_TC05_tenth_frame_spare(self):
        self.roll_many(18, 0)        # Frames 1–9: all gutter balls
        self.game.roll(7)            # Frame 10, Roll 1
        self.game.roll(3)            # Frame 10, Roll 2 → 7 + 3 = 10 = spare
        self.game.roll(5)            # Bonus roll
        self.assertEqual(self.game.score(), 15)

    def test_TC06_tenth_frame_strike(self):
        self.roll_many(18, 0)
        self.roll_strike()
        self.game.roll(10)
        self.game.roll(10)
        self.assertEqual(self.game.score(), 30)

    def test_TC07_perfect_game(self):
        self.roll_many(12, 10)
        self.assertEqual(self.game.score(), 300)

    def test_TC08_all_gutter_balls(self):
        self.roll_many(20, 0)
        self.assertEqual(self.game.score(), 0)

    def test_TC09_negative_input(self):
        with self.assertRaises(ValueError):
            self.game.roll(-1)

    def test_TC10_input_above_ten(self):
        with self.assertRaises(ValueError):
            self.game.roll(11)

    def test_TC11_all_spares(self):
        # Every frame is a spare: 5 + 5 → 10 frames
        for _ in range(10):
            self.roll_spare()
        # Bonus roll for 10th frame spare
        self.game.roll(5)

        # Each spare = 10 + next roll (5) = 15 points per frame
        # Total score = 10 frames × 15 = 150
        self.assertEqual(self.game.score(), 150)

    def test_TC12_frame_total_exceeds_ten(self):
        self.game.roll(8)
        with self.assertRaises(ValueError):
            self.game.roll(5)  # 8 + 5 = 13 > 10 → invalid


if __name__ == '__main__':
    unittest.main()
