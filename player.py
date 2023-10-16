# Python Libraries
import pygame
import math

# My Files
import video_settings

class Player:
    img = None
    player_height = None
    player_width = None
    location_y_curr = None
    location_x_curr = None


    def __init__(self):
        self.image_set()
        self.location_default()
        self.blit_player()

    def image_set(self):
        self.img = pygame.image.load('images/rock/rock.png')
        self.player_width = 50
        self.player_height = 50
        self.img = pygame.transform.scale(self.img, (self.player_width, self.player_height))


    def location_default(self):
        self.location_x_des = self.location_x_curr = self.location_x_spawn = (video_settings.screen_width / 2) - (self.player_width / 2)
        self.location_y_des = self.location_y_curr = self.location_y_spawn = (video_settings.screen_height / 2) - (self.player_height / 2)

# ------------------------------------------------------------------------------------------------------------------------------------------------

    def movement_stop(self):
        self.location_move(self.location_x_curr, self.location_y_curr)


    def location_teleport(self, location_x_des, location_y_des):
        self.location_x_curr = location_x_des
        self.location_y_curr = location_y_des


    def location_move(self, location_x_des, location_y_des):
        # Set Variable to the Object
        self.location_x_des = location_x_des
        self.location_y_des = location_y_des

        if self.location_x_des is not None:
            cathete_x = int(self.location_x_des) - int(self.location_x_curr)
            cathete_y = int(self.location_y_des) - int(self.location_y_curr)
            hypotenuse = math.sqrt(math.pow(cathete_x, 2) + math.pow(cathete_y, 2))

            if hypotenuse > 0:
                self.location_x_curr += (cathete_x / hypotenuse)
                self.location_y_curr += (cathete_y / hypotenuse)
                #print(self.location_x_curr)

            # Teleport to Destination if close enough
            if hypotenuse < 1:
                self.location_teleport(location_x_des, location_y_des)

    def blit_player(self):
        video_settings.screen.blit(self.img, (self.location_x_curr, self.location_y_curr))