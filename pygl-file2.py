
from logging import raiseExceptions
import glfw

if not glfw.init():
    raise Exception('glfw is not intialized')

window = glfw.create_window(600, 400, 'my first program', None, None)
if not window:
    glfw.terminate()
    raise Exception("cant create window")

glfw.set_window_pos(window, 300, 100)

while not glfw.window_should_close(window) :
    glfw.poll_events()
    glfw.swap_buffers(window)

glfw.terminate()

