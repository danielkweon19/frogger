# Created by Daniel Kweon (dsk3su) and Cooper Grace (cfg5bkz)
"""
We plan on making a version of Frogger
Frogger involves a player controlled frog hopping across a street making sure to avoid cars and then hopping across a river making sure to stay on logs and turtles
The optional requirements will (indicated with ***):

1.) Start the game in the start screen and use the mouse to make selections
1.) The user will start off will ***three lives***. As they play the game and collide into cars sor fall into the lake enemies, they will lose lives
2.) There also will be a ***points system*** where the more the frog gets to the other side, the more points that they will collect
3.) There will be ***enemies (cars)*** that will take away a life when the frog touches them
4.) There will be a ***timer limiting*** the amount of time the player can play before the game ends
5.) We also have a ***character selection sheet***, where the character can select which color frog they would like to play as
6.) The user is able to reset the game and start over once they die, where they can view their final score
7.) There are ***sprite animations*** for when the frog jumps, and when the frog dies, there is a ***explosion sprite animation***
5.) There will be a fly that if it is caught by the frog bonus points are awarded to the player
"""


import pygame
import gamebox
import math
import random

camera = gamebox.Camera(500, 600)
ticks_per_second = 30
title = gamebox.from_text(250, 100, "Frog Jump", 100, "green", italic=True)
title2 = gamebox.from_text(250, 50, "Frog Jump", 100, "red", italic=True)

start = gamebox.from_text(250, 300, "Start", 100, "red", italic=True)
ids = gamebox.from_text(250, 400, "Student IDS: dsk3su and cfg5bkz", 30, "pink", italic=True)
instructions = gamebox.from_text(250, 450, "Instructions: ", 30, "purple", italic=True)
instructions2 = gamebox.from_text(250, 470, "Press 'start' with mouse to begin.", 25, "red", italic=False)
instructions3 = gamebox.from_text(250, 490, "With 60 seconds and 3 lives, use the arrow keys to", 25, "red", italic=False)
instructions4 = gamebox.from_text(250, 510, "drag your frog to the other side! Avoid touching", 25, "red", italic=False)
instructions5 = gamebox.from_text(250, 530, "cars or obstacles along the way. Collect as many points", 25, "red", italic=False)
instructions6 = gamebox.from_text(250, 550, "as you can! Get flies for extra points! Good luck", 25, "red", italic=False)

start_platform = gamebox.from_color(250, 500, "purple", 600, 50)
end_platform = gamebox.from_color(250, 10, "green", 600, 270)
ground_platform = gamebox.from_color(250, 300, "brown", 600, 50)
water = gamebox.from_color(250, 10, "blue", 600, 530)

log = gamebox.from_image(100, 260, "log.png")
log2 = gamebox.from_image(300, 260, "log.png")
log3 = gamebox.from_image(500, 260, "log.png")

log4 = gamebox.from_image(100, 230, "log.png")
log5 = gamebox.from_image(300, 230, "log.png")
log6 = gamebox.from_image(500, 230, "log.png")

log7 = gamebox.from_image(100, 160, "log.png")
log8 = gamebox.from_image(200, 160, "log.png")
log9 = gamebox.from_image(300, 160, "log.png")

logs_right = [log4, log5, log6]
logs_left = [log, log2, log3]

logs_l = [log7, log8, log9]

heart = gamebox.from_image(120, 540, "heart.png")
heart2 = gamebox.from_image(140, 540, "heart.png")
heart3 = gamebox.from_image(160, 540, "heart.png")
heart.size = [20, 20]
heart2.size = [20, 20]
heart3.size = [20, 20]


sheet = gamebox.load_sprite_sheet("output-onlinepngtools (3).png", 3, 8)
sheet_cars = gamebox.load_sprite_sheet("cars.png", 1, 2)
sheet_cars2 = gamebox.load_sprite_sheet("cars22.png", 1, 2)
sheet_death = gamebox.load_sprite_sheet("death.png", 1, 7)
sheet_croc = gamebox.load_sprite_sheet("croc.png", 1, 2)
sheet_turtles = gamebox.load_sprite_sheet("turtles.png", 1, 5)

death = gamebox.from_image(250, 500, sheet_death[0])
death.size = [100, 100]

frog = gamebox.from_image(250, 500, sheet[0])

turtle1 = gamebox.from_image(100, 190, sheet_turtles[0])
turtle2 = gamebox.from_image(300, 190, sheet_turtles[0])
turtle3 = gamebox.from_image(400, 190, sheet_turtles[0])

