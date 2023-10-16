# Python Libraries
import pygame
import sys

# My Files
import video_settings
import renderings
import player
import enemy
import score

def main():
    pygame.init()

    video_settings.fpx_max = 60
    p1 = player.Player()
    player_x_input = player_y_input = None
    move = False
    continue_move = False

    e1 = enemy.Enemy()

    s1 = score.Ui(300, 100, (0, 150, 255), 3, 5)

    loop_continue = True
    while loop_continue:
        for event in pygame.event.get():
            # Close Program
            if event.type == pygame.QUIT:
                loop_continue = False


            # Move Player
            if event.type == pygame.MOUSEBUTTONDOWN: # 1025
                player_x_input, player_y_input = event.pos
                move = True
                continue_move = True
                if e1.hitted(player_x_input, player_y_input):
                    continue_move = False
                    move = False
                    e1 = mob_reset(e1)
                    s1.counter_add(1)


            if event.type == pygame.MOUSEBUTTONUP:
                continue_move = False

            if event.type == pygame.MOUSEMOTION and continue_move:
                player_x_input, player_y_input = event.pos

            # Stop Player
            if event.type == pygame.KEYDOWN and event.unicode == 's':  # 768
                continue_move = False
                move = False
                p1.movement_stop()
            # End Loop

        # Draw Score Board

        #renderings.background()
        #renderings.menu_welcome()
        if player_x_input is None:
            player_x_input = p1.location_x_spawn
            player_y_input = p1.location_y_spawn

        player_speed = 0
        while player_speed < (240 / video_settings.fpx_max):
            if move:
                p1.location_move(player_x_input, player_y_input)
            player_speed += 1
        p1.blit_player()
        e1.enemy_blit()

        # Blit Score
        s1.box_blit()
        s1.text_blit()


        # FPS part 2
        video_settings.fps_display()

        # Refresh Screen
        video_settings.screen_windows()
    # End Loop


    # Shot Down the Program
    pygame.quit()
    sys.exit()  # thi command stops the code


# Funny Functions
def mob_reset(e: enemy):
    e = None
    return enemy.Enemy()


if __name__ == '__main__':
    main()