# # Exercise 1 - Modifying the environment
# 
# In order to use RL and Dynamic programming, the agent needs to know its state.
# In the general case, it needs to estimate its state, however for the first part of the lecture we will simply provide the state to the agent.
# 
# In the case of our Dungeon environment, the state of the agent is entirely described by either the coordinates of the cell it is on, 
# or the index of the cell.
# 
# The first task is to modify the environment so that we can get all the necessary information:
# - the value function (can be represented as a dictionary, or an array) that maps the state to the value of the state. 
# As we don't know the true value at the beginning, it will be initialized at 1.
# - the transition matrix, which maps the state and actions to new states
# - the reward matrix, which maps the state and action to rewards
# 
# In the solutions of this lab, we will use the index of the cell as the state.
# 
# These can be calculated once an environment is instantiated.
# If the environment doesn't change after a reset, it doesn't need to be calculated again.
# 
# Next, we also need to adapt our step function, to return the state instead of our observations.
# 
# In order to modify the environment, a convenient way is to inherit our original Dungeon Class.

from dungeon.dungeon import Dungeon
from dungeon.dungeon import run_experiments
import numpy as np
from constants import Constants

class DungeonDP(Dungeon):
    
    def __init__(self, N):
        
        super().__init__(N)
        
        # Additional calculations to get the transition and reward matrix
        self.N = N
        self.upper = N - 1
        self.reward_matrix  = np.zeros( (N*N, 4, 1) )
        self.state_transition_matrix = np.zeros( (N*N, 4, N*N) )
        self.value_function = np.ones( (N*N) )
        self.INVALID_CELL_ID = -1
        # states empty, obstacle, lava, exit
        # fill the matrix with appropriate values
        cell_id = -1
        for x in range(self.N):
            print("-----------------")
            for y in range(self.N):
                cell_id += 1
                print("cell_id = %d x = %d y = %d" %(cell_id, x, y))
                for a in range(4):
                    self.is_valid_cell_id = True
                    new_cell_id = self.get_new_cell_id(x, y, a)
                    if self.is_valid_cell_id:    
                        self.state_transition_matrix[cell_id, a, new_cell_id] = 1

        print("State Transition matrix = ")
        print(self.state_transition_matrix)
        # What happens for cells corresponding to obstacles? what should they transition to?
        
    def get_new_cell_id(self, x, y, a):
        if a == Constants.UP:
            y += 1
        if a == Constants.DOWN:
            y -= 1
        if a == Constants.LEFT:
            x -= 1
        if a == Constants.RIGHT:
            x += 1
        return self.convert_to_cellId(x, y)

    def convert_to_cellId(self, x, y):
        if x < 0 or x > self.upper or y < 0 or y > self.upper:
            self.is_valid_cell_id = False 
            return self.INVALID_CELL_ID        
        new_cell_id = x * self.N + y
        print("new_cell_id = %d x = %d y = %d" %(new_cell_id, x, y))
        return new_cell_id
        
    """ def step(action):
        
        obs, rew, done = super().step(action)
        
        #state = ...
        
        return state, rew, done """