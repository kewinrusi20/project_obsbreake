import pygame
import video_settings
import main


class Ui:
    counter_slays = 0

    def __init__(self, width, height, box_color, boss_thickness, box_border_radius):
        self.box_color = box_color
        self.boss_thickness = boss_thickness
        self.box_border_radius = box_border_radius


        self.box_rect = self.box_define(width, height)
        self.text_define()



    # --------------------------------------------------------------------------------------------------------
    # BOX

    def box_define(self, width, height):
        self.box_x = 200
        self.box_y = 200
        self.box_width = width
        self.box_height = height

        # Create Box
        return pygame.Rect(self.box_x, self.box_y, self.box_width, self.box_height)


    # Blit Box
    def box_blit(self):
        pygame.draw.rect(video_settings.screen, self.box_color, self.box_rect, self.boss_thickness, self.box_border_radius)

    # --------------------------------------------------------------------------------------------------------
    # TEXT

    def counter_add(self, counter_slays):
        self.counter_slays += counter_slays

    def text_define(self):
        self.font_color = self.box_color

        self.font = pygame.font.Font(None, 30)
        self.text_position()

    def text_refresh(self):
        self.font_render = self.font.render(f"Score: {self.counter_slays}", True, self.font_color)

    def text_position(self):
        self.spawn_text_x = 0
        self.spawn_text_y = 0

        limit_x = 10
        if (self.box_x * 0.10) > limit_x:
            self.spawn_text_x = self.box_x + 10
        else:
            self.spawn_text_x = self.box_x * 1.10

        limit_y = 12
        if (self.box_y * 0.12) > limit_y:
            self.spawn_text_y = self.box_y + 12
        else:
            self.spawn_text_y = self.box_y * 1.12


    def text_blit(self):
        self.text_refresh()
        video_settings.screen.blit(self.font_render, (self.spawn_text_x, self.spawn_text_y))

