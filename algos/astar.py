from heapdict import heapdict
import time, math, parse
from tkinter import messagebox
import math

class AStar(object):
    def __init__(self, gridworld):
        self.gridworld = gridworld
        self.grid, self.states, self.cmap, _, __ = gridworld.get_params()
        self.pq = heapdict()
        self.src, self.dest, self.obs_set = parse.get_grid_state(self.states)
        self.vis = set()
        M, N = len(self.states), len(self.states[0])
        self.min_dist = [[float('inf')]*N for _ in range(M)]

    def path_cost(self, ps, cs):
        (pr, pc), (cr, cc) = ps, cs
        M, N = len(self.states), len(self.states[0])
        cost = (N*(cr+pr)+pc+cc+2)%min(M,N) + 1
        return cost

    def heuristic_cost(self, cs, gs, hvar):
        (gr, gc), (cr, cc) = gs, cs
        cost = math.sqrt((cr-gr)**2 + (cc-gc)**2) if(hvar == 2) else (abs(cr-gr) + abs(cc-gc))
        return cost

    def search(self, hvar):
        if(self.src is None or self.dest is None):
            messagebox.showerror("error", "Specify the source and the goal states in the Gridworld")
            return
        sr, sc = self.src
        gr, gc = self.dest
        if(hvar == 0):
            messagebox.showerror("error", "Select a Heuristic for the A-star search")
            return
        # Tuple of total cost, path cost, heuristic cost
        self.pq[sr,sc] = (0,0,0)
        moves = [(-1,0),(0,1),(1,0),(0,-1)]
        M, N = len(self.states), len(self.states[0])
        while(self.pq):
            (r,c), v = self.pq.popitem()
            self.vis.add((r,c))
            self.min_dist[r][c] = v[1]
            if(r == gr and c == gc):
                self.grid[r][c].configure(text=str(v[1]))
                return
             # Render
            if(r != sr or c != sc):
                self.states[r][c] = 5
                self.grid[r][c].configure(bg= self.cmap[5], text=str(v[1]))
                time.sleep(2)
            for dr, dc in moves:
                if(0 <= r+dr < M and 0 <= c+dc < N and (r+dr,c+dc) not in self.obs_set and (r+dr,c+dc) not in self.vis):
                    pcost, hcost = v[1] + self.path_cost((r,c), (r+dr, c+dc)), self.heuristic_cost((r+dr, c+dc), self.dest, hvar)
                    if((r+dr, c+dc) in self.pq.keys()):
                        tp, pp, hp = self.pq[r+dr,c+dc]
                        if(tp > pcost+hcost):
                             self.pq[r+dr,c+dc] = (pcost+hcost, pcost, hcost)
                    else:
                        self.pq[r+dr,c+dc] = (pcost+hcost, pcost, hcost)
                    # Render
                    if(r+dr != gr or c+dc != gc):
                        self.states[r+dr][c+dc] = 4
                        self.grid[r+dr][c+dc].configure(bg= self.cmap[4], text=str(self.pq[r+dr,c+dc][1]))
                        time.sleep(2)
            
