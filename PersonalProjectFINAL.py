#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import easygui
import random


pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([0, 0, 0])

game_title = pygame.image.load("example_title.gif")
screen.blit(game_title, [70, 20])

instructions_command = pygame.image.load("instructions_command.png")
screen.blit(instructions_command, [170, 240])

easymode_command = pygame.image.load("easymode_command.png")
screen.blit(easymode_command, [170, 300])

mediummode_command = pygame.image.load("mediummode_command.png")
screen.blit(mediummode_command, [170, 360])

hardmode_command = pygame.image.load("hardmode_command.png")
screen.blit(hardmode_command, [170, 420])

pygame.display.flip()

success_counter = 0
success_counter2 = 0

def animate(screen):
    screen.fill([0, 0, 0])
    player_sprite = pygame.image.load("player_sprite.gif")
    screen.blit(player_sprite, [20, 130])
    computer_sprite = pygame.image.load("computer_sprite.gif")
    screen.blit(computer_sprite, [420, 130])

    player_text = "Player"
    player_font = pygame.font.Font(None, 70)
    player_surf = player_font.render(player_text, 1, (255, 255, 255))
    screen.blit(player_surf, [20, 420])

    computer_text = "Newton"
    computer_font = pygame.font.Font(None, 70)
    computer_surf = computer_font.render(computer_text, 1, (255, 255, 255))
    screen.blit(computer_surf, [450, 420])

    pygame.display.flip()


def player_health_bar(screen, player_health):
    pygame.draw.rect(screen, [255, 255, 255], [20, 60, 150, 50], 2)
    pygame.draw.rect(screen, [0, 255, 0], [22, 62, 150 * player_health / 1000 - 2, 48], 0)
    pygame.display.flip()


def enemy_health_bar(screen, computer_health):
    pygame.draw.rect(screen, [255, 255, 255], [470, 60, 150, 50], 2)
    pygame.draw.rect(screen, [0, 255, 0], [472, 62, 150 * computer_health / 1000 - 2, 48], 0)
    pygame.display.flip()


def player_turn(screen, computer_health, player_damage):
    q1 = "Fully simplify the following expression: (3√5 - 2) (3√5 + 2)"
    q2 = "How many real roots does the following equation have?: x^2 + 9 = 0"
    q3 = "How many real roots does the following equation have?: x^2 + 5x - 8 = 0"
    q4 = "Expand and simplify: (2x - 5)(x + 4)"
    q5 = "Fully factor: am + an + bm + bn"
    q6 = "What is the optimal value of the following function?: y = -3(x-2)^2 + 8"
    q7 = "What is the equation of A.O.S (Axis of Symmetry) for the following function?: y = -1(x + 3)^2 + 4"
    q8 = "Factor fully: 3x^2 - 27"
    q9 = "Solve the following quadratic equation: b^2 + 4b + 4 = 0"
    q10 = "Solve the following quadratic equation: a^2 + 8a + 16 = 0"

    questions_list = (q1, q2, q3, q4, q5, q6, q7, q8, q9, q10)
    question = random.choice(questions_list)

    if question == q1:
        correct = "41"
    elif question == q2:
        correct = "0"
    elif question == q3:
        correct = "2"
    elif question == q4:
        correct = "(a + b)(m + n)"
    elif question == q5:
        correct = "2x^2 + 3x - 20"
    elif question == q6:
        correct = "8"
    elif question == q7:
        correct = "x = 4"
    elif question == q8:
        correct = "3(x + 3)(x - 3)"
    elif question == q9:
        correct = "b = -2" 
    else:
        correct = "x = -4"
    answer = easygui.enterbox(question)

    if answer == correct:
        global success_counter2
        success_counter2 = success_counter2 + 1
        easygui.msgbox("Congratulations! You are correct. You have completed an attack.")
        computer_health = computer_health - player_damage * success_counter2
        fire_ball = pygame.image.load('fire_ball1.png')
        x = 220
        y = 250
        x_speed = 5

        while x < 310:
            pygame.time.delay(20)
            pygame.draw.rect(screen, [0, 0, 0], [x, y, 50, 50], 0)
            x = x + x_speed
            screen.blit(fire_ball, [x, y])
            pygame.display.flip()
            pygame.draw.rect(screen, [0, 0, 0], [x, y, 90, 90], 0)
            pygame.draw.rect(screen, [0, 0, 0], [472, 62, 148, 48], 0)
        pygame.display.flip()

        pygame.draw.rect(screen, [255, 255, 255], [470, 60, 150, 50], 2)
        pygame.draw.rect(screen, [0, 255, 0], [472, 62, 150 * computer_health / 1000 - 2, 48], 0)
        pygame.display.flip()
        
    if answer != correct:
        easygui.msgbox("Sorry you are incorrect. The correct answer is %s. You have failed an attack!" % correct)
    

