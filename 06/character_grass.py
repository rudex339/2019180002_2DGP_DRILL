from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')
#fist start x = 400 y = 0


while(1):
    x=400
    y=0
    check = 1
    while(check):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y+90)
        if(x<800 and y==0):
            x=x+2
            if(x==400 and y==0):
                check = 0
        elif(y<510 and x==800):
            y=y+2
        elif(x>0 and y==510):
            x=x-2
        elif(x==0 and y > 0):
            y= y -2
        delay(0.01)

    check = 1
    y= 90
    count = -90
    while(check):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x =400+100*math.cos(math.pi*(count/180))
        y = 190+100*math.sin(math.pi*(count/180))
        count = count +2
        if(count==270):
            check = 0
        delay(0.01)
close_canvas()
