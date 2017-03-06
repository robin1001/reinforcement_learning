#!/usr/bin/python
import random

class State:
    def __init__(self):
        self.actions = {}
        self.qfunc = {}
        self.value = 0
        self.reward = 0

    def add_action(self, action, dest):
        self.actions[action] = dest
        self.qfunc[action] = 0.0

    def transform(self, action):
        if action in self.actions:
            return self.actions[action]
        else:
            return 0
    
    def epsilon_greedy(self, epsilon):
        # find current best qfunc
        best_q = float('-inf')
        best_a = None
        for action, val in self.qfunc.iteritems():
            if val > best_q:
                best_q = val
                best_a = action
        # greedy
        if random.random() < epsilon:
            return best_a
        else: # random select
            while True:
                all_actions = self.qfunc.keys()
                i = random.randint(0, len(all_actions) - 1)
                if all_actions[i] != best_a:
                    return all_actions[i]

class Maze:
    def __init__(self):
        # 0 for dumpy state
        self.states = [State() for x in range(9)]
        self.pi = [None for x in range(9)]
        self.finals = {6, 7, 8}
        self.gamma = 0.8
        self.states[1].add_action('r', 2)
        self.states[1].add_action('d', 6)
        self.states[2].add_action('l', 1)
        self.states[2].add_action('r', 3)
        self.states[3].add_action('l', 2)
        self.states[3].add_action('r', 4)
        self.states[3].add_action('d', 7)
        self.states[4].add_action('l', 3)
        self.states[4].add_action('r', 5)
        self.states[5].add_action('l', 4)
        self.states[5].add_action('d', 8)

        #reward
        self.states[6].reward = -1
        self.states[7].reward = 1
        self.states[8].reward = -1

    def is_final(self, state):
        if state in self.finals or state == 0: return True
        else: return False

    def reward(self, i):
        return self.states[i].reward

    def value(self, i):
        return self.states[i].value

    def num_states(self):
        return len(self.states)

    def info(self):
        print 'pi', self.pi
        for state in self.states:
            print state.value, '\t', state.reward, state.actions


if __name__ == '__main__':
    maze = Maze()
    maze.info()
