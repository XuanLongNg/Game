import pygame
import time
import random
white = (255, 255, 255)
blue=(0,0,255)
black = (0, 0, 0)
red = (255, 0, 0)

scr_width= 800
scr_height= 600
pygame.init()
scr=pygame.display.set_mode((scr_width,scr_height))

snake_block=10
snake_width=snake_block
snake_speed=10
game_over=False

lctx=scr_width/2
lcty=scr_height/2
movex=snake_block
movey=0
check_move=0
clock=pygame.time.Clock()

foodx = round(random.randrange(0, scr_width - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, scr_height - snake_block) / 10.0) * 10.0
eat = False

length_of_snake=1
snake_list = []
snake_list.append([scr_width/2,scr_height/2])
def our_snake (snake_block,snake_list):
    for i in snake_list:
        pygame.draw.rect(scr,blue,[i[0],i[1],snake_block,snake_block])
while not game_over:
    if eat == True:
        foodx = round(random.randrange(0, scr_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, scr_height - snake_block) / 10.0) * 10.0
        eat = False
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_UP and check_move != -1:
                movey=-snake_block
                movex=0
                check_move=1
            elif event.key == pygame.K_DOWN and check_move != 1:
                movey=snake_block
                movex=0
                check_move=-1
            elif event.key == pygame.K_LEFT and check_move != -2:
                movex=-snake_block
                movey=0
                check_move=2
            elif event.key == pygame.K_RIGHT and check_move != 2:
                movex=snake_block
                movey=0
                check_move=-2
        if event.type==pygame.QUIT:
            game_over=True
    lctx+=movex
    lcty+=movey
    snake_list.append(list([lctx,lcty]))
    if lctx > scr_width or lctx < 0 or lcty > scr_height or lcty <0:
        game_over = True
    if lctx == foodx and lcty == foody:
        eat = True
        length_of_snake+=1
    if len(snake_list) != length_of_snake:
        del snake_list[0]
    for i in range(1,len(snake_list)):
        if snake_list[i] == snake_list[0]:
            game_over = True
    scr.fill(black)
    pygame.draw.rect(scr, red, [foodx, foody, snake_block, snake_block])
    our_snake(snake_block,snake_list)
    pygame.display.update()
    clock.tick(snake_speed)
msg="You lose"
font = pygame.font.SysFont(None, 50)
scr.fill(black)
text = font.render(msg,True,blue)
scr.blit(text,[scr_width/2-50,scr_height/2-25])
pygame.display.update()
time.sleep(3)
msg="Your score: "
msg+=str(length_of_snake-1)
font = pygame.font.SysFont(None, 50)
scr.fill(black)
text = font.render(msg,True,blue)
scr.blit(text,[scr_width/2-100,scr_height/2-25])
pygame.display.update()
time.sleep(3)
pygame.quit()
quit()