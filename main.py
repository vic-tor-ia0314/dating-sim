import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dating Sim")

clock = pygame.time.Clock()

WHITE = (250, 157, 150) #acc light pink, too lazy to change lmao
BLACK = (0, 0, 0)
LIGHTBLUE = (255, 89, 133) #acc dark pink, too lazy to change as well

font_title = pygame.font.SysFont("timesnewroman", 72)
font_dialogue = pygame.font.SysFont("timesnewroman", 28)
font_choice = pygame.font.SysFont("timesnewroman", 20)
font_dialogue_italic = pygame.font.SysFont("timesnewroman", 28, italic=True)


bg_title = pygame.image.load(r"tree.jpg").convert()
bg_title = pygame.transform.scale(bg_title, (WIDTH, HEIGHT))

bg_home = pygame.image.load(r"home.jpeg").convert()
bg_home = pygame.transform.scale(bg_home, (WIDTH, HEIGHT))

bg_cafe = pygame.image.load(r"cafe.jpeg").convert()
bg_cafe = pygame.transform.scale(bg_cafe, (WIDTH, HEIGHT))

bg_balcony = pygame.image.load(r"balcony.jpeg").convert()
bg_balcony = pygame.transform.scale(bg_balcony, (WIDTH, HEIGHT))

bg_mall = pygame.image.load(r"mall.jpeg").convert()
bg_mall = pygame.transform.scale(bg_mall, (WIDTH, HEIGHT))

bg_void = pygame.image.load(r"void.jpg").convert()
bg_void = pygame.transform.scale(bg_void, (WIDTH, HEIGHT))

backgrounds = {
    "title": bg_title,
    "home": bg_home,
    "cafe": bg_cafe,
    "balcony": bg_balcony,
    "mall": bg_mall,
    "void": bg_void
}


char_stilton = pygame.image.load("stilton.png").convert_alpha()
char_stilton = pygame.transform.scale(char_stilton, (600, 600))

char_jinu = pygame.image.load("jinu.png").convert_alpha()
char_jinu = pygame.transform.scale(char_jinu, (450, 600))

char_peppa = pygame.image.load("peppa.png").convert_alpha()
char_peppa = pygame.transform.scale(char_peppa, (450, 600))

char_leader = pygame.image.load("leader.webp").convert_alpha()
char_leader = pygame.transform.scale(char_leader, (500, 500))


