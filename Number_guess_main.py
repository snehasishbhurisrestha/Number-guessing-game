import pygame
from random import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

manu_state = "main"

clock = pygame.time.Clock()

# intialize the pygame
pygame.init()

# create the screen
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600 
Screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Title and Icon
pygame.display.set_caption('Guess the Number')
icon  = pygame.image.load('GUESS_THE_NUMBER/Images/logo.png')
pygame.display.set_icon(icon)

font = pygame.font.SysFont("Arial",40)   # Add font 

# lode button images
start_img = pygame.image.load('GUESS_THE_NUMBER/Images/play.jpg').convert_alpha()
quit_img = pygame.image.load('GUESS_THE_NUMBER/Images/exit.jpg').convert_alpha()
guess_img = pygame.image.load('GUESS_THE_NUMBER/Images/images.png').convert_alpha()
submit_img = pygame.image.load('GUESS_THE_NUMBER/Images/submit.jpg').convert_alpha()
too_low_img = pygame.image.load('GUESS_THE_NUMBER/Images/too_low.jpg').convert_alpha()
too_high_img = pygame.image.load('GUESS_THE_NUMBER/Images/too_high.jpg').convert_alpha()
correct_img = pygame.image.load('GUESS_THE_NUMBER/Images/correct.jpg').convert_alpha()
mainGuess_img = pygame.image.load('GUESS_THE_NUMBER/Images/guess.png').convert_alpha()
computer_img = pygame.image.load('GUESS_THE_NUMBER/Images/computer.png').convert_alpha()
mainQuit_img = pygame.image.load('GUESS_THE_NUMBER/Images/quit.jpg').convert_alpha()

# button class
class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()     # get mouse position
        # check mouseover and clicked condition
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
                # print('CLICKED')
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        Screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

def text_print(str, x, y, color):
    op_str = str
    text = font.render(op_str,True,color)
    Screen.blit(text,[x, y])

def show_output(txt, x, y,color,r1,r2,r3,r4,fontsize = 50):
    Screen.fill(pygame.Color("black"),(r1, r2, r3, r4))
    font = pygame.font.Font(None, fontsize)

    font_surface = font.render(txt,True,color)
    Screen.blit(font_surface,(x,y))
    pygame.display.flip()

too_low_button = Button(70, 350, too_low_img, 0.2)
too_high_button = Button(550, 350, too_high_img, 0.2)
correct_button = Button(320, 355, correct_img, 0.2)

def computerguess():
    txt = ''
    low, high = 0, 0
    text_print('Please enter a lower bound', 10, 20, WHITE)
    try:
        low = int(computer_guess_input(450, 20, 590, 20))
    except ValueError:
        # print('please give me a integer')
        show_output('Please enter an integer', 200, 470, RED, 200, 470, 450, 50)
    # low = int(computer_guess_input(450, 20, 590, 20))
    text_print('Please enter a upper bound', 10, 90, WHITE)
    try:
        high = int(computer_guess_input(450, 90, 590, 90))
    except ValueError:
        # print('please give me a integer')
        show_output('Please enter an integer', 200, 470, RED, 200, 470, 450, 50)
    # high = int(computer_guess_input(450, 90, 590, 90))
    txt = 'You guess a number between {} and {}'.format(low,high)
    text_print(txt, 100, 170, RED)

    guess, numberofGuess = 0, 1
    test = True
    while test:
        guess = randint(low,high)
        # print("low =",low,"high =",high)
        txt = 'Computer Guess : {}'.format(guess)
        show_output(txt,200,250,GREEN,200,250,400,40)
        txt = 'Attempt : {}'.format(10 - numberofGuess)
        show_output(txt, 320, 300, RED, 320, 300, 210, 50)
        
        if 10 - numberofGuess == 0:
            # print('\nSorry, I Loose!\n')
            show_output('Sorry, I Loose!', 290, 470, WHITE, 200, 470, 490, 50)
            break
        flag = high_low_correct_button()
        if flag == "low":
            # print('Lower number Please!')
            numberofGuess += 1
            low = guess
        elif flag == "high":
            # print('Higher number Please!')
            numberofGuess += 1
            high = guess
        elif flag == "correct":
            txt = 'I guessed the number in {} attempts!'.format(numberofGuess)
            show_output(txt, 100, 470, WHITE, 100, 470, 490, 50)
            # print('I guessed the number in',numberofGuess,'attempts!')
            test = False
    pygame.time.wait(2500)

def high_low_correct_button():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
            if too_low_button.draw():
                # print("low")
                return "low"
            if correct_button.draw():
                # print("correct")
                return "correct"
            if too_high_button.draw():
                # print("high")
                return "high"
        
        pygame.display.flip()
        clock.tick(60)

