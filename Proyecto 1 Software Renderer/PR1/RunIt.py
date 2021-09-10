#Universidad del Valle de Guatemala
#Graficas por Computadora
#Laboratorio SR5
#Diego Crespo 19541
from Engine import Renderer, V3, _color
from shaders import *
from obj import Texture

import random

width = 960
height = 540

rend = Renderer(width, height)

rend.directional_light = V3(0,0,-1)

rend.normal_map = Texture('Metal.bmp')


rend.active_shader = RedBlue
rend.glLoadModel("mesa.obj",
               translate = V3(0.5, -1.5, -10),
               rotate=V3(25,0,0),
               scale = V3(2,2,2)) 

rend.active_texture = Texture('Metal.bmp')              
rend.active_shader = normalMap
rend.glLoadModel("Gun.obj",
               translate = V3(-2, 1.75, -7),
               rotate=V3(0,180,0),
               scale = V3(3,3,3)) 

rend.active_texture = Texture('cafe.bmp')          
rend.active_shader = textureBlend
rend.glLoadModel("cafe.obj",
               translate = V3(5, -1, -10),
               rotate=V3(50,150,0),
               scale = V3(2,2,2)) 

#rend.active_shader = toon
#rend.glLoadModel("model.obj",
              #   translate = V3(-2, 0, -10),
             #    rotate=V3(55,-55,55),
               #  scale = V3(2,2,2))

#rend.active_shader = unlit
#rend.glLoadModel("model.obj",
             #  translate = V3(2.5, -3, -10),
             #  rotate=V3(55,-55,55),
             #  scale = V3(2,2,2)) 


rend.glFinish("salida.bmp")



