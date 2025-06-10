import random
def inputArray(grid,pocket,s=3):
    for i in range(s):
        row=[]
        for j in range(s):
            row.append(pocket.copy())
        grid.append(row)
    return grid
#in inout array i used fiurst simply += but now changed to append and copy

def show(grid):
    s = len(grid)
    for i in range(s):
        print(grid[i],end=',')
        print("\n")
    print("\n")

def common(ls1,ls2):
    return list(set(ls1) & set(ls2))


#subraction/ entropy 

def entropyChange(grid,tileProb,centreVal,pos):
    posx,posy = pos[0],pos[1]
    grid[pos[0]][pos[1]] = centreVal
    lenGrid=[]
    s = len(grid)
    # centreVal = grid[posx][posy]
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if (i == 0 and j == 0):
                continue
            nx, ny = posx + i, posy + j

            if(0<=nx<s and 0<=ny<s ):
                if(type(grid[nx][ny])==str):
                    continue
                
                ls1 = grid[nx][ny]
                ls2 = tileProb[centreVal]
                
                grid[nx][ny] = common(ls1,ls2)

                if(grid[nx][ny] != []):
                    lenGrid.append([grid[nx][ny],[nx,ny]])
    
    return lenGrid #returns the neighbours and their posintion
    #take the return as neighbours var

# finding all min and indeces new centre
def collapse(neighbours,grid):
    templs=[]
    for i in range(len(neighbours)):
        templs.append(len(neighbours[i][0]))

    
    minFirst = min(templs)
    minEntropyls = []

    for i in range(len(neighbours)):
        if(len(neighbours[i][0])==minFirst):
            minEntropyls.append(neighbours[i])
    
    #in case already its in a collapsed state i.e. only one prob 
    if(minFirst == 1):
        for i in range(len(minEntropyls)):
            
            grid[minEntropyls[i][1][0]][minEntropyls[i][1][1]] = minEntropyls[i][0]
            
            randls = random.choice(minEntropyls)
            #collapse value and new pos
            return random.choice(randls[0]),randls[1]
    
    #random slector
    randls = random.choice(minEntropyls)
    #collapse value and new pos
    return random.choice(randls[0]),randls[1]

#backtracking 
#very simple just keeps going back to previous centres so not robust
#but works cuz eventually probability is reduced to only one collapsable list
#so works in this case
#we create a variable which has the index from last i.e. -1,-2 so on
#if the if condition is false then check automatically becomes 0 so we dont need
#an extra else to revert it back
#therefore as long as if is true it will maintain its former value
#but once if is broken it becomes 0 lol        

#checking if complete
#by checking if all data values are only strings
def gridComplete(grid):
    h = len(grid)
    for i in range(h):
        for j in range(h):
            if(type(grid[i][j]) == str):
                continue
            else:
                return 0
    return 1
#-------------------------------------------------------------------

#for backtracking checks position of new centre
#step counter for no. of iterations to solve it
def generator(chaosGrid,tileProb,newC,newPos):
    allC = [newC]
    allPos = [newPos]
    check = 0
    steps = 0
    while True:
        
        #updating grid
        neighbours = entropyChange(chaosGrid,tileProb,newC,newPos)
        
        #checking if its complete
        if(gridComplete(chaosGrid)):
            break
        
        #backtracking go above to read how it wrks
        if(neighbours==[]):
            if((check + 1) > len(allPos)):
                check = 0
            check+=1
            newC = allC[-check]
            newPos = allPos[-check]
            continue

        #Collapse and new value
        newC, newPos = collapse(neighbours,chaosGrid)
        if(newC==[]):
            if((check + 1) > len(allPos)):
                check = 0
            check+=1
            newC = allC[-check]
            newPos = allPos[-check]

        allC.append(newC)
        allPos.append(newPos)

        steps += 1
    return steps

