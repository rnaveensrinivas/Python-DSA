import turtle

def draw_triangle(points, color, t):
    # initialize the fill color
    t.fillcolor(color)
    
    # move to the current point
    t.up()
    t.goto(points[0][0], points[0][1])
    t.down()
    
    # draw the triangle
    t.begin_fill()
    t.goto(points[1][0], points[1][1]) # move to second point
    t.goto(points[2][0], points[2][1]) # move to thrid point
    t.goto(points[0][0], points[0][1]) # come back to first point
    t.end_fill()

def get_mid(p1, p2) -> tuple: 
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points: list[tuple[int]], degree: int, t: turtle.Turtle):
    color_map = ['blue', 'red', 'green', 'white', 
                 'yellow', 'violet', 'orange']
    
    draw_triangle(points, color_map[degree], t)
    if degree > 0:
        sierpinski([points[0],
                    get_mid(points[0], points[1]),
                    get_mid(points[0], points[2])], 
                   degree-1, t)
        sierpinski([points[1],
                    get_mid(points[1], points[0]),
                    get_mid(points[1], points[2])], 
                   degree-1, t)
        sierpinski([points[2],
                    get_mid(points[2], points[1]),
                    get_mid(points[2], points[0])], 
                   degree-1, t)

def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    my_points = [[-200, -100], [0, 200], [200, -100]]
    sierpinski(points=my_points, degree=5, t=t)
    my_win.exitonclick()
    
main()