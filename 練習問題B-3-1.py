import pyxel

pyxel.init(200, 200)
pyxel.cls(7)
for a in range(0,11, 1):
    for b in range(0, 11, 1):
        pyxel.line(a*20, 0, b*20, 200, 0)

pyxel.show()
