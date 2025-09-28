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
font_dialogue = pygame.font.SysFont("arial", 28)
font_choice = pygame.font.SysFont("arial", 20)
font_dialogue_italic = pygame.font.SysFont("arial", 28, italic=True)

# Load backgrounds
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

backgrounds = {
    "title": bg_title,
    "home": bg_home,
    "cafe": bg_cafe,
    "balcony": bg_balcony,
    "mall": bg_mall,
}

# Create characters
def make_character(color):
    surf = pygame.Surface((300, 400), pygame.SRCALPHA)
    pygame.draw.rect(surf, color, surf.get_rect())
    return surf

char_stilton = make_character((255, 180, 180))
char_jinu = make_character((180, 255, 180))
char_peppa = pygame.image.load("peppa.png").convert_alpha()
char_peppa = pygame.transform.scale(char_peppa, (500, 600))
char_leader = make_character((180, 180, 0))

# ---------------------------
# Dialogue Data (steps per scenario)
# ---------------------------
scenarios = [
    {
        "name": "Initiation",
        "background": "home",
        "character": char_leader,
        "steps": [
            {"type": "dialogue", "text": "Leaders: We are gathered here today to celebrate the recruitment of another member under the watchful gaze of the Almighty One."},
            {"type": "dialogue", "text": "Leaders: Although this marks the start of your journey, there remains a final challenge for your path. In order to achieve full ascension, you must perform two sacrificial rituals to Their Greatness."},
            {"type": "choice", "options": [
                ("What does that even mean?", "Leaders: As per tradition, the arrival of new members must be balanced by the removal of current members."),
                ("Let’s freaking go.", "Leaders: As per tradition, the arrival of new members must be balanced by the removal of current members.")
            ]},
            {"type": "dialogue", "text": "Leaders: This should be relatively easy, as we have prepared a list of…. troublesome participants."},
            {"type": "choice", "options": [
                ("Wow, that is messed up...", "Leaders: You have twenty four hours until you must perform the sacrifices."),
                ("Is this a dating sim?", "Leaders: You have twenty four hours until you must perform the sacrifices.")
            ]},
            {"type": "dialogue", "text": "Leaders: Choose wisely."}
        ]
    },
    {
        "name": "At the Cafe",
        "background": "cafe",
        "character": char_stilton,
        "steps": [
            {"type": "dialogue", "text": "You exit your local cafe after ordering a drink. Someone from behind addresses you in surprise."},
            {"type": "dialogue", "text": "Geronimo: *squeak* Hey, it's you, the new member! Oh you know this café? Did you know this café gets ceremonial grade matcha from Japan?"},
            {"type": "choice", "options": [
                ("Err, matcha tastes like grass.", "Geronimo: Well, it's an acquired taste."),
                ("I know! I love their matcha!", "Geronimo: Finally, someone gets it!")
            ]},
            {"type": "dialogue", "text": "Geronimo: Anyways, what are you up to, new member? "},
            {"type": "dialogue", "text": "- Well, I’m on a break from work. It was getting a bit hectic back in the office."},
            {"type": "dialogue", "text": "Geronimo: Hey, same! My lunch break's a little short, but why complain when you're in charge, right?"},
            {"type": "dialogue", "text": "- Wow, are you a manager or something?"},
            {"type": "dialogue", "text": "Geronimo: Actually, I’m the publisher for the Rodent’s Gazette. No pictures paparazzi, I know it’s important stuff."},
            {"type": "choice", "options": [
                ("Oh my gosh, you must be so rich and talented!", "Geronimo: Haha, you know, we recently had to model an online version of our articles."),
                ("Oh...", "Geronimo: Haha, you know, we recently had to model an online version of our articles.")
            ]},
            {"type": "dialogue", "text": "Geronimo: Sure, it’s efficient, but what about the paper? The crinkle of the pages, the stories people can physically hold… that doesn’t exist on a technological device."},
            {"type": "choice", "options": [
                ("Yeah! wait, why are you listening to music then?", "Geronimo: Well, that's different."),
                ("Right...but what's with the earbuds?", "Geronimo: Well, that's different.")
            ]},
            {"type": "dialogue", "text": "Geronimo: Music itself is an art that must be appreciated, no matter its form."},
            {"type": "choice", "options": [
                ("You're so right, I love music!", "You get me! Right now, I especially love Laufey."),
                ("I guess so... what do you listen to?", "Geronimo: What am I listening to? Oh you know, some Laufey.")
            ]},
            {"type": "dialogue", "text": "Geronimo: Her latest album is ethereal, like- I can barely describe it with words… it's just so enlightening! *squeak* It really evokes the reoccurring themes of women’s struggles and men’s weaponized incompetency within relationships."},
            {"type": "choice", "options": [
                ("I lover her music! It always has so much symbolism.", " "),
                ("It's not that deep… but her music’s great.", "Of course it is that deep! Can’t you see the hidden symbolism within her lyrics, the way they embellish the instrumentational choice?! It’s like magic.")
            ]}
        ]
    },
    {
        "name": "At the Mall",
        "background": "mall",
        "character": char_peppa,
        "steps": [
            {"type": "dialogue", "text": "You had just finished your lunch break and headed back to the office building. You had bigger things to think about; today was the big day where you present next year’s plan and objectives to your boss.", "italic": True},
            {"type": "dialogue", "text": "Just as the meeting started, your boss got a phone call. As they headed into another room, you coul hear the caller’s frantic complaints.", "italic": True},
            {"type": "dialogue", "text": "Peppa: I have to get it! Daddy, you just don’t understand, it’s so important!"},
            {"type": "dialogue", "text": "The project proposition was called off due to the caller’s, quote, “tamper tantrum”. You don’t know whether you feel relieved or annoyed as your boss excused you.", "italic": True},
            {"type": "dialogue", "text": "You decided to visit the mall. Your pay check recently came into the mail and you want to cheer yourself up by buying some new clothes. After walking into the nearest chic boutique you can find, you browse. You check the price tag of a stylish pair of pants and gasp. You realize you are not part of the tax bracket that can shop here.", "italic": True},
            {"type": "dialogue", "text": "Before you can leave the boutique, you hear an impatient scoff to your right.", "italic": True},
            {"type": "dialogue", "text": "Peppa: I’m sorry, this is not the correct colour I requested! Don’t you see how it clashes with my jewellery combo and shoes? This is unnaceptable!"},
            {"type": "dialogue", "text": "A few employees around you immediately jump to action, scurrying about and frantically piling clothes in their arms. You turn around and face the person screaming.", "italic": True},
            {"type": "dialogue", "text": "Peppa: *oink* Oh my gosh, I love your necklace! You must tell me where you got it, I literally have a pair of earrings with the same style!"},
            {"type": "dialogue", "text": "- Thank you so much! Actually, I got this from my mother."},
            {"type": "dialogue", "text": "Peppa: Awh, that is so sweet. What a shame though, it really is one of a kind."},
            {"type": "dialogue", "text": "Peppa: Anyways, I’m trying to get a new outfit for my daddy’s company ceremony tomorrow, but these workers are so slow! Ugh, they should know I could get them fired."},
            {"type": "choice", "options": [
                ("That’s kind of rude. They’re just doing their job.", "Peppa: Well, I’m just saying! If they really care about their business, they should prioritize their well-paying customers! *ahem* The sequin top goes here!"),
                ("Companies will hire anyone these days.", "Peppa: Exactly! Hey, they finally got some of my stuff right! Sequin top over here!")
            ]},
            {"type": "dialogue", "text": "Peppa: Wow, this is perfect! I’m definitely getting this!"},
            {"type": "dialogue", "text": "Peppa struts over to the cashier and motions at them to scan it. After a moment, the register display shows the price of the top: $100,000. Peppa takes out a silver card and swipes. Nothing happens. She swipes it again, and again, but nothing happens.", "italic": True},
            {"type": "dialogue", "text": "Peppa: Uhm, now that is just hilarious! ___ we might have a problem…. My card’s at its spending limit, ugh! Can you please cover me?!"},
            {"type": "choice", "options": [
                ("Uh, I literally don’t know you…. also, that’s way too expensive.", "Peppa: I thought we were on the same page! Ugh, way to make someone feel welcomed. Whatever, I always have my daddy’s card with me for cases like this. A girl’s gotta stay prepared! *oink oink*"),
                ("I'd love to, bit mine's also maxxed out. Maybe another time or-", "Peppa: Oh, don’t you worry! I was joking, silly. For cases like these, I always have my daddy’s card with me. A girl’s gotta stay prepared!")
            ]},
            {"type": "dialogue", "text": "You stare in astonishment as she takes out a gold coloured card and swipes. Sure enough, the transaction completes and the employee rushes to bag the garment.", "italic": True}
        ]
    },
    {
        "name": "At the Balcony",
        "background": "balcony",
        "character": char_jinu,
        "steps": [
            {"type": "dialogue", "text": "Jinu: wassup bbg"},
            {"type": "choice", "options": [
                ("heyy", "Jinu: heyy bbg"),
                ("ew", "Jinu: cmon don't be like that")
            ]},
            {"type": "dialogue", "text": "Jinu: Let's enjoy the view together!"}
        ]
    }
]

