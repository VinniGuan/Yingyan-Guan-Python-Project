# CS 177 – lab09.py

# {Yingyan Guan}

# you will use the graphics library to create a bouncing ball animation.
# The animation will stop when clicking on the circle.

from graphics import *
import time
from random import randint, choice

# implement the createGameCanvas function
def createGameCanvas():
    # draw a 500 by 500 window
    window = GraphWin("Game Canvas", 500, 500)
    # set the background to Brown
    window.setBackground("Brown")
    return window

# implemet the drawCircle function to draw the circle 
def drawCircle(window):
    # draw the circle with center(250,470) and 30 radius
    circle = Circle(Point(250,470), 30)
    # fill the ball with color blue 
    circle.setFill("blue")
    # draw the circle in the window 
    circle.draw(window)
    return circle

# The checkForClickInsideCircle checks for a mouse click inside the circle.
# First, you’ll need to call win.checkMouse method to get the click point in the window.
# After that, you may use the following formula to check whether the click is inside the circle:
def checkForClickInsideCircle(window, circle):
    pt = window.checkMouse() # get the click point in the window

    # check if there is click, if there is no click, return False
    if pt is None:
        return False
    x = pt.getX()  # the x coordinate of the check mouse 
    y = pt.getY()  # the y coordinate of the check mouse 
    centerx = circle.getCenter().getX() # x coordinate of the center of the circle 
    centery = circle.getCenter().getY() # y coordinate of the center of the circle

    # if the cick is within the cirlce, return True, otherwise, return False 
    if (centerx-x)**2 + (centery-y)**2 <= circle.getRadius()**2:
        return True
    else:
        return False

# The checkBoundary function checks whether the moving circle is within the window boundary.
def checkBoundary(circle, direction):
    # if the circle touch to the top we will change the direction, direction equal to 1 because it is from the top to bottom
    # as the number decrease the height of the ball will increase, so we use minus here
    y1 = circle.getCenter().getY() - circle.getRadius()
    if y1 <= 0 and direction == -1:
        direction = 1
    # if the circle touch to the bottom, we will change the direction, direction equal to -1 because it is it is from bottom to top
    y2 = circle.getCenter().getY() + circle.getRadius()
    if y2 >= 500 and direction == 1:
        direction = -1
    return direction


def play(window, circle, speed):
        
        # The while loop keeps the ball moving up and down
        while True:
        # until a click is detected inside the circle

            # move the circle
            circle.move(0,speed)

            # pause the execution to observe the movement
            time.sleep(0.01)

             # determine the direction of the movement based
            # on the speed
            if speed < 0:
                direction = -1
            else:
                direction = 1

            # we want the ball continue go up, if the direciton is not equal to its direction, it should bounce back
            # it should continue go up which is from the bottom to the top 
            if checkBoundary(circle, direction) != direction:
                direction = -1*direction
                speed = -1*speed

            # if there is click within the circle just break the funciton and stop
            if(checkForClickInsideCircle(window, circle)):
                break
        

def main():
        # create a window
        window = createGameCanvas()
        circle = drawCircle(window)
        
        #intial speed is negative (bottom to top)        
        speed = -2

       
        # call play to start the animation
        play(window, circle, speed)
        window.getMouse()
        window.close()
        
main()
