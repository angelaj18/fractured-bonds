define mc = Character("You", color="#FFFFFF")
define will = Character("Will", color="#FF6666")
define devin = Character("Devin", color="#66CCFF")
define unknown = Character("???", color="#AAAAAA")

# Define Backgrounds
image bg alley = "alley.png"
image bg cafe = "cafe.png"
image bg dark = "dark.png"
image bg room = "room.png"

# Define Character Sprites
image mc standing = Transform("mc_standing.png", fit="contain")
image mc sitting = Transform("mc_sitting.png", fit="contain")
image mc hand_on_chest = Transform("mc_hand_on_chest.png", fit="contain")

image will normal = Transform("Will1.png", fit="contain")
image will serious = Transform("Will2.png", fit="contain")

image devin normal = Transform("Devin.png", fit="contain")

image unknown = Transform("Unknown.png", fit="contain")

# Define Variables
default tasks = {}
$ task_manager = TaskManager()

label start:
    show screen hud
    play music "audio/Loop.mp3" loop
    scene bg room with fade
    show mc standing

    mc "My head hurts... What happened?"

    "You notice a notebook on the table. A list of tasks is written inside."

    mc "I should probably start with these..."

    menu:
        "Go to the café":
            $ tasks["Go to the café"] = True
            scene bg cafe
            show mc standing
            mc "The café feels... off today. Like something’s watching me."
            jump find_will

        "Find Will":
            $ tasks["Find Will"] = True
            jump find_will

        "Follow the alley whispers":
            $ tasks["Follow the alley whispers"] = True
            jump alley_path

## --- Will's Scene ---
label find_will:
    scene bg dark with fade
    show will normal

    mc "There you are, Will..."

    will "Hey, you okay? You look like you’ve seen a ghost."

    mc "I don’t know... something about today feels strange. Like I woke up in the wrong version of my life."

    show will serious
    will "I was looking for you too. I need to tell you something, but I don’t think you’ll believe me."

    menu:
        "Trust Will":
            mc "I trust you, Will. Just tell me the truth."
            show will normal
            will "...Okay. Just promise you won’t freak out."

            "Will hesitates, his gaze shifting to the shadows around you."

            will "You’re not supposed to be here. Not like this."

            mc "What do you mean—"

            "A sudden noise echoes from the alley behind Will. A sharp, whispering sound, like a hundred voices speaking at once."

            will "We don’t have much time. If we stay here too long, it’ll notice you."

            mc "What will?"

            "Before Will can answer, the streetlights flicker, and a deep, guttural whisper curls around your ears."

            unknown "You shouldn’t be here..."

            jump alley_path

        "Doubt him":
            mc "You’re hiding something, Will. Just tell me the truth."

            show will serious
            will "I am telling you the truth, but you won’t believe it unless you see it for yourself."

            "Will takes a slow step closer, lowering his voice."

            will "Something is wrong with this place. With us. I don’t know how to explain it, but we have to get out of here before—"

            "A sudden movement in the alley behind Will makes him stop. His breath catches."

            unknown "You shouldn’t be here."
            hide will
            show mc hand_on_chest
            mc "Will, what was that?"
            
            hide mc
            show will normal
            will "Stay close to me."

            jump alley_path

## --- Alley Scene with the Unknown Entity ---
label alley_path:
    scene bg alley with fade
    show unknown

    unknown "You don’t belong here."

    "A chill creeps up your spine. The air feels heavy, like the world itself is pressing against you."

    mc "Who are you?"

    unknown "You were not meant to wake up."

    "Its voice is layered, shifting in tone as if a dozen voices are speaking at once."
    hide unknown
    show devin normal
    devin "MC! Step away from that thing!"

    menu:
        "Run to Devin":
            hide unknown
            mc "Devin, what’s happening?!"

            devin "No time to explain. We need to move, NOW."

            "A sharp screech pierces the air as the unknown figure flickers like a glitch in reality."

            unknown "You cannot escape."

            scene bg dark with fade
            jump next_part_of_story

        "Stay frozen":
            mc "I... I can’t move."

            unknown "Then you will stay."

            "The shadows twist around you, stretching toward your feet."

            devin "MC! SNAP OUT OF IT!"

            scene bg dark with fade
            jump next_part_of_story

## --- Next Part of the Story (Placeholder) ---
label next_part_of_story:
    "The world around you twists into darkness..."
    jump check_endings

## --- The Endings ---
label check_endings:
    menu:
        "Ending with Will":
            jump ending_will
        "Ending with Devin":
            jump ending_devin
        "Ending with the Unknown":
            jump ending_sonny

label ending_will:
    scene bg dark
    show will serious
    will "You stayed with me. That means everything."
    stop music fadeout 2.0
    return

label ending_devin:
    scene bg alley
    show devin normal
    devin "You finally understand now, don’t you?"
    stop music fadeout 2.0
    return

label ending_sonny:
    scene bg room
    show unknown
    unknown "You chose the wrong path."
    stop music fadeout 2.0
    return