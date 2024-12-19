import pyxel
import math
pyxel.init(200,200)
ballx = 100
bally = 0
padx = 0
sc=0

angle = math.radians(30)
vx = math.cos(angle)
vy = math.sin(angle)
a = 0
speed = 1
def update():
    global ballx, bally, angle, vx, vy, a, speed, sc
    padx = pyxel.mouse_x
    if ballx <= 0:
        a = 0
    elif ballx >= 200:
        a = 1
    if a == 1:
        ballx -= vx*speed
        bally += vy*speed
    elif a == 0:
        ballx += vx*speed
        bally += vy*speed
    if bally >= 200:
        ballx = 100
        bally = 0
        speed += 1

    if bally >= 195:
        if padx -20<= ballx <=padx + 20:
            sc += 1
            bally = 0

def draw():
    global ballx, bally, angle, vx, vy
    pyxel.cls(7)
    pyxel.circ(ballx, bally, 10, 6)
    pyxel.rect(padx-20,195,40,5,14)
    pyxel.text(10,0,f"Score:{sc}",0)
pyxel.run(update, draw)