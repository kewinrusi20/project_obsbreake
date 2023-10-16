# Python Libraries
import pygame

pygame.display.set_caption('SpaceForce')

# SCREEN ---------------------------------------------------------------------------
screen_width = 1500
screen_height = 800
flag = pygame.HWSURFACE | pygame.DOUBLEBUF
screen = pygame.display.set_mode((screen_width, screen_height), flag)


def screen_windows():
    clock.tick(fpx_max)
    pygame.display.update()  # alternative: `.flip()`
    #screen.fill((0, 0, 0))


# FPS ------------------------------------------------------------------------------
clock = pygame.time.Clock()
fpx_max: int = 60


def fps_display():
    fps_font = pygame.font.Font(None, 28)
    fps_font_color = (200, 100, 0)
    fps_text = f"{int(clock.get_fps())}"
    fps_anti_aliasing = True
    
    fps_render = fps_font.render(fps_text, fps_anti_aliasing, fps_font_color)
    screen.blit(fps_render, (screen_width - fps_render.get_rect().width - 5, 2))
