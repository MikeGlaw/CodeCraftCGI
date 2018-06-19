#CGI World
#Kristopher Lantz
#Mike Greenlaw
# 6/13/18
# Company: CGI
# 
# Purpose: This program will allow a student to edit a variable and see said variable
# 		   printed to the screen

from codecraft import Game, Position
game = Game()
materials = game.materials
print(materials)

      

#-----------------List of functions-----------------#    


#Removes blocks in a radius. Used for TNT
def set_tnt(p):
    for i in range(-5,6):
        for j in range(-5,6):
            for k in range(-5,6):
                if((i*i)+(j*j)+(k*k) <= 25):
                    game.set_block(Position(p.x+i, p.y+j, p.z+k), 0)

#Checks block type. Calls set_tnt if block type is 88.
def block_type(p):
    block = game.get_block(p)
    if block == 88:
        print("BOOOOOOOOM!!!!!!")
        set_tnt(p)
    #print(block)
    
#This function allows the user to set blocks
def put_brick(p):
    game.set_block(p, 17)

#This function allows the user to delete blocks
def del_brick(p):
    game.set_block(p,0)
    
# The following function creates a block in the position specified
def setBlockPosition(x,y,z):
	game.set_block(Position(x,y,z), 21)


# The following function determines which letter should be created, and then calls
# the setblockPosition function to set the blocks in the correct place within
# a 5x6 grid.
def determineAndCreateLetter(newLetter,xPos,yPos,zPos):
	if newLetter == "A":
		setBlockPosition(xPos,yPos,zPos)
		setBlockPosition(xPos,yPos+1,zPos)
		setBlockPosition(xPos,yPos+2,zPos)
		setBlockPosition(xPos+1,yPos+2,zPos)
		setBlockPosition(xPos+1,yPos+3,zPos)
		setBlockPosition(xPos+1,yPos+4,zPos)
		setBlockPosition(xPos+1,yPos+5,zPos)
		setBlockPosition(xPos+2,yPos+6,zPos)
		setBlockPosition(xPos+3,yPos+6,zPos)
		setBlockPosition(xPos+4,yPos+5,zPos)
		setBlockPosition(xPos+4,yPos+4,zPos)
		setBlockPosition(xPos+4,yPos+3,zPos)
		setBlockPosition(xPos+4,yPos+2,zPos)
		setBlockPosition(xPos+5,yPos+2,zPos)
		setBlockPosition(xPos+5,yPos+1,zPos)
		setBlockPosition(xPos+5,yPos,zPos)
		setBlockPosition(xPos+2,yPos+3,zPos)
		setBlockPosition(xPos+3,yPos+3,zPos)
	
    	elif newLetter is "B":
            setBlockPosition(xPos,yPos,zPos)
            setBlockPosition(xPos,yPos+1,zPos)
            setBlockPosition(xPos,yPos+2,zPos)
            setBlockPosition(xPos,yPos+3,zPos)
            setBlockPosition(xPos,yPos+4,zPos)
            setBlockPosition(xPos,yPos+5,zPos)        	
            setBlockPosition(xPos,yPos+6,zPos)
            setBlockPosition(xPos+1,yPos+6,zPos)
            setBlockPosition(xPos+2,yPos+6,zPos)
            setBlockPosition(xPos+3,yPos+6,zPos)
            setBlockPosition(xPos+4,yPos+5,zPos)
            setBlockPosition(xPos+4,yPos+4,zPos)
            setBlockPosition(xPos+4,yPos+2,zPos)
            setBlockPosition(xPos+4,yPos+1,zPos)
            setBlockPosition(xPos+4,yPos,zPos)
            setBlockPosition(xPos+1,yPos,zPos)
            setBlockPosition(xPos+2,yPos,zPos)
            setBlockPosition(xPos+3,yPos,zPos)
            setBlockPosition(xPos+1,yPos+3,zPos)
            setBlockPosition(xPos+2,yPos+3,zPos)
            setBlockPosition(xPos+3,yPos+3,zPos)
            
        elif newLetter is "C":
            setBlockPosition(xPos+4,yPos+1,zPos)
            setBlockPosition(xPos+3,yPos,zPos)
            setBlockPosition(xPos+2,yPos,zPos)
            setBlockPosition(xPos+1,yPos,zPos)
            setBlockPosition(xPos,yPos+1,zPos)
            setBlockPosition(xPos,yPos+2,zPos)
            setBlockPosition(xPos,yPos+3,zPos)
            setBlockPosition(xPos,yPos+4,zPos)
            setBlockPosition(xPos,yPos+5,zPos)
            setBlockPosition(xPos+1,yPos+6,zPos)
            setBlockPosition(xPos+2,yPos+6,zPos)
            setBlockPosition(xPos+3,yPos+6,zPos)
            setBlockPosition(xPos+4,yPos+5,zPos)
        
        elif newLetter == "D":
            setBlockPosition(xPos,yPos,zPos)
            setBlockPosition(xPos,yPos+1,zPos)
            setBlockPosition(xPos,yPos+2,zPos)
            setBlockPosition(xPos,yPos+3,zPos)
            setBlockPosition(xPos,yPos+4,zPos)
            setBlockPosition(xPos,yPos+5,zPos)
            setBlockPosition(xPos,yPos+6,zPos)
            setBlockPosition(xPos+1,yPos+6,zPos)
            setBlockPosition(xPos+2,yPos+6,zPos)
            setBlockPosition(xPos+3,yPos+6,zPos)
            setBlockPosition(xPos+4,yPos+5,zPos)
            setBlockPosition(xPos+4,yPos+4,zPos)
            setBlockPosition(xPos+4,yPos+3,zPos)
            setBlockPosition(xPos+4,yPos+2,zPos)
            setBlockPosition(xPos+4,yPos+1,zPos)
            setBlockPosition(xPos+3,yPos,zPos)
            setBlockPosition(xPos+2,yPos,zPos)
            setBlockPosition(xPos+1,yPos,zPos)
        elif newLetter is "E":
            setBlockPosition(xPos,yPos,zPos)
            setBlockPosition(xPos,yPos+1,zPos)
            setBlockPosition(xPos,yPos+2,zPos)
            setBlockPosition(xPos,yPos+3,zPos)
            setBlockPosition(xPos,yPos+4,zPos)
            setBlockPosition(xPos,yPos+5,zPos)
            setBlockPosition(xPos,yPos+6,zPos)
            setBlockPosition(xPos+1,yPos+6,zPos)
            setBlockPosition(xPos+2,yPos+6,zPos)
            setBlockPosition(xPos+3,yPos+6,zPos)
            setBlockPosition(xPos+4,yPos+6,zPos)
            setBlockPosition(xPos+1,yPos+3,zPos)
            setBlockPosition(xPos+2,yPos+3,zPos)
            setBlockPosition(xPos+3,yPos+3,zPos)
            setBlockPosition(xPos+2,yPos,zPos)
            setBlockPosition(xPos+1,yPos,zPos)
            setBlockPosition(xPos+3,yPos,zPos)
            setBlockPosition(xPos+4,yPos,zPos)
            
        elif newLetter is "F":
            setBlockPosition(xPos,yPos,zPos)
            setBlockPosition(xPos,yPos+1,zPos)
            setBlockPosition(xPos,yPos+2,zPos)
            setBlockPosition(xPos,yPos+3,zPos)
            setBlockPosition(xPos,yPos+4,zPos)
            setBlockPosition(xPos,yPos+5,zPos)
            setBlockPosition(xPos,yPos+6,zPos)
            setBlockPosition(xPos+1,yPos+6,zPos)
            setBlockPosition(xPos+2,yPos+6,zPos)
            setBlockPosition(xPos+3,yPos+6,zPos)
            setBlockPosition(xPos+4,yPos+6,zPos)
            setBlockPosition(xPos+5,yPos+6,zPos)
            setBlockPosition(xPos+1,yPos+3,zPos)
            setBlockPosition(xPos+2,yPos+3,zPos)
            setBlockPosition(xPos+3,yPos+3,zPos)
            
        elif newLetter is "G":
            setBlockPosition(xPos+5,yPos+1,zPos)
            setBlockPosition(xPos+5,yPos+2,zPos)
            setBlockPosition(xPos+5,yPos+3,zPos)
            setBlockPosition(xPos+4,yPos+3,zPos)
            setBlockPosition(xPos+3,yPos+3,zPos)
            setBlockPosition(xPos+4,yPos,zPos)
            setBlockPosition(xPos+3,yPos,zPos)
            setBlockPosition(xPos+2,yPos,zPos)
            setBlockPosition(xPos+1,yPos,zPos)
            setBlockPosition(xPos,yPos+1,zPos)
            setBlockPosition(xPos,yPos+2,zPos)
            setBlockPosition(xPos,yPos+3,zPos)
            setBlockPosition(xPos,yPos+4,zPos)
            setBlockPosition(xPos,yPos+5,zPos)
            setBlockPosition(xPos+1,yPos+6,zPos)
            setBlockPosition(xPos+2,yPos+6,zPos)
            setBlockPosition(xPos+3,yPos+6,zPos)
            setBlockPosition(xPos+4,yPos+6,zPos)
        elif newLetter == "H":
            setBlockPosition(xPos,yPos,zPos)
            setBlockPosition(xPos,yPos+1,zPos)
            setBlockPosition(xPos,yPos+2,zPos)
            setBlockPosition(xPos,yPos+3,zPos)
            setBlockPosition(xPos,yPos+4,zPos)
            setBlockPosition(xPos,yPos+5,zPos)
            setBlockPosition(xPos,yPos+6,zPos)
            setBlockPosition(xPos+5,yPos,zPos)
            setBlockPosition(xPos+5,yPos+1,zPos)
            setBlockPosition(xPos+5,yPos+2,zPos)
            setBlockPosition(xPos+5,yPos+3,zPos)
            setBlockPosition(xPos+5,yPos+4,zPos)
            setBlockPosition(xPos+5,yPos+5,zPos)
            setBlockPosition(xPos+5,yPos+6,zPos)
            setBlockPosition(xPos+1,yPos+3,zPos)
            setBlockPosition(xPos+2,yPos+3,zPos)
            setBlockPosition(xPos+3,yPos+3,zPos)
            setBlockPosition(xPos+4,yPos+3,zPos)
        elif newLetter == "I":
            setBlockPosition(xPos+2,yPos,zPos)
            setBlockPosition(xPos+4,yPos,zPos)
            setBlockPosition(xPos+3,yPos,zPos)
            setBlockPosition(xPos+3,yPos+1,zPos)
            setBlockPosition(xPos+3,yPos+2,zPos)
            setBlockPosition(xPos+3,yPos+3,zPos)
            setBlockPosition(xPos+3,yPos+4,zPos)
            setBlockPosition(xPos+3,yPos+5,zPos)
            setBlockPosition(xPos+3,yPos+6,zPos)
            setBlockPosition(xPos+2,yPos+6,zPos)
            setBlockPosition(xPos+4,yPos+6,zPos)
            setBlockPosition(xPos+5,yPos,zPos)
            setBlockPosition(xPos+5,yPos+6,zPos)
            setBlockPosition(xPos+1,yPos,zPos)
            setBlockPosition(xPos+1,yPos+6,zPos)
        elif newLetter == "J":
            setBlockPosition(xPos+3,yPos,zPos)
            setBlockPosition(xPos+2,yPos,zPos)
            setBlockPosition(xPos+1,yPos,zPos)
            setBlockPosition(xPos+1,yPos+1,zPos)
            setBlockPosition(xPos+3,yPos+1,zPos)
            setBlockPosition(xPos+3,yPos+2,zPos)
            setBlockPosition(xPos+3,yPos+3,zPos)
            setBlockPosition(xPos+3,yPos+4,zPos)
            setBlockPosition(xPos+3,yPos+5,zPos)
            setBlockPosition(xPos+3,yPos+6,zPos)
            setBlockPosition(xPos+4,yPos+6,zPos)
            setBlockPosition(xPos+5,yPos+6,zPos)
            setBlockPosition(xPos+2,yPos+6,zPos)
            setBlockPosition(xPos+1,yPos+6,zPos)
        elif newLetter == "K":
            setBlockPosition(xPos,yPos,zPos)
            setBlockPosition(xPos,yPos+1,zPos)
            setBlockPosition(xPos,yPos+2,zPos)
            setBlockPosition(xPos,yPos+3,zPos)
            setBlockPosition(xPos,yPos+4,zPos)
            setBlockPosition(xPos,yPos+5,zPos)
            setBlockPosition(xPos,yPos+6,zPos)
            setBlockPosition(xPos+1,yPos+3,zPos)
            setBlockPosition(xPos+2,yPos+4,zPos)
            setBlockPosition(xPos+3,yPos+5,zPos)
            setBlockPosition(xPos+4,yPos+6,zPos)
            setBlockPosition(xPos+2,yPos+2,zPos)
            setBlockPosition(xPos+3,yPos+1,zPos)
            setBlockPosition(xPos+4,yPos,zPos)
            setBlockPosition(xPos+5,yPos,zPos)
            
        elif newLetter == "L":
            setBlockPosition(xPos,yPos,zPos)
            setBlockPosition(xPos,yPos+1,zPos)
            setBlockPosition(xPos,yPos+2,zPos)
            setBlockPosition(xPos,yPos+3,zPos)
            setBlockPosition(xPos,yPos+4,zPos)
            setBlockPosition(xPos,yPos+5,zPos)
            setBlockPosition(xPos,yPos+6,zPos)
            setBlockPosition(xPos+4,yPos,zPos)
            setBlockPosition(xPos+3,yPos,zPos)
            setBlockPosition(xPos+2,yPos,zPos)
            setBlockPosition(xPos+1,yPos,zPos)
        elif newLetter == "M":
            setBlockPosition(xPos,yPos,zPos)
            setBlockPosition(xPos,yPos+1,zPos)
            setBlockPosition(xPos,yPos+2,zPos)
            setBlockPosition(xPos,yPos+3,zPos)
            setBlockPosition(xPos,yPos+4,zPos)
            setBlockPosition(xPos,yPos+5,zPos)
            setBlockPosition(xPos,yPos+6,zPos)
            setBlockPosition(xPos+5,yPos,zPos)
            setBlockPosition(xPos+5,yPos+1,zPos)
            setBlockPosition(xPos+5,yPos+2,zPos)
            setBlockPosition(xPos+5,yPos+3,zPos)
            setBlockPosition(xPos+5,yPos+4,zPos)
            setBlockPosition(xPos+5,yPos+5,zPos)
            setBlockPosition(xPos+5,yPos+6,zPos)
            setBlockPosition(xPos+1,yPos+5,zPos)
            setBlockPosition(xPos+2,yPos+4,zPos)
            setBlockPosition(xPos+3,yPos+4,zPos)
            setBlockPosition(xPos+4,yPos+5,zPos)
        elif newLetter == "N":
            setBlockPosition(xPos,yPos,zPos)
            setBlockPosition(xPos,yPos+1,zPos)
            setBlockPosition(xPos,yPos+2,zPos)
            setBlockPosition(xPos,yPos+3,zPos)
            setBlockPosition(xPos,yPos+4,zPos)
            setBlockPosition(xPos,yPos+5,zPos)
            setBlockPosition(xPos,yPos+6,zPos)
            setBlockPosition(xPos+5,yPos,zPos)
            setBlockPosition(xPos+5,yPos+1,zPos)
            setBlockPosition(xPos+5,yPos+2,zPos)
            setBlockPosition(xPos+5,yPos+3,zPos)
            setBlockPosition(xPos+5,yPos+4,zPos)
            setBlockPosition(xPos+5,yPos+5,zPos)
            setBlockPosition(xPos+5,yPos+6,zPos)
            setBlockPosition(xPos+1,yPos+5,zPos)
            setBlockPosition(xPos+1,yPos+4,zPos)
            setBlockPosition(xPos+2,yPos+4,zPos)
            setBlockPosition(xPos+2,yPos+3,zPos)
            setBlockPosition(xPos+3,yPos+3,zPos)
            setBlockPosition(xPos+3,yPos+2,zPos)
            setBlockPosition(xPos+4,yPos+2,zPos)
            setBlockPosition(xPos+4,yPos+1,zPos)
        elif newLetter == "O":
            setBlockPosition(xPos,yPos+1,zPos)
            setBlockPosition(xPos,yPos+2,zPos)
            setBlockPosition(xPos,yPos+3,zPos)
            setBlockPosition(xPos,yPos+4,zPos)
            setBlockPosition(xPos,yPos+5,zPos)
            setBlockPosition(xPos+5,yPos+1,zPos)
            setBlockPosition(xPos+5,yPos+2,zPos)
            setBlockPosition(xPos+5,yPos+3,zPos)
            setBlockPosition(xPos+5,yPos+4,zPos)
            setBlockPosition(xPos+5,yPos+5,zPos)
            setBlockPosition(xPos+4,yPos+6,zPos)
            setBlockPosition(xPos+3,yPos+6,zPos)
            setBlockPosition(xPos+2,yPos+6,zPos)
            setBlockPosition(xPos+1,yPos+6,zPos)
            setBlockPosition(xPos+4,yPos,zPos)
            setBlockPosition(xPos+3,yPos,zPos)
            setBlockPosition(xPos+2,yPos,zPos)
            setBlockPosition(xPos+1,yPos,zPos)
            

        elif newLetter == "P":
            setBlockPosition(xPos,yPos,zPos)
            setBlockPosition(xPos,yPos+1,zPos)
            setBlockPosition(xPos,yPos+2,zPos)
            setBlockPosition(xPos,yPos+3,zPos)
            setBlockPosition(xPos,yPos+4,zPos)
            setBlockPosition(xPos,yPos+5,zPos)
            setBlockPosition(xPos,yPos+6,zPos)
            
            setBlockPosition(xPos+1,yPos+6,zPos)
            setBlockPosition(xPos+2,yPos+6,zPos)
            setBlockPosition(xPos+3,yPos+6,zPos)
            
            setBlockPosition(xPos+1,yPos+3,zPos)
            setBlockPosition(xPos+2,yPos+3,zPos)
            setBlockPosition(xPos+3,yPos+3,zPos)
            
            setBlockPosition(xPos+4,yPos+4,zPos)
            setBlockPosition(xPos+4,yPos+5,zPos)
                             
                             
        elif newLetter == "Q":
            setBlockPosition(xPos,yPos+1,zPos)
            setBlockPosition(xPos,yPos+2,zPos)
            setBlockPosition(xPos,yPos+3,zPos)
            setBlockPosition(xPos,yPos+4,zPos)
            setBlockPosition(xPos,yPos+5,zPos)
            setBlockPosition(xPos+5,yPos+1,zPos)
            setBlockPosition(xPos+5,yPos+2,zPos)
            setBlockPosition(xPos+5,yPos+3,zPos)
            setBlockPosition(xPos+5,yPos+4,zPos)
            setBlockPosition(xPos+5,yPos+5,zPos)
            setBlockPosition(xPos+4,yPos+6,zPos)
            setBlockPosition(xPos+3,yPos+6,zPos)
            setBlockPosition(xPos+2,yPos+6,zPos)
            setBlockPosition(xPos+1,yPos+6,zPos)
            setBlockPosition(xPos+4,yPos,zPos)
            setBlockPosition(xPos+3,yPos,zPos)
            setBlockPosition(xPos+2,yPos,zPos)
            setBlockPosition(xPos+1,yPos,zPos)
            setBlockPosition(xPos+4,yPos+1,zPos)
            setBlockPosition(xPos+3,yPos+2,zPos)
        elif newLetter == "R":
            setBlockPosition(xPos,yPos,zPos)
            setBlockPosition(xPos,yPos+1,zPos)
            setBlockPosition(xPos,yPos+2,zPos)
            setBlockPosition(xPos,yPos+3,zPos)
            setBlockPosition(xPos,yPos+4,zPos)
            setBlockPosition(xPos,yPos+5,zPos)
            setBlockPosition(xPos,yPos+6,zPos)
            setBlockPosition(xPos+1,yPos+6,zPos)
            setBlockPosition(xPos+2,yPos+6,zPos)
            setBlockPosition(xPos+3,yPos+6,zPos)
            setBlockPosition(xPos+4,yPos+5,zPos)
            setBlockPosition(xPos+4,yPos+4,zPos)
            setBlockPosition(xPos+1,yPos+3,zPos)
            setBlockPosition(xPos+2,yPos+3,zPos)
            setBlockPosition(xPos+3,yPos+3,zPos)
            setBlockPosition(xPos+3,yPos+2,zPos)
            setBlockPosition(xPos+4,yPos+1,zPos)
            setBlockPosition(xPos+5,yPos,zPos)
            
        elif newLetter == "S":
            setBlockPosition(xPos,yPos,zPos)
            setBlockPosition(xPos+1,yPos,zPos)
            setBlockPosition(xPos+2,yPos,zPos)
            setBlockPosition(xPos+3,yPos,zPos)
            setBlockPosition(xPos+4,yPos+1,zPos)
            setBlockPosition(xPos+4,yPos+2,zPos)
            setBlockPosition(xPos+3,yPos+3,zPos)
            setBlockPosition(xPos+2,yPos+3,zPos)
            setBlockPosition(xPos+1,yPos+3,zPos)
            setBlockPosition(xPos,yPos+4,zPos)
            setBlockPosition(xPos,yPos+5,zPos)
            setBlockPosition(xPos+1,yPos+6,zPos)
            setBlockPosition(xPos+2,yPos+6,zPos)
            setBlockPosition(xPos+3,yPos+6,zPos)
            setBlockPosition(xPos+4,yPos+6,zPos)
        elif newLetter == "T":
            setBlockPosition(xPos+3,yPos,zPos)
            setBlockPosition(xPos+3,yPos+1,zPos)
            setBlockPosition(xPos+3,yPos+2,zPos)
            setBlockPosition(xPos+3,yPos+3,zPos)
            setBlockPosition(xPos+3,yPos+4,zPos)
            setBlockPosition(xPos+3,yPos+5,zPos)
            setBlockPosition(xPos+3,yPos+6,zPos)
            setBlockPosition(xPos+4,yPos+6,zPos)
            setBlockPosition(xPos+5,yPos+6,zPos)
            setBlockPosition(xPos+2,yPos+6,zPos)
            setBlockPosition(xPos+1,yPos+6,zPos)
        elif newLetter == "U":
            setBlockPosition(xPos,yPos+1,zPos)
            setBlockPosition(xPos,yPos+2,zPos)
            setBlockPosition(xPos,yPos+3,zPos)
            setBlockPosition(xPos,yPos+4,zPos)
            setBlockPosition(xPos,yPos+5,zPos)
            setBlockPosition(xPos,yPos+6,zPos)
            setBlockPosition(xPos+5,yPos+1,zPos)
            setBlockPosition(xPos+5,yPos+2,zPos)
            setBlockPosition(xPos+5,yPos+3,zPos)
            setBlockPosition(xPos+5,yPos+4,zPos)
            setBlockPosition(xPos+5,yPos+5,zPos)
            setBlockPosition(xPos+5,yPos+6,zPos)
            
            setBlockPosition(xPos+1,yPos,zPos)
            setBlockPosition(xPos+2,yPos,zPos)
            setBlockPosition(xPos+3,yPos,zPos)
            setBlockPosition(xPos+4,yPos,zPos)
            
        elif newLetter == "V":
            setBlockPosition(xPos,yPos+2,zPos)
            setBlockPosition(xPos,yPos+3,zPos)
            setBlockPosition(xPos,yPos+4,zPos)
            setBlockPosition(xPos,yPos+5,zPos)
            setBlockPosition(xPos,yPos+6,zPos)
            setBlockPosition(xPos+5,yPos+2,zPos)
            setBlockPosition(xPos+5,yPos+3,zPos)
            setBlockPosition(xPos+5,yPos+4,zPos)
            setBlockPosition(xPos+5,yPos+5,zPos)
            setBlockPosition(xPos+5,yPos+6,zPos)
            setBlockPosition(xPos+2,yPos,zPos)
            setBlockPosition(xPos+3,yPos,zPos)
            setBlockPosition(xPos+1,yPos+1,zPos)
            setBlockPosition(xPos+4,yPos+1,zPos)
            
        elif newLetter == "W":
            setBlockPosition(xPos,yPos,zPos)
            setBlockPosition(xPos,yPos+1,zPos)
            setBlockPosition(xPos,yPos+2,zPos)
            setBlockPosition(xPos,yPos+3,zPos)
            setBlockPosition(xPos,yPos+4,zPos)
            setBlockPosition(xPos,yPos+5,zPos)
            setBlockPosition(xPos,yPos+6,zPos)
            setBlockPosition(xPos+5,yPos,zPos)
            setBlockPosition(xPos+5,yPos+1,zPos)
            setBlockPosition(xPos+5,yPos+2,zPos)
            setBlockPosition(xPos+5,yPos+3,zPos)
            setBlockPosition(xPos+5,yPos+4,zPos)
            setBlockPosition(xPos+5,yPos+5,zPos)
            setBlockPosition(xPos+5,yPos+6,zPos)
            setBlockPosition(xPos+1,yPos,zPos)
            setBlockPosition(xPos+4,yPos,zPos)
            setBlockPosition(xPos+3,yPos+1,zPos)
            setBlockPosition(xPos+2,yPos+1,zPos)
            setBlockPosition(xPos+2,yPos+2,zPos)
            setBlockPosition(xPos+3,yPos+2,zPos)
            
        elif newLetter == "X":
            setBlockPosition(xPos,yPos,zPos)
            setBlockPosition(xPos,yPos+1,zPos)
            setBlockPosition(xPos+5,yPos,zPos)
            setBlockPosition(xPos+5,yPos+1,zPos)
            
            setBlockPosition(xPos,yPos+6,zPos)
            setBlockPosition(xPos,yPos+5,zPos)
            setBlockPosition(xPos+5,yPos+6,zPos)
            setBlockPosition(xPos+5,yPos+5,zPos)
            
            setBlockPosition(xPos+1,yPos+4,zPos)
            setBlockPosition(xPos+1,yPos+2,zPos)
            setBlockPosition(xPos+4,yPos+4,zPos)
            setBlockPosition(xPos+4,yPos+2,zPos)
            setBlockPosition(xPos+2,yPos+3,zPos)
            setBlockPosition(xPos+3,yPos+3,zPos)
            
        elif newLetter == "Y":
            setBlockPosition(xPos+3,yPos,zPos)
            setBlockPosition(xPos+3,yPos+1,zPos)
            setBlockPosition(xPos+3,yPos+2,zPos)
            
            setBlockPosition(xPos+4,yPos+3,zPos)
            setBlockPosition(xPos+2,yPos+3,zPos)
            
            setBlockPosition(xPos+1,yPos+4,zPos)
            setBlockPosition(xPos+1,yPos+5,zPos)
            setBlockPosition(xPos+1,yPos+6,zPos)
            
            setBlockPosition(xPos+5,yPos+4,zPos)
            setBlockPosition(xPos+5,yPos+5,zPos)
            setBlockPosition(xPos+5,yPos+6,zPos)
            
        elif newLetter == "Z":
            setBlockPosition(xPos,yPos,zPos)
            setBlockPosition(xPos+4,yPos,zPos)
            setBlockPosition(xPos+3,yPos,zPos)
            setBlockPosition(xPos+2,yPos,zPos)
            setBlockPosition(xPos+1,yPos,zPos)
            setBlockPosition(xPos,yPos+6,zPos)
            setBlockPosition(xPos+1,yPos+6,zPos)
            setBlockPosition(xPos+2,yPos+6,zPos)
            setBlockPosition(xPos+3,yPos+6,zPos)
            setBlockPosition(xPos+4,yPos+6,zPos)
            setBlockPosition(xPos+4,yPos+5,zPos)
            setBlockPosition(xPos+3,yPos+4,zPos)
            setBlockPosition(xPos+2,yPos+3,zPos)
            setBlockPosition(xPos+1,yPos+2,zPos)
            setBlockPosition(xPos,yPos+1,zPos)
        elif newLetter == ".":
            setBlockPosition(xPos,yPos,zPos)	
            setBlockPosition(xPos+1,yPos,zPos)
            setBlockPosition(xPos,yPos+1,zPos)
            setBlockPosition(xPos+1,yPos+1,zPos)
            
            


