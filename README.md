# Search-Visualizer
A Reusable Learning Object (RLO) to visualize AI Search Techniques

This widget needs the following modules to be installed:

tkinter
heapdict

Clone the repo and in the root directory, run 'python create_grid.py' to start the widget

Specify the dimensions of the grid world and submit your dimensions

In the gridworld, click on the cells to toggle their state. The defined states in the gridworld and the color used to represent this is provided below

1) Free cell -> White 
2) Obstacle cell -> Black
3) Start cell -> Green
4) Goal cell -> Red
5) Added to queue -> Yellow
6) Popped from queue/Visited -> Magenta

Out of these 6 states, only the first four are user toggle'able.  Access to the last two states is only provided to the search algorithms. Also more that 1 source or goal states are prohibited. If extra goal/start states are created, the previous ones are reset to free. Hence, the following order to set the states is recommended. 

First, set the goal state (red), followed by the start state (green)> Then, set the obstacles (black) as needed.

Once, this set up is done, run any search algorithm. The algorithms provide the distance to reach any cell on it's path from the start state, and provide state information on whether it was added or popped from the queue, to help visualize the search. The distance highlighted in the maganeta or goal cells, turns out to be the shortest distance, for any algorithm apart from Depth First Search (DFS). For Djikstra's and A-Star search, which find the shortest path from a start to goal state, the cost to move around is not 1, like was for Breadth First Search and Depth First Search. The transition cost is deterministic and is calculated through the following formula.

cost(i,j) = (i + j)%(min(M, N)) + 1

Here index i corresponds to the index of the cell (starting from 1), if the entire grid was flattened row wise into a 1D array. M, N are the row and column dimensions of the grid world respectively