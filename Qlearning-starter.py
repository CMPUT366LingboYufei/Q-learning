#++++++++++++++++++++++++++++++++++++
#Course name: CMPUT 366
#Instructor: Joseph Modayil
#Author:    Yufei Zhang, Lingbo Tang
#Author Id:    1373240     1353070
#Program_No 3
#Date Last Edited: Nov 27th,2014
#++++++++++++++++++++++++++++++++++++

#========All package needed=========#
import mountaincar
from Tilecoder import numTilings, tilecode, numTiles
from pylab import *
import random
import numpy as np

#=======Initial Values===================#
#All the parameters we need
#F is feature function get from TileCode
#actions is all three actions needed
#========================================#

numRuns = 1
numEpisodes = 200
alpha = 0.05/numTilings
gamma = 1
lmbda = 0.9
epsilon = 0
n = numTiles * 3
zerovec = zeros(n)
F = [-1]*numTilings
actions = [0,1,2]

runSum = 0.0

# Initialize the returns to get the learning value and curve

returns = np.zeros(shape=(numRuns,numEpisodes))   # I add it
	
    
    
# Main function main part
for run in range(numRuns):
    
    #Initializing the weight vec
    w = -0.01*rand(n)
    returnSum = 0.0
    for episodeNum in range(numEpisodes):
        G = 0
        "..."
        "your code goes here (20-30 lines, depending on modularity)"
        S = mountaincar.init()                         #Initialize state
        e = np.zeros(n)                                #Initialize eligibility vector
        steps = 0

        while (True):
            Q = [0, 0, 0]                              #The Q learning (S, A) pair with Feature
            A = 0                                           
            tilecode (S[0], S[1], F)                   #Get the (Position, velocity) and Fearture
            for j in range(3):	
                for i in F:
                    Q[j] = Q[j] + w[i + (j*9*9*4)]     # To compplete one tiling, 4 mapping is needed
	    
                if (random.uniform(0,1) < epsilon):    # Epsilon greedy
                    A = choice(actions)
                else: 
                    A = Q.index(max(Q))
                R,Sp  = mountaincar.sample (S,A)       # Learing update in one episode 
                delta = R - Q[A]
            G += R

            for i in F: e[i+(A*4*9*9)] = 1

            if (Sp == None): w += alpha*delta*e; break # If teminal state, end the episode

            Qp = [0,0,0]
            tilecode (Sp[0], Sp[1], F)
            for j in range(3):
                for i in F:
                    Qp[j] = Qp[j] + w[i + (j*9*9*4)]   # Update the next (S,A)

            steps += 1
            delta += Qp[argmax(Qp)]
            w     += alpha*delta*e
            e,S    = gamma*lmbda*e, Sp
            
        returns[run][episodeNum] = G                   # Collect returns in each run
        "..."
        print ("Episode: ", episodeNum, "Return: ", G)
        returnSum = returnSum + G
    print ("Average return:", returnSum/numEpisodes)
    runSum += returnSum
print ("Overall average return:", runSum/numRuns/numEpisodes)

def Qs(F):
    Q = [0,0,0]
    for j in range(3):	
        for i in F: Q[j] = Q[j] + w[i + (j*9*9*4)]     # Height actual implementation
    return Q

def writeF():                                        
    fout = open('value', 'w')
    F = [0]*numTilings
    steps = 50
    for i in range(steps):
        for j in range(steps):
            tilecode(-1.2+i*1.7/steps, -0.07+j*0.14/steps, F)
            height = -max(Qs(F))
            fout.write(repr(height) + ' ')
        fout.write('\n')
    fout.close()

def writeAverages(filename,averages):
    savetxt(filename,averages)

avrReturns = np.mean(returns, axis = 0)
writeF()
writeAverages('avrReturns', avrReturns)
