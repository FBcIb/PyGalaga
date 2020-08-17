import pygame
import gamebox
import random

# Required feature: Small enough window
camera = gamebox.Camera(600,600)
game_started = False
game_started2 = False

# Set projectiles to None so we can reset them when off screen or post collision
mis = None
mis1 = None
mis2 = None
mis3 = None
mis4 = None
mis_1 = None
mis_2 = None
mis_3 = None
mis_4 = None
mis_5 = None
enmis = None
enmis1 = None
enmis2 = None
enmis3 = None
enmis4 = None

# Includes Required features: Graphics/Images and Enemies (Used in both 1 and 2 player mode)
# Creating most of our pals - Characters, borders, and enemies
char = gamebox.from_image(50, 300, 'gal_ship1.png')
char.scale_by(.35)
char1 = gamebox.from_image(50, 200, 'gal_ship1.png')
char1.scale_by(.35)
char2 = gamebox.from_image(50, 400, 'gal_ship2.png')
char2.scale_by(.35)
bonus_heart = gamebox.from_image(char.x + 800, random.randint(50,550), 'gal_heart.png')
bonus_heart.scale_by(.2)
bord_left = gamebox.from_color(-150,300, 'black', 200, 800)
bord_top = gamebox.from_color(300,-100, 'black', 800, 200)
bord_bot = gamebox.from_color(300,700, 'black', 800, 200)
enemy1 = gamebox.from_image(500, 100, 'gal_enemy1.png')
enemy1.scale_by(.5)
enemy2 = gamebox.from_image(500, 200, 'gal_enemy1.png')
enemy2.scale_by(.5)
enemy3 = gamebox.from_image(500, 300, 'gal_enemy1.png')
enemy3.scale_by(.5)
enemy4 = gamebox.from_image(500, 400, 'gal_enemy1.png')
enemy4.scale_by(.5)
enemy5 = gamebox.from_image(500, 500, 'gal_enemy1.png')
enemy5.scale_by(.5)
enemy6 = gamebox.from_image(400, 100, 'gal_enemy.png')
enemy6.scale_by(.5)
enemy7 = gamebox.from_image(400, 200, 'gal_enemy.png')
enemy7.scale_by(.5)
enemy8 = gamebox.from_image(400, 300, 'gal_enemy.png')
enemy8.scale_by(.5)
enemy9 = gamebox.from_image(400, 400, 'gal_enemy.png')
enemy9.scale_by(.5)
enemy10 = gamebox.from_image(400, 500, 'gal_enemy.png')
enemy10.scale_by(.5)

# Some preliminary values
score = 0
rando = 0 # used in tick function (last lines of code) for generating random enemy missle firing
lives = 5
lives2 = 5
t = 0 # adds up in the tick function - used to count seconds with time
time = 0 # see t or tick function (at end/bottom of file)

# Initial Enemy Movement Speed and Direction - x and y
enemy1.yspeed = 5
enemy2.yspeed = 5
enemy3.yspeed = 5
enemy4.yspeed = 5
enemy5.yspeed = 5
enemy6.yspeed = -5
enemy7.yspeed = -5
enemy8.yspeed = -5
enemy9.yspeed = -5
enemy10.yspeed = -5
enemy1.xspeed = -1
enemy2.xspeed = -1
enemy3.xspeed = -1
enemy4.xspeed = -1
enemy5.xspeed = -1
enemy6.xspeed = -1
enemy7.xspeed = -1
enemy8.xspeed = -1
enemy9.xspeed = -1
enemy10.xspeed = -1


# Required feature: Start screen
def draw_title(keys):
    '''Title Screen - Including Title, instructions, game modes, and game authors'''
    global game_started
    global game_started2
    if pygame.K_SPACE in keys:
        game_started = True
    if pygame.K_t in keys:
        game_started2 = True
    keys.clear()

    # Stuff to draw - authors ,title, instructions, game modes, and art
    ID = gamebox.from_text(100, 20, 'Claire Coffey cc2qm', 30, 'cyan')
    ID2 = gamebox.from_text(87, 40, 'Tim Perry tbp5ny', 30, 'cyan')
    title_box = gamebox.from_text(300, 200, 'Galagish', 90, 'blue', True)
    start = gamebox.from_text(300,300, 'SPACE - Singleplayer', 40, 'white', True)
    instru = gamebox.from_text(300,340, 'WASD to move SPACE to shoot', 25, 'blue')
    start2 = gamebox.from_text(300,380, 'T - Two-player', 40, 'white', True)
    instru1 = gamebox.from_text(300, 420, 'Player1: WASD to move SPACE to shoot', 25, 'blue')
    instru2 = gamebox.from_text(300, 450, 'Player2: ARROW KEYS to move PERIOD to shoot', 25, 'blue')
    player1 = gamebox.from_text(130, 500, 'Player1: ', 25, 'blue')
    char_clone = gamebox.from_image(200,500, 'gal_ship1.png')
    char_clone.scale_by(.4)
    player2 = gamebox.from_text(330, 500, 'Player2: ', 25, 'blue')
    char2_clone = gamebox.from_image(400, 500, 'gal_ship2.png')
    char2_clone.scale_by(.4)
    rocket1 = gamebox.from_image(200, 550, 'gal_rock.png')
    rocket1.scale_by(.6)
    rocket2 = gamebox.from_image(400, 550, 'gal_rock.png')
    rocket2.scale_by(.6)

    # Drawing the aforementioned stuff
    camera.draw(rocket1)
    camera.draw(rocket2)
    camera.draw(ID)
    camera.draw(ID2)
    camera.draw(title_box)
    camera.draw(start)
    camera.draw(instru)
    camera.draw(start2)
    camera.draw(instru1)
    camera.draw(instru2)
    camera.draw(player1)
    camera.draw(char_clone)
    camera.draw(player2)
    camera.draw(char2_clone)


