import numpy as np

def DFS(s0, is_goal, t, actions):
    """ Variable Description:
    s0: initial state
    is_goal: goal state
    t: transition function
    actions: list of possible actions
    """
    frontier = [] # frontier stack (LIFO)
    visited = [] # visited dictionary
    frontier.push(s0)
    while not frontier: # this checks if the frontier is empty
        s = frontier.pop()
        if is_goal(s):
            return s
        if s not in visited:
            visited.append(s)
            for a in actions(s):
                frontier.push(t(s,a)) # t is the transition function

if "__name__" == "__main__":
    s0 = [0,0]
    is_goal = [4, 3]
    t = lambda s,a: [s[0]+a[0], s[1]+a[1]]
    actions = lambda s: [[1,0], [0,1], [-1,0], [0,-1]]
    DFS(s0, is_goal, t, actions)