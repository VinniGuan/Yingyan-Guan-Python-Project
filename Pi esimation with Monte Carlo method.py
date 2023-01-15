# CS 177 – project4.py
# {Yingyan Guan}
# apply the Monte Carlo methods to approximate the value of
# You will draw a square using the graphics library. Inside the square, you will draw a circle with
# radius =  0.5 * square side. After that, you will start drawing random points in the square.
# The value of mcan be estimated using the number of points inside the circle and outside of circle.


from graphics import *
import random
import math


# Task1: implement the createWindow function
def createWindow(length, width, color):
    # create a window call project 4
    window = GraphWin("Project4", length, width)
    #set the background to Green
    window.setBackground(color)
    return window

# Task 2: implement the drawSquare function that
# draws a square on the window using the given length
def drawSquare(window, squareLength):
    margin = (window.width - squareLength)/2
    # we will use rectangle function here,We will use two points on the diagonal
    # Since we know the margin, the first point is (margin, margin) and
    # we will add the squareLength to both x and y coordinate to the margin to its diagonal point
    square = Rectangle(Point(margin,margin), Point(margin+squareLength,margin+squareLength))
    # we want the side of the Rectangle be thicker
    square.setWidth(5)
    square.draw(window)

# Task 3: implement the drawCircle function
def drawCircle(window, circleRadius, color):
    margin = (window.width - circleRadius)/2
    # since the circleRadius is squarelength when we call the function below,
    # Point(margin,margin) is one of the point of the rectangle
    # it is a square in this case, so the center coordinate of this circle should be margin plus the radius
    # in both x-axis and y-axis
    c = Circle(Point(margin+0.5*circleRadius,margin+0.5*circleRadius), circleRadius)
    # set circle color
    c.setFill(color)
    c.draw(window)

# Task 4: implement the addPoints function
def addPoints(window, squareLength, numberOfPoints):
    # initialize the number of yellow points and black points
    ypoint = 0
    bpoint = 0
    # use a for loop to specify the points 
    for i in range(numberOfPoints):
        # we will get the random point within the rectangle( including the circle)
        randompoint = Point(random.randint(250-0.5*squareLength,250+0.5*squareLength),random.randint(250-0.5*squareLength,250+0.5*squareLength))
        # we want to get the x and y coordinate of those random point
        px = randompoint.getX()
        py = randompoint.getY()
        # we want to calculate the distance between random point and the circle center 
        dist = ((px - 250)**2 + (py - 250)**2)**0.5
        # if the distance between random points and circle center is less than the radius, which means that those points
        # are within the circle, and we want those be the yellow points 
        if dist <= 0.5*squareLength:
            randompoint.setFill("yellow")
            ypoint += 1
        # if the distance between random points and circle center is greater than the radius, which means that those points
        # are outside the circle, and we want those be the black points 
        else:
            randompoint.setFill("black")
            bpoint +=1
        randompoint.draw(window)
    # return number of yellow points and black points
    return ypoint, bpoint


# Task 5: implement the estimatePi function
def estimatePi(yellowCount, blackCount):
    # use the formula to calcaulate the pi, and we will return the number as float
    piofc = (4*yellowCount)/(blackCount+yellowCount)
    return float(piofc)
    
def main():
    winLength = 500
    winWidth = 500
    squareLength = 400
    windowColor = 'green'
    circleColor = 'blue'

    window = createWindow(winLength, winWidth, windowColor)
    drawSquare(window, squareLength)
    drawCircle(window, squareLength/2, circleColor)
    
    numberOfPoints = eval(input("How many random points? "))
    yellow, black = addPoints(window, squareLength, numberOfPoints)

    estimatedPi = estimatePi(yellow, black)
    print('Estimated pi: ',estimatedPi)

    window.getMouse()
    window.close()



main()
