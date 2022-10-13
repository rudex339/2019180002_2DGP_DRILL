from pico2d import *
import game_framework
import logo_state
import item_state
import add_state

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.num = 1
        self.x, self.y = [0], [90]
        self.frame = 0
        self.dir = [1] # 오른쪽
        self.image = load_image('animation_sheet.png')
        self.item = None
        self.ball_img = load_image('ball21x21.png')
        self.big_ball_img = load_image('ball41x41.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        for n in range(0, self.num):
            self.x[n] += self.dir[n] * 2
            if self.x[n] > 800:
                self.x[n] = 800
                self.dir[n] = -1 #왼쪽
            elif self.x[n] < 0:
                self.x[n] = 0
                self.dir[n] = 1

    def draw(self):
        if self.item == 'ball':
            for n in range(0, self.num):
                self.ball_img.draw(self.x[n]+10,self.y[n]+50)
        elif self.item == 'bigball':
            for n in range(0, self.num):
                self.big_ball_img.draw(self.x[n] + 10, self.y[n] + 50)
        for n in range(0, self.num):
            if self.dir[n] == 1:
                self.image.clip_draw(self.frame*100, 100, 100, 100, self.x[n], self.y[n])
            else:
                self.image.clip_draw(self.frame*100, 0, 100, 100, self.x[n], self.y[n])
    def add_boy(self):
        self.num +=1
        self.x += [0]
        self.y += [90]
        self.dir += [1]
    def del_boy(self):
        if self.num > 1:
            del self.x[0]
            del self.y[0]
            del self.dir[0]
            self.num -= 1




def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_i:
                game_framework.push_state(item_state)
            elif event.key == SDLK_b:
                game_framework.push_state(add_state)

boy = None # c로 따지믄 NULL
grass = None
running = True

# 초기화
def enter():
    global boy, grass, running
    boy = Boy()
    grass = Grass()
    running = True

# finalization code
def exit():
    global boy, grass
    del boy
    del grass

def update():
    boy.update()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    grass.draw()
    boy.draw()


def pause():
    pass
def resume():
    pass



