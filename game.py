import pygame

pygame.init()

def crop_surface(new_width, new_height, crop_width, crop_height, image):
    new_surface = pygame.Surface((new_width, new_height), pygame.SRCALPHA, 32)
    new_surface.blit(image, (0,0), (crop_width, crop_height, new_width, new_height))
    return new_surface

width = 900
height = 700
screen_size = (width, height)

screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("It's a game!!")

background = pygame.image.load("D:\Downloads/grasslight-big.png").convert()
background = pygame.transform.scale(background, screen_size)
screen.blit(background, (0,0))


rescale = 3

player = pygame.image.load("D:\Downloads\kenney_sportsPack\PNG\Red\characterRed (5).png").convert_alpha()
player_width = player.get_rect().width
player_height = player.get_rect().height
player = pygame.transform.scale(player, (player_width * rescale, player_height*rescale))
player = pygame.transform.rotate(player, 90)

foot = pygame.image.load("D:\Downloads\kenney_sportsPack\PNG\Red\characterRed (13).png").convert_alpha()
foot_width = foot.get_rect().width
foot_height = foot.get_rect().height
foot = pygame.transform.scale(foot, (foot_width*rescale, foot_height*rescale))
foot = pygame.transform.rotate(foot,90)
#screen.blit(foot, (100, 85))
#screen.blit(player, (100, 110))

ball = pygame.image.load("D:\Downloads\kenney_sportsPack\PNG\Equipment\\ball_soccer2.png").convert_alpha()
ball_width = ball.get_rect().width
ball_height = ball.get_rect().height
ball = pygame.transform.scale(ball, (ball_width*2, ball_height*2))
#screen.blit(ball, (120, 50))

goal_left = pygame.image.load("D:\Downloads\kenney_sportsPack\PNG\Elements\\element (32).png").convert_alpha()
goal_left = pygame.transform.scale(goal_left, (250, 270))
gl_width = goal_left.get_rect().width
gl_height = goal_left.get_rect().height
goal_left = crop_surface(gl_width/2 + 12, gl_height/2 +12, gl_width/2 -12, gl_height/2 -12, goal_left)
screen.blit(goal_left, (0,0))




finished = False
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    pygame.display.flip()

pygame.quit()