def computer_turn(screen, player_health, computer_damage):
    attack_chance = random.randstr(0, 2)

    if attack_chance == 1:
        global success_counter
        success_counter = success_counter + 1
        easygui.msgbox("Newton has succesfully completed an attack. It is now your turn.")
        player_health = player_health - player_damage * success_counter
        fire_ball = pygame.image.load('fire_ball2.png')
        x = 310
        y = 250
        x_speed = -5

        while x > 220:
            pygame.time.delay(20)
            pygame.draw.rect(screen, [0, 0, 0], [x, y, 50, 50], 0)
            x = x + x_speed
            screen.blit(fire_ball, [x, y])
            pygame.display.flip()
            pygame.draw.rect(screen, [0, 0, 0], [x, y, 90, 90], 0)
            pygame.draw.rect(screen, [0, 0, 0], [22, 62, 148, 48], 0)
        pygame.display.flip()
        
        pygame.draw.rect(screen, [255, 255, 255], [20, 60, 150, 50], 2)
        pygame.draw.rect(screen, [0, 255, 0], [22, 62, 150 * player_health / 1000 - 2, 48], 0)
        pygame.display.flip()

    else:
        easygui.msgbox("Newton has failed an attack! It is now your turn")


def end_game1():
    easygui.msgbox("Congratulations! You beat Newton!")


def end_game2():
    easygui.msgbox("GAMEOVER: Oh no! Newton beat you!")

player_damage = 100
player_health = 1000
computer_damage = 100
computer_health = 1000

#********************EINSTEIN CODE STARTS HERE***********************
success_counterEINSTEIN = 0
success_counter2EINSTEIN = 0

def animateEINSTEIN(screen):
    screen.fill([0, 0, 0])
    player_sprite = pygame.image.load("player_sprite.gif")
    screen.blit(player_sprite, [20, 130])
    computer_spriteEINSTEIN = pygame.image.load("computer_spriteEINSTEIN.gif")
    screen.blit(computer_spriteEINSTEIN, [420, 130])

    player_text = "Player"
    player_font = pygame.font.Font(None, 70)
    player_surf = player_font.render(player_text, 1, (255, 255, 255))
    screen.blit(player_surf, [20, 420])

    computer_text = "Einstein"
    computer_font = pygame.font.Font(None, 70)
    computer_surf = computer_font.render(computer_text, 1, (255, 255, 255))
    screen.blit(computer_surf, [450, 420])

    pygame.display.flip()


def player_health_barEINSTEIN(screen, player_healthEINSTEIN):
    pygame.draw.rect(screen, [255, 255, 255], [20, 60, 150, 50], 2)
    pygame.draw.rect(screen, [0, 255, 0], [22, 62, 150 * player_healthEINSTEIN / 1000 - 2, 48], 0)
    pygame.display.flip()


def enemy_health_barEINSTEIN(screen, computer_healthEINSTEIN):
    pygame.draw.rect(screen, [255, 255, 255], [470, 60, 150, 50], 2)
    pygame.draw.rect(screen, [0, 255, 0], [472, 62, 150 * computer_healthEINSTEIN / 1000 - 2, 48], 0)
    pygame.display.flip()


