from dungeon.dungeon import Dungeon
from dungeon.dungeon import run_experiments
import numpy as np

# # Exercise 2 - Policy Evaluation
# 
# We will choose a random policy as initial policy.
# 
# Create a class Policy which is initialized as a random policy. (Each action can be picked with a probability of 0.25 for every state).
# 
# When calling the instance of a Policy, with a state as argument, this should return the selected action. 
# 
# We will also implement a method for policy evaluation, and a method for policy improvement.
# 

class Policy():
    
    def __init__(self, N):
        
        # the policy is a numpy array that collects all the probabilities of chosing an action when in a state
        self.policy = ...
        
    
    def __call__(self):
        
        # When called, the instance of Policy will return the selected action, sampled from the probability of actions
        
    def iterative_policy_evaluation( self, reward_matrix, state_transition_matrix, gamma):
    
        values = ... # initialize values to 0
    
        for iteration in range(k):
        
            # update values
        
        return values
         
        
    def greedy_improvement(values):
    
        new policy = ...
    
        self.policy = new_policy
        