scenarios = [
    {
        "name": "Initiation",
        "background": "home",
        "character": char_leader,
        "steps": [
            {"type": "dialogue", "text": "Leader: We are gathered here today to celebrate the recruitment of another member under the watchful gaze of the Almighty One."},
            {"type": "dialogue", "text": "Leader: Although this marks the start of your journey, there remains a final challenge for your path. In order to achieve full ascension, you must perform two sacrificial rituals to Their Greatness."},
            {"type": "choice", "options": [
                ("What does that even mean?", "Leader: As per tradition, the arrival of new members must be balanced by the removal of current members."),
                ("Let’s freaking go.", "Leader: As per tradition, the arrival of new members must be balanced by the removal of current members.")
            ]},
            {"type": "dialogue", "text": "Leader: This should be relatively easy, as we have prepared a list of…. troublesome participants."},
            {"type": "choice", "options": [
                ("Wow, that is messed up...", "Leader: You have twenty four hours until you must perform the sacrifices."),
                ("Is this a dating sim?", "Leader: You have twenty four hours until you must perform the sacrifices.")
            ]},
            {"type": "dialogue", "text": "Leader: Choose wisely."}
        ]
    },
    {
        "name": "At the Cafe",
        "background": "cafe",
        "character": char_stilton,
        "steps": [
            {"type": "dialogue", "text": "After contemplating, you decide to take a break by visiting a cafe. You exit your local cafe after ordering a drink. Someone from behind addresses you in surprise."},
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
                ("I lover her music! It always has so much symbolism.", "Sometimes songs get so emotional that I tear up…. Man, music is one of mankind’s greatest achievements. It’s practically magic."),
                ("It's not that deep… but her music’s great.", "Of course it is that deep! Can’t you see the hidden symbolism within her lyrics, the way they embellish the instrumentational choice?! It’s practically magic-")
            ]},
            {"type": "dialogue", "text": "You get a message from your supervisor, asking you to head back to the building."},
            {"type": "dialogue", "text": "Geronimo: Hey, we should totally read some of the new releases from the bookstore. I heard there were some female authors."},
            {"type": "choice", "options": [
                ("I'm so sorry, I have to go right now. But we can later!", "Geronimo: Wait-"),
                ("Yeah, no. Bye.", "Geronimo: wait-")
            ]},
            {"type": "dialogue", "text": "- See you later!"},
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
            {"type": "dialogue", "text": "The project proposition was called off due to the caller’s, quote, “temper tantrum”. You don’t know whether you feel relieved or annoyed as your boss excused you.", "italic": True},
            {"type": "dialogue", "text": "You decided to visit the mall. Your pay check recently came into the mail and you want to cheer yourself up by buying some new clothes. After walking into the nearest chic boutique you can find, you browse. You check the price tag of a stylish pair of pants and gasp. You realize you are not part of the tax bracket that can shop here.", "italic": True},
            {"type": "dialogue", "text": "Before you can leave the boutique, you hear an impatient scoff to your right.", "italic": True},
            {"type": "dialogue", "text": "Peppa: I’m sorry, this is not the correct colour I requested! Don’t you see how it clashes with my jewellery combo and shoes? This is unnacceptable!"},
            {"type": "dialogue", "text": "A few employees around you immediately jump to action, scurrying about and frantically piling clothes in their arms. You turn around and face the person screaming.", "italic": True},
            {"type": "dialogue", "text": "Peppa: *oink* Oh my gosh, I love your necklace! You must tell me where you got it, I literally have a pair of earrings with the same style!"},
            {"type": "dialogue", "text": "- Thank you so much! Actually, I got this from my mother. She's dead..."},
            {"type": "dialogue", "text": "Peppa: Awh, that is so sweet. What a shame though, it really is one of a kind."},
            {"type": "dialogue", "text": "Peppa: Anyways, I’m trying to get a new outfit for my daddy’s company ceremony tomorrow, but these workers are so slow! Ugh, they should know I could get them fired."},
            {"type": "choice", "options": [
                ("That’s kind of rude. They’re just doing their job.", "Peppa: Well, I’m just saying! If they really care about their business, they should prioritize their well-paying customers! *ahem* The sequin top goes here!"),
                ("Companies will hire anyone these days.", "Peppa: Exactly! Hey, they finally got some of my stuff right! Sequin top over here!")
            ]},
            {"type": "dialogue", "text": "Peppa: Wow, this is perfect! I’m definitely getting this!"},
            {"type": "dialogue", "text": "Peppa struts over to the cashier and motions at them to scan it. After a moment, the register display shows the price of the top: $100,000. Peppa takes out a silver card and swipes. Nothing happens. She swipes it again, and again, but nothing happens.", "italic": True},
            {"type": "dialogue", "text": "Peppa: Uhm, now that is just hilarious! Y/N, we might have a problem…. My card’s at its spending limit, ugh! Can you please cover me?!"},
            {"type": "choice", "options": [
                ("Uh, I literally don’t know you…. also, that’s way too expensive.", "Peppa: I thought we were on the same page! Ugh, way to make someone feel welcomed. Whatever, I always have my daddy’s card with me for cases like this. A girl’s gotta stay prepared! *oink oink*"),
                ("I'd love to, bit mine's also maxxed out. Maybe another time or-", "Peppa: Oh, don’t you worry! I was joking, silly. For cases like these, I always have my daddy’s card with me. A girl’s gotta stay prepared!")
            ]},
            {"type": "dialogue", "text": "You stare in astonishment as she takes out a gold coloured card and swipes. Sure enough, the transaction completes and the employee rushes to bag the garment.", "italic": True},
            {"type": "dialogue", "text": "Peppa: Alright, now I have the top, the heels, the skirt…. Maybe I need a matching skirt!"},
            {"type": "choice", "options": [
                ("Yes! Match the fit!", "Peppa: You get me! It’s an art, a lifestyle."),
                ("You buy a lot of stuff.", "Peppa: It’s not just about the items, ugh! This lifestyle is a mindset, and I’m embracing it!")
            ]},
            {"type": "dialogue", "text": "Peppa: I’m heading out now! Tell me if you see any cute handbags at the next meeting!"},
            {"type": "dialogue", "text": "Peppa trots away with her shopping bags, leaving you in the boutique."}
        ]
    },
    {
        "name": "At the Balcony",
        "background": "balcony",
        "character": char_jinu,
        "steps": [
            {"type": "dialogue", "text": "Today has been long and exhausting. You hurry home and order a healthy amount of McDonald’s. By the time you finish your meal, the sky has darkened and the moon is already out. You decide to head to the patio on your apartment's top floor for some fresh air."},
            {"type": "dialogue", "text": "As you step outside, you notice someone is already there. They are standing at the edge of the balcony, staring up at the stars. They turn as they hear you approach."},
            {"type": "dialogue", "text": "Jinu: The moon’s beautiful tonight, isn’t it?"},
            {"type": "dialogue", "text": "- Yeah, it is."},
            {"type": "dialogue", "text": "Jinu: I like this part of town. It’s calm and peaceful."},
            {"type": "choice", "options": [
                ("Yeah, a perfect place to get away from all the hustle and bustle.", "Jinu: Reminds me of my hometown… Enough about that- oh my gosh are you wearing teddy bear pajamas?"),
                ("Yup. Great observational skills.", "Jinu: *chuckles* Great comeback, especially from someone who’s in their pajamas. Are those choo-choo trains and teddy bear patterns?")
            ]},
            {"type": "dialogue", "text": "Your face flushes in embarassment as you realize you are in fact standing on the patio in your pajamas with a stranger."},
            {"type": "dialogue", "text": "Jinu: It’s alright, don’t worry. I won’t tell anyone about your…. interesting outfit style. After all, everyone has their preferences."},
            {"type": "choice", "options": [
                ("Hey, I live here so I can wear what I want!", "Jinu: Of course, whatever you say. Freewill exists for a reason!"),
                ("Let’s not talk about my attire...", "Jinu: I swear on my soul- cross my heart, I, Jinu Saja, will never speak of this encounter as long as the Earth revolves around the Sun.")
            ]},
            {"type": "dialogue", "text": "Jinu: So, Y/N, the mysterious new member that definitely does not wear pajamas, what do you do?"},
            {"type": "choice", "options": [
                ("I work as a developer for Taking Big Numbers Co.", "Jinu: Wow, that’s a pretty big score in the workforce. Good for you! I’m actually a…. let’s call it a performer."),
                ("Why do you want to know?", "Jinu: Hey, if you’re not comfortable, I’ll tell you mine first. I’m a…. I work in the music industry!")
            ]},
            {"type": "dialogue", "text": "Jinu: I’m trying to stay humble, but I’ve gathered quite a following."},
            {"type": "choice", "options": [
                ("Oh my gosh! Are you someone famous?", "Jinu: Well... yes."),
                ("You’re definitely bragging.", "Jinu: Well... fine, I’ll admit it.")
            ]},
            {"type": "dialogue", "text": "Jinu: I’m part of a- I wouldn’t call it a boy band but…. *sighs* It’s a little complicated…. you know how bosses are, right?"},
            {"type": "choice", "options": [
                ("Hey, is everything alright?", "Jinu: Sorry, I don’t want to just dump all this on someone."),
                ("Do tell.", "Jinu: Sorry, I don’t want to just dump all this on someone.")
            ]},
            {"type": "dialogue", "text": "Jinu: Hey, how have you been settling into the... group? Must be stressful with the whole orientation thing."},
            {"type": "choice", "options": [
                ("I’ve never had to do anything like this before.", "Jinu: Yeah, the Leader is pretty adamant with that whole setup."),
                ("Sacrificing people is insane, but it’s a cult so...", "Jinu: Yeah, the Leader is pretty adamant with that whole setup.")
            ]},
            {"type": "dialogue", "text": "Jinu: You should be fine, though, it’s pretty simple."},
            {"type": "choice", "options": [
                ("Choosing who lives is not simple.", "Jinu: Well, in the end, it depends on whether you want to stay in the cult, right? It does make life more…. fulfilling."),
                ("You’re one of my options bro.", "Jinu: Sorry, what did you say? I think the wind carried your voice away.")
            ]},
            {"type": "dialogue", "text": "Jinu: Anyways, I like to look at the bigger picture. It doesn’t really matter who you choose, as long as you get in. If you’re really stressed about it, though, I can put in some input. I know most of the members."},
            {"type": "dialogue", "text": "- It’s fine. Thanks for asking about it."},
            {"type": "dialogue", "text": "Jinu: No problem! Us members have to stick together."},
            {"type": "choice", "options": [
                ("Yeah, I’m glad I have you.", "Jinu: Hey... I know this is sudden but, I feel like I’ve known you my whole life."),
                ("Let's not.", "Jinu: Hey... I know this is sudden but, I feel like I’ve known you my whole life.")
            ]},
            {"type": "dialogue", "text": "Jinu: Why do I feel like I can tell you anything? Everything just flows."},
            {"type": "choice", "options": [
                ("I don’t know…. It just feels right.", "Jinu: When I gaze into your eyes, I feel myself being pulled in. It’s like staring into the expanding galaxies of the universe. Swirling and ever changing, in constant motion."),
                ("That’s a little strange, because I literally don’t even know you...", "Jinu: Yeah, we’ve just met... but when I gaze into your eyes, I feel as if all my worries are being washed away. I’m drawn in as if you were the sun of my galaxy.")
            ]},
            {"type": "dialogue", "text": "Jinu begins to step towards you with light brimming behind his eyes. Suddenly, he pauses midstep, frowning slightly as he brings one hand up to his forehead."},
            {"type": "dialogue", "text": "Jinu: I... His voice is gone. It’s really gone! All this time, and I didn’t even notice!"},
            {"type": "choice", "options": [
                ("Are you okay?", "Jinu: I’ve been suffocating silently, smothered by this burden."),
                ("You’re hearing voices??", "Jinu: I’ve been suffocating silently, smothered by this burden.")
            ]},
            {"type": "dialogue", "text": "Jinu: But here, with you, I can finally breathe."},
            {"type": "choice", "options": [
                ("Whatever it is, I’m glad you feel better!", "Jinu: Am I really free?"),
                ("What is this cryptic stuff???", "Jinu: Am I really free?")
            ]},
            {"type": "dialogue", "text": "Jinu: Is... meeting you my fate?"},
            {"type": "dialogue", "text": "Just as he takes another step towards you, the phone in your pocket starts buzzing frantically. You leave Jinu on the patio and head back to your room, thoughts spiralling. Who will you choose? How could you choose between people you’ve just gotten to know?"},
            {"type": "dialogue", "text": "You close your bedroom door and press the recent missed calls button. You wince as the familiar, ominous drawl of the Leader’s voice answer almost immediately. They tell you your time is up and you must make a decision."},
        ]
    },
    {
        "name": "Choice 1",
        "background": "void",
        "character": char_stilton,
        "steps": [
            {"type": "dialogue", "text": "All of a sudden, you find yourself in the cult’s chapel. A black, swirling void yawns in front of you, expanding over the most of the room. You realize that Geronimo, Peppa, and Jinu are being held by the Leader in front of you, gazing at the void with terror as realization dawns upon them."},
            {"type": "dialogue", "text": "Leader: You must choose one and sacrifice the other two."},
            {"type": "dialogue", "text": "Leader: Choose wisely, now."},
            {"type": "choice", "options": [
                ("Save Geronimo Stilton", "Geronimo: Wow…. well, thanks for picking me. You must’ve been enlightened by my words. Would you like to check out the thrift store that recently opened near my street tomorrow? I’ll pick you up at 11:00."),
                ("Sacrifice Geronimo Stilton", "Geronimo: But why? I followed all your orders! I did it page by page, line by line with every detail accounted for! Y/N, how could you?! What about that feminist literature we were gonna read together? Release me-wait-NOOOOOOO!")
            ]}
        ]
    },
    {
        "name": "Choice 2",
        "background": "void",
        "character": char_peppa,
        "steps": [
            {"type": "choice", "options": [
                ("Save Peppa Pig", "Peppa: I knew you liked me! My charms will work on anyone, heh! We should definitely check out my daddy’s yacht collection tomorrow!"),
                ("Sacrifice Peppa Pig", "Peppa: No! What is the meaning of this?! Let go of me! Not the purse- not the purse! Please, c'mon, I can buy anything for you! Wait! GET YOUR HANDS OFF ME! Y/N, I WON'T FORGIVE YOU FOR THIS!")
            ]}
        ]
    },
    {
        "name": "Choice 3",
        "background": "void",
        "character": char_jinu,
        "steps": [
            {"type": "choice", "options": [
                ("Save Jinu", "Jinu: Well, this is a surprise…. not really. I knew we had a connection. You know, I had tickets to go to the aquarium further in town, would you like to join me tomorrow?"),
                ("Sacrifice Jinu", "Jinu: It’s alright, I had a feeling I was one of the candidates. Maybe in another lifetime, in another universe, we could’ve worked. Y/N, I give my soul to you.")
            ]}
        ]
    },
    {
        "name": "End",
        "background": "home",
        "character": char_leader,
        "steps": [
            {"type": "dialogue", "text": "Filled with a new sense of purpose, you are welcomed into the cult by the Leader. Your ascension towards the Almighty One begins now."},
            {"type": "dialogue", "text": "Congratulations! You’ve successfully completed the game. "}
        ]
    }
]

