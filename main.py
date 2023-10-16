# Python Libraries
import pygame
import sys

# My Files
import video_settings
import renderings
import player
import enemy

def main():
    pygame.init()
    e1 = enemy.Enemy()
    p1 = player.Player()
    player_x_input = player_y_input = None
    move = False

    continue_move = False
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





        renderings.background()
        #renderings.menu_welcome()
        if player_x_input is None:
            player_x_input = p1.location_x_spawn
            player_y_input = p1.location_y_spawn

        if move:
            p1.location_move(player_x_input, player_y_input)
        p1.blit_player()
        e1.enemy_blit()


        # FPS
        video_settings.fpx_max = 60
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