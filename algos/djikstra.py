from heapdict import heapdict
import parse
import time
from tkinter import messagebox

class Djikstra(object):
    def __init__(self, gridworld):
        self.gridworld = gridworld
        self.grid, self.states, self.cmap, _, __ = gridworld.get_params()
        self.pq = heapdict()
        self.src, self.dest, self.obs_set = parse.get_grid_state(self.states)
        self.vis = set()
        M, N = len(self.states), len(self.states[0])
        self.min_dist = [[float('inf')]*N for _ in range(M)]

    def get_cost(self, ps, cs):
        (pr, pc), (cr, cc) = ps, cs
        M, N = len(self.states), len(self.states[0])
        cost = (N*(cr+pr)+pc+cc+2)%min(M,N) + 1
        return cost

    def search(self):
        if(self.src is None or self.dest is None):
            messagebox.showerror("error", "Specify the source and the goal states in the Gridworld")
            return
        sr, sc = self.src
        gr, gc = self.dest
        self.pq[sr,sc] = 0
        moves = [(-1,0),(0,1),(1,0),(0,-1)]
        M, N = len(self.states), len(self.states[0])
        while(self.pq):
            (r,c), v = self.pq.popitem()
            self.vis.add((r,c))
            self.min_dist[r][c] = v
            if(r == gr and c == gc):
                self.grid[r][c].configure(text=str(v))
                return
             # Render
            if(r != sr or c != sc):
                self.states[r][c] = 5
                self.grid[r][c].configure(bg= self.cmap[5], text=str(v))
                time.sleep(2)
            for dr, dc in moves:
                if(0 <= r+dr < M and 0 <= c+dc < N and (r+dr,c+dc) not in self.obs_set and (r+dr,c+dc) not in self.vis):
                    self.pq[r+dr,c+dc] = min(self.pq.get((r+dr,c+dc), float('inf')), v + self.get_cost((r,c), (r+dr, c+dc)))
                    # Render
                    if(r+dr != gr or c+dc != gc):
                        self.states[r+dr][c+dc] = 4
                        self.grid[r+dr][c+dc].configure(bg= self.cmap[4], text=str(self.pq[r+dr,c+dc]))
                        time.sleep(2)
            