# 1 Player version
def draw_game(keys):
    '''1-player version - Use WASD to move and SPACE to fire
    Survive as long as you can, while eliminating enemies to increase your score
    Avoid touching enemies and their missiles(white and red) - you will lose health'''
    global score
    global char
    global lives
    global mis
    global enmis
    global enmis1
    global enmis2
    global enmis3
    global enmis4
    global rando
    global mis1
    global mis2
    global mis3
    global mis4
    global bord_bot
    global bord_left
    global bord_top
    global enemy1
    global enemy2
    global enemy3
    global enemy4
    global enemy5
    global enemy6
    global enemy7
    global enemy8
    global enemy9
    global enemy10
    global bonus_heart
    global time

    # Clearing background and setting up score:
    camera.clear('black')
    score_text = gamebox.from_text(char.x + 125, 20, 'Score: ', 30, 'white')
    score_num = gamebox.from_text(char.x + 200, 20, str(score), 50, 'black')
    score_back = gamebox.from_color(char.x + 200, 20, 'white', 60, 35)

    # Enemy Missiles - Fired from SAMS hidden off camera
    SAM = gamebox.from_color(char.x + 700, random.randint(50, 100), 'black', 10, 10)
    SAM1 = gamebox.from_color(char.x +700, random.randint(200, 250), 'black', 10, 10)
    SAM2 = gamebox.from_color(char.x + 700, random.randint(300, 350), 'black', 10, 10)
    SAM3 = gamebox.from_color(char.x + 700, random.randint(400, 450), 'black', 10, 10)
    SAM4 = gamebox.from_color(char.x + 700, random.randint(500, 550), 'black', 10, 10)

    # Draw all of our pals for this part of the game
    camera.draw(char)
    camera.draw(bonus_heart)
    camera.draw(bord_left)
    camera.draw(bord_top)
    camera.draw(bord_bot)
    camera.draw(enemy1)
    camera.draw(enemy2)
    camera.draw(enemy3)
    camera.draw(enemy4)
    camera.draw(enemy5)
    camera.draw(enemy6)
    camera.draw(enemy7)
    camera.draw(enemy8)
    camera.draw(enemy9)
    camera.draw(enemy10)
    camera.draw(score_back)
    camera.draw(score_num)
    camera.draw(SAM)
    camera.draw(SAM1)
    camera.draw(SAM2)
    camera.draw(SAM3)
    camera.draw(SAM4)
    camera.draw(score_text)

    # Optional Feature: Timer - Enemies move faster every 10 seconds - max speed after 50 seconds
    if time < 10:
        timer = gamebox.from_text(char.x - 50, 550, str(time), 30, 'white')
        camera.draw(timer)
    if time >= 10 and time < 20:
        enemy1.xspeed = -2
        enemy2.xspeed = -2
        enemy3.xspeed = -2
        enemy4.xspeed = -2
        enemy5.xspeed = -2
        enemy6.xspeed = -2
        enemy7.xspeed = -2
        enemy8.xspeed = -2
        enemy9.xspeed = -2
        enemy10.xspeed = -2
        timer = gamebox.from_text(char.x - 50, 550, str(time), 35, 'cyan')
        camera.draw(timer)
    if time >= 20 and time < 30:
        enemy1.xspeed = -3
        enemy2.xspeed = -3
        enemy3.xspeed = -3
        enemy4.xspeed = -3
        enemy5.xspeed = -3
        enemy6.xspeed = -3
        enemy7.xspeed = -3
        enemy8.xspeed = -3
        enemy9.xspeed = -3
        enemy10.xspeed = -3
        timer = gamebox.from_text(char.x - 50, 550, str(time), 40, 'green')
        camera.draw(timer)
    if time >= 30 and time < 40:
        enemy1.xspeed = -4
        enemy2.xspeed = -4
        enemy3.xspeed = -4
        enemy4.xspeed = -4
        enemy5.xspeed = -4
        enemy6.xspeed = -4
        enemy7.xspeed = -4
        enemy8.xspeed = -4
        enemy9.xspeed = -4
        enemy10.xspeed = -4
        timer = gamebox.from_text(char.x - 50, 550, str(time), 45, 'yellow')
        camera.draw(timer)
    if time >= 40 and time < 50:
        enemy1.xspeed = -6
        enemy2.xspeed = -6
        enemy3.xspeed = -6
        enemy4.xspeed = -6
        enemy5.xspeed = -6
        enemy6.xspeed = -6
        enemy7.xspeed = -6
        enemy8.xspeed = -6
        enemy9.xspeed = -6
        enemy10.xspeed = -6
        timer = gamebox.from_text(char.x - 50, 550, str(time), 50, 'orange')
        camera.draw(timer)
    if time >= 50:
        enemy1.xspeed = -8
        enemy2.xspeed = -8
        enemy3.xspeed = -8
        enemy4.xspeed = -8
        enemy5.xspeed = -8
        enemy6.xspeed = -8
        enemy7.xspeed = -8
        enemy8.xspeed = -8
        enemy9.xspeed = -8
        enemy10.xspeed = -8
        timer = gamebox.from_text(char.x - 50, 550, str(time), 55, 'red')
        camera.draw(timer)

    # Player Missiles and their collisions - it's... a lot
    if mis is not None:
        camera.draw(mis)
        mis.move_speed()
        if enemy1.touches(mis):
            mis = None
            score += 1
            enemy1.x += 700
        elif enemy2.touches(mis):
            mis = None
            score += 1
            enemy2.x += 700
        elif enemy3.touches(mis):
            mis = None
            score += 1
            enemy3.x += 700
        elif enemy4.touches(mis):
            mis = None
            score += 1
            enemy4.x += 700
        elif enemy5.touches(mis):
            mis = None
            score += 1
            enemy5.x += 700
        elif enemy6.touches(mis):
            mis = None
            score += 1
            enemy6.x += 700
        elif enemy7.touches(mis):
            mis = None
            score += 1
            enemy7.x += 700
        elif enemy8.touches(mis):
            mis = None
            score += 1
            enemy8.x += 700
        elif enemy9.touches(mis):
            mis = None
            score += 1
            enemy9.x += 700
        elif enemy10.touches(mis):
            mis = None
            score += 1
            enemy10.x += 700
        elif mis.x > camera.right:
            mis = None
    if mis1 is not None:
        camera.draw(mis1)
        mis1.move_speed()
        if enemy1.touches(mis1):
            mis1 = None
            score += 1
            enemy1.x += 700
        elif enemy2.touches(mis1):
            mis1 = None
            score += 1
            enemy2.x += 700
        elif enemy3.touches(mis1):
            mis1 = None
            score += 1
            enemy3.x += 700
        elif enemy4.touches(mis1):
            mis1 = None
            score += 1
            enemy4.x += 700
        elif enemy5.touches(mis1):
            mis1 = None
            score += 1
            enemy5.x += 700
        elif enemy6.touches(mis1):
            mis1 = None
            score += 1
            enemy6.x += 700
        elif enemy7.touches(mis1):
            mis1 = None
            score += 1
            enemy7.x += 700
        elif enemy8.touches(mis1):
            mis1 = None
            score += 1
            enemy8.x += 700
        elif enemy9.touches(mis1):
            mis1 = None
            score += 1
            enemy9.x += 700
        elif enemy10.touches(mis1):
            mis1 = None
            score += 1
            enemy10.x += 700
        elif mis1.x > camera.right:
            mis1 = None
    if mis2 is not None:
        camera.draw(mis2)
        mis2.move_speed()
        if enemy1.touches(mis2):
            mis2 = None
            score += 1
            enemy1.x += 700
        elif enemy2.touches(mis2):
            mis2 = None
            score += 1
            enemy2.x += 700
        elif enemy3.touches(mis2):
            mis2 = None
            score += 1
            enemy3.x += 700
        elif enemy4.touches(mis2):
            mis2 = None
            score += 1
            enemy4.x += 700
        elif enemy5.touches(mis2):
            mis2 = None
            score += 1
            enemy5.x += 700
        elif enemy6.touches(mis2):
            mis2 = None
            score += 1
            enemy6.x += 700
        elif enemy7.touches(mis2):
            mis2 = None
            score += 1
            enemy7.x += 700
        elif enemy8.touches(mis2):
            mis2 = None
            score += 1
            enemy8.x += 700
        elif enemy9.touches(mis2):
            mis2 = None
            score += 1
            enemy9.x += 700
        elif enemy10.touches(mis2):
            mis2 = None
            score += 1
            enemy10.x += 700
        elif mis2.x > camera.right:
            mis2 = None
    if mis3 is not None:
        camera.draw(mis3)
        mis3.move_speed()
        if enemy1.touches(mis3):
            mis3 = None
            score += 1
            enemy1.x += 700
        elif enemy2.touches(mis3):
            mis3 = None
            score += 1
            enemy2.x += 700
        elif enemy3.touches(mis3):
            mis3 = None
            score += 1
            enemy3.x += 700
        elif enemy4.touches(mis3):
            mis3 = None
            score += 1
            enemy4.x += 700
        elif enemy5.touches(mis3):
            mis3 = None
            score += 1
            enemy5.x += 700
        elif enemy6.touches(mis3):
            mis3 = None
            score += 1
            enemy6.x += 700
        elif enemy7.touches(mis3):
            mis3 = None
            score += 1
            enemy7.x += 700
        elif enemy8.touches(mis3):
            mis3 = None
            score += 1
            enemy8.x += 700
        elif enemy9.touches(mis3):
            mis3 = None
            score += 1
            enemy9.x += 700
        elif enemy10.touches(mis3):
            mis3 = None
            score += 1
            enemy10.x += 700
        elif mis3.x > camera.right:
            mis3 = None
    if mis4 is not None:
        camera.draw(mis4)
        mis4.move_speed()
        if enemy1.touches(mis4):
            mis4 = None
            score += 1
            enemy1.x += 700
        elif enemy2.touches(mis4):
            mis4 = None
            score += 1
            enemy2.x += 700
        elif enemy3.touches(mis4):
            mis4 = None
            score += 1
            enemy3.x += 700
        elif enemy4.touches(mis4):
            mis4 = None
            score += 1
            enemy4.x += 700
        elif enemy5.touches(mis4):
            mis4 = None
            score += 1
            enemy5.x += 700
        elif enemy6.touches(mis4):
            mis4 = None
            score += 1
            enemy6.x += 700
        elif enemy7.touches(mis4):
            mis4 = None
            score += 1
            enemy7.x += 700
        elif enemy8.touches(mis4):
            mis4 = None
            score += 1
            enemy8.x += 700
        elif enemy9.touches(mis4):
            mis4 = None
            score += 1
            enemy9.x += 700
        elif enemy10.touches(mis4):
            mis4 = None
            score += 1
            enemy10.x += 700
        elif mis4.x > camera.right:
            mis4 = None

    # Required Feature: User input - Firing Missiles(Player) - max 5 at a time
    if pygame.K_SPACE in keys and mis is None:
        mis = gamebox.from_image(char.x+40, char.y, 'gal_rock.png')
        mis.scale_by(.5)
        camera.draw(mis)
        mis.speedx = 20
        mis.move_speed()
        keys.clear() # stops the char from shooting 5 missiles at once, but stops movement
    if pygame.K_SPACE in keys and mis is not None and mis1 is None:
        mis1 = gamebox.from_image(char.x+26, char.y-12, 'gal_rock.png')
        mis1.scale_by(.5)
        camera.draw(mis1)
        mis1.speedx = 20
        mis1.move_speed()
        keys.clear() # stops the char from shooting 5 missiles at once, but stops movement
    if pygame.K_SPACE in keys and mis1 is not None and mis2 is None:
        mis2 = gamebox.from_image(char.x+26, char.y+11, 'gal_rock.png')
        mis2.scale_by(.5)
        camera.draw(mis2)
        mis2.speedx = 20
        mis2.move_speed()
        keys.clear() # stops the char from shooting 5 missiles at once, but stops movement
    if pygame.K_SPACE in keys and mis2 is not None and mis3 is None:
        mis3 = gamebox.from_image(char.x+18, char.y-23, 'gal_rock.png')
        mis3.scale_by(.5)
        camera.draw(mis3)
        mis3.speedx = 20
        mis3.move_speed()
        keys.clear() # stops the char from shooting 5 missiles at once, but stops movement
    if pygame.K_SPACE in keys and mis3 is not None and mis4 is None:
        mis4 = gamebox.from_image(char.x-2, char.y+22, 'gal_rock.png')
        mis4.scale_by(.5)
        camera.draw(mis3)
        mis4.speedx = 20
        mis4.move_speed()
        keys.clear() # stops the char from shooting 5 missiles at once, but stops movement

    # Enemy Missile launch parameters - rando is a randint defined in the tick function
    if enmis is None and rando == 3:
        enmis = gamebox.from_image(SAM.x, SAM.y, 'gal_rock1.png')
        enmis.scale_by(1.5)
        camera.draw(enmis)
        enmis.speedx = -14
        enmis.move_speed()
    if enmis1 is None and rando == 6:
        enmis1 = gamebox.from_image(SAM1.x, SAM1.y, 'gal_rock1.png')
        enmis1.scale_by(1.5)
        camera.draw(enmis1)
        enmis1.speedx = -14
        enmis1.move_speed()
    if enmis2 is None and rando == 9:
        enmis2 = gamebox.from_image(SAM2.x, SAM2.y, 'gal_rock1.png')
        enmis2.scale_by(1.5)
        camera.draw(enmis2)
        enmis2.speedx = -14
        enmis2.move_speed()
    if enmis3 is None and rando == 12:
        enmis3 = gamebox.from_image(SAM3.x, SAM3.y, 'gal_rock1.png')
        enmis3.scale_by(1.5)
        camera.draw(enmis3)
        enmis3.speedx = -14
        enmis3.move_speed()
    if enmis4 is None and rando == 15:
        enmis4 = gamebox.from_image(SAM4.x, SAM4.y, 'gal_rock1.png')
        enmis4.scale_by(1.5)
        camera.draw(enmis4)
        enmis4.speedx = -14
        enmis4.move_speed()

    # Enemy Missile reset parameters - collisions or off screen.left
    if enmis is not None:
        camera.draw(enmis)
        enmis.move_speed()
        if char.touches(enmis):
            enmis = None
            lives -= 1
        elif enmis.x < camera.left:
            enmis = None
    if enmis1 is not None:
        camera.draw(enmis1)
        enmis1.move_speed()
        if char.touches(enmis1):
            enmis1 = None
            lives -= 1
        elif enmis1.x < camera.left:
            enmis1 = None
    if enmis2 is not None:
        camera.draw(enmis2)
        enmis2.move_speed()
        if char.touches(enmis2):
            enmis2 = None
            lives -= 1
        elif enmis2.x < camera.left:
            enmis2 = None
    if enmis3 is not None:
        camera.draw(enmis3)
        enmis3.move_speed()
        if char.touches(enmis3):
            enmis3 = None
            lives -= 1
        elif enmis3.x < camera.left:
            enmis3 = None
    if enmis4 is not None:
        camera.draw(enmis4)
        enmis4.move_speed()
        if char.touches(enmis4):
            enmis4 = None
            lives -= 1
        elif enmis4.x < camera.left:
            enmis4 = None

    # More User Inputs (Required Feature) - Movement(player)
    if pygame.K_w in keys:
        char.y -= 10
    if pygame.K_s in keys:
        char.y += 10
    if pygame.K_d in keys:
        char.x += 10
    if pygame.K_a in keys:
        char.x -= 10

    # Optional Feature: Scrolling Level - Camera follows the player as well as the boundaries
    camera.x = char.x + 200
    bord_top.x = char.x
    bord_bot.x = char.x

    # Character Touching - Boundaries - Keeps player in the camera
    if char.touches(bord_left):
        char.move_to_stop_overlapping(bord_left)
    if char.touches(bord_top):
        char.move_to_stop_overlapping(bord_top)
    if char.touches(bord_bot):
        char.move_to_stop_overlapping(bord_bot)

    # Game Over
    if lives == 0:
        keys.clear()
        camera.clear('black')
        game_over = gamebox.from_text(char.x + 200, 300, 'Game Over', 100, 'red', True)
        camera.draw(game_over)
        camera.draw(score_back)
        camera.draw(score_num)
        camera.draw(score_text)
        gamebox.pause()

    # Keeping enemies on screen
    if enemy1.x < camera.left:
        enemy1.x += 700
    if enemy2.x < camera.left:
        enemy2.x += 700
    if enemy3.x < camera.left:
        enemy3.x += 700
    if enemy4.x < camera.left:
        enemy4.x += 700
    if enemy5.x < camera.left:
        enemy5.x += 700
    if enemy6.x < camera.left:
        enemy6.x += 700
    if enemy7.x < camera.left:
        enemy7.x += 700
    if enemy8.x < camera.left:
        enemy8.x += 700
    if enemy9.x < camera.left:
        enemy9.x += 700
    if enemy10.x < camera.left:
        enemy10.x += 700

    # Optional Feature: Enemies - Enemy Movement
        # Initial movement
    enemy1.move_speed()
    enemy2.move_speed()
    enemy3.move_speed()
    enemy4.move_speed()
    enemy5.move_speed()
    enemy6.move_speed()
    enemy7.move_speed()
    enemy8.move_speed()
    enemy9.move_speed()
    enemy10.move_speed()

        # Reverses direction at the top and bottom
    if enemy6.y == camera.top:
        enemy6.yspeed = 5
        enemy7.yspeed = 5
        enemy8.yspeed = 5
        enemy9.yspeed = 5
        enemy10.yspeed = 5
        enemy6.move_speed()
        enemy7.move_speed()
        enemy8.move_speed()
        enemy9.move_speed()
        enemy10.move_speed()
    if enemy10.y == camera.bottom:
        enemy6.yspeed = -5
        enemy7.yspeed = -5
        enemy8.yspeed = -5
        enemy9.yspeed = -5
        enemy10.yspeed = -5
        enemy6.move_speed()
        enemy7.move_speed()
        enemy8.move_speed()
        enemy9.move_speed()
        enemy10.move_speed()
    if enemy1.y == camera.top:
        enemy1.yspeed = 5
        enemy2.yspeed = 5
        enemy3.yspeed = 5
        enemy4.yspeed = 5
        enemy5.yspeed = 5
        enemy1.move_speed()
        enemy2.move_speed()
        enemy3.move_speed()
        enemy4.move_speed()
        enemy5.move_speed()
    if enemy5.y == camera.bottom:
        enemy1.yspeed = -5
        enemy2.yspeed = -5
        enemy3.yspeed = -5
        enemy4.yspeed = -5
        enemy5.yspeed = -5
        enemy1.move_speed()
        enemy2.move_speed()
        enemy3.move_speed()
        enemy4.move_speed()
        enemy5.move_speed()

    # Character touching enemy - nearly instantly takes all the player's lives:
    if char.touches(enemy1):
        lives -= 1
    if char.touches(enemy2):
        lives -= 1
    if char.touches(enemy3):
        lives -= 1
    if char.touches(enemy4):
        lives -= 1
    if char.touches(enemy5):
        lives -= 1
    if char.touches(enemy6):
        lives -= 1
    if char.touches(enemy7):
        lives -= 1
    if char.touches(enemy8):
        lives -= 1
    if char.touches(enemy9):
        lives -= 1
    if char.touches(enemy10):
        lives -= 1

    # Optional Feature: Health Meter - Health System:
    if lives == 5:
        heart1 = gamebox.from_image(char.x, 550, 'gal_heart.png')
        heart1.scale_by(.3)
        heart2 = gamebox.from_image(char.x + 30, 550, 'gal_heart.png')
        heart2.scale_by(.3)
        heart3 = gamebox.from_image(char.x + 60, 550, 'gal_heart.png')
        heart3.scale_by(.3)
        heart4 = gamebox.from_image(char.x + 90, 550, 'gal_heart.png')
        heart4.scale_by(.3)
        heart5 = gamebox.from_image(char.x + 120, 550, 'gal_heart.png')
        heart5.scale_by(.3)
        camera.draw(heart1)
        camera.draw(heart2)
        camera.draw(heart3)
        camera.draw(heart4)
        camera.draw(heart5)
    if lives == 4:
        heart1 = gamebox.from_image(char.x, 550, 'gal_heart.png')
        heart1.scale_by(.3)
        heart2 = gamebox.from_image(char.x + 30, 550, 'gal_heart.png')
        heart2.scale_by(.3)
        heart3 = gamebox.from_image(char.x + 60, 550, 'gal_heart.png')
        heart3.scale_by(.3)
        heart4 = gamebox.from_image(char.x + 90, 550, 'gal_heart.png')
        heart4.scale_by(.3)
        camera.draw(heart1)
        camera.draw(heart2)
        camera.draw(heart3)
        camera.draw(heart4)
    if lives == 3:
        heart1 = gamebox.from_image(char.x, 550, 'gal_heart.png')
        heart1.scale_by(.3)
        heart2 = gamebox.from_image(char.x + 30, 550, 'gal_heart.png')
        heart2.scale_by(.3)
        heart3 = gamebox.from_image(char.x + 60, 550, 'gal_heart.png')
        heart3.scale_by(.3)
        camera.draw(heart1)
        camera.draw(heart2)
        camera.draw(heart3)
    if lives == 2:
        heart1 = gamebox.from_image(char.x, 550, 'gal_heart.png')
        heart1.scale_by(.3)
        heart2 = gamebox.from_image(char.x + 30, 550, 'gal_heart.png')
        heart2.scale_by(.3)
        camera.draw(heart1)
        camera.draw(heart2)
    if lives == 1:
        heart1 = gamebox.from_image(char.x, 550, 'gal_heart.png')
        heart1.scale_by(.3)
        camera.draw(heart1)

    # Optional Feature: Bonus Health/Collectible - gives score if full health (5 hearts/lives)
    if char.touches(bonus_heart):
        bonus_heart = gamebox.from_image(char.x + 800, random.randint(50, 550), 'gal_heart.png')
        bonus_heart.scale_by(.2)
        camera.draw(bonus_heart)
        if lives < 5:
            lives += 1
        else:
            score += 5
    elif bonus_heart.x < camera.left:
        bonus_heart = gamebox.from_image(char.x + 800, random.randint(50, 550), 'gal_heart.png')
        bonus_heart.scale_by(.2)
        camera.draw(bonus_heart)


