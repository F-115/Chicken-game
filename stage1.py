import random
import time
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from modules.stage1animate import stage1animate
from modules.listeners import keyboardListener
from modules.listeners import mouseListener_stage1
from modules.listeners import specialKeyListener
import math
from modules.playPauseX import draw_pause, draw_play, draw_x
from modules.shapes import draw_boat, draw_bucket, draw_chicken2, draw_diamond,draw_basket
from modules.config import config
from modules.straightline import draw_any_line, draw_circle2, draw_points


# Creating a detailed basket image like the one you uploaded using OpenGL primitives is a complex task. Here's some simplified pseudocode for the outline and basic weave pattern. This pseudocode assumes the use of the draw_any_line, draw_circle2, and draw_points functions you provided earlier.

# Please note that this is a conceptual representation and would not result in a detailed basket as in the image. The actual implementation would require more complex logic to handle the curves and the weave pattern's intricacies.

# python
# Copy code
# def draw_basket_outline(base_x, base_y, width, height):
#     # Draw the top ellipse of the basket using partial circles
#     # This would require a modified version of draw_circle2 to draw ellipses or partial circles
#     # draw_circle2(base_x + width // 2, base_y + height, width // 2, height // 5)

#     # Draw the bottom base of the basket
#     draw_any_line(base_x, base_y, base_x + width, base_y)

#     # Draw the sides of the basket, assuming they curve inwards
#     draw_any_line(base_x, base_y, base_x + width // 4, base_y + height)
#     draw_any_line(base_x + width, base_y, base_x + 3 * width // 4, base_y + height)

# def draw_basket_weave(base_x, base_y, width, height):
#     # Weaving pattern, simplified as horizontal and vertical lines
#     vertical_spacing = 10
#     horizontal_spacing = 10
#     for i in range(base_x, base_x + width, vertical_spacing):
#         draw_any_line(i, base_y, i, base_y + height)  # vertical lines
#     for j in range(base_y, base_y + height, horizontal_spacing):
#         draw_any_line(base_x, j, base_x + width, j)  # horizontal lines

# def draw_basket():
#     base_x, base_y = 100, 100  # Starting point for the basket
#     width, height = 150, 100  # Width and height of the basket
#     draw_basket_outline(base_x, base_y, width, height)
#     draw_basket_weave(base_x, base_y, width, height)
def draw_half_circle(x_center, y_center, radius):
    x = radius
    y = 0
    d = 1 - radius  # Initial decision parameter

    # Create empty lists to store the coordinates of the half-circle
    x_coords = []
    y_coords = []

    # Plot the initial point on the circle, which will also be a point on the half-circle
    x_coords.append(x + x_center)
    y_coords.append(y + y_center)

    # Iterate while the x coordinate is greater than the y coordinate
    while x >= y:
        y += 1

        # Mid-point is inside or on the perimeter of the circle
        if d < 0:
            d += 2 * y + 1
        else:
            x -= 1
            d += 2 * (y - x) + 1

        # Only store the points that are on the upper half of the circle
        if y <= x:  # This ensures that we are only considering the upper semi-circle
            # Add points in the first and second quadrant
          x_coords.append(x + x_center)
          y_coords.append(y + y_center)
          x_coords.append(-x + x_center)#important
          y_coords.append(y + y_center)#important
         
          x_coords.append(y + x_center)
          y_coords.append(x + y_center) #important
          x_coords.append(-y + x_center) #important
          y_coords.append(x + y_center)
      
    # Draw the half-circle using the coordinates
    for i in range(len(x_coords)):
        draw_points(x_coords[i], y_coords[i], 1)  # Assuming a point size of 1 for simplicity


def draw_basket(base_x, base_y, width, height):
    # Define some parameters for the basket
    rim_height = height / 10
    body_height = height - 2 * rim_height

    basket_width = width  # Assume basket_width is defined as the width of the basket
    basket_height = height  # Assume basket_height is defined as the height of the basket
    handle_radius = basket_width // 2  # Set the radius of the handle

    # Coordinates for the center of the half-circle handle
    handle_center_x = basket_width // 2
    handle_center_y = basket_height + handle_radius

    draw_half_circle(handle_center_x+base_x, handle_center_y-2, handle_radius)
    draw_half_circle(handle_center_x+base_x, handle_center_y-2, handle_radius-10)

    # Draw the top rim
    top_rim_y = base_y + height - rim_height
    draw_any_line(base_x, top_rim_y, base_x + width, top_rim_y)

    # Draw the bottom rim
    bottom_rim_y = base_y + rim_height
    draw_any_line(base_x, bottom_rim_y, base_x + width, bottom_rim_y)

    # Draw the left side of the basket
    draw_any_line(base_x, bottom_rim_y, base_x, top_rim_y)

    # Draw the right side of the basket
    draw_any_line(base_x + width, bottom_rim_y, base_x + width, top_rim_y)

    # Draw horizontal weave lines across the body of the basket
    num_weave_lines = 5
    weave_spacing = body_height / num_weave_lines
    for i in range(num_weave_lines):
        y = bottom_rim_y + i * weave_spacing
        draw_any_line(base_x, y, base_x + width, y)

    # Draw vertical weave lines down the body of the basket
    # This is a simplification; actual vertical lines would be arcs
    num_vertical_weaves = 7
    vertical_weave_spacing = width / num_vertical_weaves
    for i in range(num_vertical_weaves):
        x = base_x + i * vertical_weave_spacing
        draw_any_line(x, bottom_rim_y, x, top_rim_y)


def display():
    # //clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 0);  # //color black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # //load the correct matrix -- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    # //initialize the matrix
    glLoadIdentity()
    # //now give three info
    # //1. where is the camera (viewer)?
    # //2. where is the camera looking?
    # //3. Which direction is the camera's UP direction?
    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
    glMatrixMode(GL_MODELVIEW)
    # Example call to the draw_basket function
    # draw_basket(50, 50, 100, 50)
    
    draw_x()
    draw_pause()
    draw_play()
    draw_diamond()
    draw_boat()
     
    draw_chicken2()

    if (config.create_new):
        m, n = config.create_new
        glBegin(GL_POINTS)
        glColor3f(0.7, 0.8, 0.6)
        glVertex2f(m, n)
        glEnd()
    if (config.end):
        config.speed = 1
       
        glutLeaveMainLoop()
    glutSwapBuffers()


def init():
    # //clear the screen
    glClearColor(0, 0, 0, 0)
    # //load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    # //initialize the matrix
    glLoadIdentity()
    # //give PERSPECTIVE parameters
    gluPerspective(104, 1, 1, 1000.0)
    # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
    # //near distance
    # //far distance

glutInit()
glutInitWindowSize(config.W_Width, config.W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)  # //Depth, Double buffer, RGB color

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"OpenGL Coding Practice")
init()

glutDisplayFunc(display) 


 # display callback function
glutIdleFunc(stage1animate)  # what you want to do in the idle time (when no drawing is occuring)

glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener_stage1)

glutMainLoop()
    # return something
    # The main loop of OpenGL