turtles = [turtle1, turtle2, turtle3]
# croc = gamebox.from_image(250, 220, sheet_croc[1])
# croc.size = [100, 50]
cnum = 0

car = gamebox.from_image(100, 450, sheet_cars[0])
car1 = gamebox.from_image(400, 450, sheet_cars[1])

car2 = gamebox.from_image(200, 350, sheet_cars[0])
car3 = gamebox.from_image(500, 350, sheet_cars[1])

car4 = gamebox.from_image(300, 400, sheet_cars2[0])
car5 = gamebox.from_image(500, 400, sheet_cars2[1])


cars = [car, car1]
cars2 = [car4, car5]
cars3 = [car2, car3]

fly = gamebox.from_image(250, 300, 'fly.png')

score = 0
lives = 3
lives_box = gamebox.from_text(60, 530, "Lives Remaining: ", 20, "white")
score_box = gamebox.from_text(200, 530, "Score: " + str(score), 20, "white")
game_over_box = gamebox.from_text(250, 100, "Game Over", 100, "red", italic=True)
restart = gamebox.from_text(250, 300, "Restart", 100, "red", italic=True)
final_score = gamebox.from_text(250, 500, "Score: " + str(score), 100, "red", italic=True)

select1 = gamebox.from_image(100, 500, sheet[0])
select2 = gamebox.from_image(250, 500, sheet[8])
select3 = gamebox.from_image(400, 500, sheet[16])
selections = [select1, select2, select3]
frog.size = [50, 50]
gamestart = False
gamestart2 = False
gameover = False
ticks = 0
seconds = 0
time_left = ""
time_box = gamebox.from_text(60, 550, "Time Remaining: " + time_left, 20, "white")
level_time = 60
frog_values = []


def set_logpos():
    """
    Used the set the size of the logs before the game starts
    :return: n/a
    """
    for t in turtles:
        t.size = [50, 50]
    for l in logs_left:
        l.size = [70, 50]
    for l2 in logs_right:
        l2.size = [70, 50]
    for l3 in logs_l:
        l3.size = [70, 50]

set_logpos()  # Calling set_logpos() as a way to set the logs before any other function is called


def tick(keys):
    """
    #A method that will be called every frame. Must have parameter"keys"
    :param keys: key pressed
    :return: n/a
    """
    global ticks, seconds, time_left, level_time, gamestart2, gamestart, gameover
    if gamestart is False and gameover is False: # If the game has just begun with no resets
        intro()
        draw_images_intro()
    if gamestart is True and gamestart2 is False: # If the user has pressed the start button
        draw_selection()
    if gamestart2 is True: # If the user picked a frog color
        movecars()
        if pygame.K_UP in keys:
            i = 0
            while i < 30:
                move_up(i)
                i += 1
            frog.y -= 30
        if pygame.K_DOWN in keys:
            i = 0
            while i < 30:
                move_down(i)
                i += 1
            frog.y += 30
        if pygame.K_RIGHT in keys:
            i = 0
            while i < 30:
                move_right(i)
                i += 1
            frog.x += 30
        if pygame.K_LEFT in keys:
            i = 0
            while i < 30:
                move_left(i)
                i += 1
            frog.x -= 30
        ticks += 1
        seconds = int((ticks / ticks_per_second))
        time_left = str(level_time - seconds).zfill(3)
        keys.clear()
        constraints()
        fly1()
        water_touch()
        draw_images()
        if lives == 0 or time_left == "000":
            gamestart2 = False
            gamestart = False
            gameover = True
    if gameover is True:
        restart_page()
        draw_restart()

def fly1():
    """
    This function manages the fly. The fly will move around randomly. If the frog catches the fly it will disapear and
    the player and will receive 150 points
    :return:
    """
    global score
    if ticks % 40 == 0:
        xfly = random.randint(1, 2)
        if xfly == 1:
            fly.x += 50
            if fly.x > 500:
                fly.x = 500
        elif xfly == 2:
            fly.x -= 50
            if fly.x < 0:
                fly.x = 0
    if ticks % 50 == 0:
        yfly = random.randint(1, 2)
        if yfly == 1:
            fly.y += 50
            if fly.y > 600:
                fly.y = 600
        elif yfly == 2:
            fly.y -= 50
            if fly.y < 0:
                fly.y = 0
    distance_fly = math.sqrt(((fly.x - frog.x) ** 2) + ((fly.y - frog.y) ** 2))
    if 0 <= distance_fly < 30:
        score += 150
        fly.x = 1000

