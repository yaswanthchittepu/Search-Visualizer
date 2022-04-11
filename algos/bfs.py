from collections import deque
import parse
import time
from tkinter import messagebox

class BFS(object):
    def __init__(self, gridworld):
        self.gridworld = gridworld
        self.grid, self.states, self.cmap, _, __ = gridworld.get_params()
        self.q = deque([])
        self.src, self.dest, self.obs_set = parse.get_grid_state(self.states)
        self.vis = set()

    def search(self):
        if(self.src is None or self.dest is None):
            messagebox.showerror("error", "Specify the source and the goal states in the Gridworld")
            return
        gr, gc = self.dest
        sr, sc = self.src
        self.q.appendleft((sr, sc, 0))
        self.vis.add(self.src)
        moves = [(-1,0),(0,1),(1,0),(0,-1)]
        M, N = len(self.states), len(self.states[0])
        while(self.q):
            r, c, v = self.q.pop()
            if(r == gr and c == gc):
                self.grid[r][c].configure(text=str(v))
                time.sleep(2)
                return
            # Render
            if(r != sr or c != sc):
                self.states[r][c] = 5
                self.grid[r][c].configure(bg= self.cmap[5], text=str(v))
                time.sleep(2)
            for dr, dc in moves:
                if(0 <= r+dr < M and 0 <= c+dc < N and (r+dr,c+dc) not in self.obs_set and (r+dr,c+dc) not in self.vis):
                    self.q.appendleft((r+dr,c+dc,v+1))
                    self.vis.add((r+dr,c+dc))
                    # Render
                    if(r+dr != gr or c+dc != gc):
                        self.states[r+dr][c+dc] = 4
                        self.grid[r+dr][c+dc].configure(bg= self.cmap[4])
                        time.sleep(2)
            
