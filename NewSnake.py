import curses
import random
import time

headC = ">"
win = curses.initscr()
border = win.getmaxyx()
title = "SNAKE by Csibi & Dzsoni"
speed = 0.10
head = [int(border[0]/2),int(border[1]/2)]
body = [head[:]]*3
apple = [random.randint(2, border[0]-2), random.randint(2, border[1]-2)]
pois = [random.randint(2, border[0]-2), random.randint(2, border[1]-2)]
q = 0
points = 0
direct = 8
win.nodelay(1)
last = []
def declarations():
    win = curses.initscr()
    curses.start_color()
    curses.noecho()
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_GREEN)
    win.bkgd(" " , curses.color_pair(1))

declarations()
def bodygrow():
    global head, body, last
    for z in range(len(body)-1, 0, -1):
        body[z] = body[z-1]
        win.addch(body[z][0],body[z][1] , "o", curses.color_pair(2))
    body[0] = head[:]

def food():
    global q, head, apple, points, body, speed, pois
    win.addch(apple[0], apple[1], "B", curses.color_pair(2))
    if head[0] == apple[0] and head[1] == apple[1]:
        points += 1
        win.delch(apple[0], apple[1])
        apple = [random.randint(2, border[0]-2), random.randint(2, border[1]-2)]
        win.refresh()
        body.append(body[-1])
        speed -= 0.0008
        win.delch(pois[0], pois[1])
        pois = [random.randint(2, border[0]-2), random.randint(2, border[1]-2)]
        win.addch(pois[0], pois[1], "ß", curses.color_pair(2))
        win.refresh()
    win.addstr(0, 0, "Points:" + str(points), curses.color_pair(2))

def poison():
    global q, head, pois, points
    win.addch(pois[0], pois[1], "ß", curses.color_pair(2))
    win.refresh()
    if head[0] == pois[0] and head[1] == pois[1]:
        q = ord("q")

def hitWall():
    global head, q, border
    border = win.getmaxyx()
    if head[0] == border[0]-1:
        q = ord("q")
    elif head[0] == 0:
        q = ord("q")
    elif head[1] == border[1]-1:
        q = ord("q")
    elif head[1] == 0:
        q = ord("q")

def turn():
    global headC, head, q, border, direct

    if q == ord("8") and head[0] > 0:
        headC = "^"
        direct = 8
    elif q == ord("5") and head[0] < border[0] - 1:
        headC = "v"
        direct = 5
    elif q == ord("6") and head[1] < border[1] - 1:
        headC = ">"
        direct = 6
    elif q == ord("4") and head[1] > 0:
        headC = "<"
        direct = 4

def forward():
    global q, head, headC, direct, speed
    if direct ==  4:
        if direct != 6:
            head[1] -= 1
    elif direct ==  6:
        if direct != 4:
            head[1] += 1
    elif direct == 5:
        if direct != 8:
            head[0] += 1
    elif direct == 8:
        if direct != 5:
            head[0] -= 1
    time.sleep(speed)

def start():
    global border
    win.clear()
    mess1="   #######    ###     ##       ####       ##     ##  ###########"
    mess2=" ##      ##   ####    ##      ##  ##      ##    ##   ##         "
    mess3="##        ##  ## ##   ##      ##  ##      ##   ##    ##         "
    mess4="##        ##  ## ##   ##     ##    ##     ##  ##     ##         "
    mess5=" ##           ##  ##  ##     ##    ##     ## ##      ##         "
    mess6="   #######    ##  ##  ##    ##########    ####       ###########"
    mess7="         ##   ##   ## ##    ##      ##    ## ##      ##         "
    mess8="##        ##  ##   ## ##   ##        ##   ##  ##     ##         "
    mess9="##        ##  ##    ####   ##        ##   ##   ##    ##         "
    mess10=" ##      ##   ##    ####  ##          ##  ##    ##   ##         "
    mess11="  ########    ##     ###  ##          ##  ##     ##  ###########"
    mess12="Press letter S to start"
    snakeText = [mess1, mess2, mess3,mess4,mess5,mess6,mess7,mess8,mess9,mess10,mess11,mess12]
    coordY = -5
    for z in snakeText:
        win.addstr(int(border[0]/2)+coordY, int((int(border[1])-len(z))//2), z, curses.A_BOLD)
        coordY += 1

    win.refresh()

def game():
    global headC, q, head, direct, points, body
    direct = 0
    q = -1
    points = 0
    body = [head[:]]*3
    head = [int(border[0]/2),int(border[1]/2)]

    while q != ord("s"):
        q = win.getch()
        start()

    while q != ord("q"):
        win.clear()
        win.border(1)
        turn()
        win.addstr(0, int(border[1]/2)-int(len(title)/2), title, curses.A_BOLD)
        food()
        forward()
        bodygrow()
        win.addstr(head[0], head[1], headC, curses.color_pair(2))
        win.refresh()
        q = win.getch()
        poison()
        hitWall()
    gameover()

def gameover():
    global q
    win.clear()
    while q != ord("r"):
        q = win.getch()
        if q == ord("q"):
            curses.endwin()
            raise SystemExit
        pnts = 'You got ' + str(points) + ' points!'
        message1 ="     #######      ########     ###       ###  ########### "
        message2 ="   ##      ##     ##    ##     ####     ####  ##          "
        message3 ="  ##             ##      ##    ##  ## ##  ##  ##          "
        message4 =" ##              ##########    ##   ###   ##  ########### "
        message5 =" ##     ######  ##        ##   ##         ##  ########### "
        message6 ="  ##        ##  ##        ##   ##         ##  ##          "
        message7 ="   ##      ##  ##          ##  ##         ##  ##          "
        message8 ="    ########   ##          ##  ##         ##  ########### "
        message9 ="                                                          "
        message10 = "     ########   ##          ##  ###########   #########   "
        message11 = "    ##      ##  ##          ##  ##            ##      ##  "
        message12 = "   ##        ##  ##        ##   ##            ##       ## "
        message13 = "  ##          ## ##        ##   ###########   ##      ##  "
        message14 = "  ##          ##  ##      ##    ###########   #########   "
        message15 = "   ##        ##    ##    ##     ##            ##      ##  "
        message16 = "    ##      ##      ##  ##      ##            ##       ## "
        message17 = "     ########        ####       ###########   ##        ##"

        GOText = [message1, message2, message3,message4,message5,message6,message7,message8,message9,message10,message11,message12,message13,message14,message15,message16,message17]
        k = -8
        for z in GOText:
            win.addstr(int(border[0]/2)+k, int((int(border[1])-len(z))//2), z, curses.A_BOLD)
            k += 1

            win.addstr(int(border[0]/2)+11, int((int(border[1])-18)//2), "Press R to restart,or Q to quit", curses.A_BOLD)
            win.addstr(int(border[0]/2)+10, int((int(border[1])-len(pnts))//2), pnts, curses.A_BOLD)
            win.refresh()
            win.clear
    game()
game()
curses.endwin()
