# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

x = int(input('Enter Your ID: '))


def init():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    if x % 2 == 1:
        dda(130, 100, 130, 400)
        dda(370, 100, 370, 400)
        dda(130, (100 + 400) // 2, 370, (100 + 400) // 2)

    else:
        dda(130, 400, 370, 400)
        dda((130 + 370) // 2, 100, (130 + 370) // 2, 400)

    glutSwapBuffers()


def dda(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    steps = 0
    if dx > dy:
        steps = dx
    else:
        steps = dy

    (x_inc, y_inc) = (dx / steps, dy / steps)

    for i in range(0, steps):
        if i % 3 == 0:
            glPointSize(2)
            glColor3d(1, 0, 0)
            glBegin(GL_POINTS)
            glVertex2f(x0, y0)
            glEnd()
        x0 = x0 + x_inc
        y0 = y0 + y_inc


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow("OpenGL Template")
glutDisplayFunc(showScreen)

init()

glutMainLoop()
