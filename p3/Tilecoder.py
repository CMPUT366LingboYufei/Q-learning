import math

numTilings = 16
numTiles = 9 * 9 * numTilings
    
def tilecode(inx,iny,tileIndices):
    inx += 1.2 
    iny += 0.07

    for i in range (0, numTilings):
        xoffset = i * (0.2125) / numTilings
        yoffset = i * (0.0175 ) / numTilings 
        inXindex = int(math.floor (8 * (inx + xoffset)/1.7))
        inYindex = int(math.floor (8 * (iny + yoffset)/0.14))
        tileIndices[i] = int((81 * i) + (9 * inYindex) + inXindex)
    
    
def printTileCoderIndices(inx,iny):
    tileIndices = [-1]*numTilings
    tilecode(inx,iny,tileIndices)
    print ('Tile indices for input (',inx,',',iny,') are : ', tileIndices)

