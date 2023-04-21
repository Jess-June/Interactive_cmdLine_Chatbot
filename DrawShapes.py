''' ChatBot for drawing shapes '''
import turtle
from os import system, name

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

clear()

recognized_words = ["square", "circle","rectangle", "triangle", "star", "spiral", "line", "left", "right", "forward", "backward", "up", "down", "turn", "penup", "pendown", "reset", "clear", "bye", "quit", "exit", "help"]
recognized_colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "black", "white", "brown", "gray", "grey"]
T = turtle.Turtle()
T.showturtle()

def parse(msg):
    msg = msg.lower()
    to_draw = []
    for word in msg.split():
        if word in recognized_words or word in recognized_colors:
            to_draw.append(word)
    return to_draw

def square(size):
    for i in range(4):
        T.forward(size)
        T.right(90)

def rectangle(l, b):
    for i in range(2):
        T.forward(l)
        T.right(90)
        T.forward(b)
        T.right(90)

def circle(r):
    T.circle(r)

def triangle(l):
    for i in range(3):
        T.forward(l)
        T.right(120)

def star(l):
    for i in range(5):
        T.forward(l)
        T.right(144)

def spiral(l):
    for i in range(100):
        T.forward(l)
        T.right(90)
        l += 1

def line(l):
    T.forward(l)

def left(angle):
    T.left(angle)

def right(angle):
    T.right(angle)

def backward(l):
    T.backward(l)

def up(l):
    T.up(l)
    
def down(l):
    T.down(l)

def turn(angle):
    T.right(angle)

def penup():
    T.penup()

def pendown():
    T.pendown()

def reset():
    T.reset()

def clear():
    T.clear()



def main():
    print("""Hi! My name's SKETCHBOT, and I can help you draw shapes!
You can tell me to draw basic shapes, like squares, circles, and triangles,
or you can tell me to draw more complex shapes, like stars and spirals.
Or we can go simpler and draw lines as well!
          
""")
    while True:
        to_fill = False
        try:
            msg = input(">>> ")
            to_draw = parse(msg)
            if to_draw == []:
                print("I don't understand what you want me to draw. Try again.")
                continue
            for word in to_draw:
                if word in recognized_colors:
                    to_fill = True
                    T.fillcolor(word)
                    T.begin_fill()
                    continue
                if word == "square":
                    square(int(input("Enter the size of the square: ")))
                elif word == "rectangle":
                    rectangle(int(input("Enter the length of the rectangle: ")), int(input("Enter the breadth of the rectangle: ")))
                elif word == "circle":
                    circle(int(input("Enter the radius of the circle: ")))
                elif word == "triangle":
                    triangle(int(input("Enter the length of the triangle: ")))
                elif word == "star":
                    star(int(input("Enter the length of the star: ")))
                elif word == "spiral":
                    spiral(int(input("Enter the length of the spiral: ")))
                elif word == "line" or word=="forward":
                    line(int(input("Enter the length of the line: ")))
                elif word == "left":
                    left(int(input("Enter the angle to turn left: ")))
                elif word == "right":
                    right(int(input("Enter the angle to turn right: ")))
                elif word == "backward":
                    backward(int(input("Enter the length to move backward: ")))
                elif word == "up":
                    up(int(input("Enter the length to move up: ")))
                elif word == "down":
                    down(int(input("Enter the length to move down: ")))
                elif word == "turn":
                    turn(int(input("Enter the angle to turn: ")))
                elif word == "penup":
                    penup()
                elif word == "pendown":
                    pendown()
                elif word == "reset":
                    reset()
                elif word == "clear":
                    clear()
                elif word == "bye" or word == "quit" or word == "exit":
                    print("Bye!")
                    return
                elif word == "help":
                    print("Just tell me what you want me to draw!")
                else:
                    print("I don't understand what you want me to draw. Try again.")
                if to_fill:
                    T.end_fill()
                    to_fill = False
        except KeyboardInterrupt:
            print("Bye!")
        except:
            print("Oops! Something went wrong. Try again.")
                
            

main()
