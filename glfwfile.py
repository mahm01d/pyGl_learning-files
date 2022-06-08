#!/usr/bin/env python
from lib2to3.pgen2.token import OP
from modulefinder import IMPORT_NAME
from sre_constants import SUCCESS
import OpenGL
import OpenGL.GL 
import OpenGL.GLUT
import OpenGL.GLU
print ("import SUCCESSful")

def showscreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition (0, 0)

wind = glutCreateWindow("Opengl coding practice")
            glutDisplayFunc (showscreen)
                glutIdleFunc (showscreen)
                      glutMaineLoop ()
