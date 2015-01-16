#++++++++++++++++++++++++++++++++++++
#Course name: CMPUT 366
#Instructor: Joseph Modayil
#Author:    Yufei Zhang, Lingbo Tang
#Author Id:    1373240     1353070 
#Date Last Edited: Nov 3rd,2014
#++++++++++++++++++++++++++++++++++++

import blackjack

from numpy import *
from random import *
from scipy import *
numEpisodes = 20


def showOneGame():
    s=blackjack.init()
    moves=[0,1] 
    turn=0
    Reward_sum = 0
    while s!=-1: #-1 is terminal
        a= moves[turn]
        r,sp=blackjack.sample(s,a)
        #print("turn %d: s %d a %d -> r %d sp %d "%(turn,s,a,r,sp),end="")
        #print("\t Player Sum: %d  Dealer Card: %d  Usable Ace: %d"%(blackjack.playerSum,blackjack.dealerCard, blackjack.usableAce))
        s=sp
        turn=random.randint(0,1)
        Reward_sum +=r
    return Reward_sum


returnSum = 0.0
for episodeNum in range(numEpisodes):
    G = showOneGame()
    print("Episode: ", episodeNum, "Return: ", G)
    returnSum = returnSum + G
    
print("Average return: ", returnSum/numEpisodes)