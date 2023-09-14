#numpy
#matplotlib
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

class Board:
    def __init__(self, seed=None):
        self.grid = np.zeros((9, 9), dtype=int)

    def is_Valid(self, num, row, col):
        grid = (row//3, col//3)
        if(num>9):
            return False
        s_row, e_row = grid[0]*3, grid[0]*3 + 3
        s_col, e_col = grid[1]*3, grid[1]*3 + 3
        if(num in self.grid[s_row: e_row, s_col:e_col]):
            return False
        elif(num in self.grid[:, col] or num in self.grid[row, :]):
            return False
        return True

    def fill_grid(self):
        for i in range(3):
            arr = np.arange(1, 10)
            np.random.shuffle(arr)
            arr = np.reshape(arr, (3, 3))
            self.grid[i*3:i*3+3, i*3:i*3+3] = arr
        i = j = 0
        prev_i = []
        prev_j = []
        prev_k = []
        k = 1
        while(i < 9):
            j = 0
            flag = 0
            while(j < 9):
                if(self.grid[i, j] == 0):
                    if(not flag):
                        temp = [x for x in range(1, 10)]
                    else:
                        temp = [x for x in range(k, 10)]
                    for k in temp:
                        if(self.is_Valid(k, i, j)):
                            self.grid[i, j] = k
                            prev_i.append(i)
                            prev_j.append(j)
                            prev_k.append(k)
                            temp.remove(k)
                            flag = 0
                            break
                    else:
                        i = prev_i.pop()
                        j = prev_j.pop()
                        self.grid[i, j] = 0
                        k = prev_k.pop() + 1
                        flag = 1
                        j -= 1
                j += 1
            if(0 in self.grid[i, :]):
                break
            i += 1

    def create_puzzle(self):
        n = 0
        self.puzzle = np.zeros((9, 9), dtype=str)        
        while(n < 15):
            i = np.random.randint(9)
            j = np.random.randint(9)
            if(self.puzzle[i, j] == ''):
                self.puzzle[i, j] = self.grid[i, j]
                self.puzzle[j, i] = self.grid[j, i]
                n += 1
        for row in range(9):
            for col in range(9):
                if(self.puzzle[row, col]==''):
                    self.puzzle[row, col]=' '
        print(self.puzzle)

    def show_puzzle(self):
        fig, abc = plt.subplots()
        abc.set_ylim(abc.get_ylim()[::-1])
        for i in range(0, 9):
            for j in range(0, 9):
                val = self.puzzle[j, i]
                abc.text(i+0.5, 9-(j+0.5), str(val), fontweight='bold', va='center', ha='center')
        abc.set_xlim(0, 9)
        abc.set_ylim(0, 9)
        abc.set_xticks(np.arange(9))
        abc.set_yticks(np.arange(9))
        abc.xaxis.set_major_locator(MultipleLocator(3))
        abc.xaxis.set_minor_locator(MultipleLocator(1))
        abc.yaxis.set_major_locator(MultipleLocator(3))
        abc.yaxis.set_minor_locator(MultipleLocator(1))
        abc.xaxis.grid(True,'minor')
        abc.yaxis.grid(True,'minor')
        abc.xaxis.grid(True,'major',linewidth=3)
        abc.yaxis.grid(True,'major',linewidth=3)
        plt.show()

board = Board()
board.fill_grid()
board.create_puzzle()
board.show_puzzle()
