#!/usr/bin/python
import random

# Monte Carlo 

def mc(num_iters, epsilon):
    maze = Maze()
    for x in range(num_iters):
        s = random.randint(0, maze.num_states())
        t = True
        while t == True:
            a = maze.states[s].epsilon_greedy(epsilon)

    