def player_turnEINSTEIN(screen, computer_healthEINSTEIN, player_damageEINSTEIN):
    q1 = "Find the maximum or minimum value of f(x) = -3x2 + 9x"
    q2 = "Solve for n: n2 + 4n + 3 = 0. If there are multiple answers, separate them with commas."
    q3 = "Solve for d: d2 – 6d + 8 = 0. If there are multiple answers, separate them with commas."
    q4 = "Solve for g: g2 + 16g – 17 = 0. If there are multiple answers, separate them with commas."
    q5 = "Find the axis of symmetry of the graph of f(x) = -2x2 - x - 2"
    q6 = "Factor fully: 9z^3 – 9z^2 + z – 1"
    q7 = "Factor fully: 10k^3 – 10k^2 + 7k –7"
    q8 = "Factor fully: 10r^3 – 10r^2 + r – 1"
    q9 = "Two numbers differ by 8. Find the two numbers if their product is a minimum. Seperate the two values by a comma, from greatest to least."
    q10 = "Sally wants to put a border around a 4x6 cm picture. She would like the border to be twice the area of the picture.",
    "What is the border width she should use. Round the value to the nearest tenth"

    questions_list = (q1, q2, q3, q4, q5, q6, q7, q8, q9, q10)
    question = random.choice(questions_list)

    if question == q1:
        correct = "27/4"
    elif question == q2:
        correct = "-1, -3"
    elif question == q3:
        correct = "2, 4"
    elif question == q4:
        correct = "-17, 1"
    elif question == q5:
        correct = "x = -1/4"
    elif question == q6:
        correct = "(9z^2 + 1)(z – 1)"
    elif question == q7:
        correct = "(10k^2 + 7)(k – 1)"
    elif question == q8:
        correct = "(10r^2 + 1)(r – 1)"
    elif question == q9:
        correct = "4, -4"
    else:
        correct = "1.8"
    answer = easygui.enterbox(question)

    if answer == correct:
        global success_counter2EINSTEIN
        success_counter2EINSTEIN = success_counter2EINSTEIN + 1
        easygui.msgbox("Congratulations! You are correct. You have completed an attack.")
        computer_healthEINSTEIN = computer_healthEINSTEIN - player_damageEINSTEIN * success_counter2EINSTEIN
        fire_ball = pygame.image.load('fire_ball1.png')
        x = 220
        y = 250
        x_speed = 5

        while x < 310:
            pygame.time.delay(20)
            pygame.draw.rect(screen, [0, 0, 0], [x, y, 50, 50], 0)
            x = x + x_speed
            screen.blit(fire_ball, [x, y])
            pygame.display.flip()
            pygame.draw.rect(screen, [0, 0, 0], [x, y, 90, 90], 0)
            pygame.draw.rect(screen, [0, 0, 0], [472, 62, 148, 48], 0)
        pygame.display.flip()

        pygame.draw.rect(screen, [255, 255, 255], [470, 60, 150, 50], 2)
        pygame.draw.rect(screen, [0, 255, 0], [472, 62, 150 * computer_healthEINSTEIN / 1000 - 2, 48], 0)
        pygame.display.flip()
        
    if answer != correct:
        easygui.msgbox("Sorry you are incorrect. The correct answer is %s. You have failed an attack!" % correct)
    

def computer_turnEINSTEIN(screen, player_healthEINSTEIN, computer_damageEINSTEIN):
    attack_chance = random.randint(0, 2)

    if attack_chance == 1:
        global success_counterEINSTEIN
        success_counter = success_counterEINSTEIN + 1
        easygui.msgbox("Einstein has succesfully completed an attack. It is now your turn.")
        player_healthEINSTEIN = player_healthEINSTEIN - player_damageEINSTEIN * success_counterEINSTEIN
        fire_ball = pygame.image.load('fire_ball2.png')
        x = 310
        y = 250
        x_speed = -5

        while x > 220:
            pygame.time.delay(20)
            pygame.draw.rect(screen, [0, 0, 0], [x, y, 50, 50], 0)
            x = x + x_speed
            screen.blit(fire_ball, [x, y])
            pygame.display.flip()
            pygame.draw.rect(screen, [0, 0, 0], [x, y, 90, 90], 0)
            pygame.draw.rect(screen, [0, 0, 0], [22, 62, 148, 48], 0)
        pygame.display.flip()
        
        pygame.draw.rect(screen, [255, 255, 255], [20, 60, 150, 50], 2)
        pygame.draw.rect(screen, [0, 255, 0], [22, 62, 150 * player_healthEINSTEIN / 1000 - 2, 48], 0)
        pygame.display.flip()

    else:
        easygui.msgbox("Einstein has failed an attack! It is now your turn")


def end_game1EINSTEIN():
    easygui.msgbox("Congratulations! You beat Einstein!")


def end_game2EINSTEIN():
    easygui.msgbox("GAMEOVER: Oh no! Einstein beat you!")

player_damageEINSTEIN = 100
player_healthEINSTEIN = 1000
computer_damageEINSTEIN = 111
computer_healthEINSTEIN = 1100


#********************GALILEO CODE STARTS HERE************************

success_counterGALILEO = 0
success_counter2GALILEO = 0

def animateGALILEO(screen):
    screen.fill([0, 0, 0])
    player_sprite = pygame.image.load("player_sprite.gif")
    screen.blit(player_sprite, [20, 130])
    computer_spriteGALILEO = pygame.image.load("computer_spriteGALILEO.gif")
    screen.blit(computer_spriteGALILEO, [420, 130])

    player_text = "Player"
    player_font = pygame.font.Font(None, 70)
    player_surf = player_font.render(player_text, 1, (255, 255, 255))
    screen.blit(player_surf, [20, 420])

    computer_text = "Galileo"
    computer_font = pygame.font.Font(None, 70)
    computer_surf = computer_font.render(computer_text, 1, (255, 255, 255))
    screen.blit(computer_surf, [450, 420])

    pygame.display.flip()


