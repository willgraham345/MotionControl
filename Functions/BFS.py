from collections import deque

def BFS(initial_state, goal_state, actions, transition_fn):
    """
    Function Description:
    This function implements the Breadth First Search algorithm. These are basic algorithms for searching tree or graph data structures. 
    Variable Description:
    initial_state: initial state
    goal_state: goal state
    actions: list of possible actions
    transition: transition function
    """
    queue = deque([initial_state])
    visited = {}
    while queue:
        current_state = queue.popleft()
        if current_state == goal_state:
            print("Finished searching")
            return current_state
        visited.add(current_state)
        for action in actions:
            new_state = transition_fn(current_state, action)
            if new_state not in visited:
                queue.append(new_state)
        print("Current queue: ", queue)
        print("Current visited: ", visited)
        print("Current state: ", current_state)
    return None

if __name__ == "__main__":
    initial_state = [0,0]
    goal_state = [4, 3]
    actions = [[1,0], [0,1], [-1,0], [0,-1]]
    transition_fn = lambda s,a: [s[0]+a[0], s[1]+a[1]]
    BFS(initial_state, goal_state, actions, transition_fn)
    print("Finished searching")

