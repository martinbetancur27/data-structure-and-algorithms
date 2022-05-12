import turtle
import random

#El de la clase
'''myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def draw(myTurtle, length):
  if length > 0:
    myTurtle.forward(length)
    myTurtle.left(90)
    draw(myTurtle, length-10)

draw(myTurtle, 100)
myWin.exitonclick()'''



#Dibujar un cuadrado
'''myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def draw(myTurtle, length):
  if length > 0:
    myTurtle.forward(length)
    myTurtle.left(90)
    draw(myTurtle, length)

draw(myTurtle, 100)
myWin.exitonclick()'''

#El de un comentario
#Les comparto un proyecto parecido que hice mientras estaba de intercambio
#Era sobre usando turtle, crear de forma recursiva los troncos de un árbol ( de forma aleatoria )
#Creates a branch of a tree

def tree(branchLen,t):
    LIMIT = 5 #Limit for minimum length of the tree

    #Check if the length is grather than the limit
    if branchLen > LIMIT:

        #Get the lengths of the next two branches
        left = branchLen - getLen()
        right = branchLen - getLen()

        #Acorrding to those lengths, check to see if this one is the last one
        #If it is, then this one is sa leaf. So use color green
        #Else, use color brown
        if amItheLast(left, right, LIMIT):
            t.color("green")
        else:
            t.color("brown")

        #The size of the pen is proporcional of the length
        t.pensize(branchLen * .12)
        #Print forward
        t.forward(branchLen)

        #Get angles of next two branches
        rig = getAngle()
        lef = getAngle() + rig
        ret = t.heading() #Store for return later

        #Go to the right
        t.right(rig)
        tree(left, t)

        #Go to the left
        t.left(lef)
        tree(right, t)

        #Return to original angle, stop drowing with the pen and go back
        t.setheading(ret)
        t.up()
        t.backward(branchLen)
        t.down() #Continue drowing

#Returns if the actual branch is the last one (leaf?)
#@Lef: Length of left branch - INT
#@Rig: Length of right branch - INT
#@Limit: The limit of the lenght in order to be draw - INT
def amItheLast(lef, rig, limit):
    if lef > limit or rig > limit:
        return False
    else:
        return True

#Get a random angle, between 15 and 45
def getAngle():
    return random.randint(15,45)

#Get a random length, between 5 and 20
def getLen():
    return random.randint(5,20)
    
#Creates and prints a tree
def main():
    #Pencile and canvas
    t = turtle.Turtle()
    myWin = turtle.Screen()

    #Set start position
    t.shape("turtle")
    t.left(90)
    t.up()
    t.backward(100)
    t.down()

    #Start drawing
    tree(75,t)
    myWin.exitonclick()

main()

