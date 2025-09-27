import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dating Sim")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 150, 255)
LIGHTBLUE = (150, 200, 255)

font_title = pygame.font.SysFont("arial", 72)
font_button = pygame.font.SysFont("arial", 40)
font_dialogue = pygame.font.SysFont("arial", 28)
font_choice = pygame.font.SysFont("arial", 32)

bg_title = pygame.image.load(r"tree.jpg").convert()
bg_title = pygame.transform.scale(bg_title, (WIDTH, HEIGHT))

bg_home = pygame.image.load(r"home.jpg").convert()
bg_home = pygame.transform.scale(bg_home, (WIDTH, HEIGHT))

bg_cafe = pygame.image.load(r"cafe.jpg").convert()
bg_cafe = pygame.transform.scale(bg_cafe, (WIDTH, HEIGHT))

bg_balcony = pygame.image.load(r"balcony.jpg").convert()
bg_balcony = pygame.transform.scale(bg_balcony, (WIDTH, HEIGHT))

bg_mall = pygame.image.load(r"mall.jpg").convert()
bg_mall = pygame.transform.scale(bg_mall, (WIDTH, HEIGHT))

character = pygame.Surface((300, 400), pygame.SRCALPHA)
pygame.draw.rect(character, (255, 180, 180), character.get_rect())


backgrounds = {
    "title": bg_title,
    "home": bg_home,
    "cafe": bg_cafe,
    "balcony": bg_balcony,
    "mall": bg_mall
}

def make_character(color):
    surf = pygame.Surface((300, 400), pygame.SRCALPHA)
    pygame.draw.rect(surf, color, surf.get_rect())
    return surf

char_stilton = make_character((255, 180, 180))
char_jinu = make_character((180, 255, 180))
char_peppa = make_character((180, 180, 255))

# ---------------------------
# Dialogue Data
# ---------------------------
scenarios = [
    {
        "name": "At the Cafe",
        "background": "cafe",
        "character": char_stilton,
        "dialogue": "Geronimo: *squeak* Hey, it's you! Oh you know this café? Did you know that they get their ceremonial grade matcha imported from Japan itself.",
        "choices": [
            ("Err, matcha tastes like grass, so I usually order from their tea selection.", "Geronimo: Well, it's an acquired taste. Not many people get it."),
            ("I know! I love their matcha, it's so high quality!", "Geronimo: Finally, someone gets it!")
        ]
    },
    {
        "name": "At the Mall",
        "background": "mall",
        "character": char_peppa,
        "dialogue": "Peppa: hi",
        "choices": [
            ("hi", "Peppa: wasssup"),
            ("bye", "Peppa: aww")
        ]
    },
    {
        "name": "At the Balcony",
        "background": "balcony",
        "character": char_jinu,
        "dialogue": "Jinu: wassup bbg",
        "choices": [
            ("heyy", "Jinu: heyy bbg"),
            ("ew", "Jinu: cmon don't be like that")
        ]
    }
]

current_scenario_index = 0
current_scenario = scenarios[current_scenario_index]

# ---------------------------
# UI Elements
# ---------------------------
dialogue_box = pygame.Rect(50, HEIGHT - 200, WIDTH - 100, 100)
choice_boxes = [
    pygame.Rect(150, HEIGHT - 80, 400, 50),
    pygame.Rect(650, HEIGHT - 80, 400, 50)
]

# ---------------------------
# States
# ---------------------------
STATE_TITLE = "title"
STATE_DIALOGUE = "dialogue"
STATE_CHOICES = "choices"
STATE_RESPONSE = "response"
state = STATE_TITLE

choice_text = ""
response_text = ""

# ---------------------------
# Draw Functions
# ---------------------------
def draw_title():
    screen.blit(backgrounds["title"], (0, 0))
    title_surface = font_title.render("Dating Sim", True, WHITE)
    title_rect = title_surface.get_rect(center=(WIDTH//2, HEIGHT//3))
    screen.blit(title_surface, title_rect)

    subtitle = font_dialogue.render("Press SPACE to Start", True, WHITE)
    sub_rect = subtitle.get_rect(center=(WIDTH//2, HEIGHT//2 + 50))
    screen.blit(subtitle, sub_rect)

def draw_scenario():
    # background and character
    screen.blit(backgrounds[current_scenario["background"]], (0, 0))
    screen.blit(current_scenario["character"], (WIDTH//2 - 150, HEIGHT//2 - 250))

    # dialogue box
    pygame.draw.rect(screen, WHITE, dialogue_box)
    pygame.draw.rect(screen, BLACK, dialogue_box, 3)

    if state == STATE_DIALOGUE:
        text_surface = font_dialogue.render(current_scenario["dialogue"], True, BLACK)
        screen.blit(text_surface, (dialogue_box.x + 20, dialogue_box.y + 30))

    elif state == STATE_RESPONSE:
        text_surface = font_dialogue.render(response_text, True, BLACK)
        screen.blit(text_surface, (dialogue_box.x + 20, dialogue_box.y + 30))

    # choices
    if state == STATE_CHOICES:
        for i, box in enumerate(choice_boxes):
            pygame.draw.rect(screen, LIGHTBLUE, box)
            pygame.draw.rect(screen, BLACK, box, 2)
            choice_text = current_scenario["choices"][i][0]
            txt = font_choice.render(choice_text, True, BLACK)
            txt_rect = txt.get_rect(center=box.center)
            screen.blit(txt, txt_rect)

# ---------------------------
# Main Loop
# ---------------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if state == STATE_TITLE:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                state = STATE_DIALOGUE

        elif state == STATE_DIALOGUE:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                state = STATE_CHOICES

        elif state == STATE_CHOICES:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, box in enumerate(choice_boxes):
                    if box.collidepoint(event.pos):
                        # pick this choice
                        response_text = current_scenario["choices"][i][1]
                        state = STATE_RESPONSE

        elif state == STATE_RESPONSE:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                current_scenario_index += 1
                if current_scenario_index < len(scenarios):
                    current_scenario = scenarios[current_scenario_index]
                    state = STATE_DIALOGUE
                else:
                    running = False

    # Draw based on state
    if state == STATE_TITLE:
        draw_title()
    else:
        draw_scenario()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
