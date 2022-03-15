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

    # call the draw methods here
    draw_house()
    draw_roof()
    draw_door()
    draw_window()
    glutSwapBuffers()


# put your drawing codes inside this 'draw' function
def draw_house():
    glPointSize(5)
    glColor3d(1, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(110, 80)
    glVertex2f(390, 80)
    glVertex2f(110, 80)
    glVertex2f(110, 330)
    glVertex2f(390, 80)
    glVertex2f(390, 330)
    glVertex2f(110, 330)
    glVertex2f(390, 330)
    glEnd()


def draw_roof():
    glPointSize(5)
    glColor3d(1, 0, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(110, 330)
    glVertex2f(250, 480)
    glVertex2f(390, 330)
    glVertex2f(250, 480)
    glEnd()


def draw_door():
    glPointSize(5)
    glColor3d(1, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(210, 80)
    glVertex2f(210, 200)
    glVertex2f(290, 80)
    glVertex2f(290, 200)
    glVertex2f(210, 200)
    glVertex2f(290, 200)
    glEnd()
    glBegin(GL_POINTS)
    glVertex2f(220, 140)
    glEnd()


def draw_window():
    glPointSize(5)
    glColor3d(1, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(190, 230)
    glVertex2f(130, 230)
    glVertex2f(130, 230)
    glVertex2f(130, 290)
    glVertex2f(190, 230)
    glVertex2f(190, 290)
    glVertex2f(130, 290)
    glVertex2f(190, 290)

    glVertex2f(310, 230)
    glVertex2f(370, 230)
    glVertex2f(310, 230)
    glVertex2f(310, 290)
    glVertex2f(370, 230)
    glVertex2f(370, 290)
    glVertex2f(310, 290)
    glVertex2f(370, 290)
    glEnd()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow("OpenGL Template")
glutDisplayFunc(showScreen)

init()

glutMainLoop()
