import unittest

class Game:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def display_board(self):
        for row in self.board:
            print("|".join(row))
        print()

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            return True
        return False

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for i in range(3):
            if all(self.board[i][j] == self.current_player for j in range(3)) or \
               all(self.board[j][i] == self.current_player for j in range(3)):
                return True
        if all(self.board[i][i] == self.current_player for i in range(3)) or \
           all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        return False

    def is_draw(self):
        return all(cell != " " for row in self.board for cell in row)

    def play(self):
        print("Tic Tac Toe Game!")
        while True:
            self.display_board()
            try:
                row, col = map(int, input(f"Player {self.current_player}, enter row and column (1-3): ").split())
                if 1 <= row <= 3 and 1 <= col <= 3 and self.make_move(row - 1, col - 1):
                    if self.check_winner():
                        self.display_board()
                        print(f"Player {self.current_player} wins!")
                        break
                    if self.is_draw():
                        self.display_board()
                        print("It's a draw!")
                        break
                    self.switch_player()
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Enter two numbers between 1 and 3.")

# Unit Test Program
class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_make_valid_move(self):
        self.assertTrue(self.game.make_move(0, 0))

    def test_make_invalid_move(self):
        self.game.make_move(0, 0)
        self.assertFalse(self.game.make_move(0, 0))

    def test_switch_player(self):
        self.game.switch_player()
        self.assertEqual(self.game.current_player, "O")

    def test_check_winner_row(self):
        self.game.board = [["X", "X", "X"], [" ", " ", " "], [" ", " ", " "]]
        self.assertTrue(self.game.check_winner())

    def test_check_draw(self):
        self.game.board = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]
        self.assertTrue(self.game.is_draw())

if __name__ == "__main__":
    while True:
        choice = input("Enter 'P' to play the game, 'T' to run tests, or 'Q' to quit: ").strip().upper()
        if choice == "P":
            Game().play()
        elif choice == "T":
            unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromTestCase(TestTicTacToe))
        elif choice == "Q":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 'P', 'T', or 'Q'.")
