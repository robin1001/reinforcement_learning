#!/usr/bin/python

from maze import Maze

def value_iteration(num_iters):
    maze = Maze()
    for x in range(num_iters):
        for i, state in enumerate(maze.states):
            if maze.is_final(i): continue
            maxi = float('-inf')
            best_action = None
            for action, dest in state.actions.iteritems():
                r = maze.reward(dest)
                v = maze.value(dest)
                if r + maze.gamma * v > maxi:
                    maxi = r + maze.gamma * v
                    best_action = action
                #print i, action, dest, r
            #print maxi
            state.value = maxi
            maze.pi[i] = best_action
    maze.info()
   

if __name__ == '__main__':
    value_iteration(num_iters)