# ---------------------------
# Game State
# ---------------------------
current_scenario_index = 0
current_scenario = scenarios[current_scenario_index]
current_step_index = 0
current_step = current_scenario["steps"][current_step_index]
response_text = ""

STATE_TITLE = "title"
STATE_DIALOGUE = "dialogue"
STATE_CHOICES = "choices"
STATE_RESPONSE = "response"
state = STATE_TITLE  # start at title screen

# Dialogue and choice boxes
dialogue_box = pygame.Rect(50, HEIGHT - 200, WIDTH - 100, 150)
choice_boxes = [
    pygame.Rect(150, HEIGHT - 80, 400, 50),
    pygame.Rect(650, HEIGHT - 80, 400, 50)
]

def draw_text_wrapped(text, font, color, rect, surface, line_spacing=5, padding=10):
    words = text.split(' ')
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] > rect.width - 2*padding:
            lines.append(current_line)
            current_line = word + " "
        else:
            current_line = test_line
    lines.append(current_line)

    y_offset = padding
    for line in lines:
        text_surface = font.render(line.strip(), True, color)
        surface.blit(text_surface, (rect.x + padding, rect.y + y_offset))
        y_offset += font.get_height() + line_spacing

# ---------------------------
# Drawing Functions
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
        font_to_use = font_dialogue_italic if current_step.get("italic") else font_dialogue
        draw_text_wrapped(current_step["text"], font_dialogue, BLACK, dialogue_box, screen)
    elif state == STATE_RESPONSE:
        draw_text_wrapped(response_text, font_dialogue, BLACK, dialogue_box, screen)
    elif state == STATE_CHOICES:
        for i, box in enumerate(choice_boxes):
            pygame.draw.rect(screen, LIGHTBLUE, box)
            pygame.draw.rect(screen, BLACK, box, 2)
            draw_text_wrapped(current_step["options"][i][0], font_choice, BLACK, box, screen)