def water_touch():
    """
    This function handles the water. If the frog touches the water then the frog loses a life.
    :return:
    """
    global lives
    if 260 >= frog.y > 140:
        return True
    else:
        return False


def platforms():
    """
    This function draws the platforms
    :return:
    """
    camera.draw(water)
    camera.draw(start_platform)
    camera.draw(end_platform)
    camera.draw(ground_platform)


def draw_characters():
    """
    This function draws the timer, lives, score, fly, and frog
    :return:
    """
    camera.draw(time_box)
    camera.draw(lives_box)
    camera.draw(score_box)
    if lives == 3:
        camera.draw(heart)
        camera.draw(heart2)
        camera.draw(heart3)
    elif lives == 2:
        camera.draw(heart)
        camera.draw(heart2)
    elif lives == 1:
        camera.draw(heart)
    for t in turtles:
        camera.draw(t)
    for l in logs_left:
        camera.draw(l)
    for l2 in logs_right:
        camera.draw(l2)
    for l3 in logs_l:
        camera.draw(l3)
    # camera.draw(croc)
    camera.draw(frog)
    camera.draw(fly)
    for c in cars:
        camera.draw(c)
    for c2 in cars2:
        camera.draw(c2)
    for c3 in cars3:
        camera.draw(c3)
    camera.draw(title2)


def move_up(i):
    """
    This function handles the frog's movement in the up direction
    :param i:
    :return:
    """
    if i < 10:
        i = frog_values[0]
    if 10 <= i < 20:
        i = frog_values[1]
    if i >= 20:
        i = frog_values[0]
    camera.clear("black")
    platforms()
    frog.image = sheet[i]
    draw_characters()
    camera.display()


def move_down(i):
    """
    This function handles the frog's movement in the right direction
    :param i:
    :return:
    """
    if i < 10:
        i = frog_values[4]
    if 10 <= i < 20:
        i = frog_values[5]
    if i >= 20:
        i = frog_values[4]
    camera.clear("black")
    platforms()
    frog.image = sheet[i]
    draw_characters()
    camera.display()


def move_right(i):
    """
    This function handles the frog's movement in the right direction
    :param i:
    :return:
    """
    if i < 10:
        i = frog_values[6]
    if 10 <= i < 20:
        i = frog_values[7]
    if i >= 20:
        i = frog_values[6]
    camera.clear("black")
    platforms()
    frog.image = sheet[i]
    draw_characters()
    camera.display()


def move_left(i):
    """
    This function handles the frog's movement in the left direction
    :param i:
    :return:
    """
    if i < 10:
        i = frog_values[2]
    if 10 <= i < 20:
        i = frog_values[3]
    if i >= 20:
        i = frog_values[2]
    camera.clear("black")
    platforms()
    frog.image = sheet[i]
    draw_characters()
    camera.display()


def draw_selection():
    """
    Called to draw the basic images for certain actions
    :return:
    """
    global gamestart2
    global frog
    global frog_values
    ask = gamebox.from_text(250, 300, "Pick a Frog", 100, "green", italic=True)
    camera.clear("black")
    camera.draw(title)
    camera.draw(ask)
    distance1 = math.sqrt((camera.mousex - select1.x) ** 2 + (camera.mousey - select1.y) ** 2)
    distance2 = math.sqrt((camera.mousex - select2.x) ** 2 + (camera.mousey - select2.y) ** 2)
    distance3 = math.sqrt((camera.mousex - select3.x) ** 2 + (camera.mousey - select3.y) ** 2)
    if 0 <= distance1 <= 40:
        select1.image = sheet[1]
        if camera.mouseclick is True:
            gamestart2 = True
            frog.image = sheet[0]
            frog_values = [0, 1, 2, 3, 4, 5, 6, 7]
    else:
        select1.image = sheet[0]
    if 0 <= distance2 <= 40:
        select2.image = sheet[9]
        if camera.mouseclick is True:
            gamestart2 = True
            frog.image = sheet[8]
            frog_values = [8, 9, 10, 11, 12, 13, 14, 15]
    else:
        select2.image = sheet[8]
    if 0 <= distance3 <= 40:
        select3.image = sheet[17]
        if camera.mouseclick is True:
            gamestart2 = True
            frog.image = sheet[16]
            frog_values = [16, 17, 18, 19, 20, 21, 22, 23]
    else:
        select3.image = sheet[16]
    for s in selections:
        s.size = [100, 100]
        camera.draw(s)
    camera.display()