# Optional Feature: Two players simultaneously
def draw_game2(keys):
    '''two-player version:
    Player1 - WASD to move, SPACE to shoot
    Player2 -  ARROW KEYS to move, PERIOD to shoot
    If either player's health (hearts) get to zero, the game ends
    Shoot enemies, and don't let them or their missiles touch you, to increase your score
    Survive as long as you can'''
    global score
    global char1
    global char2
    global lives
    global lives2
    global mis_1
    global mis_2
    global mis_3
    global mis_4
    global mis_5
    global mis
    global mis2
    global enmis
    global enmis1
    global enmis2
    global enmis3
    global enmis4
    global rando
    global mis1
    global mis2
    global mis3
    global mis4
    global bord_bot
    global bord_left
    global bord_top
    global enemy1
    global enemy2
    global enemy3
    global enemy4
    global enemy5
    global enemy6
    global enemy7
    global enemy8
    global enemy9
    global enemy10
    global bonus_heart
    global time

    # Clear camera and setup score graphics
    camera.clear('black')
    score_num = gamebox.from_text(char1.x + 200, 20, str(score), 50, 'black')
    score_back = gamebox.from_color(char1.x + 200, 20, 'white', 60, 35)
    score_text = gamebox.from_text(char1.x + 125, 20, 'Score: ', 30, 'white')

    # Enemy Missiles - Fired from SAMS hidden off camera
    SAM = gamebox.from_color(char1.x + 700, random.randint(50, 100), 'black', 10, 10)
    SAM1 = gamebox.from_color(char1.x + 700, random.randint(200, 250), 'black', 10, 10)
    SAM2 = gamebox.from_color(char1.x + 700, random.randint(300, 350), 'black', 10, 10)
    SAM3 = gamebox.from_color(char1.x + 700, random.randint(400, 450), 'black', 10, 10)
    SAM4 = gamebox.from_color(char1.x + 700, random.randint(500, 550), 'black', 10, 10)

    # Draw all of our pals for this part of the game
    camera.draw(char1)
    camera.draw(char2)
    camera.draw(bonus_heart)
    camera.draw(bord_left)
    camera.draw(bord_top)
    camera.draw(bord_bot)
    camera.draw(enemy1)
    camera.draw(enemy2)
    camera.draw(enemy3)
    camera.draw(enemy4)
    camera.draw(enemy5)
    camera.draw(enemy6)
    camera.draw(enemy7)
    camera.draw(enemy8)
    camera.draw(enemy9)
    camera.draw(enemy10)
    camera.draw(score_back)
    camera.draw(score_num)
    camera.draw(SAM)
    camera.draw(SAM1)
    camera.draw(SAM2)
    camera.draw(SAM3)
    camera.draw(SAM4)
    camera.draw(score_text)

    # Optional Feature: Timer - Enemies move faster every 10 seconds - max speed after 50 seconds
    if time < 10:
        timer = gamebox.from_text(char1.x - 50, 550, str(time), 30, 'white')
        camera.draw(timer)
    if time >= 10 and time < 20:
        enemy1.xspeed = -2
        enemy2.xspeed = -2
        enemy3.xspeed = -2
        enemy4.xspeed = -2
        enemy5.xspeed = -2
        enemy6.xspeed = -2
        enemy7.xspeed = -2
        enemy8.xspeed = -2
        enemy9.xspeed = -2
        enemy10.xspeed = -2
        timer = gamebox.from_text(char1.x - 50, 550, str(time), 35, 'cyan')
        camera.draw(timer)
    if time >= 20 and time < 30:
        enemy1.xspeed = -3
        enemy2.xspeed = -3
        enemy3.xspeed = -3
        enemy4.xspeed = -3
        enemy5.xspeed = -3
        enemy6.xspeed = -3
        enemy7.xspeed = -3
        enemy8.xspeed = -3
        enemy9.xspeed = -3
        enemy10.xspeed = -3
        timer = gamebox.from_text(char1.x - 50, 550, str(time), 40, 'green')
        camera.draw(timer)
    if time >= 30 and time < 40:
        enemy1.xspeed = -4
        enemy2.xspeed = -4
        enemy3.xspeed = -4
        enemy4.xspeed = -4
        enemy5.xspeed = -4
        enemy6.xspeed = -4
        enemy7.xspeed = -4
        enemy8.xspeed = -4
        enemy9.xspeed = -4
        enemy10.xspeed = -4
        timer = gamebox.from_text(char1.x - 50, 550, str(time), 45, 'yellow')
        camera.draw(timer)
    if time >= 40 and time < 50:
        enemy1.xspeed = -6
        enemy2.xspeed = -6
        enemy3.xspeed = -6
        enemy4.xspeed = -6
        enemy5.xspeed = -6
        enemy6.xspeed = -6
        enemy7.xspeed = -6
        enemy8.xspeed = -6
        enemy9.xspeed = -6
        enemy10.xspeed = -6
        timer = gamebox.from_text(char1.x - 50, 550, str(time), 50, 'orange')
        camera.draw(timer)
    if time >= 50:
        enemy1.xspeed = -8
        enemy2.xspeed = -8
        enemy3.xspeed = -8
        enemy4.xspeed = -8
        enemy5.xspeed = -8
        enemy6.xspeed = -8
        enemy7.xspeed = -8
        enemy8.xspeed = -8
        enemy9.xspeed = -8
        enemy10.xspeed = -8
        timer = gamebox.from_text(char1.x - 50, 550, str(time), 55, 'red')
        camera.draw(timer)

    # Player Missiles and their collisions - it's... even more than before
    if mis is not None:
        camera.draw(mis)
        mis.move_speed()
        if enemy1.touches(mis):
            mis = None
            score += 1
            enemy1.x += 700
        elif enemy2.touches(mis):
            mis = None
            score += 1
            enemy2.x += 700
        elif enemy3.touches(mis):
            mis = None
            score += 1
            enemy3.x += 700
        elif enemy4.touches(mis):
            mis = None
            score += 1
            enemy4.x += 700
        elif enemy5.touches(mis):
            mis = None
            score += 1
            enemy5.x += 700
        elif enemy6.touches(mis):
            mis = None
            score += 1
            enemy6.x += 700
        elif enemy7.touches(mis):
            mis = None
            score += 1
            enemy7.x += 700
        elif enemy8.touches(mis):
            mis = None
            score += 1
            enemy8.x += 700
        elif enemy9.touches(mis):
            mis = None
            score += 1
            enemy9.x += 700
        elif enemy10.touches(mis):
            mis = None
            score += 1
            enemy10.x += 700
        elif mis.x > camera.right:
            mis = None
    if mis1 is not None:
        camera.draw(mis1)
        mis1.move_speed()
        if enemy1.touches(mis1):
            mis1 = None
            score += 1
            enemy1.x += 700
        elif enemy2.touches(mis1):
            mis1 = None
            score += 1
            enemy2.x += 700
        elif enemy3.touches(mis1):
            mis1 = None
            score += 1
            enemy3.x += 700
        elif enemy4.touches(mis1):
            mis1 = None
            score += 1
            enemy4.x += 700
        elif enemy5.touches(mis1):
            mis1 = None
            score += 1
            enemy5.x += 700
        elif enemy6.touches(mis1):
            mis1 = None
            score += 1
            enemy6.x += 700
        elif enemy7.touches(mis1):
            mis1 = None
            score += 1
            enemy7.x += 700
        elif enemy8.touches(mis1):
            mis1 = None
            score += 1
            enemy8.x += 700
        elif enemy9.touches(mis1):
            mis1 = None
            score += 1
            enemy9.x += 700
        elif enemy10.touches(mis1):
            mis1 = None
            score += 1
            enemy10.x += 700
        elif mis1.x > camera.right:
            mis1 = None
    if mis2 is not None:
        camera.draw(mis2)
        mis2.move_speed()
        if enemy1.touches(mis2):
            mis2 = None
            score += 1
            enemy1.x += 700
        elif enemy2.touches(mis2):
            mis2 = None
            score += 1
            enemy2.x += 700
        elif enemy3.touches(mis2):
            mis2 = None
            score += 1
            enemy3.x += 700
        elif enemy4.touches(mis2):
            mis2 = None
            score += 1
            enemy4.x += 700
        elif enemy5.touches(mis2):
            mis2 = None
            score += 1
            enemy5.x += 700
        elif enemy6.touches(mis2):
            mis2 = None
            score += 1
            enemy6.x += 700
        elif enemy7.touches(mis2):
            mis2 = None
            score += 1
            enemy7.x += 700
        elif enemy8.touches(mis2):
            mis2 = None
            score += 1
            enemy8.x += 700
        elif enemy9.touches(mis2):
            mis2 = None
            score += 1
            enemy9.x += 700
        elif enemy10.touches(mis2):
            mis2 = None
            score += 1
            enemy10.x += 700
        elif mis2.x > camera.right:
            mis2 = None
    if mis3 is not None:
        camera.draw(mis3)
        mis3.move_speed()
        if enemy1.touches(mis3):
            mis3 = None
            score += 1
            enemy1.x += 700
        elif enemy2.touches(mis3):
            mis3 = None
            score += 1
            enemy2.x += 700
        elif enemy3.touches(mis3):
            mis3 = None
            score += 1
            enemy3.x += 700
        elif enemy4.touches(mis3):
            mis3 = None
            score += 1
            enemy4.x += 700
        elif enemy5.touches(mis3):
            mis3 = None
            score += 1
            enemy5.x += 700
        elif enemy6.touches(mis3):
            mis3 = None
            score += 1
            enemy6.x += 700
        elif enemy7.touches(mis3):
            mis3 = None
            score += 1
            enemy7.x += 700
        elif enemy8.touches(mis3):
            mis3 = None
            score += 1
            enemy8.x += 700
        elif enemy9.touches(mis3):
            mis3 = None
            score += 1
            enemy9.x += 700
        elif enemy10.touches(mis3):
            mis3 = None
            score += 1
            enemy10.x += 700
        elif mis3.x > camera.right:
            mis3 = None
    if mis4 is not None:
        camera.draw(mis4)
        mis4.move_speed()
        if enemy1.touches(mis4):
            mis4 = None
            score += 1
            enemy1.x += 700
        elif enemy2.touches(mis4):
            mis4 = None
            score += 1
            enemy2.x += 700
        elif enemy3.touches(mis4):
            mis4 = None
            score += 1
            enemy3.x += 700
        elif enemy4.touches(mis4):
            mis4 = None
            score += 1
            enemy4.x += 700
        elif enemy5.touches(mis4):
            mis4 = None
            score += 1
            enemy5.x += 700
        elif enemy6.touches(mis4):
            mis4 = None
            score += 1
            enemy6.x += 700
        elif enemy7.touches(mis4):
            mis4 = None
            score += 1
            enemy7.x += 700
        elif enemy8.touches(mis4):
            mis4 = None
            score += 1
            enemy8.x += 700
        elif enemy9.touches(mis4):
            mis4 = None
            score += 1
            enemy9.x += 700
        elif enemy10.touches(mis4):
            mis4 = None
            score += 1
            enemy10.x += 700
        elif mis4.x > camera.right:
            mis4 = None

        # Player 2's missiles
    if mis_1 is not None:
        camera.draw(mis_1)
        mis_1.move_speed()
        if enemy1.touches(mis_1):
            mis_1 = None
            score += 1
            enemy1.x += 700
        elif enemy2.touches(mis_1):
            mis_1 = None
            score += 1
            enemy2.x += 700
        elif enemy3.touches(mis_1):
            mis_1 = None
            score += 1
            enemy3.x += 700
        elif enemy4.touches(mis_1):
            mis_1 = None
            score += 1
            enemy4.x += 700
        elif enemy5.touches(mis_1):
            mis_1 = None
            score += 1
            enemy5.x += 700
        elif enemy6.touches(mis_1):
            mis_1 = None
            score += 1
            enemy6.x += 700
        elif enemy7.touches(mis_1):
            mis_1 = None
            score += 1
            enemy7.x += 700
        elif enemy8.touches(mis_1):
            mis_1 = None
            score += 1
            enemy8.x += 700
        elif enemy9.touches(mis_1):
            mis_1 = None
            score += 1
            enemy9.x += 700
        elif enemy10.touches(mis_1):
            mis_1 = None
            score += 1
            enemy10.x += 700
        elif mis_1.x > camera.right:
            mis_1 = None
    if mis_2 is not None:
        camera.draw(mis_2)
        mis_2.move_speed()
        if enemy1.touches(mis_2):
            mis_2 = None
            score += 1
            enemy1.x += 700
        elif enemy2.touches(mis_2):
            mis_2 = None
            score += 1
            enemy2.x += 700
        elif enemy3.touches(mis_2):
            mis_2 = None
            score += 1
            enemy3.x += 700
        elif enemy4.touches(mis_2):
            mis_2 = None
            score += 1
            enemy4.x += 700
        elif enemy5.touches(mis_2):
            mis_2 = None
            score += 1
            enemy5.x += 700
        elif enemy6.touches(mis_2):
            mis_2 = None
            score += 1
            enemy6.x += 700
        elif enemy7.touches(mis_2):
            mis_2 = None
            score += 1
            enemy7.x += 700
        elif enemy8.touches(mis_2):
            mis_2 = None
            score += 1
            enemy8.x += 700
        elif enemy9.touches(mis_2):
            mis_2 = None
            score += 1
            enemy9.x += 700
        elif enemy10.touches(mis_2):
            mis_2 = None
            score += 1
            enemy10.x += 700
        elif mis_2.x > camera.right:
            mis_2 = None
    if mis_3 is not None:
        camera.draw(mis_3)
        mis_3.move_speed()
        if enemy1.touches(mis_3):
            mis_3 = None
            score += 1
            enemy1.x += 700
        elif enemy2.touches(mis_3):
            mis_3 = None
            score += 1
            enemy2.x += 700
        elif enemy3.touches(mis_3):
            mis_3 = None
            score += 1
            enemy3.x += 700
        elif enemy4.touches(mis_3):
            mis_3 = None
            score += 1
            enemy4.x += 700
        elif enemy5.touches(mis_3):
            mis_3 = None
            score += 1
            enemy5.x += 700
        elif enemy6.touches(mis_3):
            mis_3 = None
            score += 1
            enemy6.x += 700
        elif enemy7.touches(mis_3):
            mis_3 = None
            score += 1
            enemy7.x += 700
        elif enemy8.touches(mis_3):
            mis_3 = None
            score += 1
            enemy8.x += 700
        elif enemy9.touches(mis_3):
            mis_3 = None
            score += 1
            enemy9.x += 700
        elif enemy10.touches(mis_3):
            mis_3 = None
            score += 1
            enemy10.x += 700
        elif mis_3.x > camera.right:
            mis_3 = None
    if mis_4 is not None:
        camera.draw(mis_4)
        mis_4.move_speed()
        if enemy1.touches(mis_4):
            mis_4 = None
            score += 1
            enemy1.x += 700
        elif enemy2.touches(mis_4):
            mis_4 = None
            score += 1
            enemy2.x += 700
        elif enemy3.touches(mis_4):
            mis_4 = None
            score += 1
            enemy3.x += 700
        elif enemy4.touches(mis_4):
            mis_4 = None
            score += 1
            enemy4.x += 700
        elif enemy5.touches(mis_4):
            mis_4 = None
            score += 1
            enemy5.x += 700
        elif enemy6.touches(mis_4):
            mis_4 = None
            score += 1
            enemy6.x += 700
        elif enemy7.touches(mis_4):
            mis_4 = None
            score += 1
            enemy7.x += 700
        elif enemy8.touches(mis_4):
            mis_4 = None
            score += 1
            enemy8.x += 700
        elif enemy9.touches(mis_4):
            mis_4 = None
            score += 1
            enemy9.x += 700
        elif enemy10.touches(mis_4):
            mis_4 = None
            score += 1
            enemy10.x += 700
        elif mis_4.x > camera.right:
            mis_4 = None
    if mis_5 is not None:
        camera.draw(mis_5)
        mis_5.move_speed()
        if enemy1.touches(mis_5):
            mis_5 = None
            score += 1
            enemy1.x += 700
        elif enemy2.touches(mis_5):
            mis_5 = None
            score += 1
            enemy2.x += 700
        elif enemy3.touches(mis_5):
            mis_5 = None
            score += 1
            enemy3.x += 700
        elif enemy4.touches(mis_5):
            mis_5 = None
            score += 1
            enemy4.x += 700
        elif enemy5.touches(mis_5):
            mis_5 = None
            score += 1
            enemy5.x += 700
        elif enemy6.touches(mis_5):
            mis_5 = None
            score += 1
            enemy6.x += 700
        elif enemy7.touches(mis_5):
            mis_5 = None
            score += 1
            enemy7.x += 700
        elif enemy8.touches(mis_5):
            mis_5 = None
            score += 1
            enemy8.x += 700
        elif enemy9.touches(mis_5):
            mis_5 = None
            score += 1
            enemy9.x += 700
        elif enemy10.touches(mis_5):
            mis_5 = None
            score += 1
            enemy10.x += 700
        elif mis_5.x > camera.right:
            mis_5 = None

    # Required Feature: User Inputs: Firing Missiles(Players) - max 5 at a time(each)
        # Player 1's inputs
    if pygame.K_SPACE in keys and mis is None:
        mis = gamebox.from_image(char1.x+40, char1.y, 'gal_rock.png')
        mis.scale_by(.5)
        camera.draw(mis)
        mis.speedx = 20
        mis.move_speed()
        keys.clear()
    if pygame.K_SPACE in keys and mis is not None and mis1 is None:
        mis1 = gamebox.from_image(char1.x+26, char1.y-12, 'gal_rock.png')
        mis1.scale_by(.5)
        camera.draw(mis1)
        mis1.speedx = 20
        mis1.move_speed()
        keys.clear()
    if pygame.K_SPACE in keys and mis1 is not None and mis2 is None:
        mis2 = gamebox.from_image(char1.x+26, char1.y+11, 'gal_rock.png')
        mis2.scale_by(.5)
        camera.draw(mis2)
        mis2.speedx = 20
        mis2.move_speed()
        keys.clear()
    if pygame.K_SPACE in keys and mis2 is not None and mis3 is None:
        mis3 = gamebox.from_image(char1.x+18, char1.y-23, 'gal_rock.png')
        mis3.scale_by(.5)
        camera.draw(mis3)
        mis3.speedx = 20
        mis3.move_speed()
        keys.clear()
    if pygame.K_SPACE in keys and mis3 is not None and mis4 is None:
        mis4 = gamebox.from_image(char1.x-2, char1.y+22, 'gal_rock.png')
        mis4.scale_by(.5)
        camera.draw(mis3)
        mis4.speedx = 20
        mis4.move_speed()
        keys.clear()

        # Player 2's inputs
    if pygame.K_PERIOD in keys and mis_1 is None:
        mis_1 = gamebox.from_image(char2.x+40, char2.y, 'gal_rock.png')
        mis_1.scale_by(.5)
        camera.draw(mis_1)
        mis_1.speedx = 20
        mis_1.move_speed()
        keys.clear()
    if pygame.K_PERIOD in keys and mis_1 is not None and mis_2 is None:
        mis_2 = gamebox.from_image(char2.x+26, char2.y-12, 'gal_rock.png')
        mis_2.scale_by(.5)
        camera.draw(mis_2)
        mis_2.speedx = 20
        mis_2.move_speed()
        keys.clear()
    if pygame.K_PERIOD in keys and mis_2 is not None and mis_3 is None:
        mis_3 = gamebox.from_image(char2.x+26, char2.y+11, 'gal_rock.png')
        mis_3.scale_by(.5)
        camera.draw(mis_3)
        mis_3.speedx = 20
        mis_3.move_speed()
        keys.clear()
    if pygame.K_PERIOD in keys and mis_3 is not None and mis_4 is None:
        mis_4 = gamebox.from_image(char2.x+18, char2.y-23, 'gal_rock.png')
        mis_4.scale_by(.5)
        camera.draw(mis_4)
        mis_4.speedx = 20
        mis_4.move_speed()
        keys.clear()
    if pygame.K_PERIOD in keys and mis_4 is not None and mis_5 is None:
        mis_5 = gamebox.from_image(char2.x+18, char2.y+21, 'gal_rock.png')
        mis_5.scale_by(.5)
        camera.draw(mis_5)
        mis_5.speedx = 20
        mis_5.move_speed()
        keys.clear()

    # Enemy Missile launch parameters - rando is a randint defined in the tick function
    if enmis is None and rando == 3:
        enmis = gamebox.from_image(SAM.x, SAM.y, 'gal_rock1.png')
        enmis.scale_by(1.5)
        camera.draw(enmis)
        enmis.speedx = -14
        enmis.move_speed()
    if enmis1 is None and rando == 6:
        enmis1 = gamebox.from_image(SAM1.x, SAM1.y, 'gal_rock1.png')
        enmis1.scale_by(1.5)
        camera.draw(enmis1)
        enmis1.speedx = -14
        enmis1.move_speed()
    if enmis2 is None and rando == 9:
        enmis2 = gamebox.from_image(SAM2.x, SAM2.y, 'gal_rock1.png')
        enmis2.scale_by(1.5)
        camera.draw(enmis2)
        enmis2.speedx = -14
        enmis2.move_speed()
    if enmis3 is None and rando == 12:
        enmis3 = gamebox.from_image(SAM3.x, SAM3.y, 'gal_rock1.png')
        enmis3.scale_by(1.5)
        camera.draw(enmis3)
        enmis3.speedx = -14
        enmis3.move_speed()
    if enmis4 is None and rando == 15:
        enmis4 = gamebox.from_image(SAM4.x, SAM4.y, 'gal_rock1.png')
        enmis4.scale_by(1.5)
        camera.draw(enmis4)
        enmis4.speedx = -14
        enmis4.move_speed()

    # Enemy Missile reset parameters - collisions or off screen.left
    if enmis is not None:
        camera.draw(enmis)
        enmis.move_speed()
        if char1.touches(enmis):
            enmis = None
            lives -= 1
        elif char2.touches(enmis):
            enmis = None
            lives2 -= 1
        elif enmis.x < camera.left:
            enmis = None
    if enmis1 is not None:
        camera.draw(enmis1)
        enmis1.move_speed()
        if char1.touches(enmis1):
            enmis1 = None
            lives -= 1
        elif char2.touches(enmis1):
            enmis1 = None
            lives2 -= 1
        elif enmis1.x < camera.left:
            enmis1 = None
    if enmis2 is not None:
        camera.draw(enmis2)
        enmis2.move_speed()
        if char1.touches(enmis2):
            enmis2 = None
            lives -= 1
        elif char2.touches(enmis2):
            enmis2 = None
            lives2 -= 1
        elif enmis2.x < camera.left:
            enmis2 = None
    if enmis3 is not None:
        camera.draw(enmis3)
        enmis3.move_speed()
        if char1.touches(enmis3):
            enmis3 = None
            lives -= 1
        elif char2.touches(enmis3):
            enmis3 = None
            lives2 -= 1
        elif enmis3.x < camera.left:
            enmis3 = None
    if enmis4 is not None:
        camera.draw(enmis4)
        enmis4.move_speed()
        if char1.touches(enmis4):
            enmis4 = None
            lives -= 1
        elif char2.touches(enmis4):
            enmis4 = None
            lives2 -= 1
        elif enmis4.x < camera.left:
            enmis4 = None

    # Require Feature: User input - Movement(players)
        # Player1
    if pygame.K_w in keys:
        char1.y -= 10
    if pygame.K_s in keys:
        char1.y += 10
    if pygame.K_d in keys:
        char1.x += 10
    if pygame.K_a in keys:
        char1.x -= 10

        # Player2
    if pygame.K_UP in keys:
        char2.y -= 10
    if pygame.K_DOWN in keys:
        char2.y += 10
    if pygame.K_RIGHT in keys:
        char2.x += 10
    if pygame.K_LEFT in keys:
        char2.x -= 10

    # Camera and boundaries follow char1
    camera.x = char1.x + 200
    bord_top.x = char1.x
    bord_bot.x = char1.x
    bord_left.x = char1.x -200 # left edge set by char1's position

    # character Touching - Boundaries - Keeps player in the camera
    if char1.touches(bord_left):
        char1.move_to_stop_overlapping(bord_left)
    if char1.touches(bord_top):
        char1.move_to_stop_overlapping(bord_top)
    if char1.touches(bord_bot):
        char1.move_to_stop_overlapping(bord_bot)
    if char2.touches(bord_left):
        char2.move_to_stop_overlapping(bord_left)
    if char2.touches(bord_top):
        char2.move_to_stop_overlapping(bord_top)
    if char2.touches(bord_bot):
        char2.move_to_stop_overlapping(bord_bot)

    # Optional Feature: Enemies - Enemy Movement
        # Initial movement
    enemy1.move_speed()
    enemy2.move_speed()
    enemy3.move_speed()
    enemy4.move_speed()
    enemy5.move_speed()
    enemy6.move_speed()
    enemy7.move_speed()
    enemy8.move_speed()
    enemy9.move_speed()
    enemy10.move_speed()

        # Reverses direction at the top and bottom
    if enemy6.y == camera.top:
        enemy6.yspeed = 5
        enemy7.yspeed = 5
        enemy8.yspeed = 5
        enemy9.yspeed = 5
        enemy10.yspeed = 5
        enemy6.move_speed()
        enemy7.move_speed()
        enemy8.move_speed()
        enemy9.move_speed()
        enemy10.move_speed()
    if enemy10.y == camera.bottom:
        enemy6.yspeed = -5
        enemy7.yspeed = -5
        enemy8.yspeed = -5
        enemy9.yspeed = -5
        enemy10.yspeed = -5
        enemy6.move_speed()
        enemy7.move_speed()
        enemy8.move_speed()
        enemy9.move_speed()
        enemy10.move_speed()
    if enemy1.y == camera.top:
        enemy1.yspeed = 5
        enemy2.yspeed = 5
        enemy3.yspeed = 5
        enemy4.yspeed = 5
        enemy5.yspeed = 5
        enemy1.move_speed()
        enemy2.move_speed()
        enemy3.move_speed()
        enemy4.move_speed()
        enemy5.move_speed()
    if enemy5.y == camera.bottom:
        enemy1.yspeed = -5
        enemy2.yspeed = -5
        enemy3.yspeed = -5
        enemy4.yspeed = -5
        enemy5.yspeed = -5
        enemy1.move_speed()
        enemy2.move_speed()
        enemy3.move_speed()
        enemy4.move_speed()
        enemy5.move_speed()

    # Stop characters' overlap
    if char1.touches(char2):
        char1.move_to_stop_overlapping(char2)
    if char2.touches(char1):
        char2.move_to_stop_overlapping(char1)

        # Character touching enemy:
    if char1.touches(enemy1):
        lives -= 1
    if char1.touches(enemy2):
        lives -= 1
    if char1.touches(enemy3):
        lives -= 1
    if char1.touches(enemy4):
        lives -= 1
    if char1.touches(enemy5):
        lives -= 1
    if char1.touches(enemy6):
        lives -= 1
    if char1.touches(enemy7):
        lives -= 1
    if char1.touches(enemy8):
        lives -= 1
    if char1.touches(enemy9):
        lives -= 1
    if char1.touches(enemy10):
        lives -= 1
    if char2.touches(enemy1):
        lives2 -= 1
    if char2.touches(enemy2):
        lives2 -= 1
    if char2.touches(enemy3):
        lives2 -= 1
    if char2.touches(enemy4):
        lives2 -= 1
    if char2.touches(enemy5):
        lives2 -= 1
    if char2.touches(enemy6):
        lives2 -= 1
    if char2.touches(enemy7):
        lives2 -= 1
    if char2.touches(enemy8):
        lives2 -= 1
    if char2.touches(enemy9):
        lives2 -= 1
    if char2.touches(enemy10):
        lives2 -= 1

    # Keeping enemies on screen
    if enemy1.x < camera.left:
        enemy1.x += 700
    if enemy2.x < camera.left:
        enemy2.x += 700
    if enemy3.x < camera.left:
        enemy3.x += 700
    if enemy4.x < camera.left:
        enemy4.x += 700
    if enemy5.x < camera.left:
        enemy5.x += 700
    if enemy6.x < camera.left:
        enemy6.x += 700
    if enemy7.x < camera.left:
        enemy7.x += 700
    if enemy8.x < camera.left:
        enemy8.x += 700
    if enemy9.x < camera.left:
        enemy9.x += 700
    if enemy10.x < camera.left:
        enemy10.x += 700

    # Optional Feature: Health meter - Health System for both players:
    if lives == 5:
        heart1 = gamebox.from_image(char1.x, 50, 'gal_heart.png')
        heart1.scale_by(.3)
        heart2 = gamebox.from_image(char1.x + 30, 50, 'gal_heart.png')
        heart2.scale_by(.3)
        heart3 = gamebox.from_image(char1.x + 60, 50, 'gal_heart.png')
        heart3.scale_by(.3)
        heart4 = gamebox.from_image(char1.x + 90, 50, 'gal_heart.png')
        heart4.scale_by(.3)
        heart5 = gamebox.from_image(char1.x + 120, 50, 'gal_heart.png')
        heart5.scale_by(.3)
        camera.draw(heart1)
        camera.draw(heart2)
        camera.draw(heart3)
        camera.draw(heart4)
        camera.draw(heart5)
    if lives == 4:
        heart1 = gamebox.from_image(char1.x, 50, 'gal_heart.png')
        heart1.scale_by(.3)
        heart2 = gamebox.from_image(char1.x + 30, 50, 'gal_heart.png')
        heart2.scale_by(.3)
        heart3 = gamebox.from_image(char1.x + 60, 50, 'gal_heart.png')
        heart3.scale_by(.3)
        heart4 = gamebox.from_image(char1.x + 90, 50, 'gal_heart.png')
        heart4.scale_by(.3)
        camera.draw(heart1)
        camera.draw(heart2)
        camera.draw(heart3)
        camera.draw(heart4)
    if lives == 3:
        heart1 = gamebox.from_image(char1.x, 50, 'gal_heart.png')
        heart1.scale_by(.3)
        heart2 = gamebox.from_image(char1.x + 30, 50, 'gal_heart.png')
        heart2.scale_by(.3)
        heart3 = gamebox.from_image(char1.x + 60, 50, 'gal_heart.png')
        heart3.scale_by(.3)
        camera.draw(heart1)
        camera.draw(heart2)
        camera.draw(heart3)
    if lives == 2:
        heart1 = gamebox.from_image(char1.x, 50, 'gal_heart.png')
        heart1.scale_by(.3)
        heart2 = gamebox.from_image(char1.x + 30, 50, 'gal_heart.png')
        heart2.scale_by(.3)
        camera.draw(heart1)
        camera.draw(heart2)
    if lives == 1:
        heart1 = gamebox.from_image(char1.x, 50, 'gal_heart.png')
        heart1.scale_by(.3)
        camera.draw(heart1)

        # Player 2 health
    if lives2 == 5:
        heart6 = gamebox.from_image(char1.x, 550, 'gal_heart.png')
        heart6.scale_by(.3)
        heart7 = gamebox.from_image(char1.x + 30, 550, 'gal_heart.png')
        heart7.scale_by(.3)
        heart8 = gamebox.from_image(char1.x + 60, 550, 'gal_heart.png')
        heart8.scale_by(.3)
        heart9 = gamebox.from_image(char1.x + 90, 550, 'gal_heart.png')
        heart9.scale_by(.3)
        heart10 = gamebox.from_image(char1.x + 120, 550, 'gal_heart.png')
        heart10.scale_by(.3)
        camera.draw(heart6)
        camera.draw(heart7)
        camera.draw(heart8)
        camera.draw(heart9)
        camera.draw(heart10)
    if lives2 == 4:
        heart6 = gamebox.from_image(char1.x, 550, 'gal_heart.png')
        heart6.scale_by(.3)
        heart7 = gamebox.from_image(char1.x + 30, 550, 'gal_heart.png')
        heart7.scale_by(.3)
        heart8 = gamebox.from_image(char1.x + 60, 550, 'gal_heart.png')
        heart8.scale_by(.3)
        heart9 = gamebox.from_image(char1.x + 90, 550, 'gal_heart.png')
        heart9.scale_by(.3)
        camera.draw(heart6)
        camera.draw(heart7)
        camera.draw(heart8)
        camera.draw(heart9)
    if lives2 == 3:
        heart6 = gamebox.from_image(char1.x, 550, 'gal_heart.png')
        heart6.scale_by(.3)
        heart7 = gamebox.from_image(char1.x + 30, 550, 'gal_heart.png')
        heart7.scale_by(.3)
        heart8 = gamebox.from_image(char1.x + 60, 550, 'gal_heart.png')
        heart8.scale_by(.3)
        camera.draw(heart6)
        camera.draw(heart7)
        camera.draw(heart8)
    if lives2 == 2:
        heart6 = gamebox.from_image(char1.x, 550, 'gal_heart.png')
        heart6.scale_by(.3)
        heart7 = gamebox.from_image(char1.x + 30, 550, 'gal_heart.png')
        heart7.scale_by(.3)
        camera.draw(heart6)
        camera.draw(heart7)
    if lives2 == 1:
        heart6 = gamebox.from_image(char1.x, 550, 'gal_heart.png')
        heart6.scale_by(.3)
        camera.draw(heart6)

    # Optional Feature: Bonus Health/Collectible:
    if char1.touches(bonus_heart):
        bonus_heart = gamebox.from_image(char1.x + 800, random.randint(50, 550), 'gal_heart.png')
        bonus_heart.scale_by(.2)
        camera.draw(bonus_heart)
        if lives < 5:
            lives += 1
        else:
            score += 5
    elif char2.touches(bonus_heart):
        bonus_heart = gamebox.from_image(char2.x + 800, random.randint(50, 550), 'gal_heart.png')
        bonus_heart.scale_by(.2)
        camera.draw(bonus_heart)
        if lives < 5:
            lives2 += 1
        else:
            score += 5
    elif bonus_heart.x < camera.left:
        bonus_heart = gamebox.from_image(char1.x + 800, random.randint(50, 550), 'gal_heart.png')
        bonus_heart.scale_by(.2)
        camera.draw(bonus_heart)

    # Game Over
    if lives == 0 or lives2 == 0:
        keys.clear()
        camera.clear('black')
        game_over = gamebox.from_text(char1.x + 200, 300, 'Game Over', 100, 'red', True)
        camera.draw(game_over)
        camera.draw(score_back)
        camera.draw(score_num)
        camera.draw(score_text)
        gamebox.pause()


def tick(keys):
    '''
    Makes the game possible along with the rando, time, and t variables
    :rando: generates a random number, which can allow enemies to fire their missiles - see # Enemy missiles
    :t: every iteration of the tick function adds one to t
    :time: once t = 15, time += 1 - i.e. tracks time in the game, 15 ticks = 1 second
    '''
    global rando
    global time
    global t
    if not game_started and not game_started2:
        draw_title(keys)
    if game_started:
        draw_game(keys)
        t += 1
        if t % 15 == 0:
            time += 1
    if game_started2:
        draw_game2(keys)
        t += 1
        if t % 15 == 0:
            time += 1
    camera.display()
    rando = random.randint(0,15) # used for randomizing enemy missiles


gamebox.timer_loop(30, tick)
