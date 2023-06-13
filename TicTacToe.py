#numpy
from tkinter import *
import numpy as n

board_size = 300
letter_size = (board_size / 3 - board_size / 8) / 2
letter_thickness = 25
X_color = '#EE4035'
O_color = '#0492CF'
Green = '#7BC043'

class Tic_Tac_Toe():
    def __init__(self):
        self.window = Tk()
        self.window.title('Tic-Tac-Toe')
        self.canvas = Canvas(self.window, width=board_size, height=board_size)
        self.canvas.pack()
        self.window.bind('<Button-1>', self.click)
        self.initialize()
        self.X_turns = True
        self.status = n.zeros(shape=(3, 3))
        self.X_starts = True
        self.reset = False
        self.gameover = False
        self.tie = False
        self.X_wins = False
        self.O_wins = False
        self.X_score = 0
        self.O_score = 0
        self.tie_score = 0

    def mainloop(self):
        self.window.mainloop()

    def initialize(self):
        for i in range(2):
            self.canvas.create_line((i + 1) * board_size / 3, 0, (i + 1) * board_size / 3, board_size)
        for i in range(2):
            self.canvas.create_line(0, (i + 1) * board_size / 3, board_size, (i + 1) * board_size / 3)

    def play_again(self):
        self.initialize()
        self.X_starts = not self.X_starts
        self.X_turns = self.X_starts
        self.status = n.zeros(shape=(3, 3))

    def create_O(self, logical_position):
        logical_position = n.array(logical_position)
        grid_position = self.grid_position(logical_position)
        self.canvas.create_oval(grid_position[0] - letter_size, grid_position[1] - letter_size,
                                grid_position[0] + letter_size, grid_position[1] + letter_size, width=letter_thickness,outline=O_color)

    def create_X(self, logical_position):
        grid_position = self.grid_position(logical_position)
        self.canvas.create_line(grid_position[0] - letter_size, grid_position[1] - letter_size,
                                grid_position[0] + letter_size, grid_position[1] + letter_size, width=letter_thickness,fill=X_color)
        self.canvas.create_line(grid_position[0] - letter_size, grid_position[1] + letter_size,
                                grid_position[0] + letter_size, grid_position[1] - letter_size, width=letter_thickness,fill=X_color)

    def Gameover(self):
        if(self.X_wins):
            self.X_score += 1
            text = 'Winner: (X)'
            color = X_color
        elif(self.O_wins):
            self.O_score += 1
            text = 'Winner: (O)'
            color = O_color
        else:
            self.tie_score += 1
            text = 'tie'
            color = 'gray'
        self.canvas.delete('all')
        self.canvas.create_text(board_size / 2, board_size / 3, font='cmr 30 bold', fill=color, text=text)
        score_text = 'Scores'
        self.canvas.create_text(board_size / 2, 5 * board_size / 8, font='cmr 10 bold', fill=Green,text=score_text)
        score_text = '(X) : ' + str(self.X_score)
        score_text += '(O): ' + str(self.O_score)
        score_text += ' Tie: ' + str(self.tie_score)
        self.canvas.create_text(board_size / 2, 3 * board_size / 4, font='cmr 15 bold', fill=Green,text=score_text)
        self.reset = True
        score_text = 'please click'
        self.canvas.create_text(board_size / 2, 15 * board_size / 16, font='cmr 5 bold', fill='gray',text=score_text)

    def grid_position(self, log_position):
        log_position = n.array(log_position, dtype=int)
        return (board_size / 3) * log_position + board_size / 6

    def log_position(self, grid_position):
        grid_position = n.array(grid_position)
        return n.array(grid_position // (board_size / 3), dtype=int)

    def taken(self, log_position):
        if(self.status[log_position[0]][log_position[1]]==0):
            return False
        else:
            return True

    def wins(self, player):
        player = -1 if(player=='X')else 1
        for i in range(3):
            if(self.status[i][0]==self.status[i][1]==self.status[i][2]==player):
                return True
            if(self.status[0][i]==self.status[1][i]==self.status[2][i]==player):
                return True
        if(self.status[0][0]==self.status[1][1]==self.status[2][2]==player):
            return True
        if(self.status[0][2]==self.status[1][1]==self.status[2][0]==player):
            return True
        return False

    def ties(self):
        row, col = n.where(self.status == 0)
        tie = False
        if(len(row)==0):
            tie = True
        return tie

    def game_over(self):
        self.X_wins = self.wins('X')
        if(not self.X_wins):
            self.O_wins = self.wins('O')
        if(not self.O_wins):
            self.tie = self.ties()
        gameover = self.X_wins or self.O_wins or self.tie
        if(self.X_wins):
            print('X wins')
        if(self.O_wins):
            print('O wins')
        if(self.tie):
            print('tie')
        return gameover

    def click(self, event):
        grid_position = [event.x, event.y]
        log_position = self.log_position(grid_position)
        if(not self.reset):
            if(self.X_turns):
                if(not self.taken(log_position)):
                    self.create_X(log_position)
                    self.status[log_position[0]][log_position[1]] = -1
                    self.X_turns = not self.X_turns
            else:
                if(not self.taken(log_position)):
                    self.create_O(log_position)
                    self.status[log_position[0]][log_position[1]] = 1
                    self.X_turns = not self.X_turns
            if(self.game_over()):
                self.Gameover()
        else:
            self.canvas.delete('all')
            self.play_again()
            self.reset = False

instance = Tic_Tac_Toe()
instance.mainloop()