# The following function takes sentences or single words and turns them into a list.
# It then calls the convertWordToSingleLetter function for every letter in the list,
# which then assembles the blocks in the game to create the word or sentence.
def convertStringToBlocks(textString):
	
    # The following three variables will be used to position and track the text that will be
	# created after calling the convertStringToBlocks function.
	xCoord = -80
	yCoord = 1
	zCoord = -80
	
	textString = textString.upper()
	words = textString.split()
	
	#if statement executes if there is more than one word in the array
	if len(words) > 1:
		for word in words:
			convertWordToSingleLetter = list(word)
			for wordLetter in convertWordToSingleLetter:
				determineAndCreateLetter(wordLetter, xCoord, yCoord, zCoord)
      
				#This increase to xCoord is based on size and spacing of each letter
				xCoord+=7
			
			#This increase to xCoord is based on the spacing between each word. 
      		#There will be five spaces as when xCoord increases by seven
			#after the last letter, it adds a space after said letter.
			xCoord+=4
	
	#else if executes if there is either one word or just letters
	elif len(words) == 1:
		wordList = list(textString)
		for letter in wordList:
			determineAndCreateLetter(letter, xCoord, yCoord, zCoord)
			#Using +=7 because each letter is six wide plus a slight space inbetween
			xCoord+=7
			
	else:
        	textString = "Error. Hold the power button for ten seconds to restart game."
		convertStringToBlocks(textString)



