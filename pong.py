from random import randint
from ursina import *
import pygame
app = Ursina()

#Variables
can_move = 0
cd = 0.15
pygame.mixer.init()
pygame.mixer.music.load('boing.mp3')

def update():
    global can_move
    #Left Paddle Movement
    if held_keys['w']:
        lpaddle.y += 3 * time.dt * can_move
    if held_keys['s']:
        lpaddle.y -= 3 * time.dt * can_move
    #Right Paddle Movement
    if held_keys['up arrow']:
        rpaddle.y += 3 * time.dt * can_move
    if held_keys['down arrow']:
        rpaddle.y -= 3 * time.dt * can_move
    #Left Paddle Boarder Stop
    if lpaddle.y <= -3.3:
        lpaddle.y += 3 * time.dt
    if lpaddle.y >= 3.3:
        lpaddle.y -= 3 * time.dt
    #Right Paddle Boarder Stop
    if rpaddle.y <= -3.3:
        rpaddle.y += 3 * time.dt
    if rpaddle.y >= 3.3:
        rpaddle.y -= 3 * time.dt
    #Ball Movement
    global dx, dy
    ball.x += ball.dx
    ball.y += ball.dy
    hit_info = ball.intersects()
    if hit_info.hit:
        if hit_info.entity == ceiling:
            pygame.mixer.music.play()
            ball.dx = +ball.dx
            ball.dy = -ball.dy
        if hit_info.entity == rpaddle:
            pygame.mixer.music.play()
            ball.dx = -ball.dx
            ball.dy = +ball.dy
        if hit_info.entity == floors:
            pygame.mixer.music.play()
            ball.dx = +ball.dx
            ball.dy = -ball.dy
        if hit_info.entity == lpaddle:
            pygame.mixer.music.play()
            ball.dx = -ball.dx
            ball.dy = ball.dy
        if hit_info.entity == lwall:
            pygame.mixer.music.load('gameover.mp3')
            red_win = Text(text='Green Wins!!!!', x=-0.15, y=0.05)
            close = Text(text='PRESS Q TO EXIT', x=-0.15 )
            ball.dx = 0
            ball.dy = 0
            can_move = 0
            pygame.mixer.music.play()
        if hit_info.entity == rwall:
            pygame.mixer.music.load('gameover.mp3')
            blue_win = Text(text='Blue Wins!!!!', x=-0.15, y=0.05)
            close = Text(text='PRESS Q TO EXIT', x=-0.15)
            ball.dx = 0
            ball.dy = 0
            can_move = 0
            pygame.mixer.music.play()


def input(key):
    if key == 'q':
        quit()
    if key == 'space':
        ball.dx = 0.05
        ball.dy = 0.05
        start_text.visible = False
        global can_move
        can_move = 1

#Left Paddle
lpaddle = Entity(model='quad', color=color.blue, scale=(0.38,1.5), position=(-7.2,0), collider='box')

#Right Paddle
rpaddle = Entity(model='quad', color=color.lime, scale=(0.38,1.5), position=(7.2,0), collider='box')

#Ball
ball = Entity(model='sphere', scale=.25, position=(0,0,0), collider='box', collision_cooldown=cd, dx=0, dy=0)

#Ceiling Wall
ceiling = Entity(model='quad', x=0, y=4, scale=(16,0.2), collider='box', color=color.orange, visible=False)

#Floor
floors = Entity(model='quad', x=0, y=-4, scale=(16,0.2), collider='box', color=color.orange, visible=False)

#Left Wall
lwall = Entity(model='quad', visible=False, collider='box', x=-7.9, scale_y=10)

#Right Wall
rwall = Entity(model='quad', visible=False, collider='box', x=7.9, scale_y=10)

#Start Text
start_text = Text(text='PRESS SPACE TO START!!!', x=-0.15, y=0.05)

app.run()