def draw_images_intro():
    """
    Used to draw the images for the introduction (start page)
    :return:
    """
    camera.draw(start)
    camera.draw(title)
    camera.draw(ids)
    camera.draw(instructions)
    camera.draw(instructions2)
    camera.draw(instructions3)
    camera.draw(instructions4)
    camera.draw(instructions5)
    camera.draw(instructions6)
    camera.display()


def intro():
    """
    This function takes care of the start button color change when the mouse hovers over it
    :return:
    """
    global start
    global gamestart
    distance = math.sqrt((camera.mousex - start.x) ** 2 + (camera.mousey - start.y) ** 2)
    if 0 <= distance <= 70:
        start = gamebox.from_text(250, 300, "Start", 100, "blue", italic=True)
        if camera.mouseclick is True:
            gamestart = True
    else:
        start = gamebox.from_text(250, 300, "Start", 100, "red", italic=True)


def draw_images():
    """
    This function handles the drawing of everything
    :return:
    """
    global time_box
    global lives_box
    global score_box
    time_box = gamebox.from_text(70, 570, "Time Remaining: " + time_left, 20, "white")
    lives_box = gamebox.from_text(60, 540, "Lives Remaining: ", 20, "white")
    score_box = gamebox.from_text(200, 540, "Score: " + str(score), 20, "white")
    camera.clear("black")
    platforms()
    draw_characters()
    camera.display()


def restart_page():
    """
    This function handles the restart page
    :return:
    """
    global restart, gameover, gamestart, lives, level_time, seconds, score, time_left, ticks
    distance = math.sqrt(((camera.mousex - restart.x) ** 2) + ((camera.mousey - restart.y) ** 2))
    if 0 <= distance <= 70:
        restart = gamebox.from_text(250, 300, "Restart", 100, "blue", italic=True)
        if camera.mouseclick is True:
            gameover = False
            lives = 3
            ticks = 0
            level_time = 60
            seconds = 0
            score = 0
            time_left = ""
            fly.x = 400
            gamestart = True
    else:
        restart = gamebox.from_text(250, 300, "Restart", 100, "red", italic=True)


def draw_restart():
    """
    This function draws the necessary components for a restart
    :return:
    """
    camera.clear("black")
    camera.draw(game_over_box)
    camera.draw(restart)
    final_score = gamebox.from_text(250, 500, "Score: " + str(score), 100, "red", italic=True)
    camera.draw(final_score)
    camera.display()


def draw_basic():
    """
    This function draws everything when the game is started
    :return:
    """
    global time_box
    global lives_box
    global score_box
    time_box = gamebox.from_text(70, 570, "Time Remaining: " + time_left, 20, "white")
    lives_box = gamebox.from_text(60, 540, "Lives Remaining: ", 20, "white")
    score_box = gamebox.from_text(200, 540, "Score: " + str(score), 20, "white")
    camera.clear("black")
    platforms()
    draw_characters()
    camera.display()


def constraints():
    """
    This function handles the constraints for the size of cars and where the frog can be
    :return:
    """
    global score
    for c in cars:
        c.size = [50, 50]
    for c2 in cars2:
        c2.size = [50, 50]
    for c3 in cars3:
        c3.size = [50, 50]
    if 260 < frog.y:
        if frog.x > 470:
            frog.x = 470
        if frog.x < 20:
            frog.x = 20
    else:
        if frog.x > 470:
            death_method()
        if frog.x < 20:
            death_method()
    if frog.y <= 140:
        frog.x = 250
        frog.y = 500
        score += 100
    if frog.y > 500:
        frog.y = 500


