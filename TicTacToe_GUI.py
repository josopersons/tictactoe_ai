from tkinter import Frame, Canvas, Button, ALL, Tk

from TicTacToe_Game import TicTacToe
from TicTacToe_AI import TicTacToeAI


class main:

    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack(fill="both", expand=True)
        self.canvas = Canvas(self.frame, width=300, height=300)
        self.canvas.pack(fill="both", expand=True)
        self.frameb = Frame(self.frame)
        self.frameb.pack(fill="both", expand=True)
        self.Start = Button(self.frameb, text='Click here to start', height=4, command=self.start, bg='white', fg='purple')
        self.Start.pack(fill="both", expand=True)
        self._board()

    def start(self):
        self.canvas.delete(ALL)
        self._board()
        self.canvas.bind("<ButtonPress-1>", self.user_action)
        self.game = TicTacToe()
        self.game.start()
        self.ai = TicTacToeAI()
        self.ai_symbol = 'o'

    def _board(self):
        self.canvas.create_rectangle(0, 0, 300, 300, outline="black")
        self.canvas.create_rectangle(100, 300, 200, 0, outline="black")
        self.canvas.create_rectangle(0, 100, 300, 200, outline="black")
 
    def user_action(self, event):
        move_x = event.x // 100
        move_y = event.y // 100
        move_result = self.game.update('x', (move_x, move_y))
        print(move_result) # TODO: maybe display something
        if move_result == "Success":
            board_x = (200 * move_x + 100) / 2
            board_y = (200 * move_y + 100) / 2
            self.draw_x(board_x, board_y)
            self.ai_action()

    def ai_action(self):
        state = self.game.get_board()
        move = self.ai.get_move(state)
        move_result = self.game.update(self.ai_symbol, move)
        print(move_result) # TODO: display
        if move_result == "Success":
            board_x = (200 * move[0] + 100) / 2
            board_y = (200 * move[1] + 100) / 2
            self.draw_o(board_x, board_y)
        
    def draw_x(self, x, y):
        self.canvas.create_line(x+20, y+20, x-20, y-20, width=4, fill="black")
        self.canvas.create_line(x-20, y+20, x+20, y-20, width=4, fill="black")
        
    def draw_o(self, x, y):
        self.canvas.create_oval(x+25, y+25, x-25, y-25, width=4, outline="red")

root = Tk()
app = main(root)
root.mainloop()


# TODO: add a message box for errors
# TODO: add stuff for when the game is done
# TODO: allowing choosing x, or o
# TODO: make tictactoe for any odd game size
# TODO: add tests
