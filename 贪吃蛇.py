from graphics import *
import random
import time

t1 = 0.2


# 画蛇
def drawl(list):
    for p in list:
        (x, y) = p
        rect = Rectangle(Point(12 * x, 12 * y), Point(12 * x + 12, 12 * y + 12))
        rect.setFill('yellow')
        rect.draw(win)
    p = list[0]
    (x, y) = p
    cir = Circle(Point(12 * x + 6, 12 * y + 6), 2)
    cir.setFill('green')
    cir.draw(win)


def draw(n, f):
    (x, y) = n
    rect = Rectangle(Point(12 * x, 12 * y), Point(12 * x + 12, 12 * y + 12))
    rect.setFill('yellow')
    rect.draw(win)
    if f:
        cir = Circle(Point(12 * x + 6, 12 * y + 6), 2)
        cir.setFill('green')
        cir.draw(win)


# 删2333333
def delete(n):
    (x, y) = n
    rect = Rectangle(Point(12 * x, 12 * y), Point(12 * x + 12, 12 * y + 12))
    rect.setFill('grey')
    rect.setOutline('grey')
    rect.draw(win)


# 游戏失败23333333
def lose():
    message = Text(Point(180, 180), "You lose.Click anywhere to quit.")
    message.draw(win)


def produce_bean(list):
    x = random.randint(0, 29)
    y = random.randint(0, 29)
    while (x, y) in list:
        x = random.randint(0, 29)
        y = random.randint(0, 29)
    cir = Circle(Point(12 * x + 6, 12 * y + 6), 6)
    cir.setFill('red')
    cir.draw(win)
    return (x, y)


# 接收方向键操作，控制小蛇
def tanchishe():
    list1 = [(15, 15), (15, 16), (15, 17)]
    drawl(list1)
    bean = produce_bean(list1)
    a = win.getKey()
    get = False

    while True:
        b = a
        time.sleep(t1)
        a = win.checkKey()
        if a == "":
            a = b

        if a == "Up":
            (x, y) = list1[0]
            y -= 1
            if (y == -1 or (x, y) in list1):
                lose()
                break
            list1.insert(0, (x, y))
            if (x, y) != bean:
                delete(list1[-1])
                list1.pop()
                delete(list1[1])
                draw(list1[1], False)
                draw(list1[0], True)
            else:
                get = True
                delete(list1[1])
                draw(list1[1], False)
                draw(list1[0], True)
                bean = produce_bean(list1)

        elif a == "Down":
            (x, y) = list1[0]
            y += 1
            if (y == 30 or (x, y) in list1):
                lose()
                break
            list1.insert(0, (x, y))
            if (x, y) != bean:
                delete(list1[-1])
                list1.pop()
                delete(list1[1])
                draw(list1[1], False)
                draw(list1[0], True)
            else:
                get = True
                delete(list1[1])
                draw(list1[1], False)
                draw(list1[0], True)
                bean = produce_bean(list1)

        elif a == "Left":
            (x, y) = list1[0]
            x -= 1
            if (x == -1 or (x, y) in list1):
                lose()
                break
            list1.insert(0, (x, y))
            if (x, y) != bean:
                delete(list1[-1])
                list1.pop()
                delete(list1[1])
                draw(list1[1], False)
                draw(list1[0], True)
            else:
                get = True
                delete(list1[1])
                draw(list1[1], False)
                draw(list1[0], True)
                bean = produce_bean(list1)

        elif a == "Right":
            (x, y) = list1[0]
            x += 1
            if (x == 30 or (x, y) in list1):
                lose()
                break
            list1.insert(0, (x, y))
            if (x, y) != bean:
                delete(list1[-1])
                list1.pop()
                delete(list1[1])
                draw(list1[1], False)
                draw(list1[0], True)
            else:
                get = True
                delete(list1[1])
                draw(list1[1], False)
                draw(list1[0], True)
                bean = produce_bean(list1)

    win.getMouse()
    win.close()


# 游戏界面
win = GraphWin("贪吃蛇", 360, 360)
win.setBackground('grey')
tanchishe()
