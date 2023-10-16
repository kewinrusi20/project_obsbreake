import math

import pygame
import video_settings

rock_height = 50
rock_width = 50
x_curr = x_start = (video_settings.screen_width / 2) - (rock_width / 2)
y_curr = y_start = (video_settings.screen_height / 2) - (rock_height / 2)
stop = False


img_rock = pygame.image.load('images/rock/rock.png')
img_rock = pygame.transform.scale(img_rock, (rock_width, rock_height))

def player_main(x_input, y_input):
    player_move(x_input, y_input)


def player_move(x_des, y_des):
    global x_curr, y_curr

    # Stop Player
    if stop:
        x_des = x_curr
        y_des = y_curr

    if x_des is not None and y_des is not None:
        x_diff = x_des - x_curr
        y_diff = y_des - y_curr

        dist = math.sqrt(math.pow(x_diff, 2) + math.pow(y_diff, 2))
        #print(dist)

        if dist > 0:
            x_diff /= dist
            y_diff /= dist

            x_curr += x_diff
            y_curr += y_diff

        # Teleport to Destination if close enough
        if dist < 1:
            x_curr = x_des
            y_curr = y_des

    # Blit Player
    video_settings.screen.blit(img_rock, (x_curr , y_curr))

    # Reset Destination Position
    if x_curr is x_des and y_curr is y_des:
        x_des = y_des = None

