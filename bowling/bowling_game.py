"""
Bowling Game Implementation.

This module provides a BowlingGame class to track and calculate scores
for a standard 10-frame bowling game. It handles strikes, spares,
open frames, and calculates bonus rolls for strikes and spares.

Example:
    game = BowlingGame()
    game.roll(10)  # Strike
    game.roll(3)
    game.roll(6)
    print(game.score())  # Returns the total score
"""


class BowlingGame:
    """A class to represent a standard 10-frame bowling game."""

    def __init__(self):
        """Initialize a new bowling game with no rolls yet."""
        self.rolls = []        # List to store the number of pins knocked down for each roll
        # Tracks current roll index (unused, kept for potential extensions)
        self.current_roll = 0

    def roll(self, pins):
        """Record a roll in the game and validate input.

        Args:
            pins (int): Number of pins knocked down in this roll.

        Raises:
            TypeError: If pins is not an integer.
            ValueError: If pins < 0 or > 10 or frame total exceeds 10 (except 10th frame).
        """
        # --- Input validation ---
        if not isinstance(pins, int):
            raise TypeError("Pins must be an integer")
        if pins < 0 or pins > 10:
            raise ValueError("Pins must be between 0 and 10")

        # --- Determine current frame (frames 1-9) ---
        frame = 0
        i = 0
        while frame < 9 and i < len(self.rolls):
            if self.rolls[i] == 10:  # Strike consumes only 1 roll in a frame
                i += 1
            else:                     # Open frame or spare consumes 2 rolls
                i += 2
            frame += 1

        # --- Validate that frame total doesn't exceed 10 (except 10th frame) ---
        if frame < 9 and len(self.rolls) > 0:
            rolls_in_current_frame = []
            j = len(self.rolls) - 1
            while j >= 0 and len(rolls_in_current_frame) < 2:
                if self.rolls[j] != 10 or len(rolls_in_current_frame) == 1:
                    # Collect last two rolls for current frame (unless strike)
                    rolls_in_current_frame.insert(0, self.rolls[j])
                j -= 1

            # If first roll + current roll > 10, raise error
            if len(rolls_in_current_frame) == 1 and rolls_in_current_frame[0] + pins > 10:
                raise ValueError("Frame total cannot exceed 10 pins")

        # --- Record the roll ---
        self.rolls.append(pins)

    def score(self):
        """Calculate the total score for the game.

        Handles strikes, spares, and open frames including bonus rolls.

        Returns:
            int: Total score of the game.
        """
        score = 0
        frame_index = 0

        # --- Loop over 10 frames ---
        for _ in range(10):
            if self._is_strike(frame_index):
                # Strike: 10 + sum of next two rolls
                score += 10 + self._strike_bonus(frame_index)
                frame_index += 1
            elif self._is_spare(frame_index):
                # Spare: 10 + next roll as bonus
                score += 10 + self._spare_bonus(frame_index)
                frame_index += 2
            else:
                # Open frame: sum of two rolls
                score += self.rolls[frame_index] + self.rolls[frame_index + 1]
                frame_index += 2

        return score

    # --- Helper methods ---

    def _is_strike(self, i):
        """Check if a roll is a strike (10 pins)."""
        return i < len(self.rolls) and self.rolls[i] == 10

    def _is_spare(self, i):
        """Check if a frame is a spare (sum of two rolls == 10)."""
        return i + 1 < len(self.rolls) and self.rolls[i] + self.rolls[i + 1] == 10

    def _strike_bonus(self, i):
        """Calculate bonus points for a strike (sum of next two rolls)."""
        return sum(self.rolls[i + 1:i + 3])

    def _spare_bonus(self, i):
        """Calculate bonus points for a spare (next roll)."""
        return self.rolls[i + 2] if i + 2 < len(self.rolls) else 0
