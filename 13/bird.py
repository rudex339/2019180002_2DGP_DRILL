from pico2d import *
import game_framework
import random
animation = [[34,1,146,143],
             [216,2,146,141],
             [398,12,146,130],
             [555,17,171,122],
             [728,48,182,88],
             [34,217,146,118],
             [216,216,146,124],
             [398,216,146,120],
             [580,217,146,109],
             [762,219,146,110],
             [34,392,146,108],
             [216,394,146,106],
             [376,395,168,88],
             [546,370,180,114]]
PIXEL_PER_METER = (10.0/0.3)
RUN_SPEED_KMPH = 50.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14
class Bird:
    image = None
    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.dir = random.randint(0,1)
        if self.dir == 0:
            self.dir = -1
        self.x = random.randint(25,1600-25)
        self.y = random.randint(300,350)
        self.frame = 0
    def update(self):
        self.x+= self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        if self.x > 1600 or self.x<25:
            self.dir *=-1
        pass

    def draw(self):
        x, y, wid, hei = animation[int(self.frame)]
        if self.dir == -1:
            self.image.clip_composite_draw(x, 506-y-hei, wid, hei,
                                          3.141592, 'v', self.x + 25, self.y - 25, wid, hei)
        else:
            self.image.clip_composite_draw(x, 506-y-hei, wid, hei,
                                          0, '', self.x - 25, self.y - 25, wid, hei)