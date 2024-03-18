import pygame
from Config import *
pygame.init()
pygame.font.init()

# Open a new window
size = (1920, 1080)
screen = pygame.display.set_mode(size)
# Toggle fullscreen --------------- dont add until minimise and close button
# pygame.display.toggle_fullscreen()
pygame.display.set_caption("Pineapple")

# Background
screen.fill(CYAN)
# screen.fill(YELLOW, (0, 0, screen.get_height()// 2, screen.get_width()))
screen.fill(YELLOW, (0, (screen.get_height()// 3) * 2, 1920, screen.get_height()// 3))
pygame.display.flip()

# Get the screen dimensions
width = screen.get_width()
height = screen.get_height()

# Render "Quit" text
quit_text = button_font.render('Quit', True, button)

# Render "Minimize" text
minimize_text = button_font.render('Minimize', True, button)

while True:
    # Get mouse position
    mouse = pygame.mouse.get_pos()

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            # Checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:
            # The game is terminated
            if width - 140 <= mouse[0] <= width and 0 <= mouse[1] <= 40:
                pygame.quit()

            # Check if the mouse is clicked on the "Minimize" button
            elif width - 2 * button_width <= mouse[0] <= width - button_width and 0 <= mouse[1] <= button_height:
                pygame.display.iconify()

    # if mouse is hovered on a button it changes to lighter shade
    if width - 140 <= mouse[0] <= width and 0 <= mouse[1] <= 40:
        pygame.draw.rect(screen, BUTTON_BACKGROUND_COLOR, [width - 140, 0, 140, 40])

    else:
        pygame.draw.rect(screen, ACTIVE_BUTTON_BACKGROUND_COLOR, [width - 140, 0, 140, 40])

    # Draw minimise button
    if width - 2 * button_width <= mouse[0] <= width - button_width and 0 <= mouse[1] <= button_height:
        pygame.draw.rect(screen, BUTTON_BACKGROUND_COLOR, [width - 2 * button_width, 0, button_width, button_height])
    else:
        pygame.draw.rect(screen, ACTIVE_BUTTON_BACKGROUND_COLOR, [width - 2 * button_width, 0, button_width, button_height])

    # Calculate the center of the buttons
    button_center_x_quit = width - button_width + button_width // 2
    button_center_y = button_height // 2

    button_center_x_minimize = width - 2 * button_width + button_width // 2

    # Calculate the position to center the "Quit" text within the "Quit" button
    quit_text_x = button_center_x_quit - quit_text.get_width() // 2
    quit_text_y = button_center_y - quit_text.get_height() // 2

    # Calculate the position to center the "Minimize" text within the "Minimize" button
    minimize_text_x = button_center_x_minimize - minimize_text.get_width() // 2
    minimize_text_y = button_center_y - minimize_text.get_height() // 2

    # Superimpose "Quit" text onto the "Quit" button
    screen.blit(quit_text, (quit_text_x, quit_text_y))

    # Superimpose "Minimize" text onto the "Minimize" button
    screen.blit(minimize_text, (minimize_text_x, minimize_text_y))

    # Updates the frames of the game
    pygame.display.update()


# Close the window
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

