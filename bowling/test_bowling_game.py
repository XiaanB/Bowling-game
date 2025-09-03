"""
Unit tests for the BowlingGame class.

This module tests all core functionality of the BowlingGame scoring system:
- Open frames
- Spares and strikes
- Tenth frame bonus logic
- Edge cases (perfect game, all gutter balls)
- Input validation (negative pins, rolls > 10, invalid frame totals)

All tests use Python’s built-in unittest framework.
"""

import unittest
from bowling_game import BowlingGame


class TestBowlingGame(unittest.TestCase):
    """
    Test suite for the BowlingGame scoring logic.

    Each test case covers a specific scoring rule or input validation scenario.
    """

    def setUp(self):
        """Create a fresh game before each test."""
        self.game = BowlingGame()

    def roll_many(self, rolls, pins):
        """Rolls the same number of pins for a given number of rolls."""
        for _ in range(rolls):
            self.game.roll(pins)

    def roll_spare(self):
        """Roll a spare (5 + 5)."""
        self.game.roll(5)
        self.game.roll(5)

    def roll_strike(self):
        """Roll a strike (10 pins)."""
        self.game.roll(10)

    def test_TC01_open_frame(self):
        """Test: Basic open frame scoring (no bonuses)."""
        self.game.roll(4)
        self.game.roll(3)          # Frame 1: 4 + 3 = 7
        self.roll_many(18, 0)      # Rest of game: gutter balls
        self.assertEqual(self.game.score(), 7)

    def test_TC02_spare(self):
        """Test: Spare adds next roll as bonus."""
        self.roll_spare()          # Frame 1: 5 + 5 = 10 (spare)
        self.game.roll(5)          # Frame 2: first roll = 5 → bonus for spare
        self.roll_many(17, 0)      # Rest of game: gutter balls
        self.assertEqual(self.game.score(), 20)

    def test_TC03_strike(self):
        """Test: Strike adds next two rolls as bonus."""
        self.roll_strike()         # Frame 1: 10 (strike)
        self.game.roll(4)          # Frame 2: 4
        self.game.roll(3)          # Frame 2: 3 → bonus = 4 + 3
        self.roll_many(16, 0)
        self.assertEqual(self.game.score(), 24)

    def test_TC04_two_strikes(self):
        """Test: Double strike followed by regular frame."""
        self.roll_strike()         # Frame 1: 10
        self.roll_strike()         # Frame 2: 10
        self.game.roll(4)          # Frame 3: 4
        self.game.roll(2)          # Frame 3: 2
        self.roll_many(14, 0)
        # Frame 1 = 10 + 10 + 4 = 24
        # Frame 2 = 10 + 4 + 2 = 16
        # Frame 3 = 4 + 2 = 6
        self.assertEqual(self.game.score(), 46)

    def test_TC05_tenth_frame_spare(self):
        """Test: Spare in the 10th frame gets one bonus roll."""
        self.roll_many(18, 0)      # Frames 1–9: all gutter balls
        self.game.roll(7)          # Frame 10: roll 1
        self.game.roll(3)          # Frame 10: roll 2 → 10 = spare
        self.game.roll(5)          # Bonus roll for spare
        self.assertEqual(self.game.score(), 15)  # 10 + 5

    def test_TC06_tenth_frame_strike(self):
        """Test: Strike in the 10th frame gets two bonus rolls."""
        self.roll_many(18, 0)      # Frames 1–9: all gutter balls
        self.roll_strike()         # Frame 10: strike
        self.game.roll(10)         # Bonus roll 1
        self.game.roll(10)         # Bonus roll 2
        self.assertEqual(self.game.score(), 30)  # 10 + 10 + 10

    def test_TC07_perfect_game(self):
        """Test: 12 strikes result in a perfect score of 300."""
        self.roll_many(12, 10)     # 12 strikes = perfect game
        self.assertEqual(self.game.score(), 300)

    def test_TC08_all_gutter_balls(self):
        """Test: 20 gutter balls result in 0 score."""
        self.roll_many(20, 0)
        self.assertEqual(self.game.score(), 0)

    def test_TC09_negative_input(self):
        """Test: Negative pin count raises ValueError."""
        with self.assertRaises(ValueError):
            self.game.roll(-1)

    def test_TC10_input_above_ten(self):
        """Test: Pin count above 10 raises ValueError."""
        with self.assertRaises(ValueError):
            self.game.roll(11)

    def test_TC11_all_spares(self):
        """Test: All spares (10 x 5+5) with bonus roll results in 150."""
        for _ in range(10):
            self.roll_spare()      # 10 frames of 5 + 5
        self.game.roll(5)          # Bonus roll after 10th-frame spare
        # Each frame = 10 + 5 = 15; 10 × 15 = 150
        self.assertEqual(self.game.score(), 150)

    def test_TC12_frame_total_exceeds_ten(self):
        """Test: Frame total > 10 (without a strike) raises ValueError."""
        self.game.roll(8)          # First roll of frame
        with self.assertRaises(ValueError):
            self.game.roll(5)      # 8 + 5 = 13 → invalid


if __name__ == '__main__':
    unittest.main()
