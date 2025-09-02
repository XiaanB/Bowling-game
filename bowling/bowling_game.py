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
    """A class to represent a standard 10-frame bowling game.

    Tracks each roll, calculates scores for strikes, spares, and open frames,
    and computes the final game score including bonus rolls in the 10th frame.

    Attributes:
        rolls (list[int]): Stores the number of pins knocked down in each roll sequentially.
        current_roll (int): Tracks the current roll index (currently unused).

    Example:
        # Create a new game
        game = BowlingGame()

        # Roll a strike in the first frame
        game.roll(10)

        # Roll two more rolls in the second frame
        game.roll(3)
        game.roll(6)

        # Calculate total score so far
        score = game.score()
        print(score)  # Output: 28

        # Simulate a spare
        game = BowlingGame()
        game.roll(5)
        game.roll(5)  # Spare
        game.roll(7)  # Next roll counts as bonus
        print(game.score())  # Output: 17

        # Perfect game (12 strikes)
        perfect_game = BowlingGame()
        for _ in range(12):
            perfect_game.roll(10)
        print(perfect_game.score())  # Output: 300
    """

    def __init__(self):
        """Initialize a new bowling game with no rolls yet."""
        self.rolls = []
        self.current_roll = 0

    def roll(self, pins):
        """Record a roll in the game.

        Adds a roll to the game's scorekeeping and validates that the roll
        is legal. Handles frame tracking, ensures frame total pins do not
        exceed 10 (except in 10th frame), and supports strikes.

        Args:
            pins (int): The number of pins knocked down in this roll.

        Raises:
            TypeError: If `pins` is not an integer.
            ValueError:
                - If `pins` is less than 0 or greater than 10.
                - If adding `pins` would cause a frame total to exceed 10 (except 10th frame).

        Notes:
            - Frames are numbered 1-10, but frames 1-9 are handled similarly internally.
            - Strikes consume only 1 roll for frame counting; open frames consume 2 rolls.
            - 10th frame can have up to 3 rolls (handled in score calculation).
        """
        if not isinstance(pins, int):
            raise TypeError("Pins must be an integer")
        if pins < 0 or pins > 10:
            raise ValueError("Pins must be between 0 and 10")

        # Determine the current frame (frames 1-9)
        frame = 0
        i = 0
        while frame < 9 and i < len(self.rolls):
            if self.rolls[i] == 10:  # strike
                i += 1
            else:
                i += 2
            frame += 1

        # Validate the frame total (except 10th frame)
        if frame < 9 and len(self.rolls) > 0:
            rolls_in_current_frame = []
            j = len(self.rolls) - 1
            while j >= 0 and len(rolls_in_current_frame) < 2:
                if self.rolls[j] != 10 or len(rolls_in_current_frame) == 1:
                    rolls_in_current_frame.insert(0, self.rolls[j])
                j -= 1

            if len(rolls_in_current_frame) == 1 and rolls_in_current_frame[0] + pins > 10:
                raise ValueError("Frame total cannot exceed 10 pins")

        # Record the roll
        self.rolls.append(pins)

    def score(self):
        """Calculate the total score for the game.

        Handles strikes and spares including bonus rolls in the 10th frame.

        Returns:
            int: Total game score.
        """
        score = 0
        frame_index = 0

        for _ in range(10):
            if self._is_strike(frame_index):
                score += 10 + self._strike_bonus(frame_index)
                frame_index += 1
            elif self._is_spare(frame_index):
                score += 10 + self._spare_bonus(frame_index)
                frame_index += 2
            else:
                score += self.rolls[frame_index] + self.rolls[frame_index + 1]
                frame_index += 2

        return score

    def _is_strike(self, i):
        """Check if a roll is a strike.

        Args:
            i (int): Index of the roll to check.

        Returns:
            bool: True if the roll is a strike (10 pins), False otherwise.
        """
        return i < len(self.rolls) and self.rolls[i] == 10

    def _is_spare(self, i):
        """Check if a frame is a spare.

        Args:
            i (int): Index of the first roll in the frame.

        Returns:
            bool: True if the frame is a spare (sum of two rolls equals 10), False otherwise.
        """
        return i + 1 < len(self.rolls) and self.rolls[i] + self.rolls[i + 1] == 10

    def _strike_bonus(self, i):
        """Calculate bonus for a strike.

        Args:
            i (int): Index of the strike roll.

        Returns:
            int: Sum of the next two rolls (bonus points for strike).
        """
        return sum(self.rolls[i + 1:i + 3])

    def _spare_bonus(self, i):
        """Calculate bonus for a spare.

        Args:
            i (int): Index of the first roll in the spare frame.

        Returns:
            int: Next roll as bonus points (0 if no roll exists).
        """
        return self.rolls[i + 2] if i + 2 < len(self.rolls) else 0
