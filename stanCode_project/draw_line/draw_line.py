"""
File: draw_line.py
Name: Lydia
-------------------------
his program creates lines on an instance of GWindow class.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10
window = GWindow()
check = False
point = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(event):
    global check
    line = GLine(point.x + SIZE / 2, point.y + SIZE / 2, event.x, event.y)
    if not check:
        window.add(point, x=event.x - SIZE / 2, y=event.y - SIZE / 2)
        check = True
    else:
        window.remove(point)
        window.add(line)
        check = False


if __name__ == "__main__":
    main()
