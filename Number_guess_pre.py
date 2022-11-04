import pygame
from random import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()

# intialize the pygame
pygame.init()

# create the screen
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600 # width, height
# Screen = pygame.display.set_mode((800,600)) # width, height  
Screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Title and Icon
pygame.display.set_caption('Guess the Number')
icon  = pygame.image.load('logo.png')
pygame.display.set_icon(icon)

font = pygame.font.SysFont("Arial",40)   # Add font 

# lode button images
start_img = pygame.image.load('play.jpg').convert_alpha()
quit_img = pygame.image.load('exit.jpg').convert_alpha()
guess_img = pygame.image.load('images.png').convert_alpha()

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

def show_output(txt, x, y,color,r1,r2,r3,r4):
    Screen.fill(pygame.Color("black"),(r1, r2, r3, r4))
    font = pygame.font.Font(None, 50)

    font_surface = font.render(txt,True,color)
    Screen.blit(font_surface,(x,y))
    pygame.display.flip()

def guessnumber():
    low = randint(1,200)
    high = randint(300,500)
    number = randint(low,high)
    # print(number)
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
        
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if input_rect.collidepoint(event.pos):
            #         active = True
            #     else:
            #         active = False
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
        # Screen.blit(text_surface,(input_rect.x + 5, input_rect.y + 5))
        # input_rect.w = max(100, text_surface.get_width() + 10)
        input_rect.w = 90
        pygame.display.flip()
        clock.tick(60)
    

# create button object
start_button = Button(100, 240, start_img, 0.8)
quit_button = Button(450, 240, quit_img, 0.8)

# low = randint(1,200)
# high = randint(300,500)

GameStart = False
# Game Loop
gameOn = True
while gameOn:

    Screen.fill((85, 39, 89))     # screen color
    # draw_text("PLAY", font,BLACK,100, 240)
    if GameStart == True:
        Screen.fill((0, 0, 0))
        # low = randint(1,200)
        # high = randint(300,500)
        guessnumber() 
        GameStart = False

    else:
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


pygame.quit()