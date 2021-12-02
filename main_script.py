# Drawing Sierpinski n-gons (polygons of n-sides with fractal composition)
import turtle
import numpy as np
from random import choice

def get_vertices(radius, n_vertices,offset=(0,0)):
    angle = 2*np.pi/n_vertices
    pos_ant = (0,radius)
    vertices_pos=[(pos_ant[0]-offset[0], pos_ant[1]-offset[1])]
    for nn in range(n_vertices-1):
        new_pos = (pos_ant[0]*np.cos(angle)-pos_ant[1]*np.sin(angle), 
                   pos_ant[0]*np.sin(angle)+pos_ant[1]*np.cos(angle))
        pos_ant = new_pos
        vertices_pos.append((new_pos[0]-offset[0], new_pos[1]-offset[1]))
    return(vertices_pos)
    
def draw_circle(turtle, size, x, y):
    turtle.goto(x,y)
    turtle.dot(size)

tommy = turtle.Turtle()
tommy.penup()
tommy.hideturtle()
tommy.speed(0)
turtle.tracer(30000,0)
size = 2

# Setting up the Figure (radius and number of vertices)
radius_size = 300
n = 8

# Drawing Vertices
vertices = get_vertices(radius=radius_size, n_vertices=n, offset=(0,0))
for position in vertices:
    draw_circle(tommy, size, position[0], position[1])
tommy.goto(choice(vertices))
i = 0

# Setting the Scale Factor and Proportion
# Source: http://larryriddle.agnesscott.org/ifs/pentagon/sierngon.htm
x = n//4
factor = 0
for k in range(x):
    k_angle = 2*np.pi*(k+1)/n
    factor = factor + np.cos(k_angle)
scale_factor = 1/(2*(1+factor))

prop = 1-scale_factor

# By hand use: 0.5 for 3 and 4 vertices, 0.62 for 5 vertices, 2/3 for 6 vertices
#prop = 1/2

# Drawing the fractal figure
while (i<50000):
    new_ref = choice(vertices)

    tommy.left(tommy.towards(new_ref))
    tommy.penup()
    tommy.forward(tommy.distance(new_ref)*prop)
    tommy.pendown()

    current_pos = tommy.pos()
    draw_circle(tommy, size, current_pos[0], current_pos[1])

    tommy.setheading(0)
    
    i = i+1

print("Done!")