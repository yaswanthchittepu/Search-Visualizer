import parse, time
from tkinter import messagebox

class DFS(object):

    def __init__(self, gridworld):
        self.gridworld = gridworld
        self.grid, self.states, self.cmap, _, __ = gridworld.get_params()
        self.src, self.dest, self.obs_set = parse.get_grid_state(self.states)
        self.vis = set()

    def dfsUtil(self, r, c, v):
        gr, gc = self.dest
        sr, sc = self.src
        if(r == gr and c == gc):
            self.grid[r][c].configure(text = str(v))
            return True
        # Render
        if(r != sr or c != sc):
            self.states[r][c] = 4
            self.grid[r][c].configure(bg= self.cmap[4], text=str(v))
            time.sleep(2)
        self.vis.add((r,c))
        moves = [(-1,0),(0,1),(1,0),(0,-1)]
        M, N = len(self.states), len(self.states[0])
        for dr, dc in moves:
            if(0 <= r+dr < M and 0 <= c+dc < N and (r+dr,c+dc) not in self.obs_set and (r+dr,c+dc) not in self.vis and self.dfsUtil(r+dr, c+dc, v+1)):
                return True
        # Render
        if(r != sr or c != sc):
            self.states[r][c] = 5
            self.grid[r][c].configure(bg= self.cmap[5])
            time.sleep(2)
        return False

    def search(self):
        if(self.src is None or self.dest is None):
            messagebox.showerror("error", "Specify the source and the goal states in the Gridworld")
            return
        r, c = self.src
        self.dfsUtil(r, c, 0)