#states
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

#box styles
dialogue_box = pygame.Rect(50, HEIGHT - 200, WIDTH - 100, 150)
choice_boxes = [
    pygame.Rect(150, HEIGHT - 80, 400, 70),
    pygame.Rect(650, HEIGHT - 80, 400, 70)
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


#draws
def draw_title():
    screen.blit(backgrounds["home"], (0, 0))
    title_surface = font_title.render(" ", True, WHITE)
    title_rect = title_surface.get_rect(center=(WIDTH//2, HEIGHT//3))
    screen.blit(title_surface, title_rect)

    subtitle = font_dialogue.render("Press SPACE to Start", True, WHITE)
    sub_rect = subtitle.get_rect(center=(WIDTH//2, HEIGHT//2 + 50))
    screen.blit(subtitle, sub_rect)

def draw_scenario():
    #bg&char
    screen.blit(backgrounds[current_scenario["background"]], (0, 0))
    screen.blit(current_scenario["character"], (WIDTH//2 - 150, HEIGHT//2 - 325))

    #dialogue
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


#main
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #title
        if state == STATE_TITLE:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                state = STATE_DIALOGUE  #first

        #dialogue
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

        #choice
        elif state == STATE_CHOICES:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, box in enumerate(choice_boxes):
                    if box.collidepoint(event.pos):
                        response_text = current_step["options"][i][1]
                        state = STATE_RESPONSE

        #response
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

    #title or scenario
    if state == STATE_TITLE:
        draw_title()
    else:
        draw_scenario()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()