from Engine import Renderer, V3, _color
from shaders import *
from obj import Texture

import random

width = 960
height = 540

rend = Renderer(width, height)

rend.directional_light = V3(0,0,-1)

rend.normal_map = Texture('models/Metal.bmp')

rend.background = Texture('models/rendering.bmp')
rend.glClearBackground()


rend.active_shader = RedBlue
rend.glLoadModel("models/mesa.obj",
               translate = V3(0.5, -2, -10),
               rotate=V3(25,0,0),
               scale = V3(2,2,2)) 

rend.active_texture = Texture('models/Metal.bmp')              
rend.active_shader = normalMap
rend.glLoadModel("models/Gun.obj",
               translate = V3(-2, 1.75, -7),
               rotate=V3(0,180,0),
               scale = V3(3,3,3)) 

rend.active_texture = Texture('models/cafe.bmp')          
rend.active_shader = textureBlend
rend.glLoadModel("models/cafe.obj",
               translate = V3(5, -1, -10),
               rotate=V3(50,150,0),
               scale = V3(2,2,2)) 

rend.active_texture = Texture('models/lobo.bmp')          
rend.active_shader = textureBlend
rend.glLoadModel("models/wolf.obj",
               translate = V3(-2, -5, -10),
               rotate=V3(0,55,0),
               scale = V3(5,5,5)) 

rend.active_shader = GreenBlue
rend.glLoadModel("models/conejo.obj",
               translate = V3(3, -4, -10),
               rotate=V3(0,-55,0),
               scale = V3(1,1,1)) 





rend.glFinish("salida.bmp")