def computer_guess_input(x, y, b1, b2):
    global guessing

    color_passive = pygame.Color('gray')
    color_active = pygame.Color('white')
    color = color_passive

    user_text = ''

    # active = False
    active = True
    # create rectangle
    input_rect = pygame.Rect(x, y, 30, 50)
    submit_button = Button(b1, b2, submit_img, 0.5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
            if event.type == pygame.KEYDOWN:
                if active == True: 
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
                    # print(user_text)
                if event.key == pygame.K_KP_ENTER:
                    guessing = user_text
                    return guessing
            if submit_button.draw():
                guessing = user_text
                return guessing
        
        if active:
            color = color_active
        else:
         color = color_passive

        pygame.draw.rect(Screen,color,input_rect)
        text_surface = font.render(user_text,True,(0,0,0))
        Screen.blit(text_surface,input_rect)
        input_rect.w = 90
        pygame.display.flip()
        clock.tick(60)

def guessnumber():
    low = randint(1,200)
    high = randint(300,500)
    number = randint(low,high)
    txt = ''
    numberofGuess, guess = 0, 0
    txt = 'Guess a number between {} and {}'.format(low,high)
    text_print(txt,110,50,WHITE)
    text_print('Your guess ',110,155,WHITE)
    while(guess != number):
        txt = 'Attempt : {}'.format(10 - numberofGuess)
        show_output(txt, 580, 160, RED, 580, 160, 210, 50)

        if numberofGuess > 9:
            txt = 'You Loose!'
            # print('\nYou Loose!\n')
            show_output(txt, 300, 400, WHITE, 0, 400, 650, 50)
            break 
        # guess = int(input())
        try:
            guess = int(input())
        except ValueError:
            show_output('Please enter an integer', 220, 400, WHITE, 220, 400, 450, 50)
        if guess > number:
            txt = '{}, Lower number Please!'.format(guess)
            show_output(txt, 190, 400, WHITE, 190, 400, 490, 50)
            numberofGuess += 1
        elif guess < number:
            txt = '{}, Higher number Please!'.format(guess)
            show_output(txt, 190, 400, WHITE, 190, 400, 490, 50)
            numberofGuess += 1
        else:
            # print('\nYou own the game in passes',numberofGuess,'!\n')
            txt = 'You guessed the number in {} attempts!'.format(numberofGuess)
            show_output(txt, 70, 400, WHITE, 0, 400, 650, 50)
    pygame.time.wait(2500)

def input():
    global guessing

    color_passive = pygame.Color('gray')
    color_active = pygame.Color('white')
    color = color_passive

    user_text = ''

    # active = False
    active = True
    # create rectangle
    input_rect = pygame.Rect(350, 156, 30, 50)

    guess_button = Button(280, 280, guess_img, 0.3)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
            if event.type == pygame.KEYDOWN:
                if active == True: 
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
                    # print(user_text)
                if event.key == pygame.K_KP_ENTER:
                    guessing = user_text
                    return guessing
            if guess_button.draw():
                guessing = user_text
                return guessing
            #     # print(guess == number)
        
        if active:
            color = color_active
        else:
         color = color_passive

        pygame.draw.rect(Screen,color,input_rect)
        text_surface = font.render(user_text,True,(0,0,0))
        Screen.blit(text_surface,input_rect)
        input_rect.w = 90
        pygame.display.flip()
        clock.tick(60)
    

# create button object
start_button = Button(100, 240, start_img, 0.8)
quit_button = Button(450, 240, quit_img, 0.8)
your_guess = Button(278, 50, mainGuess_img, 0.5)
computer_guess = Button(275, 220, computer_img, 0.5)
manu_quit_button = Button(285, 410, mainQuit_img, 0.5)
def name():
    show_output("Developed by,",30,200,WHITE,0,0,0,0,60)
    show_output("Snehasish Bhurisrestha",140,300,WHITE,0,0,0,0,80)
    pygame.time.wait(1500)
GameStart = False
# Game Loop
num = 0
gameOn = True
while gameOn:
    Screen.fill((85, 39, 89))     # screen color
    # name()
    if GameStart == True:
        Screen.fill((255, 0, 0))
        if manu_state == "main":
            if your_guess.draw():
                manu_state = "your_guess"
                # print("your")
            if computer_guess.draw():
                manu_state = "computer_guess"
                # print("computer")
            if manu_quit_button.draw():
                gameOn = False
        if manu_state == "your_guess":
            Screen.fill((0, 0, 0))
            guessnumber()
            manu_state = "main"
        if manu_state == "computer_guess":
            Screen.fill((0, 0, 0))
            computerguess()
            manu_state = "main"

    else:
        if num!=1:
            name()
            num +=1
        if start_button.draw():
            GameStart = True
            # print('START')

        if quit_button.draw():
            gameOn = False
            # print('QUIT')

    # event handler
    for events in pygame.event.get():
        if events.type == pygame.QUIT:        # quit game
            gameOn = False
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()