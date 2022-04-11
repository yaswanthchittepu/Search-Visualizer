# Returns the start state, end_state and a set of obstacles in the grid, given the state array
def get_grid_state(state):
    M, N = len(state), len(state[0])
    src = dest = None
    obs_set = set()
    for r in range(M):
        for c in range(N):
            if(state[r][c] == 1):
                obs_set.add((r,c))
            elif(state[r][c] == 2):
                src = (r, c)
            elif(state[r][c] == 3):
                dest = (r, c)
    return src, dest, obs_set