# ---------------------------
# Main Loop
# ---------------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # TITLE SCREEN
        if state == STATE_TITLE:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                state = STATE_DIALOGUE  # move to first scenario

        # DIALOGUE
        elif state == STATE_DIALOGUE:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                current_step_index += 1
                if current_step_index < len(current_scenario["steps"]):
                    current_step = current_scenario["steps"][current_step_index]
                    state = STATE_CHOICES if current_step["type"] == "choice" else STATE_DIALOGUE
                else:
                    current_scenario_index += 1
                    if current_scenario_index < len(scenarios):
                        current_scenario = scenarios[current_scenario_index]
                        current_step_index = 0
                        current_step = current_scenario["steps"][current_step_index]
                        state = STATE_DIALOGUE if current_step["type"] == "dialogue" else STATE_CHOICES
                    else:
                        running = False

        # CHOICES
        elif state == STATE_CHOICES:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, box in enumerate(choice_boxes):
                    if box.collidepoint(event.pos):
                        response_text = current_step["options"][i][1]
                        state = STATE_RESPONSE

        # RESPONSE
        elif state == STATE_RESPONSE:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                current_step_index += 1
                if current_step_index < len(current_scenario["steps"]):
                    current_step = current_scenario["steps"][current_step_index]
                    state = STATE_CHOICES if current_step["type"] == "choice" else STATE_DIALOGUE
                else:
                    current_scenario_index += 1
                    if current_scenario_index < len(scenarios):
                        current_scenario = scenarios[current_scenario_index]
                        current_step_index = 0
                        current_step = current_scenario["steps"][current_step_index]
                        state = STATE_DIALOGUE if current_step["type"] == "dialogue" else STATE_CHOICES
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