HEIGHT = 500
WIDTH = 500

robot_obj = Actor('robot_win',(250,250))
cherry_obj = Actor('cherry',(100,100))

robot_obj.moving_switch = 'key'

bg = 'bg'

active = 'robot'

score_count = 0

def draw():
    global score_count
    screen.blit(bg,(0,0))
    robot_obj.draw()
    cherry_obj.draw()
    screen.draw.text(f'score: {score_count}',(125,200),color = (71,255,14),fontsize = 100)

    if robot_obj.colliderect(cherry_obj):
        score_count = score_count + 1
def update():
    robot_keyboard_mov()

def robot_keyboard_mov():
    if keyboard.up:
        robot_obj.top -= 4
    if keyboard.down:
        robot_obj.bottom += 4
    if keyboard.left:
        robot_obj.left -= 4
    if keyboard.right:
        robot_obj.right += 4

def on_key_down(key):

    if key == key.R and robot_obj.moving_switch == 'key':
        robot_obj.moving_switch = 'mouse'

    elif key == key.R and robot_obj.moving_switch == 'mouse':
        robot_obj.moving_switch = 'key'

def on_mouse_move(pos,buttons):
    if robot_obj.moving_switch == 'mouse' and active == 'robot':
        robot_obj.pos = pos
