# This program sets up one programmer to change the image being drawn (the unit)
# while a 2nd programmer changes the number of times the shape is displayed
# and other aspects of the final display.

# This version contains only the function to draw the unit & related variables.

from graphics import *

def draw_unit(unitWin, unitX, unitY, unitRad):
    """So far, this function only requires a window,
       2D coords and a size in pixels. Colors are locked."""
    
    unitA = Circle(Point(unitX, unitY), unitRad)
    unitA.setFill("black")
    unitA.draw(unitWin)
    
    unitB = Circle(Point(unitX, unitY), unitRad - 10)
    unitB.setFill("red")
    unitB.draw(unitWin)

    unitC = Circle(Point(unitX, unitY), unitRad - 20)
    unitC.setFill("yellow")
    unitC.draw(unitWin)

uRad = 25
uTotX = 10
uTotY = 10
spaceX = 1.2
spaceY = 1.2
winX = (uRad * 2) * uTotX * spaceX
winY = (uRad * 2) * uTotY * spaceY

