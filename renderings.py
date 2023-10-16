# Python Libraries
import pygame

# My Files
import video_settings


def menu_welcome():
    render_content()
    render_box()
    blit_box()
    blit_content()


def render_content():
    # Menu Content's List
    menu_default = {
        'welcome': {'text': 'Yo'},
        'continue': {'text': 'Continue', 'status': True},
        'new': {'text': 'New Game'},
        'load': {'text': 'Load Game', 'status': False},
        'settings': {'text': 'Settings'},
        'exit': {'text': 'Exit'}
    }

    font = pygame.font.Font('./fonts/Roboto-Bold.ttf', 30,)
    font.set_bold(False)
    font_color = (0, 0, 0)
    global menu_rendered
    menu_rendered = []

    # Render Menu Content
    for key, value in menu_default.items():
        # Exclude the Title
        if key == 'welcome':
            continue
        # Exclude the disable Options
        elif 'status' in value and value['status'] is False:
            continue
        else:
            menu_rendered.append(font.render(f"{value['text']}", True, font_color))


def render_box():
    box_width = 200
    global box_x
    box_x = video_settings.screen_width - box_width - 50
    global box_y
    box_y = 50

    # Fix height
    box_height = 0 # default size
    for element in menu_rendered:
        box_height += element.get_rect().height

    # Render Menu Box
    global box
    box = pygame.Rect(box_x, box_y, box_width, box_height)


def blit_box():
    screen = video_settings.screen
    thickness = 5
    border_radius = 10
    color = (255, 255, 255)
    pygame.draw.rect(screen, color, box, thickness, border_radius)


def blit_content():
    text_x = box_x + 10
    text_y = box_y

    # Blit Menu Content
    for counter, element in enumerate(menu_rendered):
        video_settings.screen.blit(element, (text_x, text_y))
        # Exclude last iteration
        if counter < len(menu_rendered) -1:
            text_y += element.get_rect().height

img_sky = pygame.image.load('images/sky.png')
img_ground = pygame.image.load('images/ground.png')
img_dirt = pygame.image.load('images/dirt.jpg')
img_dirt = pygame.transform.scale(img_dirt, (video_settings.screen_width, video_settings.screen_height))

def background():
    video_settings.screen.blit(img_dirt, (0, 0))
    #video_settings.screen.blit(img_sky, (0, 0))
    #video_settings.screen.blit(img_ground, (0, 300))
    # WuW
