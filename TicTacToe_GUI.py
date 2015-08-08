try:
    from tkinter import Frame, Canvas, Button, Label, ALL, Tk
except ImportError:
    from Tkinter import Frame, Canvas, Button, Label, ALL, Tk


from TicTacToe_Game import TicTacToe
from TicTacToe_AI import TicTacToeAI


class TicTacToeGUI:

    def __init__(self, master):
        # Initial Frame
        self.frame = Frame(master)
        self.frame.pack(fill="both", expand=True)

        # Board canvas
        self.canvas = Canvas(self.frame, width=300, height=300)

        # Symbol selection buttons
        self.x_button = Button(self.frame, text='Play as X', height=4, command=self.set_player_x, bg='white', fg='black')
        self.o_button = Button(self.frame, text='Play as O', height=4, command=self.set_player_o, bg='white', fg='red')

        # Game start button and info box
        self.start_button = Button(self.frame, text="START", height=4, command=self.start, bg='white', fg='purple')
        self.info_box = Label(self.frame, text='Tic Tac Toe Game', height=4, bg='white', fg='blue')

        self.clean_game_board()

    def start(self):
        self.set_game_board()
        self.game = TicTacToe()
        self.game.start()
        self.ai = TicTacToeAI()

        if self.ai_symbol == 'x':
            self.ai_action()

    def _board(self):
        self.canvas.create_rectangle(0, 0, 300, 300, outline="black")
        self.canvas.create_rectangle(100, 300, 200, 0, outline="black")
        self.canvas.create_rectangle(0, 100, 300, 200, outline="black")

    def user_action(self, event):
        move_x = event.x // 100
        move_y = event.y // 100
        move_result = self.game.update(self.player_symbol, (move_x, move_y))
        if move_result == "Success":
            board_x = (200 * move_x + 100) / 2
            board_y = (200 * move_y + 100) / 2
            if self.player_symbol == 'x':
                self.draw_x(board_x, board_y)
            else:
                self.draw_o(board_x, board_y)
            if not self.completed():
                self.ai_action()
        else:
            self.info_box['text'] = move_result

    def ai_action(self):
        state = self.game.get_board()
        move = self.ai.get_move(state)
        move_result = self.game.update(self.ai_symbol, move)
        if move_result == "Success":
            board_x = (200 * move[0] + 100) / 2
            board_y = (200 * move[1] + 100) / 2
            if self.ai_symbol == 'x':
                self.draw_x(board_x, board_y)
            else:
                self.draw_o(board_x, board_y)
            self.completed()

    def completed(self):
        status = self.game.done()
        if status == 'e':
            return False
        message = "Click to start a new game."
        if status == 't':
            message = "Tie game. " + message
        else:
            message = "Player " + status.upper() + " has won. " + message
        self.info_box.pack_forget()
        self.start_button.pack(fill="both", expand=True)
        self.start_button["text"] = message
        self.start_button["command"] = self.clean_game_board

    def draw_x(self, x, y):
        self.canvas.create_line(x+20, y+20, x-20, y-20, width=4, fill="black")
        self.canvas.create_line(x-20, y+20, x+20, y-20, width=4, fill="black")

    def draw_o(self, x, y):
        self.canvas.create_oval(x+25, y+25, x-25, y-25, width=4, outline="red")

    def set_game_board(self):
        self.start_button.pack_forget()
        self.x_button.pack_forget()
        self.o_button.pack_forget()
        self.canvas.delete(ALL)
        self.canvas.pack(fill="both", expand=True)
        self.info_box.pack(fill="both", expand=True)
        self.canvas.bind("<ButtonPress-1>", self.user_action)
        self._board()

    def clean_game_board(self):
        self.canvas.pack_forget()
        self.info_box.pack_forget()
        self.start_button.pack_forget()
        self.x_button.pack(fill="both", expand=True)
        self.o_button.pack(fill="both", expand=True)

    def set_player_x(self):
        self.player_symbol = 'x'
        self.ai_symbol = 'o'
        self.start()

    def set_player_o(self):
        self.player_symbol = 'o'
        self.ai_symbol = 'x'
        self.start()

if __name__ == "__main__":
    root = Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
