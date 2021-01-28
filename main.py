
# # Exercise 1 - Modifying the environment
# 
# See dungeonDP.py

from dungeon.dungeon import Dungeon
from dungeon.dungeon import run_experiments
from dungeonDP import DungeonDP
import numpy as np

# # Exercise 2 - Policy Evaluation
# 
# We will choose a random policy as initial policy.
# 
# See policy.py
# 


        
# # Policy Iteration
# 
# Now that you have both policy evaluation and improvement, you can interatively perform evaluation and improvement.
# 
# Calculate, after each improvement, how well the policy is doing. Maybe add some plots to see how it performs depending on parameters gamma and k (number of steps for policy evaluation).

def main():
    dungeon = DungeonDP(5)
    gamma = 0.2

    """ policy = Policy(10)

    for n_improvements in range(100):
        
        values = policy.iterative_policy_evaluation(reward_matrix, state_transition_matrix, gamma)
        policy.greedy_improvement(values)
        
        _, max_reward, mean_reward, var_reward = run_experiments(dungeon, policy) """
    
if __name__ == "__main__":
    main()

    
    
    
    
    


