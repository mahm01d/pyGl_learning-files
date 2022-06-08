from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from svg.path import *
print("Imports successful!")

#not_working for showing point:
    #from OpenGL.GL import glEnable, GL_PROGRAM_POINT_SIZE 


def myInit():
    glClearColor(1.0, 1.0, 0.0, 1.0) 
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(10.0)
    gluOrtho2D(0, 500, 0, 500)




#do not use glBegin() / glEnd or glVertexAttribPointer()
    ##because its removed in the last version
    

def display() :
    glClear(GL_COLOR_BUFFER_BIT)
    
    #FUNC NAME MUST BE IN CAPITAL LETTERS
    glBegin(GL_POINTS)
    glVertex2f(100, 100)
    glVertex2f(200, 200)
    glVertex2f(400, 400)
    glEnd()

    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
#CREATE WINDOW + SETTING THE NAME
glutCreateWindow("sfsf")
myInit()
glutDisplayFunc(display)
glutMainLoop ()



