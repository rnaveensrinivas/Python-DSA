from turtle import Turtle, Screen
from random import randint

# https://cs111.wellesley.edu/labs/lab02/colors
COLORS = {
    1: "DarkOliveGreen3",
    2: "DarkOliveGreen4",
    3: "coral2", 
    4: "coral3",
    5: "coral4",
}
def tree(branch_len: int, t: Turtle, pen_size: int, color: int) -> None:
    if branch_len > 5: 
        
        if pen_size < 2: 
            pen_size=1
        t.pensize(pen_size)
        
        if color < 1: 
            color = 1
        if color > 5: 
            color = 5
        t.color(COLORS[color])
        
        t.forward(branch_len)
        
        angle = randint(15,45)
        t.right(angle)
        
        decrement_branch = randint(15,20)
        tree(branch_len-decrement_branch, t, pen_size-1, color-1)
        t.left(angle*2)
        tree(branch_len-decrement_branch, t, pen_size-1, color-1)
        t.right(angle)
        t.backward(branch_len)
        
t = Turtle()
t.left(90)
t.pensize(4)
t.up()
t.backward(200)
t.down()

tree(branch_len=120, t=t, pen_size=5, color=5)
my_win = Screen()
my_win.exitonclick()
        