"""
File: breakout.py
Name: Lydia
---------------------------------
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 50         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    count = NUM_LIVES
    # Add the animation loop here!
    while True:
        """
        1. Click it will start the game
        2. The game miss out of lives time or no more bricks will break the loop 
        """
        graphics.ball_bouncing()
        ball_vx = graphics.get_dx()
        ball_vy = graphics.get_dy()
        graphics.ball.move(ball_vx, ball_vy)
        count = graphics.restart(count)
        brick_count = graphics.get_bricks_count()
        if count == 0:
            break
        elif brick_count == 0:
            break
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
