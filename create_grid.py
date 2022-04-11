from tkinter import *
from tkinter import ttk, messagebox
from algos.bfs import BFS
from algos.dfs import DFS
from algos.djikstra import Djikstra
from algos.astar import AStar
import threading

class GridWorld(object):

    def __init__(self):

        # Defined States
        # 0 -> Free Cell (white)
        # 1 -> Obstacle (black)
        # 2 -> Source cell (green)
        # 3 -> Goal Cell (red)
        # 4 -> Push to frontier (yellow)
        # 5 -> Pop from frontier i.e (Mark state as visited) (magenta)

        self.grid = []
        self.states = []
        self.cmap = {0: 'white', 1: 'black', 2: 'green', 3: 'red', 4: 'yellow', 5: 'magenta'}
        self.src = None
        self.dest = None

    def set_params(self, grid):
        M = len(grid)
        if(M == 0):
            self.grid, self.states = [], []
        else:
            N = len(grid[0])
            self.grid = grid
            self.states = [[0]*N for _ in range(M)]

    def get_params(self):
        return self.grid, self.states, self.cmap, self.src, self.dest

    def _toggle(self, row, col, trgt):
        self.states[row][col] = trgt
        self.grid[row][col].configure(bg= self.cmap[trgt])
        self.grid[row][col].update()

    def user_toggle(self, row, col):
        if(self.states[row][col] == 0):
            pass
        elif(self.states[row][col] == 1):
            if(self.src is not None):
                r, c = self.src
                self._toggle(r, c, 0)
                self.grid[r][c].update()
            self.src = (row, col)
        elif(self.states[row][col] == 2):
            self.src = None
            if(self.dest is not None):
                r, c = self.dest
                self._toggle(r, c, 0)
                self.grid[r][c].update()
            self.dest = (row, col)
        else:
            self.dest = None
        self._toggle(row, col, (self.states[row][col]+1)%4)

    def search_toggle(self, row, col, frontier_state):
        self._toggle(row, col, frontier_state)


gridworld = GridWorld()

root = Tk()

frm = ttk.Frame(root, padding=30)
frm.grid()

board = ttk.Frame(root, padding=30)

radio_var = IntVar()

rLabel = Label(frm, text="Enter the Number of rows (max=15): ")
rLabel.grid(row=0, column=0)

e1 = Entry(frm, width=50)
e1.grid(row=0, column=1)

cLabel = Label(frm, text="Enter the Number of columns (max=15): ")
cLabel.grid(row=1, column=0)

e2 = Entry(frm, width=50)
e2.grid(row=1, column=1)

def emptyBoard():
    grid, states,_, __, ___ = gridworld.get_params()
    M, N = len(grid), len(grid[0])
    for r in range(M):
        for c in range(N):
            if(states[r][c]):
                states[r][c] = 0
                grid[r][c].configure(bg= 'white')
                grid[r][c].update()

def resetBoard():
    grid, states,_, __, ___ = gridworld.get_params()
    M, N = len(grid), len(grid[0])
    for r in range(M):
        for c in range(N):
            if(states[r][c] in [4,5]):
                states[r][c] = 0
                grid[r][c].configure(bg= 'white', text='')
                grid[r][c].update()
            else:
                grid[r][c].configure(text='')

def createBoard():
    M, N = e1.get(), e2.get()
    global board
    board.destroy()
    grid = []
    if((M == '' or N == '') or (int(M)*int(N) == 1)):
        gridworld.set_params(grid)
        messagebox.showerror("error", "Enter values for the dimensions of the grid")
    else:
        board = ttk.Frame(root, padding=30)
        board.grid()
        M, N = int(M), int(N)
        if(M > 15 or N > 15):
            M, N = min(M, 15), min(N, 15)
            messagebox.showwarning("Warning", "Dimensions were clipped to the max value, 15")
        for r in range(int(M)):
            grid.append([])
            for c in range(int(N)):
                cell = Button(board, bg='white', width=3, padx=20, pady=10, command=lambda r=r, c=c: gridworld.user_toggle(r, c))
                grid[r].append(cell)
                cell.grid(row=r, column=c)

        def start_thread_bfs(g):
            thread = threading.Thread(target=lambda : BFS(g).search())
            thread.start()

        def start_thread_dfs(g):
            thread = threading.Thread(target=lambda : DFS(g).search())
            thread.start()

        def start_thread_djikstra(g):
            thread = threading.Thread(target=lambda : Djikstra(g).search())
            thread.start()

        def start_thread_astar(g):
            thread = threading.Thread(target=lambda : AStar(g).search(radio_var.get()))
            thread.start()

        gridworld.set_params(grid)
        bfsButton = Button(board, text="Run BFS", command=lambda g=gridworld: start_thread_bfs(g))
        bfsButton.grid(row=0, column = N+2, columnspan=2)
        dfsButton = Button(board, text="Run DFS", command=lambda g=gridworld: start_thread_dfs(g))
        dfsButton.grid(row=1, column = N+2, columnspan=2)
        djikstraButton = Button(board, text="Run Djikstra", command=lambda g=gridworld: start_thread_djikstra(g))
        djikstraButton.grid(row=2, column = N+2, columnspan=2)
        aStarButton = Button(board, text="Run A-Star", command=lambda g=gridworld: start_thread_astar(g))
        aStarButton.grid(row=3, column = N+2, columnspan=2)
        radio_l1 = Radiobutton(board,text='L1-Norm', value=1,variable = radio_var)
        radio_l1.grid(row=3, column = N+4, columnspan=2)
        radio_l2_squared = Radiobutton(board,text='Squared L2-norm', value=2,variable = radio_var)
        radio_l2_squared.grid(row=3, column = N+6, columnspan=2)
        resetButton = Button(board, text="Reset Board", command=resetBoard)
        resetButton.grid(row=4, column = N+2, columnspan=2)
        emptyButton = Button(board, text="Empty Board", command=emptyBoard)
        emptyButton.grid(row=5, column = N+2, columnspan=2)


dimButton = Button(frm, text="Submit Dimensions", command = createBoard)
dimButton.grid(row=4, column=1)

root.mainloop()

