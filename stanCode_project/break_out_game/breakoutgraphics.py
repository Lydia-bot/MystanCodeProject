"""
File: breakoutgraphics.py
Name: Lydia
------------------------------------------
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 15    # Initial vertical speed for the ball
MAX_X_SPEED = 7        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        self.paddle_offset = paddle_offset
        self.__dx = 0
        self.__dy = 0

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width-paddle_width)/2, y=self.window.height - paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)

        # Default initial velocity for the ball
        # Initialize our mouse listeners
        onmouseclicked(self.ball_position)
        onmousemoved(self.paddle_move)

        # Draw bricks
        brick_x = 0
        self.bricks = 0
        brick_y = brick_offset
        for i in range(brick_rows):
            brick_y += brick_height + brick_spacing
            for j in range(brick_cols):
                brick_x = (brick_width+brick_spacing)*j
                brick = GRect(brick_width, brick_height)
                brick.filled = True
                self.bricks += 1
                # print(self.bricks)
                self.window.add(brick, x=brick_x, y=brick_y)
                if i // 2 == 0:
                    brick.fill_color = 'red'
                elif i // 2 == 1:
                    brick.fill_color = 'orange'
                elif i // 2 == 2:
                    brick.fill_color = 'yellow'
                elif i // 2 == 3:
                    brick.fill_color = 'green'
                else:
                    brick.fill_color = 'blue'

        self.score = 0
        self.score_label = GLabel('Score: ' + str(self.score))
        self.score_label.font = '-20'
        self.window.add(self.score_label, x=0, y=self.score_label.height)

    def paddle_move(self, mouse):
        """
        1. The paddle always move at axis-x and stay at the same axis-y, controlled by the cursor.
        2. While the cursor moves outside the window, the paddle cannot move outside (it will be disappear in window).
        """
        if mouse.x + self.paddle.width / 2 > self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        elif mouse.x - self.paddle.width / 2 < 0:
            self.paddle.x = 0
        else:
            self.paddle.x = mouse.x - self.paddle.width / 2
            self.paddle.y = self.window.height - self.paddle_offset - self.paddle.height

    def ball_position(self, event):
        """
        While the user click, the ball that start at the middle of window will move
        """
        if self.ball.x == (self.window.width-self.ball.width) / 2 and self.ball.y == (self.window.height-self.ball.height) / 2:
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def ball_bouncing(self):
        """
        1. While tha ball bounce at the right and left side of window, it will go -x, and bounce at the top of window will go -y
        2. While the ball bounce at the paddle, it will go -y
        3. While the ball bounce at a brick, it will remove the brick and go -y
        """
        # ball setting
        # ball_1 = self.window.get_object_at(self.ball.x, self.ball.y)  # 球左上
        # ball_2 = self.window.get_object_at(self.ball.x + BALL_RADIUS * 2, self.ball.y)  # 球右上
        # ball_3 = self.window.get_object_at(self.ball.x, self.ball.y + BALL_RADIUS * 2)  # 球左下
        # ball_4 = self.window.get_object_at(self.ball.x + BALL_RADIUS * 2, self.ball.y + BALL_RADIUS * 2)  # 球右下
        # ball_top = ball_1 and ball_2  # 球上
        # ball_btm = ball_3 and ball_4  # 球下

        # the ball bounce at the window
        if self.ball.x <= 0 or self.ball.x + BALL_RADIUS * 2 >= self.window.width:
            self.__dx = -self.__dx
        elif self.ball.y <= 0:
            self.__dy = -self.__dy

        # elif ball_3 is self.paddle or ball_4 is self.paddle:
        #     self.__dy = -self.__dy
        #     # ball in paddle
        #     if self.ball.y + BALL_RADIUS * 2 < self.paddle.y:
        #         d = self.ball.y + BALL_RADIUS * 2 - self.paddle.y + 1
        #         self.ball.move(self.__dx, -d)
        if self.__dx:
            for i in range(2):
                for j in range(2):
                    # The four corners of the ball are used as detection points
                    obj = self.window.get_object_at(self.ball.x + (BALL_RADIUS * 2) * i, self.ball.y + (BALL_RADIUS * 2) * j)
                    # the ball bounce at the brick
                    if obj is not None and obj is not self.paddle and obj is not self.score_label:
                        self.__dy = -self.__dy
                        self.window.remove(obj)
                        self.bricks -= 1
                        self.score += 1
                        self.score_label.text = 'Score: ' + str(self.score)
                        self.__dy += 0.2
                    # the ball bounce on the paddle
                    elif obj is not None and obj is self.paddle and obj is not self.score_label:
                        self.__dy = -self.__dy
                        # ball in paddle
                        distance = self.ball.y + BALL_RADIUS * 2 - self.paddle.y + 1  # 球底 - 板上緣 + 1(偵測點在球底外，才不會一直偵測到球本身)
                        self.ball.move(self.__dx, -distance)  # 球y軸切到板多少，就移動板多少出去(避免震動)

    def restart(self, count):
        """
        The ball move outside the bottom of window, it will minus 1 lives time and restart at the original point
        """
        if self.ball.y > self.window.height:
            self.window.add(self.ball, x=(self.window.width-self.ball.width) / 2, y=(self.window.height-self.ball.height) / 2)
            self.__dx = 0
            self.__dy = 0
            count -= 1
        return count

    def get_bricks_count(self):
        return self.bricks


