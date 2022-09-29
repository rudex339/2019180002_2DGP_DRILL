from pico2d import *


TUK_WIDTH, TUK_HEIGHT = 1280, 1024

def handle_events():
    global running
    global dir_x
    global dir_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1


open_canvas(TUK_WIDTH, TUK_HEIGHT)
TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
y= 90
frame = 0
dir_x = 0
dir_y = 0
point_frame = 1
point_direct = 1
while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if dir_x == 0 and dir_y == 0:
        point_frame = 2
    else: point_frame = 0
    if dir_x < 0:
        point_frame=0
        point_direct = 0
    elif dir_x > 0:
        point_frame = 0
        point_direct = 1
    character.clip_draw(frame * 100, 100 * (point_frame+point_direct), 100, 100, x, y)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    if x+dir_x*5>0 and x+dir_x*5 < TUK_WIDTH:
        x += dir_x*5
    if y+dir_y*5 > 0 and y+dir_y*5 < TUK_HEIGHT:
        y += dir_y*5
    delay(0.01)

close_canvas()

