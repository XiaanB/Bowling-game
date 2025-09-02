"""
Example Usage of the Bowling Game

This module demonstrates how to use the BowlingGame class to:
1. Create a game
2. Roll balls and knock down pins
3. Calculate and display the score

For each example, we show:
- The rolls in each frame
- The expected score based on standard bowling rules
- The actual score calculated by our implementation

Note: Students should use these examples to verify their implementation
is calculating scores correctly after fixing any bugs.
"""

from bowling_game import BowlingGame


def print_game_results(game_name, rolls, expected_score, actual_score):
    """
    Print the results of a game, showing expected vs actual score.

    Displays whether the score was calculated correctly.
    """
    print(f"\n{game_name}:")
    print(f"Rolls: {rolls}")
    print(f"Expected score: {expected_score}")
    print(f"Actual score: {actual_score}")
    print(
        f"Correct implementation: {'✓' if expected_score == actual_score else '✗'}")


def example_game():
    """
    Play a sample game with a mix of strikes, spares and open frames.

    Scoring Breakdown:
    - Frame 1: Strike         → 10 + 3 + 6 = 19
    - Frame 2: 3, 6           → 9
    - Frame 3: Spare (5,5)    → 10 + 8 = 18
    - Frame 4: 8, 1           → 9
    - Frame 5: Strike         → 10 + 10 + 10 = 30
    - Frame 6: Strike         → 10 + 10 + 9 = 29
    - Frame 7: Strike         → 10 + 9 + 0 = 19
    - Frame 8: 9, 0           → 9
    - Frame 9: Spare (7,3)    → 10 + 10 = 20
    - Frame10: 10,10,8        → 28

    Total expected score: 190
    """
    game = BowlingGame()
    rolls = []

    # Rolling each frame manually with inline comments
    game.roll(10)  # Strike
    rolls.append(10)

    game.roll(3)
    game.roll(6)
    rolls.extend([3, 6])

    game.roll(5)
    game.roll(5)  # Spare
    rolls.extend([5, 5])

    game.roll(8)
    game.roll(1)
    rolls.extend([8, 1])

    game.roll(10)  # Strike
    rolls.append(10)

    game.roll(10)  # Strike
    rolls.append(10)

    game.roll(10)  # Strike
    rolls.append(10)

    game.roll(9)
    game.roll(0)
    rolls.extend([9, 0])

    game.roll(7)
    game.roll(3)  # Spare
    rolls.extend([7, 3])

    game.roll(10)
    game.roll(10)
    game.roll(8)  # 10th frame: Strike, Strike, then 8
    rolls.extend([10, 10, 8])

    actual_score = game.score()
    expected_score = 190

    print_game_results("Example Game", rolls, expected_score, actual_score)
    return actual_score


def perfect_game():
    """
    Play a perfect game — 12 strikes in a row.

    Total: 10 frames * 30 = 300
    """
    game = BowlingGame()
    rolls = []

    for _ in range(12):  # 10 frames + 2 bonus rolls
        game.roll(10)
        rolls.append(10)

    actual_score = game.score()
    expected_score = 300

    print_game_results("Perfect Game", rolls, expected_score, actual_score)
    return actual_score


def all_spares():
    """
    Every frame is a spare (5 + 5), followed by a bonus 5.

    Total: 10 frames * 15 = 150
    """
    game = BowlingGame()
    rolls = []

    for _ in range(21):  # 10 frames * 2 + 1 bonus roll
        game.roll(5)
        rolls.append(5)

    actual_score = game.score()
    expected_score = 150

    print_game_results("All Spares Game", rolls, expected_score, actual_score)
    return actual_score


def gutter_game():
    """
    All gutter balls (0 pins every roll).

    Total score: 0
    """
    game = BowlingGame()
    rolls = []

    for _ in range(20):  # 10 frames * 2 rolls
        game.roll(0)
        rolls.append(0)

    actual_score = game.score()
    expected_score = 0

    print_game_results("Gutter Game", rolls, expected_score, actual_score)
    return actual_score


def regular_game():
    """
    A normal game with no strikes or spares.

    Frame-by-frame:
    - Frame 1: 3 + 4 = 7
    - Frame 2: 2 + 5 = 7
    - Frame 3: 1 + 6 = 7
    - Frame 4: 4 + 2 = 6
    - Frame 5: 8 + 1 = 9
    - Frame 6: 7 + 1 = 8
    - Frame 7: 5 + 3 = 8
    - Frame 8: 2 + 3 = 5
    - Frame 9: 4 + 3 = 7
    - Frame10: 2 + 6 = 8

    Total: 72
    """
    game = BowlingGame()
    rolls = [3, 4, 2, 5, 1, 6, 4, 2, 8, 1,
             7, 1, 5, 3, 2, 3, 4, 3, 2, 6]

    for pins in rolls:
        game.roll(pins)

    actual_score = game.score()
    expected_score = 72

    print_game_results("Regular Game", rolls, expected_score, actual_score)
    return actual_score


def main():
    """
    Run all example games and print results.

    Shows whether the implementation matches expected scoring logic.
    """
    print("BOWLING GAME EXAMPLES")
    print("=====================")
    print("These examples demonstrate how bowling scoring should work.")
    print("The 'Correct implementation' indicator shows if our current")
    print("implementation calculates the score correctly.")
    print("\nStudents should ensure their fixed implementation correctly")
    print("calculates all of these scenarios.")

    example_game()
    perfect_game()
    all_spares()
    gutter_game()
    regular_game()


if __name__ == "__main__":
    main()
