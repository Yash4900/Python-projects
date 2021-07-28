#imorting required modules
import pygame
import random
import os

pygame.init()

#creating game window
window_width = 900
window_height = 650
gameWindow = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snakes")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

#function for creating button
def button(color, font_color, button_x, button_y, font_x, font_y, button_width, button_height, text=''):
    pygame.draw.rect(gameWindow, color, [button_x, button_y, button_width, button_height])
    display_text(text, font_color, font_x, font_y)

#function for displaying text
def display_text(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

#function for plotting snake
def plot_snake(gameWindow, color, snake_body, snake_size):    
    for i in range (len(snake_body)):
        pygame.draw.circle(gameWindow, color, [snake_body[i][0], snake_body[i][1]], snake_size)

#instruction window
def instructions():
    exit_game = False
    while not exit_game:
        gameWindow.fill((137,202,2))
        button((0,138,0), (255,255,255),750,50,756,57,90,40,"BACK")

        #displaying instructions
        display_text("INSTRUCTIONS:",(0,0,0),150,160)
        display_text("1. Do not collapse the head on the wall or snake body",(0,0,0),150,200)
        display_text("2. Use your cursor keys: up, left, right, and down",(0,0,0),150,260)
        display_text("3. Keyboard p is used for Play and Pause",(0,0,0), 150, 320)
        display_text("4. Eat the colored apples to gain points",(0,0,0), 150, 380)
       
        #get mouse position
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
                pygame.quit()

            #logic for clicking on BACK button    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(750<mouse_pos[0]<840 and 50<mouse_pos[1]<90):
                    start_window()

        pygame.display.update()
        clock.tick(60)

#welcome window
def start_window():
    exit_game = False
    while not exit_game:
        bgimg = pygame.image.load("img/startgame.jpg")
        bgimg = pygame.transform.scale(bgimg, (window_width, window_height)).convert_alpha()
        gameWindow.blit(bgimg, (0, 0))

        button((0,138,0), (255,255,255), 310, 250, 340, 260, 270, 40, "INSTRUCTIONS")        
        button((0,138,0), (255,255,255), 370, 350, 395, 360, 130, 40, "PLAY")

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(310<mouse_pos[0]<580 and 250<mouse_pos[1]<290):
                    instructions()
                if(370<mouse_pos[0]<500 and 350<mouse_pos[1]<390):
                    gameloop()
            if event.type == pygame.QUIT:
               exit_game = True

        # for event in pygame.event.get():
           
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_SPACE:
        #             gameloop()
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         gameloop()

        pygame.display.update()
        clock.tick(60)

#game window
def gameloop():

    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = random.randint(15,window_width-15)
    snake_y = random.randint(100,window_height-15)
    speed_x = 0
    speed_y = 0
    snake_body = []
    snake_length = 10
    score = 0
    game_speed = 5
    fps = 60
    snake_size = 15
    count = 0
    pause = False
    colours = [(255,0,0),(255,255,128),(128,255,0),(255,128,0),(128,0,255),(0,128,255),(255,128,192)]
    snake_colour = (255,255,255)

    # Check if high-score file exists
    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")

    #if exists then read high-score
    with open("hiscore.txt", "r") as f:
        high_score = f.read()

    #get random coordinates for food
    food_x = random.randint(15, window_width-15)
    food_y = random.randint(100, window_height-15)

    while not exit_game:

        #pause
        if(pause):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        pause =False
            continue

        #game-over
        if game_over:
            #update high-score file if high-score was made
            with open("hiscore.txt", "w") as f:
                f.write(str(high_score))

            bgimg = pygame.image.load("img/gameover.jpg")
            bgimg = pygame.transform.scale(bgimg, (window_width, window_height)).convert_alpha()
            gameWindow.blit(bgimg, (0, 0))   

            display_text("Press Enter To Continue", (255,255,255), 285, 450)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        start_window()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    #controlling snake
                    if event.key == pygame.K_RIGHT:
                        speed_x = game_speed
                        speed_y = 0

                    if event.key == pygame.K_LEFT:
                        speed_x = - game_speed
                        speed_y = 0

                    if event.key == pygame.K_UP:
                        speed_y = - game_speed
                        speed_x = 0

                    if event.key == pygame.K_DOWN:
                        speed_y = game_speed
                        speed_x = 0

                    if event.key == pygame.K_p:
                        pause = True            
                    #basically we are increasing/decreasing the coordinates of snake
            snake_x = snake_x + speed_x
            snake_y = snake_y + speed_y

            #eat food
            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                pygame.mixer.music.load('sounds/BITE.mp3')
                pygame.mixer.music.play()
                score +=10   
                #new food coordinates        
                food_x = random.randint(15, window_width-15)
                food_y = random.randint(100, window_height-15)
                snake_length +=5
                snake_colour = random.choice(colours)
                if score>int(high_score):
                    high_score = score


            gameWindow.fill((0,0,0))
        
            pygame.draw.rect(gameWindow, (0,0,0), [0, 0, window_width, 50])
            pygame.draw.rect(gameWindow, (255,255,255), [0, 48, window_width, 2])
            display_text("Score: " + str(score) + "        High-score: "+str(high_score), (255,255,255), 5, 5)
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            pygame.draw.circle(gameWindow, (r,g,b), [food_x, food_y], snake_size)


            snake_head = []
            snake_head.append(snake_x)
            snake_head.append(snake_y)
            #this will add a new part to snake in each loop cycle
            snake_body.append(snake_head)
            #but we want to limit the length upto snake length so we delete the head
            if len(snake_body)>snake_length:
                del snake_body[0]

            #snake head collapses with body then game-over
            if snake_head in snake_body[:-1] and len(snake_body)>10:
                game_over = True
                pygame.mixer.music.load('sounds/GAMEOVER.mp3')
                pygame.mixer.music.play()

            #snake head collapses with wall then game-over
            if snake_x<0 or snake_x>window_width or snake_y<50 or snake_y>window_height:
                game_over = True
                pygame.mixer.music.load('sounds/GAMEOVER.mp3')
                pygame.mixer.music.play()

            plot_snake(gameWindow, snake_colour, snake_body, snake_size)
            
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

start_window()
