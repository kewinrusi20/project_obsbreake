# python libraries
import pygame
import sys

# my files
import video_settings
import renderings
import player
import enemy


def main():
    pygame.init()
    e1 = enemy.Enemy()

    player_x_input = player_y_input = None
    continue_move = False
    loop_continue = True
    while loop_continue:
        for event in pygame.event.get():
            #print(event)

            # Close Program
            if event.type == pygame.QUIT:
                loop_continue = False


            # Move Player
            if event.type == pygame.MOUSEBUTTONDOWN: # 1025
                player_x_input, player_y_input = event.pos
                continue_move = True
                player.stop = False
                if e1.hitbox(player_x_input, player_y_input):
                    player.stop = True
                    e1 = None
                    e1 = enemy.Enemy()



            if continue_move:
                if event.type == pygame.MOUSEBUTTONUP:
                    player_x_input, player_y_input = event.pos
                    continue_move = False

                if event.type == pygame.MOUSEMOTION:
                    player_x_input, player_y_input = event.pos
                    player.stop = False





            # Stop Player
            if event.type == 768 and event.unicode == 's':
                player.stop = True


        renderings.background()
        #renderings.menu_welcome()

        player.player_main(player_x_input, player_y_input)
        e1.enemy_blit()


        # FPS
        video_settings.fpx_max = 60
        video_settings.fps_display()

        # Refresh Screen
        video_settings.screen_windows()

    # Shot Down the Program
    pygame.quit()
    sys.exit()  # thi command stops the code

if __name__ == '__main__':
    main()