# The following functions builds the platform the CGI lettering stands on
def buildPlatform():
    for i in range(1,18):
        for j in range(1,17):
            game.set_block(Position(i, 1, j), 86)


    # Builds the enclosure around CGI lettering
    for i in range(19):
        game.set_block(Position(i, 0, 0), 15)
        game.set_block(Position(i, 11, 0), 15)
        game.set_block(Position(i, 0, 17), 15)
        game.set_block(Position(i, 11, 17), 15)

    for i in range(12):
        game.set_block(Position(0,i,0), 15)
        game.set_block(Position(0,i,17), 15)
        game.set_block(Position(18,i,0), 15)
        game.set_block(Position(18,i,17), 15)

    for i in range(18):
        game.set_block(Position(0,0,i), 15)
        game.set_block(Position(0,11,i), 15)
        game.set_block(Position(18,11,i), 15)
        game.set_block(Position(18,0,i), 15)


    # This code creates the letter C    
    game.set_block(Position(11,3,8),13)    
    game.set_block(Position(12,2,8),13)
    game.set_block(Position(13,2,8),13)
    game.set_block(Position(14,2,8),13)

    game.set_block(Position(15,3,8),13)

    game.set_block(Position(16,4,8),13)
    game.set_block(Position(16,5,8),13)
    game.set_block(Position(16,6,8),13)
    game.set_block(Position(16,7,8),13)

    game.set_block(Position(15,8,8),13)

    game.set_block(Position(14,9,8),13)
    game.set_block(Position(13,9,8),13)
    game.set_block(Position(12,9,8),13)

    game.set_block(Position(11,8,8),13)


    # The following code creates the letter G
    game.set_block(Position(4,3,8),13)
    game.set_block(Position(4,2,8),13)
    game.set_block(Position(5,2,8),13)
    game.set_block(Position(6,2,8),13)
    game.set_block(Position(7,2,8),13)
    game.set_block(Position(4,4,8),13)
    game.set_block(Position(4,5,8),13)
    game.set_block(Position(5,5,8),13)


    game.set_block(Position(8,3,8),13)
    game.set_block(Position(8,2,8),13)
    game.set_block(Position(9,3,8),13)

    game.set_block(Position(9,4,8),13)
    game.set_block(Position(9,5,8),13)
    game.set_block(Position(9,6,8),13)
    game.set_block(Position(9,7,8),13)

    game.set_block(Position(8,8,8),13)
    game.set_block(Position(9,8,8),13)
    game.set_block(Position(8,9,8),13)

    game.set_block(Position(7,9,8),13)
    game.set_block(Position(6,9,8),13)
    game.set_block(Position(5,9,8),13)

    game.set_block(Position(4,8,8),13)


    # The following code creates the letter I

    for i in range(2,10):
        game.set_block(Position(2,i,8),13)


      

    
