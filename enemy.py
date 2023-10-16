# Python Libraries
import pygame
import random

# My Files
import video_settings

class Enemy:
    fly = pygame.image.load('./images/Fly/Fly1.png')

    random_x = None
    random_y = None

    def __init__(self):
        self.get_random_coordinates_for_spawn(self.fly)


    def get_random_coordinates_for_spawn(self, entity):
        #TODO
        # Area that can NOT spawn
        # e.g. on player position

        margin = 0.2

        #x
        entity_width = entity.get_rect().width
        start_x = int(0 + (entity_width/2) - (entity_width * margin))
        end_x = int(video_settings.screen_width - (entity_width/2) + (entity_width * margin))

        self.random_x = random.randrange(start_x, end_x)
        #print('Width:', video_settings.screen_width, '- Entity Width:', entity_width, '+ Margin:', (entity_width * margin))
        #print('End X:', end_x, '| Random X', self.random_x)

        #y
        entity_height = entity.get_rect().height
        start_y = int(0 + (entity_height/2) - (entity_height * margin))
        end_y = int(video_settings.screen_height - (entity_height/2) + (entity_height * margin))

        self.random_y = random.randrange(start_y, end_y)


        # Area that can spawn
    def enemy_blit(self):
        # Center the Dot
        self.random_x += int(self.fly.get_rect().top * 0.5)
        self.random_y += int(self.fly.get_rect().left * 0.5)


        video_settings.screen.blit(self.fly, (self.random_x, self.random_y))


    def hitted(self, x, y):
        left = self.fly.get_rect().left + self.random_x
        right = self.fly.get_rect().right + self.random_x
        top = self.fly.get_rect().top + self.random_y
        bottom = self.fly.get_rect().bottom + self.random_y

        if left <= x <= right and top <= y <= bottom:
            return True
        else:
            return False
