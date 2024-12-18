import turtle

def tree(branch_len, t):
    if branch_len > 5: 
        t.forward(branch_len)
        t.right(30) # going right 20deg
        tree(branch_len-10, t)
        t.left(60) # going back to center 20deg + goign left 20deg = 40deg
        tree(branch_len-10, t)
        t.right(30) # comming back
        t.backward(branch_len)    
        
def main(): 
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90) # initially turtle points right
    t.up() # lift pen upward
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t)
    my_win.exitonclick()
    
main()