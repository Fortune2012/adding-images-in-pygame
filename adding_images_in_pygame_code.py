import pygame

#initialize pygam and screen direction
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

#initialize display surface and set title
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding image and background image')

#Load and scale images directly
background_image = pygame.transform.scale(
    pygame.image.load("baccc.jpeg").convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT),

)

penguin_image = pygame.transform.scale(
    pygame.image.load('hello.png').convert_alpha(), (200, 200))
penguin_react = penguin_image.get_rect(center = (SCREEN_WIDTH // 2,
                                                 SCREEN_HEIGHT // 2-30))

#INITIALIZE FONT,RENDER TEXT, AND SET TEXT POSITION
text = pygame.font.Font(None, 36).render('Hello world', True,
                                         pygame.color('black'))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2 , SCREEN_HEIGHT // 2 + 110))