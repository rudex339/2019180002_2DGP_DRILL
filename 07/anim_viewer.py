from pico2d import *
open_canvas()
img = load_image('player.png')#2379
waiting_up = [[84, 4,29,26,5,12],#4
         [116, 4, 29, 26,5,12],
         [149, 4, 29, 26,5,12],
         [181, 4, 29, 26,5,12]
         ]
waiting_down = [150,1601,21,25,0,0]
walking_up =[[215,4,28,26,5,12],#18
         [245,4,28,26,5,12],
         [276,4,28,26,5,12],
         [310,4,28,26,5,12],
         [341,4,28,26,5,12],
         [372,4,29,26,5,12],
         [404,4,29,26,5,12],
         [436,4,29,26,5,12],
         [468,4,30,26,5,12],
         [501,4,29,26,5,12],
         [533,4,27,27,5,12],
         [563,4,28,27,5,12],
         [595,4,29,26,5,12],
         [628,4,29,26,5,12],
         [661,4,29,26,5,12],
         [693,4,29,26,5,12],
         [726,4,29,26,5,12],
         [758,4,28,27,5,12]]
walking_down=[[176,1599,23,27,0,0],
              [204,1602,28,24,0,0],
              [236,1599,18,27,0,0],
              [259,1600,22,26,0,0],
              [285,1600,31,26,0,0],
              [320,1599,19,27,0,0]
              ]
walking_stop=[[343,1601,23,25,0,0],
              [369,1601,26,25,0,0],
              [398,1601,26,25,0,0],
              [427,1601,24,25,0,0]]
shot_up =[[422,184,49,20,15,15],
          [474,184,52,20,15,15],
          [530,183,52,21,15,15],
          [586,182,30,22,5,15],
          [619,181,30,23,5,15],
          [652,184,34,20,5,15],#
          [689,184,34,20,5,15],
          [726,184,34,21,5,12],
          [763,184,33,24,5,12],
          [800,183,31,26,5,12]]
def draw_img_up(List):
    x, y, wid, hei,px,py = List
    img.clip_draw(x, 2379 - y - hei, wid, hei, 400+px, 50+py)
    pass
def draw_img_down(List):
    x, y, wid, hei,px,py = List
    img.clip_draw(x, 2379 - y - hei, wid, hei, 400, 50)
    pass

def standing():
    count = 0
    U_num = 0;
    while(count<50):
        clear_canvas()
        draw_img_down(waiting_down)
        draw_img_up(waiting_up[U_num])
        U_num +=1
        if(U_num==4):
            U_num=0

        update_canvas()
        delay(0.1)
        count +=1
    pass
def standing_shot():
    count = 0
    U_num = 0;
    while (count < 50):
        clear_canvas()
        draw_img_down(waiting_down)
        draw_img_up(shot_up[U_num])
        U_num += 1
        if (U_num == 6):
            U_num = 0

        update_canvas()
        delay(0.1)
        count += 1
    for i in range(U_num,10):
        clear_canvas()
        draw_img_down(waiting_down)
        draw_img_up(shot_up[i])
        update_canvas()
        delay(0.1)
    pass
def runing():
    count = 0
    D_num = 0;
    U_num = 0;
    while (count < 50):
        clear_canvas()
        draw_img_down(walking_down[D_num])
        D_num += 1
        if (D_num == 6):
            D_num = 0

        draw_img_up(walking_up[U_num])
        U_num += 1
        if (U_num == 18):
            U_num = 0

        update_canvas()
        delay(0.1)
        count += 1
    pass
def run_shot():
    count = 0
    D_num = 0;
    U_num = 0;
    while (count < 50):
        clear_canvas()
        draw_img_down(walking_down[D_num])
        D_num += 1
        if (D_num == 6):
            D_num = 0

        draw_img_up(shot_up[U_num])
        U_num += 1
        if (U_num == 6):
            U_num = 0

        update_canvas()
        delay(0.1)
        count += 1
    for i in range(U_num, 10):
        clear_canvas()
        if i-U_num > 3 :
            draw_img_down(waiting_down)
        else : draw_img_down(walking_stop[i-U_num])
        draw_img_up(shot_up[i])
        update_canvas()
        delay(0.1)
    pass


count = 0
a=0
while (True):
    standing()

    standing_shot()

    runing()

    run_shot()



close_canvas()