"""
File: bouncing_ball.py
Name: Lydia
-------------------------
This program simulates a bouncing ball by campy library
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked


VX = 3
# This controls the pause time (in millisecond) for the animation
DELAY = 50
GRAVITY = 1
# This controls the width and height of the circle
SIZE = 20
REDUCE = 0.9
# This controls the start of position of the circle
START_X = 30
START_Y = 40

ball = GOval(SIZE, SIZE)
# This controls how many times does ball bounce
count = 0
switch = False

window = GWindow(800, 500, title='bouncing_ball.py')


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global switch, count
    ball.filled = True
    onmouseclicked(bounced)
    window.add(ball, x=START_X, y=START_Y)
    while True:
        pause(DELAY)
        if switch:
            if count < 3:
                vy = 0
                while True:
                    ball.move(VX, vy)
                    vy += GRAVITY
                    if ball.y + ball.height >= window.height:
                        # Each bounce reduces y velocity
                        vy = -vy * REDUCE
                    if ball.x >= window.width:
                        count += 1
                        switch = False
                        break
                    pause(DELAY)
                window.add(ball, x=START_X, y=START_Y)
            else:
                break


def bounced(event):
    global switch
    if not switch:
        switch = True



if __name__ == "__main__":
    main()