def player_health_barGALILEO(screen, player_healthGALILEO):
    pygame.draw.rect(screen, [255, 255, 255], [20, 60, 150, 50], 2)
    pygame.draw.rect(screen, [0, 255, 0], [22, 62, 150 * player_healthGALILEO / 1000 - 2, 48], 0)
    pygame.display.flip()


def enemy_health_barGALILEO(screen, computer_healthGALILEO):
    pygame.draw.rect(screen, [255, 255, 255], [470, 60, 150, 50], 2)
    pygame.draw.rect(screen, [0, 255, 0], [472, 62, 150 * computer_healthGALILEO / 1000 - 2, 48], 0)
    pygame.display.flip()


def player_turnGALILEO(screen, computer_healthGALILEO, player_damageGALILEO):
    q1 = "One side of a right triangle is 2cm shorter than the hypotenuse and 7cm longer than the third side. ",
    "Find the lengths of the sides of the triangle. Seperate the two values by a comma, from greatest to least."
    q2 = "A rectangular enclosure has an area in square metres given by A = -7w^2 + 42w, where 'w' is the width of the rectangle in metres. ",
    "What is the maximum area of the enclosure. Give the answer as an interger."
    q3 = "A baseball is thrown into the air. Its height (h) above the ground after 't' seconds is modelled by h = -3t^2 + 12t + 2. ",
    "For how long does the baseball have a height of 10m or greater? Round the answer as a value, to 1 decimal place."
    q4 = "Mike wants to build an enclosure along the side of his house. He has 40m of fencing to border the three sides (the wall will act as the third side ",
    "Determine the dimensions that will maximize the area of the enclosure. Type the answer as a width and length seperated by a comma."
    q5 = "The sum of two numbers is 5 and their product is −84. Find these numbers. Give your answer as two digits, from greatest to least, seperated by a comma."
    q6 = "Within 11 years, the age of Peter will be half the square of the age he was 13 years ago. Calculate the current age of Peter."
    q7 = "The three sides of a right-angled triangle are proportional to the numbers 3, 4 and 5. Find the length (as an interger) of the longest side knowing that the area of the triangle is 168 m²."
    q8 = "A piece of iron rod costs $60. If the rod was 2 meter shorter and each meter costs $1 more, the cost would remain unchanged. What is the length of the rod? (as an interger)"
    q9 = "The sides of an equilateral triangle are shortened by 12 units, 13 units and 14 units respectively and a right angle triangle is formed. What is the side length of ",
    "the equilateral triangle? (as an interger)"
    q10 = "A distributor of apple juice has 5000 bottles in the store that it wishes to distribute in a month. From experience, it is known that demand D is given by D = -2000p² + 2000p + 17000. ",
    "Find the price (as an interger) per bottle that will result zero inventory."

    questions_list = (q1, q2, q3, q4, q5, q6, q7, q8, q9, q10)
    question = random.choice(questions_list)

    if question == q1:
        correct = "8, 15, 7"
    elif question == q2:
        correct = "63"
    elif question == q3:
        correct = "2.3"
    elif question == q4:
        correct = "10, 20"
    elif question == q5:
        correct = "12, -7"
    elif question == q6:
        correct = "21"
    elif question == q7:
        correct = "70"
    elif question == q8:
        correct = "12"
    elif question == q9:
        correct = "17"
    else:
        correct = "2"
    answer = easygui.enterbox(question)

    if answer == correct:
        global success_counter2GALILEO
        success_counter2GALILEO = success_counter2GALILEO + 1
        easygui.msgbox("Congratulations! You are correct. You have completed an attack.")
        computer_healthGALILEO = computer_healthGALILEO - player_damageGALILEO * success_counter2GALILEO
        fire_ball = pygame.image.load('fire_ball1.png')
        x = 220
        y = 250
        x_speed = 5

        while x < 310:
            pygame.time.delay(20)
            pygame.draw.rect(screen, [0, 0, 0], [x, y, 50, 50], 0)
            x = x + x_speed
            screen.blit(fire_ball, [x, y])
            pygame.display.flip()
            pygame.draw.rect(screen, [0, 0, 0], [x, y, 90, 90], 0)
            pygame.draw.rect(screen, [0, 0, 0], [472, 62, 148, 48], 0)
        pygame.display.flip()

        pygame.draw.rect(screen, [255, 255, 255], [470, 60, 150, 50], 2)
        pygame.draw.rect(screen, [0, 255, 0], [472, 62, 150 * computer_healthGALILEO / 1000 - 2, 48], 0)
        pygame.display.flip()
        
    if answer != correct:
        easygui.msgbox("Sorry you are incorrect. The correct answer is %s. You have failed an attack!" % correct)
    