def movecars():
    """
    This function handles the movement of cars
    :return:
    """
    global lives, valid_place
    distance_log = math.sqrt(((log.x - frog.x) ** 2) + ((log.y - frog.y) ** 2))
    distance_log2 = math.sqrt(((log2.x - frog.x) ** 2) + ((log2.y - frog.y) ** 2))
    distance_log3 = math.sqrt(((log3.x - frog.x) ** 2) + ((log3.y - frog.y) ** 2))
    distance_log4 = math.sqrt(((log4.x - frog.x) ** 2) + ((log4.y - frog.y) ** 2))
    distance_log5 = math.sqrt(((log5.x - frog.x) ** 2) + ((log5.y - frog.y) ** 2))
    distance_log6 = math.sqrt(((log6.x - frog.x) ** 2) + ((log6.y - frog.y) ** 2))
    distance_log7 = math.sqrt(((log7.x - frog.x) ** 2) + ((log7.y - frog.y) ** 2))
    distance_log8 = math.sqrt(((log8.x - frog.x) ** 2) + ((log8.y - frog.y) ** 2))
    distance_log9 = math.sqrt(((log9.x - frog.x) ** 2) + ((log9.y - frog.y) ** 2))
    distance_turtle = math.sqrt(((turtle1.x - frog.x) ** 2) + ((turtle1.y - frog.y) ** 2))
    distance_turtle2 = math.sqrt(((turtle2.x - frog.x) ** 2) + ((turtle2.y - frog.y) ** 2))
    distance_turtle3 = math.sqrt(((turtle3.x - frog.x) ** 2) + ((turtle3.y - frog.y) ** 2))
    if 0 <= distance_log < 30 or 0 <= distance_log2 < 30 or 0 <= distance_log3 < 30 or 0 <= distance_turtle < 30 or 0 <= distance_turtle2 < 30 or 0 <= distance_turtle3 < 30 or 0 <= distance_log7 < 30 or 0 <= distance_log8 < 30 or 0 <= distance_log9 < 30:
        frog.x -= 5
    elif 0 <= distance_log4 < 30 or 0 <= distance_log5 < 30 or 0 <= distance_log6 < 30:
        frog.x += 5
    else:
        if water_touch() is True:
            death_method()
    for l in logs_left:
        l.x -= 5
        if l.x < 0:
            l.x = 500
    for l2 in logs_right:
        l2.x += 5
        if l2.x > 500:
            l2.x = 0
    for l3 in logs_l:
        l3.x -= 5
        if l3.x < 0:
            l3.x = 500
    for t in turtles:
        t.x -= 5
        if t.x < 0:
            t.x = 500
    for ca1 in cars:
        ca1.x -= 5
        if ca1.x < 0:
            #ran = random.randint(500,700)
            ca1.x = 500
    for ca2 in cars2:
        ca2.x += 5
        if ca2.x > 500:
            #ran1 = random.randint(-200, 0)
            ca2.x = 0
    for ca3 in cars3:
        ca3.x -= 5
        if ca3.x < 0:
            #ran2 = random.randint(500, 700)
            ca3.x = 500
    for c in cars:
        distance1 = math.sqrt(((c.x - frog.x) ** 2) + ((c.y - frog.y) ** 2))
        if 0 <= distance1 < 22:
            death_method()
    for c2 in cars2:
        distance2 = math.sqrt(((c2.x - frog.x) ** 2) + ((c2.y - frog.y) ** 2))
        if 0 <= distance2 < 22:
            death_method()
    for c3 in cars3:
        distance3 = math.sqrt(((c3.x - frog.x) ** 2) + ((c3.y - frog.y) ** 2))
        if 0 <= distance3 < 22:
            death_method()


def death_method():
    """
    This function handles when the frog runs out of lives
    :return:
    """
    global lives
    death.x = frog.x
    death.y = frog.y
    lives -= 1
    i = 0
    while i < 49:
        show_death(i)
        i += 1
    frog.x = 250
    frog.y = 500


def show_death(i):
    """
    This function handles the display of what happens when the frog dies
    :param i:
    :return:
    """
    if i < 14:
        i = 0
    if 14 <= i < 28:
        i = 1
    if 28 <= i < 42:
        i = 2
    if 42 <= i < 56:
        i = 3
    if 56 <= i < 70:
        i = 4
    if 70 <= i < 84:
        i = 5
    if 84 <= i < 98:
        i = 6
    camera.clear("black")
    platforms()
    death.image = sheet_death[i]
    camera.draw(time_box)
    camera.draw(lives_box)
    camera.draw(score_box)
    if lives == 3:
        camera.draw(heart)
        camera.draw(heart2)
        camera.draw(heart3)
    elif lives == 2:
        camera.draw(heart)
        camera.draw(heart2)
    elif lives == 1:
        camera.draw(heart)
    # camera.draw(turtles)
    for t in turtles:
        camera.draw(t)
    for l in logs_left:
        camera.draw(l)
    for l2 in logs_right:
        camera.draw(l2)
    for l3 in logs_l:
        camera.draw(l3)
    # camera.draw(croc)
    for c in cars:
        camera.draw(c)
    for c2 in cars2:
        camera.draw(c2)
    for c3 in cars3:
        camera.draw(c3)
    camera.draw(fly)
    camera.draw(death)
    camera.draw(title2)
    camera.display()


# tell gamebox to call the tick method 30 times per second
gamebox.timer_loop(ticks_per_second, tick)


