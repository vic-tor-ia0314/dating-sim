import pygame
import sys
import time
import math

pygame.init()

WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dating Sim")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
pygame.font.init()
font = pygame.font.SysFont("arial", 28)

background = pygame.Surface((WIDTH, HEIGHT))
background.fill((180, 210, 250))  # light sky-blue background

character = pygame.Surface((300, 400), pygame.SRCALPHA)
pygame.draw.rect(character, (255, 180, 180), character.get_rect())  # pink placeholder box

# Dialogue
dialogue = [
    "You wake up in a quiet room.",
    "A mysterious figure appears...",
    "They smile: 'Welcome to our world.'",
    "End of demo!"
]
current_line = 0

# Dialogue box area
dialogue_box = pygame.Rect(50, HEIGHT - 150, WIDTH - 100, 100)

# ---------------------
# Main Loop
# ---------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Advance dialogue
                current_line += 1
                if current_line >= len(dialogue):
                    running = False

    # Draw background
    screen.blit(background, (0, 0))

    # Draw character
    screen.blit(character, (WIDTH//2 - 150, HEIGHT//2 - 200))

    # Draw dialogue box
    pygame.draw.rect(screen, WHITE, dialogue_box)
    pygame.draw.rect(screen, BLACK, dialogue_box, 3)  # border

    # Render current text
    if current_line < len(dialogue):
        text_surface = font.render(dialogue[current_line], True, BLACK)
        screen.blit(text_surface, (dialogue_box.x + 20, dialogue_box.y + 30))

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()