def computer_turnGALILEO(screen, player_healthGALILEO, computer_damageGALILEO):
    attack_chance = random.randint(0, 2)

    if attack_chance == 1:
        global success_counterGALILEO
        success_counter = success_counterGALILEO + 1
        easygui.msgbox("Galileo has succesfully completed an attack. It is now your turn.")
        player_healthGALILEO = player_healthGALILEO - player_damageGALILEO * success_counterGALILEO
        fire_ball = pygame.image.load('fire_ball2.png')
        x = 310
        y = 250
        x_speed = -5

        while x > 220:
            pygame.time.delay(20)
            pygame.draw.rect(screen, [0, 0, 0], [x, y, 50, 50], 0)
            x = x + x_speed
            screen.blit(fire_ball, [x, y])
            pygame.display.flip()
            pygame.draw.rect(screen, [0, 0, 0], [x, y, 90, 90], 0)
            pygame.draw.rect(screen, [0, 0, 0], [22, 62, 148, 48], 0)
        pygame.display.flip()
        
        pygame.draw.rect(screen, [255, 255, 255], [20, 60, 150, 50], 2)
        pygame.draw.rect(screen, [0, 255, 0], [22, 62, 150 * player_healthGALILEO / 1000 - 2, 48], 0)
        pygame.display.flip()

    else:
        easygui.msgbox("Galileo has failed an attack! It is now your turn")


def end_game1GALILEO():
    easygui.msgbox("Congratulations! You beat Galileo!")


def end_game2GALILEO():
    easygui.msgbox("GAMEOVER: Oh no! Galileo beat you!")

player_damageGALILEO = 100
player_healthGALILEO = 1000
computer_damageGALILEO = 125
computer_healthGALILEO = 1200



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                easygui.msgbox("Hello and welcome to 'Math Wiz'! This is a game to practice your quadractic "
                               "math skills while you battle and prove yourself against the best Math Wizards "
                               "in the land: Isaac (easy), Albert (medium), and Galileo (hard). The objective "
                               "of the game is to defeat the opponents by diminishing their health. If all your "
                               "health is gone before the enemy's, you lose. To attempt an attack, press the "
                               "key instructed on the screen. To successfully execute an attack, answer the "
                               "question given, with the correct solution. Providing the wrong solution will "
                               "result in a failed attack (no damage). Then it is the opponents (computer) turn."
                               "Press the key instructed on the screen to initialize it. He may or may "
                               "not attack you back successfully. Keep alternating turns until a winner is declared. "
                               "Have fun!")
            elif event.key == pygame.K_b:
                animate(screen)
                player_health_bar(screen, player_health)
                enemy_health_bar(screen, computer_health)

            if  event.key == pygame.K_z:
                player_turn(screen, computer_health, player_damage)
            if event.key == pygame.K_x:
                computer_turn(screen, player_health, computer_damage)

        if success_counter == 10:
            end_game2()
            running = False
        if success_counter2 == 10:
            end_game1()
            running = False

            if event.key == pygame.K_c:
                animateEINSTEIN(screen)
                player_health_barEINSTEIN(screen, player_healthEINSTEIN)
                enemy_health_barEINSTEIN(screen, computer_healthEINSTEIN)

            if event.key == pygame.K_h:
                player_turnEINSTEIN(screen, computer_healthEINSTEIN, player_damageEINSTEIN)
            if event.key == pygame.K_j:
                computer_turnEINSTEIN(screen, player_healthEINSTEIN, computer_damageEINSTEIN)

        if success_counterEINSTEIN == 11:
            end_game2EINSTEIN()
            running = False
        if success_counter2EINSTEIN == 9:
            end_game1EINSTEIN()
            running = False 

            if event.key == pygame.K_d:
                animateGALILEO(screen)
                player_health_barGALILEO(screen, player_healthGALILEO)
                enemy_health_barGALILEO(screen, computer_healthGALILEO)

            if event.key == pygame.K_t:
                player_turnGALILEO(screen, computer_healthGALILEO, player_damageGALILEO)
            if event.key == pygame.K_y:
                computer_turnGALILEO(screen, player_healthGALILEO, computer_damageGALILEO)

        if success_counterGALILEO == 12:
            end_game2GALILEO()
            running = False
        if success_counter2GALILEO == 8:
            end_game1GALILEO()
            running = False 
pygame.quit()
