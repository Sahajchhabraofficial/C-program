import pygame
root=pygame.init()
window=pygame.display.set_mode((600,400))
pygame.display.set_caption("Sahaj's first game")
exit_game=False
game_over=False

# game loop 
while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True

pygame.quit()
quit()