# This puts a gap between the CGI platform and land. If timed correctly one can jump from
# the grass to the platform. A possible rewarding challenge for students.
def makePlatformGap():
    for i in range(-10,29):
        for j in range(-10,28):
            game.set_block(Position(i,0,j),0)
      

# This function builds a platform to prevent having to refresh after a fall
def preventFall():
    for i in range(-50,50):
        for j in range(-50,50):
            game.set_block(Position(i,-20,j),34)
    

# This function builds the target by creating the outer circle first, and each consecutive
# smaller circle overwrites the blocks of the previous larger circle.
def buildTarget():
    for i in range(-50,51):
        for j in range(-50,51):
            if (i*i + j*j <= 2500):
                game.set_block(Position(i-80,0,j-20),13)
    for i in range(-40,41):
        for j in range(-40,41):
            if (i*i + j*j <= 1600):
                game.set_block(Position(i-80,0,j-20),8)
    
    for i in range(-30,31):
        for j in range(-30,31):
            if (i*i + j*j <= 900):
                game.set_block(Position(i-80,0,j-20),13)
    
    for i in range(-20,21):
        for j in range(-20,21):
            if (i*i + j*j <= 400):
                game.set_block(Position(i-80,0,j-20),8)
    
    for i in range(-10,11):
        for j in range(-10,11):
            if (i*i + j*j <= 100):
                game.set_block(Position(i-80,0,j-20),13)
    
    for i in range(-5,6):
        for j in range(-5,6):
            if (i*i + j*j <= 25):
                game.set_block(Position(i-80,0,j-20),67)
    
    for i in range(1,15):
        game.set_block(Position(-80,i,-20),19)
      

    
# This function builds the steps for the students to get back to the main level
def buildSteps():
    i = -11
    k = 8
    j = -20 
    
    for j in range(-20,80):
        game.set_block(Position(i+1, j, k),88)
        game.set_block(Position(i+2, j, k),88)
        k += 1

    
# This function creates a sphere of material(int val 1-88)    
def sphere(x,y,z,m):
    #print("sphere function called")
    for i in range(-30,31):
        for j in range(-30,31):
            for k in range(-30,31):
                if ((i*i)+(j*j)+(k*k) <= 900):
                    game.set_block(Position(i+x,j+y,k+z),m)
                                


# This function is used to teleport the player to a fixed position on the map
def teleportPlayer(p):
    game.set_player_position(Position(0,200,-20))
      

        
   
 







# The following function sets player position and clears the console.
def setPlayPosAndClearConsole():
    game.set_player_position(Position(0,10,-12))
    game.clear_console() 



setPlayPosAndClearConsole()
screenQuestion = "What would you like your world to display?"



































#-----------------Students Area-----------------#



























