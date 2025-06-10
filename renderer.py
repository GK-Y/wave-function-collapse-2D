#only take sqr tiles
from PIL import Image
import wfc 
#----------------------------------------------------------------------
#setting up pillow
def Graphics(ls,imgSize):
    #side of sqr * length of each img
    totalSize = len(ls)*imgSize

    terrain = Image.new('RGB',(totalSize,totalSize))
    for i in range(len(ls)):
        arrHeight = i*imgSize
        for j in range(len(ls)):
            arrWidth = j*imgSize
            terrain.paste(tileMap[ls[i][j]],(arrWidth,arrHeight))
    return terrain

#dont use '\' as python gets confused u should use '/' which is also accepted file path format in windows
tileMap = {
    'g':Image.open("Tiles/grass.png"),
    'w':Image.open("Tiles/water.png"),
    's':Image.open("Tiles/sand.png"),
    'r':Image.open("Tiles/rock.png"),
    'l':Image.open("Tiles/lava.png")
    }

#-----------------------------------------------------------------------------------------------

#WFC
#setting up grid and tiles
chaosGrid = []
entropyPocket = ['g','w','s','r','l']
tileProb={
    'g':['g','w','s'],
    'w':['w','g'],
    's':['s','g','r'],
    'r':['r','l','s'],
    'l':['l','r'],
}

#control valves
size = 50 #size is length of map 
startPoint = [10,10]
startTile = 'r'

#initializer
wfc.inputArray(chaosGrid,entropyPocket,size)

#Terrain generation
wfc.generator(chaosGrid,tileProb,startTile,startPoint)

grid = chaosGrid
#----------------------------------------------------------------------------------

# terrain = Image.new('RGB',(1000,1000))
# terrain.paste(tileMap[0],(0,0))
s = tileMap[startTile].size[0]
terrain = Graphics(grid,s)

terrain.show()