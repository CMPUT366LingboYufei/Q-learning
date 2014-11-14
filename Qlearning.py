#++++++++++++++++++++++++++++++++++++
#Course name: CMPUT 366
#Instructor: Joseph Modayil
#Author:    Yufei Zhang, Lingbo Tang
#Author Id:    1373240     1353070 
#Date Last Edited: Nov 3rd,2014
#++++++++++++++++++++++++++++++++++++

#========All package needed=========#
import blackjack
from numpy import *
from random import *
from scipy import *
#=======Initial Values==============#
# Create the experience data
# The "ex" is a 2-D array which stores 
# the value of the state action pair
# for each episode.

returnSum= 0.0
ex = zeros((182,2))
numEpisodes,alpha,epsilon = 10000000, 0.001, 1   


# Once we done all the episodes we can derive a policy
def policy(s): return argmax([ex[s,0], ex[s,1]])


# Qlearning Algorithms derived from randomPolicy is done by all the part
def Qlearning(ex):
  
  # Initial the state (deal the first card )
  s=blackjack.init()
  segma_r = 0
  while s!=-1:                                      # -1 is terminal
    a = argmax([ex[s,0], ex[s,1]])                 # Choose argmax(Q(s,a))   
    if random.uniform(0,1) < epsilon/2:            # e-greedy
      a = abs(a-1)    
      
    # Q(s,a) <- Q(s,a) + alpha * (r + argmax(Q(sp,a)) - Q(s,a))
    
    r,sp=blackjack.sample(s,a)                      # Get the reward and s'
    ex[s,a] += alpha * (r - ex[s,a] + ex[sp,argmax([ex[sp,0],ex[sp,1]])])  
    s=sp; segma_r += r                              # Return the value and next state
  return segma_r                                   

for episodeNum in range(numEpisodes):
  epsilon = 1/(episodeNum+1)                        # Stepwise alternated epsilon is best
  returnSum += Qlearning(ex)                        # Update for each episode

print("\nAverage return: ", returnSum/numEpisodes)
blackjack.printPolicy(policy)