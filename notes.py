# Initialize the module
from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create()

# Send text to the screen
mc.postToChat("Hello World")                

# Warp to a point
mc.player.setTilePos(0,120,0)

# Define block
blocktype=103

# Create a block
mc.setBlock(7,1200,8,blocktype)       

# Gey your current position
mc.player.getPos()                         

# Make a big stack of blocks
# note: cannot be higher than 256
for i in range(612,1200): 
    mc.setBlock(-452.8469964701511,i,-63.63623952982889, blocktype)

mc.setBlocks(-1, -1, -1, 1, 1, 1, block.STONE.id)

# Make a big stack of TNT to blow up
blocktype = 46
for i in range(11,250): 
    mc.setBlock((-472.47649708497295,i,-50.14625260341045), blocktype)

# build a solid house
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
width = 10
height = 5
length = 6
blocktype = 4
mc.setBlocks(x,y,z,x + width, y + height, z + length, blocktype)

# make a hollow house (did not work)
x = pos.x + 1
y = pos.y + 1
z = pos.z + 1
width = 9
height = 4
length = 5
blocktype = 0
mc.setBlocks(x,y,z,x + width,y + height, z + length, blocktype)

# correct solution to build a hollow house from book
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
width = 10
height = 5
length = 6
blockType = 4
air = 0
mc.setBlocks(x, y, z, x + width, y + height, z + length, blockType)
mc.setBlocks(x + 1, y + 1, z + 1,
             x + width - 1, y + height - 1, z + length - 1, air)

# stacking blocks example from book
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
blockType = block.GLASS
up = 1
mc.setBlock(x, y, z, blockType)
mc.setBlock(x, y + up, z, blockType)

# More efficient way to make a stack of blocks
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
blockType = block.GLASS
for i in range(1,250):
    mc.setBlock(x, y+i, z, blockType)
