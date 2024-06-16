"""
File: my_drawing.py
Name: Lydia
----------------------
This file uses the campy module to
draw on a GWindow object.
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLabel
from campy.graphics.gwindow import GWindow

window = GWindow(550, 700, title='Welcome to stanKode!')


def main():
    """
    Title: Welcome to stanKode!

    There is a cute dog welcomes you to stanKode class!
    """
    head()
    logo()
    hand()
    body()
    karel()


def body():
    hair =GPolygon()
    hair.add_vertex((347, 320))
    hair.add_vertex((345, 355))
    hair.add_vertex((340, 340))
    hair.add_vertex((335, 375))
    hair.add_vertex((330, 380))
    hair.add_vertex((328, 355))
    hair.add_vertex((325, 380))
    hair.add_vertex((220, 380))
    hair.add_vertex((220, 370))
    hair.add_vertex((225, 330))
    hair.add_vertex((235, 300))
    hair.add_vertex((230, 365))
    hair.add_vertex((235, 375))
    hair.add_vertex((245, 380))
    hair.add_vertex((265, 380))
    hair.add_vertex((270, 310))
    hair.add_vertex((280, 345))
    hair.add_vertex((290, 365))
    hair.add_vertex((300, 375))
    hair.add_vertex((305, 345))
    hair.add_vertex((300, 320))
    hair.add_vertex((310, 335))
    hair.add_vertex((320, 375))
    hair.add_vertex((325, 340))
    hair.add_vertex((335, 350))
    hair.add_vertex((338, 320))
    hair.add_vertex((342, 335))
    hair.filled = True
    hair.fill_color = 'linen'
    hair.color = 'linen'
    window.add(hair)

    tail = GPolygon()
    tail.add_vertex((80, 380))
    tail.add_vertex((130, 380))
    tail.add_vertex((120, 350))
    tail.add_vertex((120, 300))
    tail.add_vertex((125, 250))
    tail.add_vertex((140, 200))
    tail.add_vertex((120, 220))
    tail.add_vertex((80, 300))
    tail.add_vertex((75, 350))
    tail.filled = True
    tail.fill_color = 'goldenrod'
    tail.color = 'goldenrod'
    window.add(tail)

    t_shadow = GPolygon()
    t_shadow.add_vertex((80, 380))
    t_shadow.add_vertex((75, 350))
    t_shadow.add_vertex((80, 300))
    t_shadow.add_vertex((100, 260))
    t_shadow.add_vertex((95, 290))
    t_shadow.add_vertex((100, 350))
    t_shadow.add_vertex((130, 380))
    t_shadow.filled = True
    t_shadow.fill_color = 'darkgoldenrod'
    t_shadow.color = 'darkgoldenrod'
    window.add(t_shadow)


    window.add(tail)

def hand():
    r_hand = GPolygon()
    r_hand.add_vertex((350, 365))
    r_hand.add_vertex((360, 360))
    r_hand.add_vertex((390, 360))
    r_hand.add_vertex((400, 365))
    r_hand.add_vertex((405, 375))
    r_hand.add_vertex((400, 400))
    r_hand.add_vertex((350, 400))
    r_hand.add_vertex((345, 375))
    r_hand.filled = True
    r_hand.fill_color = 'goldenrod'
    r_hand.color = 'saddlebrown'
    window.add(r_hand)

    r_shadow = GPolygon()
    r_shadow.add_vertex((350, 400))
    r_shadow.add_vertex((365, 398))
    r_shadow.add_vertex((367, 375))
    r_shadow.add_vertex((369, 395))
    r_shadow.add_vertex((371, 398))
    r_shadow.add_vertex((380, 398))
    r_shadow.add_vertex((382, 395))
    r_shadow.add_vertex((384, 375))
    r_shadow.add_vertex((386, 398))
    r_shadow.add_vertex((400, 400))
    r_shadow.filled = True
    r_shadow.fill_color = 'saddlebrown'
    r_shadow.color = 'saddlebrown'
    window.add(r_shadow)


def karel():
    body = GRect(80, 80, x=235, y=450)
    body.filled = True
    body.fill_color = 'blue'
    body.color = 'darkblue'
    window.add(body)

    head = GOval(80, 50, x=235, y=395)
    head.filled = True
    head.fill_color = 'gray'
    head.color = 'darkgray'
    window.add(head)

    l_eye = GRect(10, 10, x=255, y=415)
    l_eye.filled = True
    l_eye.fill_color = 'blue'
    l_eye.color = 'darkblue'
    window.add(l_eye)

    r_eye = GRect(10, 10, x=285, y=415)
    r_eye.filled = True
    r_eye.fill_color = 'blue'
    r_eye.color = 'darkblue'
    window.add(r_eye)

    l_leg = GOval(30, 18, x=235, y=535)
    l_leg.filled = True
    l_leg.fill_color = 'red'
    l_leg.color = 'maroon'
    window.add(l_leg)

    r_leg = GOval(30, 18, x=285, y=535)
    r_leg.filled = True
    r_leg.fill_color = 'red'
    r_leg.color = 'maroon'
    window.add(r_leg)

    r_hand = GPolygon()
    r_hand.add_vertex((380, 415))
    r_hand.add_vertex((370, 410))
    r_hand.add_vertex((320, 460))
    r_hand.add_vertex((330, 465))
    r_hand.filled = True
    r_hand.fill_color = 'forestgreen'
    r_hand.color = 'green'
    window.add(r_hand)

    l_hand = GPolygon()
    l_hand.add_vertex((220, 465))
    l_hand.add_vertex((230, 460))
    l_hand.add_vertex((190, 410))
    l_hand.add_vertex((180, 415))
    l_hand.filled = True
    l_hand.fill_color = 'forestgreen'
    l_hand.color = 'green'
    window.add(l_hand)

    k_label = GLabel('K', x=250, y=530)
    k_label.font = '-60'
    k_label.color = 'white'
    window.add(k_label)


def logo():
    banner1 = GRect(450, 220, x=50, y=380)
    banner1.filled = True
    banner1.fill_color = 'firebrick'
    banner1.color = 'tomato'
    window.add(banner1)

    label = GLabel('stan     ode', x=100, y=530)
    label.font = '-60'
    label.color = 'white'
    window.add(label)


def head():
    top1 = GPolygon()
    top1.add_vertex((180, 190))
    top1.add_vertex((230, 150))
    top1.add_vertex((280, 145))
    top1.add_vertex((310, 155))
    top1.add_vertex((330, 200))
    top1.add_vertex((360, 400))
    top1.add_vertex((150, 450))
    top1.add_vertex((180, 320))
    top1.add_vertex((150, 280))
    top1.filled = True
    top1.fill_color = 'goldenrod'
    top1.color = 'goldenrod'
    window.add(top1)

    top2 = GPolygon()
    top2.add_vertex((305, 180))
    top2.add_vertex((355, 220))
    top2.add_vertex((305, 220))
    top2.add_vertex((280, 190))
    top2.filled = True
    top2.fill_color = 'palegoldenrod'
    top2.color = 'palegoldenrod'
    window.add(top2)

    mouth3 = GPolygon()
    mouth3.add_vertex((250, 250))
    mouth3.add_vertex((260, 270))
    mouth3.add_vertex((300, 300))
    mouth3.add_vertex((350, 300))
    mouth3.filled = True
    window.add(mouth3)

    jaw = GPolygon()
    jaw.add_vertex((240, 250))
    jaw.add_vertex((250, 250))
    jaw.add_vertex((260, 270))
    jaw.add_vertex((340, 300))
    jaw.add_vertex((300, 300))
    jaw.add_vertex((260, 280))
    jaw.filled = True
    jaw.fill_color = 'darkgoldenrod'
    jaw.color = 'darkgoldenrod'
    window.add(jaw)

    shadow1 = GPolygon()
    shadow1.add_vertex((180, 190))
    shadow1.add_vertex((150, 280))
    shadow1.add_vertex((180, 320))
    shadow1.add_vertex((200, 320))
    shadow1.add_vertex((230, 280))
    shadow1.add_vertex((200, 180))
    shadow1.add_vertex((220, 280))
    shadow1.add_vertex((200, 300))
    shadow1.add_vertex((180, 300))
    shadow1.add_vertex((170, 280))
    shadow1.filled = True
    shadow1.fill_color = 'saddlebrown'
    shadow1.color = 'saddlebrown'
    window.add(shadow1)

    shadow1 = GPolygon()
    shadow1.add_vertex((180, 190))
    shadow1.add_vertex((220, 280))
    shadow1.add_vertex((200, 300))
    shadow1.add_vertex((180, 300))
    shadow1.add_vertex((170, 280))
    shadow1.filled = True
    shadow1.fill_color = 'darkgoldenrod'
    shadow1.color = 'darkgoldenrod'
    window.add(shadow1)

    tonque1 = GPolygon()
    tonque1.add_vertex((340, 250))
    tonque1.add_vertex((270, 250))
    tonque1.add_vertex((310, 310))
    tonque1.add_vertex((330, 320))
    tonque1.add_vertex((350, 310))
    tonque1.add_vertex((355, 300))
    tonque1.filled = True
    tonque1.fill_color = 'salmon'
    tonque1.color = 'salmon'
    window.add(tonque1)

    tonque1 = GPolygon()
    tonque1.add_vertex((320, 250))
    tonque1.add_vertex((340, 280))
    tonque1.add_vertex((340, 310))
    tonque1.add_vertex((335, 280))

    tonque1.filled = True
    tonque1.fill_color = 'darkred'
    tonque1.color = 'darkred'
    window.add(tonque1)

    mouth1 = GPolygon()
    mouth1.add_vertex((350, 240))
    mouth1.add_vertex((330, 250))
    mouth1.add_vertex((340, 270))
    mouth1.add_vertex((345, 270))
    mouth1.add_vertex((350, 260))
    mouth1.filled = True
    mouth1.fill_color = 'khaki'
    mouth1.color = 'khaki'
    window.add(mouth1)

    mouth2 = GPolygon()
    mouth2.add_vertex((330, 250))
    mouth2.add_vertex((250, 220))
    mouth2.add_vertex((240, 250))
    mouth2.add_vertex((280, 270))
    mouth2.add_vertex((300, 270))
    mouth2.filled = True
    mouth2.fill_color = 'khaki'
    mouth2.color = 'khaki'
    window.add(mouth2)

    top3 = GPolygon()
    top3.add_vertex((330, 250))
    top3.add_vertex((250, 220))
    top3.add_vertex((280, 190))
    top3.filled = True
    top3.fill_color = 'gold'
    top3.color = 'gold'
    window.add(top3)

    nose = GPolygon()
    nose.add_vertex((355, 220))
    nose.add_vertex((340, 215))
    nose.add_vertex((325, 215))
    nose.add_vertex((305, 220))
    nose.add_vertex((310, 240))
    nose.add_vertex((320, 250))
    nose.add_vertex((340, 250))
    nose.add_vertex((350, 240))
    nose.filled = True
    window.add(nose)

    eye1 = GPolygon()
    eye1.add_vertex((250, 185))
    eye1.add_vertex((260, 190))
    eye1.add_vertex((225, 200))
    eye1.add_vertex((230, 190))
    eye1.filled = True
    window.add(eye1)

    eye2 = GPolygon()
    eye2.add_vertex((305, 180))
    eye2.add_vertex((323, 185))
    eye2.add_vertex((325, 190))
    eye2.add_vertex((320, 190))
    eye2.filled = True
    window.add(eye2)

    dog_label = GLabel('woof !', x=370, y=120)
    dog_label.font = '-40'
    window.add(dog_label)

    mark1 = GPolygon()
    mark1.add_vertex((320, 60))
    mark1.add_vertex((290, 120))
    mark1.add_vertex((300, 60))
    mark1.filled = True
    window.add(mark1)

    mark2 = GPolygon()
    mark2.add_vertex((380, 190))
    mark2.add_vertex((450, 165))
    mark2.add_vertex((450, 180))
    mark2.filled = True
    window.add(mark2)


if __name__ == '__main__':
    main()
