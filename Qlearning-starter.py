import mountaincar
from Tilecoder import numTilings, tilecode, numTiles
from pylab import *
 
numRuns = 1
numEpisodes = 300
alpha = 0.05/numTilings
gamma = 1
lmbda = 0.9
epsilon = 0
n = numTiles * 3
zerovec = zeros(n)
F = [-1]*numTilings
 
runSum = 0.0
for run in range(numRuns):
    w = -0.01*rand(n)
    returnSum = 0.0
    for episodeNum in range(numEpisodes):
        G = 0
        "..."
        "your code goes here (20-30 lines, depending on modularity)"
        "..."
        print("Episode: ", episodeNum, "Return: ", G)
        returnSum = returnSum + G
    print("Average return:", returnSum/numEpisodes)
    runSum += returnSum
print("Overall average return:", runSum/numRuns/numEpisodes)
 
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
