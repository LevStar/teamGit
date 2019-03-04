# This program sets up one programmer to change the image being drawn (the unit)
# while a 2nd programmer changes the number of times the shape is displayed
# and other aspects of the final display.

from graphics import *

def draw_unit(unitWin, unitX, unitY, unitRad):
    unit = Circle(unitX, unitY, unitRad)
    unit.draw(unitWin)

uRad = 25
uTotX = 20
uTotY = 20
spaceX = 1.2
spaceY = 1.2
winX = uRad * uTotX * spaceX
winY = uRad * uTotY * spaceY

tgWin = GraphWin("Teamwork Makes the Dream Work!", winX, winY)


tgWin.getMouse()
tgWin.close()
