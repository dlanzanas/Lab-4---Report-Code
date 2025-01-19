class Game:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def display_board(self):
        for row in self.board:
            print("|".join(row))
        print()

    def make_move(self, row, col):
        row, col = row - 1, col - 1
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            return True
        print("Invalid move. Try again.")
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
        print("=== Welcome to Tic Tac Toe! ===")
        print("Take turns entering row and column numbers (1-3).")
        print("The first player to get three in a row wins!")
        print()
        
        while True:
            self.display_board()
            try:
                row, col = map(int, input(f"Player {self.current_player}, enter row and column (1-3): ").split())
                if row < 1 or row > 3 or col < 1 or col > 3:
                    print("Invalid input. Row and column must be between 1 and 3.")
                    continue
                if self.make_move(row, col):
                    if self.check_winner():
                        self.display_board()
                        print(f"Player {self.current_player} wins!")
                        break
                    if self.is_draw():
                        self.display_board()
                        print("It's a draw!")
                        break
                    self.switch_player()
            except (ValueError, IndexError):
                print("Invalid input. Enter two numbers between 1 and 3.")

if __name__ == "__main__":
    Game().play()
