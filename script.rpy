# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define spat = Character('Spat', color ="#FFFFFF")
define unknown = Character('???', color ="#FFFFFF")
define paws = Character('Paws', color ="#FFFFFF")
define mustache = Character('Mustache', color ="#FFFFFF")
define elias = Character('Elias', color ="#FFFFFF")
define basilio = Character('Basilio', color ="#FFFFFF")
define crisostomo = Character(' Crisostomo ', color ="#FFFFFF")
define salvi = Character('Salvi', color ="#FFFFFF")
define crispin = Character('Crispin', color ="#FFFFFF")
define santiago = Character('Santiago', color ="#FFFFFF")
define damaso = Character('Damaso', color = "#FFFFFF")
define crowdmurmurs = Character('Crowd', color ="#FFFFFF")

image credits = Movie(play="credits.webm")
image goodcredits = Movie(play="goodcredits.webm")

# Define custom placement
transform defaultright: #placement to ni spat
    xalign 0.77
    xsize 574
    ysize  720
    yalign 0.5

transform defaultdog: #placement ng doggy ko uwu
    xalign 0.725
    xsize 349
    ysize 480
    yalign 0.7

transform itemshow:
    xalign 0.298
    xsize 250
    ysize 250   
    yalign 0.098

# Define custom transition
transform blurred:
    blur 20

transform unblur:
    linear 1 blur 0

init:
    transform earthquake:
        linear 0.1 xoffset -2 yoffset 2 
        linear 0.1 xoffset 3 yoffset -3 
        linear 0.1 xoffset 2 yoffset -2
        linear 0.1 xoffset -3 yoffset 3
        linear 0.1 xoffset 0 yoffset 0
        repeat

define slowdissolve = Dissolve(5.0)

define fastdissolve = Dissolve(0.3)

define veryfastdissolve = Dissolve(0.1)

define flash = Fade(.25, 0.0, .75, color="#fff")


# The game starts here.

label start:
    stop music fadeout 0.5
    $ quick_menu = False
    
    play sound "audio/bird chirping.mp3" volume 1.0
    
    scene bg skyday with slowdissolve

    pause 1.0
    play sound "audio/dog happy arf.mp3" volume 0.5
    # [paws nudges side]
    $ quick_menu = True
    
    unknown "Arf Arf!"
    play sound "audio/dog happy arf.mp3" volume 0.5
    unknown "Arf!"
    unknown "Mm, hey, Paws. Isn't it too early?"
   
label choices_1:
    # [paws whines]
    play sound "audio/dog question arf.mp3" volume 0.5
    paws "Arf?"
$ quick_menu = False
menu:
    "Get up":
            jump choices1_a
    "Sleep in":
            jump choices1_b
label choices1_a:
        $ quick_menu = True
        unknown "Alright, Paws, you win. Where are we off today?"
        jump choices1_common

label choices1_b:
        $ quick_menu = True
        unknown "Maybe later, Paws. Wake me up in an hour."
        
        unknown "(...)"
        
        unknown "(zzz)"
        
        unknown "(zzzzzz)"
        
        unknown "(...)"
        
        unknown "(..)"
        # [paws jumps on spat's leg]
        play sound "audio/dog happy arf.mp3" volume 0.5
        paws "Arf!"
        
        unknown "Alright, Paws, you win. Where are we off today?"
        jump choices1_common
        
label choices1_common:
        # [*Jumps around happily*]
        play sound "audio/dog happy arf.mp3" volume 0.5
        paws "Arf arf!"
        unknown "Lead the way buddy!"

label start_1v1:
    scene bg dumpsiteday with fade
    play music "audio/bgm happy.mp3" volume 0.8
    show spat idle at defaultright with moveinright
    unknown "(My name is Spat.)" 
    show spat joyful at defaultright with veryfastdissolve
    spat "(This is how life has been for me for so long. I don't know what life outside the landfill is like.)"
    show spat sad at defaultright with veryfastdissolve
    spat "(I don’t recall much about having any family or parents at all.)"
    show spat verysad at defaultright with veryfastdissolve
    spat "(As a kid, I’ve always lived here. I don’t know if I’ve had any.)"
    show spat emotional at defaultright with veryfastdissolve
    spat "(All I remember is waking up in this landfill and learning how to get through.)"
    show spat idle at defaultright with veryfastdissolve
    spat "(Me and Paws scavenge the landfill for any materials we can sell.)"
    show spat joyful at defaultright with veryfastdissolve
    show tin canframe at itemshow with fastdissolve
    spat "(Tin cans are bulky but sell for the lowest price.)"
    show spat sad at defaultright with veryfastdissolve
    show paper papelframe at itemshow with fastdissolve
    spat "(The paper does well, but getting the weight up takes time.)"
    show spat likewise at defaultright with veryfastdissolve
    show plastic bottleframe at itemshow with fastdissolve
    spat "(Plastic bottles are easy to find and sell the most.)"
    show spat thumbsup at defaultright with veryfastdissolve
    show glass bottleframe at itemshow with fastdissolve
    spat "(Glass bottles sell by the piece and are my best seller.)"
    hide tin canframe
    hide paper papelframe
    hide plastic bottleframe
    hide glass bottleframe
    show spat cheerful at defaultright with veryfastdissolve
    spat "(Whenever it's glass bottle day, me and Paws always eat fancy.)"
    show spat idle at defaultright with veryfastdissolve
    spat "(Nothing beats rice and chicken, and the best meals always come after a day of hard work.)"
    show spat verytired at defaultright with veryfastdissolve
    spat "(One day, I hope me and Paws earn enough money to always have rice and chicken, so we don’t always have to wait for glass bottle day.)"
    show spat sad at defaultright with veryfastdissolve
    spat "(Maybe one day…)"

label start_1v2:
    $ quick_menu = False
    stop music fadeout 2.0
    scene bg dumpsitegovernment with fade
    play sound "audio/crowd noise muffled.mp3" fadeout 1.0
    pause 5.0
    $ quick_menu = True
    show mustache idle at defaultright with moveinright
    mustache "We advise all residents to evacuate the landfill immediately."
    show mustache mic at defaultright with veryfastdissolve
    mustache "There have been many incidents of landfills collapsing and catching fire recently."
    show mustache idle at defaultright with veryfastdissolve
    mustache "This place is unsuitable for living, so we advise all of you to vacate the landfill imme-"
    hide mustache idle
    play music "audio/bgm serious.mp3" volume 0.8 fadein 2.0
    show elias idle2 at defaultright with vpunch
    elias "Evacuate? Where will we go!? This is the only place for us to go to!!"
    hide elias idle2
    show basilio idle at defaultright with vpunch
    basilio "Yeah! Do you think it's easy for us to leave?!"
    hide basilio idle
    show mustache mic at defaultright with veryfastdissolve
    mustache "Please realize that we’re only doing this for your safety. Staying here will only pose a greater risk to your lives!"
    hide mustache mic at defaultright
    show crisostomo idle2 at defaultright with vpunch
    crisostomo "We refuse! We have nothing, you hear me? Nothing!!"
    hide crisostomo idle2
    show salvi idle2 at defaultright with vpunch
    salvi "Even if we did leave, where would you put us? On the streets so you can kick us around like trash?"
    hide salvi idle2
    show crispin idle2 at defaultright with vpunch
    crispin "At least around trash, we feel more human. Around people like you, we’re only trash."
    hide crispin idle2
    show santiago idle2 at defaultright with vpunch
    santiago "Come back when you finally understand how we feel!"
    hide santiago idle2
    show spat tired at defaultright with veryfastdissolve
    spat "Sigh, he’s right though… We can’t live here. I mean, look at this place! It’s a dump!"
    hide spat tired
    show paws worried2 at defaultdog
    play sound "audio/dog whimper arf.mp3" volume 0.5 fadein 1.0 fadeout 1.0
    paws  "*Whimpers*"
    hide paws worried2
    show spat sad at defaultright with veryfastdissolve
    stop sound
    spat "*Paws nudges my leg as if he's trying to comfort me*"
    show spat idle at defaultright with veryfastdissolve
    stop music fadeout 0.5
    play music "audio/bgm happy.mp3" volume 0.7
    spat "Well, on the bright side, it’s our dump! And it’s our home!"
    hide spat idle
    show paws happy at defaultdog with veryfastdissolve
    play sound "audio/dog happy arf.mp3" volume 0.5
    paws "Arf!"
    hide paws happy
    show spat sad at defaultright with veryfastdissolve
    spat "(The button-up people always come here to drive us out, so it’s nothing new.)"
    show spat idle at defaultright with veryfastdissolve
    spat "(It’s best we just mind our business and look for things to sell.)"
    show spat verytired at defaultright with veryfastdissolve
    spat "(Also, I’m starving, so some bread would be perfect!)"
    hide spat verytired with moveoutright
    $ quick_menu = False
    scene bg dumpsiteday with fade
    play sound "audio/gathering sound effect.mp3" volume 0.3 fadein 2.0
    pause 3.0

    # [show spat and paws]
    # [gathering sounds]

    scene bg dumpsitedayzoomflip with fade
    play sound "audio/dropping wood sound effect.mp3" volume 0.3 fadein 2.0

    # [show spat and paws]

    # [gathering sounds]

    pause 2.5
    show spat tired at defaultright with moveinright
    pause 0.5
    show spat exhausted at defaultright with veryfastdissolve
    $ quick_menu = True
    spat "Huff… huff…"

    $ quick_menu = False
    scene bg dumpsitedayflip with fade
    play sound "audio/gathering sound effect.mp3" volume 0.5 fadein 1.0
    
    pause 3.0

    # [show spat and paws]

    # [gathering sounds]
    play sound "audio/grabbing sound effect.mp3" volume 0.5 fadein 1.0
    scene bg dumpsitedayzoom with fade
    
    pause 2.5

    # [show spat and paws]
    $ quick_menu = True
    play sound "audio/dog grr.mp3" volume 0.3 fadein 1.0
    show paws worried3 at defaultdog with veryfastdissolve
    paws "Grr… huff…"
    hide paws worried3 with moveoutright
    # [gathering sounds]

label start_1v3:
    $ quick_menu = False
    scene bg dumpsiteday with fade
    show kariton fill with moveinright
    # [Show kariton with bottles, cans, rolled up wire, and paper]
    $ quick_menu = True
    show spat joyful at defaultright with moveinright
    spat "You know what, Paws? It’s been a while,  I think we could afford a filling meal today!"
    # [play coins clacking sound]
    show spat idle at defaultright with veryfastdissolve
    play sound "audio/coin clacking sound.mp3" volume 0.3
    spat "1, 2, 3, 4, 5—"
    show spat likewise at defaultright with veryfastdissolve
    spat "Let’s go get chicken? What are your thoughts, Paws?"
    # [show spat jumping happily, his tail wagging happily]
    hide spat likewise
    show paws happy2 at defaultdog with veryfastdissolve
    play sound "audio/dog happy arf.mp3" volume 0.5
    paws "Arf arf!!"
    hide paws happy2
    show spat cheerful at defaultright with veryfastdissolve
    spat "Attaboy Paws! Let’s go! We don’t wanna miss out on the hot chicken!"
    play sound "audio/dog happy arf.mp3" volume 0.5
    hide spat cheerful
    show paws happy3 at defaultdog with veryfastdissolve
    paws "Arf!"
    hide paws happy3 with moveoutright
    $ quick_menu = False

    scene bg vendorday with fade
    $ quick_menu = True
    spat "(I still find it funny how Damaso hated chicken neck soup but ended up as a chicken neck vendor.)"
    show spat happy at defaultright with moveinright
    pause 0.5
    show spat likewise at defaultright with veryfastdissolve
    spat "10 pieces please! Extra vinegar and 1 rice."
    show spat idle at defaultright with veryfastdissolve
    damaso "Is that all?"
    pause 0.5
    show spat thumbsup at defaultright with veryfastdissolve 
    pause 0.5
    show spat idle at defaultright with veryfastdissolve
    spat "How much?"
    damaso "35 in total."
    show spat happy at defaultright with veryfastdissolve
    spat "Alright, thanks!"
    hide spat happy with moveoutright
    # [show paws wags tail happily from behind spat]
    $ quick_menu = False
    stop music fadeout 2.0
    scene bg houseday with fade
    # [distinct coughing noises can be heard in the background]
    # [show paws concerned look]
    play sound "audio/distinct coughing.mp3"
    pause 5.0
    $ quick_menu = True
    play sound "audio/dog grr.mp3" volume 0.5 fadein 1.0 fadeout 2.0
    show paws angry2 at defaultdog with moveinright
    paws "Arf!"
    # [show alarmed spat]
    hide paws angry2
    show spat worried at defaultright with veryfastdissolve
    pause 0.8
    show spat idle at defaultright with veryfastdissolve
    spat "It’s probably nothing buddy..."
    show spat cheerful at defaultright with veryfastdissolve
    spat "Anyways, here ya go!"
    show spat likewise at defaultright with veryfastdissolve
    play sound "audio/eating sound effect.mp3" volume 0.5 fadein 1.0 fadeout 3.0
    pause 3.0
    show spat sad at defaultright with veryfastdissolve
    # [feeds paws]
    # [spat eats]
    # [spats sigh]
    play music "audio/bgm saddening.mp3" volume 0.7
    spat "If only we could get this as much as we want....."
    # [paws sad whine]
    show spat verysad at defaultright with veryfastdissolve
    spat "......"
    show spat emotional at defaultright with veryfastdissolve
    spat "Someday..."
    show spat tired at defaultright with veryfastdissolve
    spat "Maybe we’ll hit the jackpot and get a massive sale! Probably get enough money to start a business…"
    show spat verytired at defaultright with veryfastdissolve
    spat "Then get a lot of money from that, and get ourselves a nicer place than what we have now…"
    show spat joyful at defaultright with veryfastdissolve
    stop music fadeout 2.0
    play music "audio/bgm happy.mp3" volume 0.7
    spat "Still a bit too farfetched but hey - we’ll get there!"
    hide spat joyful
    show paws happy at defaultdog with veryfastdissolve
    play sound "audio/dog happy arf.mp3" volume 0.5
    # [paws happy barking]
    paws "Arf Arf!"
    hide paws happy
    show spat happy at defaultright with veryfastdissolve
    spat "For now, we’ll just have to work extra hard!"
    show spat likewise at defaultright with veryfastdissolve
    spat "You done bud? We gotta go and look for more stuff to sell!"
    hide spat likewise
    show paws happy2 at defaultdog with veryfastdissolve
    play sound "audio/dog happy arf.mp3" volume 0.5
    paws "Arf!"
    hide paws happy with moveoutright

    $ quick_menu = False
    scene bg dumpsitenoon with fade
    play sound "audio/gathering sound effect.mp3" volume 0.3 fadein 2.0
    # [show spat and paws]
    # [gathering sounds]
    pause 4.0
    
    scene bg dumpsitenoonzoomflip with fade
    play sound "audio/dropping wood sound effect.mp3" volume 0.3 fadein 2.0
    # [show spat and paws]
    # [gathering sounds]
    pause 2.5
    
    show spat tired at defaultright with moveinright
    pause 0.5
    show spat exhausted at defaultright with veryfastdissolve
    $ quick_menu = True
    spat "Huff… huff…"

    $ quick_menu = False
    play sound "audio/grabbing sound effect.mp3" volume 0.5 fadein 1.0
    scene bg dumpsitenoon with fade
    pause 1.0
    # [show spat and paws]
    # [gathering sounds]

    play sound "audio/dog grr.mp3" volume 0.5 fadein 1.0 fadeout 2.0
    $ quick_menu = True
    show paws worried2 at defaultdog with veryfastdissolve
    paws "Grr… huff…"
    $ quick_menu = False
    scene bg dumpsitenight with fade
    show spat likewise at defaultright with veryfastdissolve
    $ quick_menu = True
    spat "Is that too heavy Paws? You can always put it in my cart."
    
    # [*show kariton*]
    # [*paws shakes head*]
    play sound "audio/dog grr.mp3" volume 0.5
    hide spat likewise
    show paws worried3 at defaultdog with veryfastdissolve
    paws "Arf arf!"
    hide paws worried3
    show spat idle at defaultright with veryfastdissolve
    spat "Alright Paws. I trust you."
    show spat happy at defaultright with veryfastdissolve
    spat "Hmm…"
    show spat likewise at defaultright with veryfastdissolve
    spat "I think we should call it a day bud."
    hide spat likewise
    show paws happy at defaultdog with veryfastdissolve
    play sound "audio/dog happy arf.mp3" volume 0.5
    paws "Arf!"
    hide paws happy with moveoutright
    stop music fadeout 0.5
    $ quick_menu = False
    scene bg blacklang with fade
    play sound "audio/night ambience sound.mp3"
    scene bg housenightlight with slowdissolve
    scene bg blacklang with slowdissolve
    scene bg insidehousenight with fade
    stop sound fadeout 1.0
    play sound "audio/box shuffling.mp3"
    pause 1.0
    stop sound fadeout 1.0
    pause 0.5
    show spat tired at defaultright with moveinright
    pause 0.5
    show spat exhausted at defaultright with veryfastdissolve
    $ quick_menu = True
    spat "We got a lot today but I don’t think its gonna be worth a lot"
    show spat idle at defaultright with veryfastdissolve
    spat "Doesn’t matter!"
    show spat joyful at defaultright with veryfastdissolve
    spat "We’ll still have enough to eat tomorrow"
    hide spat joyful
    show paws happy2 at defaultdog with veryfastdissolve
    play sound "audio/dog happy arf.mp3" volume 0.5
    paws "Arf!"

label choices_2:
    hide paws happy2
    show spat idle at defaultright with veryfastdissolve
    spat "What are we getting tomorrow? Bread? Or how about some fishball?"
    # [paws indecisive head shake]
    hide spat idle
    $ quick_menu = False
menu:
    "Pandesal":
            jump choices2_a
    "Fishball":
            jump choices2_b
label choices2_a: 
        # [spat chuckles]
        $ quick_menu = True
        show spat joyful at defaultright with veryfastdissolve
        spat " I think I know what I want..."
        jump choices2_common

label choices2_b:
        # [spat chuckles]
        $ quick_menu = True
        show spat joyful at defaultright with veryfastdissolve
        spat " I think I know what I want..."
        jump choices2_common
        
label choices2_common:
        show spat idle at defaultright with veryfastdissolve
        spat "Well bud, I’m gonna call it a day. A bit tired, but at least we got a good meal today!"
        hide spat idle
        show paws happy3 at defaultdog with veryfastdissolve
        play sound "audio/dog happy arf.mp3" volume 0.5
        paws "Arf!"
        hide paws happy3
        show spat happy at defaultright with veryfastdissolve
        spat "Good night, bud."
        $ quick_menu = False
        pause 0.5
        play sound "audio/cricket noise.mp3" volume 0.5 fadein 2.0
        show spat sleepy at defaultright with veryfastdissolve
        pause 1.0
        

label start_2v1:
    scene bg blacklang with slowdissolve
    # [cricket sounds]
    pause 2.0
    stop sound fadeout 1.0
    play sound "audio/rooster sound.mp3" volume 0.6

    scene bg insidehouseday with slowdissolve
    
    stop sound fadeout 2.0
    $ quick_menu = True
    show spat cheerful at defaultright with veryfastdissolve
    spat "Mm..."
    show spat idle at defaultright with veryfastdissolve
    spat "Another day..."
    show spat tired at defaultright with veryfastdissolve
    spat "(I’d like to stay in and sleep but…)"
    show spat sad at defaultright with veryfastdissolve
    spat "(I need to be at the yard early…)"
    show spat verytired at defaultright with veryfastdissolve
    spat "(If I don’t get up, I’ll have less time to gather material…)"
    show spat cheerful at defaultright with veryfastdissolve
    spat "(Alright, time to get up!)"
    hide spat cheerful
    show paws happy2 at defaultdog with veryfastdissolve
    play sound "audio/dog happy arf.mp3" volume 0.5
    paws "Arf!"
    hide paws happy2
    # [spat chuckles]
    show spat happy at defaultright with veryfastdissolve
    spat "Good morning to you too, buddy."
    show spat sad at defaultright with veryfastdissolve
    spat "Sigh..."
    show spat idle at defaultright with veryfastdissolve
    spat "Same old, same old."
    hide spat idle with moveoutright
    $ quick_menu = False
    scene bg houseday with fade
    play sound "audio/coughing sound.mp3" volume 0.7
    # [coughing]
    # [sniffling]
    # [sneezing]
    # [wheezing]
    pause 5.0
    stop sound
    $ quick_menu = True
    show spat shocked at defaultright with moveinright
    spat "(Oh no…)"
    show spat tired at defaultright with veryfastdissolve
    play music "audio/bgm saddening.mp3" volume 0.7
    spat "(Is there a disease going around?)"
    show spat worried at defaultright with veryfastdissolve
    spat "(This isn’t good…)"
    hide spat worried
    show paws worried2 at defaultdog with veryfastdissolve
    play sound "audio/dog grr.mp3" volume 0.5
    paws "Grr...."
    hide paws worried2
    show spat idle at defaultright with veryfastdissolve
    stop sound
    spat "*Paws gently grabs my hand with his mouth, and drags me away from the crowd*"
    show spat likewise at defaultright with veryfastdissolve
    stop music fadeout 2.0
    spat "Yeah..."
    play music "audio/bgm happy.mp3" volume 0.7 
    show spat joyful at defaultright with veryfastdissolve
    spat "Let’s not go there… Lead the way buddy!"
    hide spat joyful with moveoutright

    $ quick_menu = False
    
    scene bg dumpsiteday with fade
    
    play sound "audio/gathering sound effect.mp3" volume 0.5 fadein 1.0
    # [show spat and paws]
    # [gathering sounds]
    pause 3.0
    $ quick_menu = True
    show spat tired at defaultright with veryfastdissolve
    pause 0.5
    show spat exhausted at defaultright with veryfastdissolve
    spat "Huff… huff…"
    $ quick_menu = False
    scene bg dumpsitenoon with fade
    
    play sound "audio/dropping wood sound effect.mp3"
    # [show spat and paws]
    # [gathering sounds]
    pause 3.0
    show paws worried at defaultdog with veryfastdissolve
    play sound "audio/dog grr.mp3"
    $ quick_menu = True
    paws "Grr… huff…"
    $ quick_menu = False
    stop music fadeout 2.0
    scene bg dumpsitenight with fade
    play music "audio/night ambience sound.mp3" 
    # [spat and paws *huff of relief*]
    show spat tired at defaultright with veryfastdissolve
    play sound "audio/relief sound effect.mp3"
    $ quick_menu = True
    spat "Let’s sell this tomorrow… Let’s go home buddy!"
    hide spat tired with moveoutright
    $ quick_menu = False
    scene bg blacklang with fastdissolve
    scene bg insidehousenight with fade
    play sound "audio/boxes shuffling sound effect.mp3" volume 0.5 fadeout 4.0
    # [sound boxes shuffling]
    pause 3.0
    $ quick_menu = True
    show spat likewise at defaultright with moveinright
    spat "With this much recyclables, we can afford to relax a bit with our gathering."
    show spat idle at defaultright with veryfastdissolve
    spat "But for now, I think we should rest."
    hide spat idle
    show paws happy2 at defaultdog with veryfastdissolve
    play sound "audio/dog happy arf.mp3"
    paws "Arf!"
    hide paws happy2
    show spat joyful at defaultright with veryfastdissolve
    spat "Well, goodnight paws!"
    hide spat joyful
    play sound "audio/dog happy arf.mp3"
    show paws happy3 at defaultdog with veryfastdissolve
    paws "Arf Arf!"
    hide paws happy 3 with moveoutbottom
    $ quick_menu = False
    play sound "audio/cricket noise.mp3" volume 0.5 fadein 2.0
    scene bg blacklang with slowdissolve
    # [cricket sound]
    pause 2.0
    stop sound
    play sound "audio/rooster sound.mp3" volume 0.6
    stop music fadeout 2.0
    scene bg insidehouseday with slowdissolve
    stop sound fadeout 2.0
    # [violent coughing fits]
    # [loud sneezing]
    # [crying]
    # [spat shivers]
    play sound "audio/eerie sound.mp3" fadein 3.0 fadeout 2.0
    pause 3.0
    $ quick_menu = True
    show spat shocked at defaultright with veryfastdissolve
    spat "Why is it so eerie..?"
    hide spat shocked with moveoutright
    scene bg houseday with fade
    stop sound fadeout 3.0
    play sound "audio/all coughing.mp3"
    pause 5.0
    show spat worried at defaultright with moveinright
    play sound "audio/eerie sound.mp3" fadein 3.0 fadeout 2.0
    spat "Impossible how they got all sick this fast..."
    # [paws *nudging spat's leg with his nose*]
    hide spat worried
    show paws angry at defaultdog with veryfastdissolve
    stop sound fadeout 3
    play sound "audio/dog grr.mp3" volume 0.5
    paws "grrr..."
    hide paws angry
    show spat idle at defaultright with veryfastdissolve
    spat "*Paws nudges my leg with his nose*"
    show spat likewise at defaultright with veryfastdissolve
    spat "Oop… Sorry buddy. Can’t stay out here?"
    hide spat likewise
    $ quick_menu = False

    # [paws *Shakes head*]

label choices_3:
menu:
    
    "Go to work":
            jump choices3_a
    "Stay at home":
            jump choices3_b

label choices3_a: 
        $ quick_menu = True
        show spat happy at defaultright with veryfastdissolve
        spat "Mm..."
        show spat likewise at defaultright with veryfastdissolve
        spat "Let’s go work somewhere away from them."
        hide spat likewise
        show paws happy3 at defaultdog with veryfastdissolve
        play sound "audio/dog happy arf.mp3"
        paws "Arf!"
        hide paws happy3 with moveoutright
        $ quick_menu = False
        scene bg dumpsiteday with fade
        play sound "audio/gathering sound effect.mp3" volume 0.3 fadein 2.0
        pause 3.0

        scene bg dumpsitedayzoomflip with fade
        play sound "audio/dropping wood sound effect.mp3" volume 0.3 fadein 2.0

        # [show spat and paws]

        # [gathering sounds]

        pause 2.5
        $ quick_menu = True
        show spat tired at defaultright with veryfastdissolve
        pause 0.5
        show spat exhausted at defaultright with veryfastdissolve
        spat "Huff… huff…"

        $ quick_menu = False
        play sound "audio/grabbing sound effect.mp3" volume 0.5 fadein 1.0
        scene bg dumpsitenoonzoomflip with fade
        
        # [show spat and paws]
        # [gathering sounds]

        pause 2.0
        $ quick_menu = True
        play sound "audio/dog whimper arf.mp3" volume 0.5
        
        show paws worried at defaultdog with veryfastdissolve
        paws "Grr… huff…"
        scene bg dumpsitenoon with fade
        show spat joyful at defaultright with veryfastdissolve
        spat "Let’s sell this tomorrow, alright bud? I don’t like how everyone is just sick right now."
        show spat sad at defaultright with veryfastdissolve
        spat "Can't risk getting sick..."
        show spat verytired at defaultright with veryfastdissolve
        spat "We can't afford medicine..."
        hide spat verytired with moveoutright
        $ quick_menu = False
        scene bg insidehousenight with fade

        jump choices3_common

label choices3_b:
        $ quick_menu = True

        show spat joyful at defaultright with veryfastdissolve
        spat "We should stay at home today buddy."
        hide spat joyful
        show paws angry3 at defaultdog with veryfastdissolve
        play sound "audio/dog grr.mp3" volume 0.5
        paws "*growling lowly at the groups of people.*"
        hide paws angry3 with moveoutright

        scene bg insidehouseday with fade

        jump choices3_common
        
label choices3_common:
        $ quick_menu = True
        show spat sad at defaultright with moveinright
        play music "audio/bgm saddening.mp3" volume 0.7
        spat "I know people here get sick every once in a while but it hasn’t been this bad before…"
        show spat verytired at defaultright with veryfastdissolve
        spat "To be honest Paws, I think the megaphone man has a point."

label start_2v2:
    show spat emotional at defaultright with veryfastdissolve
    spat "We don't have much of a future here…"
    hide spat emotional
    show paws calm3 at defaultdog with veryfastdissolve
    play sound "audio/dog happy arf.mp3" volume 0.5
    paws "Arf!"
    hide paws calm3
    show spat idle at defaultright with veryfastdissolve
    spat "But then again..."
    show spat sad at defaultright with veryfastdissolve
    spat "We can’t afford anything in the city…"
    show spat emotional at defaultright with veryfastdissolve
    spat "We’ll be living worse than we are here…"
    hide spat emotional
    show paws worried at defaultdog with veryfastdissolve
    play sound "audio/dog whimper arf.mp3"
    paws "*whines sadly*"
    hide paws worried
    show spat joyful at defaultright with veryfastdissolve
    spat "Aw... We'll be fine buddy"
    show spat likewise at defaultright with veryfastdissolve
    spat "Let’s enjoy a little break today"
    hide spat likewise
    show paws happy at defaultdog with veryfastdissolve 
    paws "*Snuggles up next to Spat*"
    hide paws happy
    show spat idle at defaultright with veryfastdissolve
    spat "*Chuckles*"
    stop music fadeout 2.0
    pause 1.5
    play sound "audio/cricket noise.mp3" volume 0.8
    show spat sleepy at defaultright with veryfastdissolve
    pause 2.5
    $ quick_menu = False
    scene bg blacklang with fade
    # [play cricket sounds]
    # [bg insidehousenoon]
    stop sound fadeout 1.0
    scene bg insidehousenoon with slowdissolve
    $ quick_menu = True
    show spat veryshocked at defaultright with vpunch
    spat "Oh dear..."
    show spat worried at defaultright with veryfastdissolve
    spat "I didn’t mean to sleep till this late!"
    hide spat worried
    show paws confused3 at defaultdog with veryfastdissolve
    play sound "audio/dog whimper arf.mp3" volume 0.6
    paws "Arf?"
    hide paws confused3
    show spat shocked at defaultright with veryfastdissolve
    spat "Oh man, we gotta sell our things!"
    show spat veryworried at defaultright with veryfastdissolve
    spat "Quick bud, before the shop closes!"
    hide spat veryworried
    show paws happy at defaultdog with veryfastdissolve
    play sound "audio/dog happy arf.mp3" volume 0.5
    paws "Arf arf!"
    hide paws happy with moveoutright
    $ quick_menu = False
    scene bg blacklang with slowdissolve
    scene bg junkshopclose with fade
    show spat sad at defaultright with moveinright
    $ quick_menu = True
    spat "Oh no..."
    show spat tired at defaultright with veryfastdissolve
    spat "They're closed beause of the sickness going around..."
    show spat idle at defaultright with veryfastdissolve 
    spat "Well, it doesn't matter."
    show spat joyful at defaultright with veryfastdissolve
    spat "Let’s just drop these off at home and get some food, yeah?"
    hide spat joyful 
    show paws happy2 at defaultdog with veryfastdissolve
    play sound "audio/dog happy arf.mp3"
    paws "Arf!"
    hide paws happy2 with moveoutright
    
    scene bg blacklang with slowdissolve
    scene bg dumpsitebodybagclose with fade

    show spat likewise at defaultright with moveinright
    spat "I wonder what’s going on here..."
    hide spat likewise
    play music "audio/bgm serious.mp3" volume 0.6
    elias "Are you crazy?! You can’t just dump that here!"

    basilio "It’s not like we can put it anywhere else!"
    show spat idle at defaultright with veryfastdissolve
    spat "What are they talking about?"
    hide spat idle
    $ quick_menu = False
label choices_4:
menu:
    "Get closer":
            jump choices4_a
    "Mind your own business":
            jump choices4_b

label choices4_a: 
        $ quick_menu = True
        show spat joyful at defaultright with veryfastdissolve
        spat "I’m gonna take a closer look bud.."
        hide spat joyful
        show paws angry3 at defaultdog with veryfastdissolve
        play sound "audio/angry bark arf.mp3" volume 0.7
        paws "grrr"
        hide paws angry3
        show spat idle at defaultright with veryfastdissolve
        spat "(I don't think Paws wants me to go there...)"
        show spat shocked at defaultright with veryfastdissolve
        play sound "audio/disgust sound.mp3" volume 0.7
        spat "*Nose scrunches up in disgust* Eugh… That smells horrible…"
        show spat worried at defaultright with veryfastdissolve
        spat "I’ve never smelled anything like this before…"
        hide spat worried
        show crisostomo idle at defaultright with vpunch
        crisostomo "You think we’re just gonna leave this thing in our house?!"
        hide crisostomo idle
        show elias idle2 at defaultright with hpunch
        elias "You absolutely cannot dump that here!"
        hide elias idle2
        show basilio idle2 at defaultright with hpunch
        basilio "Quit pushing us!"
        hide basilio idle2 at defaultright with hpunch
        show crisostomo idle2 at defaultright with vpunch
        crisostomo "Hey! Hey! Quit it!"
        stop music fadeout 2.0
        play sound "audio/thud sound.mp3"
        scene bg blacklang
        pause 1.0
        # [*loud thud sound*]
        crisostomo "STOP IT!"
        $ quick_menu = False

        narrator "The sack they were holding then unfurls, revealing a body with bloodshot eyes, and extremely pale complexion."
        
        scene bg dumpsitebodybagopen with slowdissolve 
        $ quick_menu = True
        
        show spat veryworried at defaultright with hpunch
        spat "AAAH!!!"
        hide spat verryworried
        show paws angry at defaultdog with veryfastdissolve 
        play sound "audio/angry bark arf.mp3" volume 0.7
        paws "ARF! "
        show paws angry2 at defaultdog with veryfastdissolve
        play sound "audio/angry bark arf.mp3" volume 0.7
        paws "ARF!" 
        show paws angry3 at defaultdog with veryfastdissolve
        play sound "audio/angry bark arf.mp3" volume 0.7
        paws "ARF!"
        hide paws angry3
        show spat shocked at defaultright with veryfastdissolve
        spat "PAWS! WE NEED TO GO!"
        hide spat shocked with moveoutright
        show basilio idle2 at defaultright with veryfastdissolve
        basilio "Great, you caused a commotion!"
        hide basilio idle2
        show crisostomo idle at defaultright with veryfastdissolve
        crisostomo "I hope you’re proud of yourself for scaring the kid!"
        hide crisostomo idle
        show elias idle at defaultright with veryfastdissolve
        elias "I wasn’t…"
        show elias idle2 at defaultright with veryfastdissolve
        elias "All I’m saying is, not here! Not where we’re all living."
        show elias idle at defaultright with veryfastdissolve
        elias "God knows the other diseases we’ll be getting…"

        jump choices4_common

label choices4_b:
        $ quick_menu = True
        stop music fadeout 2.0
        show spat joyful at defaultright with veryfastdissolve
        spat "Probably just some adults fighting…"
        show spat idle at defaultright with veryfastdissolve
        spat "Shouldn’t involve ourselves…"
        show spat likewise at defaultright with veryfastdissolve
        spat "Not when there’s a disease going around…"
        hide spat likewise at defaultright with veryfastdissolve
        show paws worried3 at defaultdog with veryfastdissolve
        play sound "audio/dog grr.mp3"
        paws "*Sneering at the sack the people were holding*"
        show paws angry at defaultdog with veryfastdissolve
        play sound "audio/angry bark arf.mp3" volume 0.7
        paws "Grr…"
        hide paws angry
        elias "Are you freaking kidding me!?"
        elias "That’s a corpse for God’s sake!"
        elias "Adding another disease to the area so it just kills us all?!"
        show spat idle at defaultright with veryfastdissolve
        spat "A... a c-..."
        show spat happy at defaultright with veryfastdissolve
        spat "…"
        show spat shocked at defaultright with veryfastdissolve
        spat "A CORPSE?!"
        show spat worried at defaultright with veryfastdissolve
        spat "P-paws… W-w-we need to…"
        hide spat worried
        show paws worried at defaultdog with veryfastdissolve
        play sound "audio/dog whimper arf.mp3"
        paws "*Worried whining*"
        hide paws worried
        show spat veryshocked at defaultright with veryfastdissolve
        spat "We need to.. *gulp* go…"
        hide spat with moveoutright
        play sound "audio/dog question arf.mp3"
        show paws worried at defaultdog with veryfastdissolve
        paws "*whimpers*"
        hide paws worried with moveoutright
        

        jump choices4_common
        
label choices4_common:
    scene bg insidehousenoon with fade
    show spat tired at defaultright with moveinright
    spat "Bud…"
    show spat sad at defaultright with veryfastdissolve    
    spat "…"
    show spat verytired at defaultright with veryfastdissolve
    spat "I don’t feel so good…"
    show spat verytired at defaultright with veryfastdissolve
    spat "I..."
    play sound "audio/thud sound.mp3"
    hide spat verytired with moveoutbottom

    spat "Eugh..."
    show bg blacklang with slowdissolve
    $ quick_menu = False
    # [*thud sound on wood*]

label start_2v3:

    scene bg blacklang with fade
    # [play rooster sound]
    play sound "audio/rooster sound.mp3" volume 0.6
    scene bg insidehouseday with slowdissolve
    stop sound fadeout 2.0
    # [play stomach rumbling sound]
    $ quick_menu = True
    show spat tired at defaultright with moveinbottom
    spat "Mmm…"
    play sound "audio/stomach rumble sound.mp3"
    show spat sad at defaultright with veryfastdissolve
    spat "My head hurts…"
    hide spat sad
    # [play stomach rumbling sound]
    show paws confused2 at defaultdog with veryfastdissolve
    play sound "audio/dog whimper arf.mp3" volume 0.7
    paws "Arf? *concerned whines*"
    hide paws confused2
    show spat sad at defaultright with veryfastdissolve
    spat "Paws...?"
    hide paws confused2
    show spat tired at defaultright with veryfastdissolve
    spat "What happened...?"
    show bg insidehouseday with flash
    hide paws confused2
    show spat emotional at defaultright with flash
    spat "I remember..."
    hide spat emotional
    show paws worried2 at defaultdog with veryfastdissolve
    play sound "audio/dog whimper arf.mp3" volume 0.7
    paws "Arf..."
    hide paws worried2
    play sound "audio/stomach rumble sound.mp3"
    show spat thumbsup at defaultright with veryfastdissolve 
    spat "It's okay, buddy… I'm fine now."
    # [play stomach rumbling sound]
    show spat sad at defaultright with veryfastdissolve
    spat "I'm hungry... I haven't eaten since yesterday…"
    hide spat sad
    show paws angry2 at defaultdog with veryfastdissolve
    play sound "audio/angry bark arf.mp3" volume 0.7
    paws "*Concerned Whining* Arf! Arf!"
    hide paws angry2 with moveoutright
    $ quick_menu = False
    scene bg dumpsitedaywithpeople with fade
    play sound "audio/crowd noise muffled.mp3" 
    show spat idle at defaultright with moveinright
    pause 0.8
    show spat tired at defaultright with veryfastdissolve
    stop sound fadeout 3.0
    $ quick_menu = True
    spat "What is it now...?"
    hide spat tired
    crowdmurmurs "Died yesterday…"
    crowdmurmurs "3 people packed up and left…"
    show spat verytired at defaultright with veryfastdissolve
    spat "I don't... wanna eat anymore..."
    hide spat verytired
    $ quick_menu = False

label choices_5:
menu:
    "Go to dumpsite peak":
        jump choices5_a
    "Talk to the locals":
        jump choices5_b

label choices5_a:
    scene bg blacklang with slowdissolve 
    play sound "audio/climbing sound effect.mp3"
    pause 4.0
    scene bg dumpsitepeaknoon with fade
    $ quick_menu = True
    play music "audio/bgm saddening.mp3" volume 0.7
    spat "I… I don’t know what to do anymore Paws…"

    spat "I don’t see a future in here anymore"

    spat "Somebody… just died."

    spat "Government man told us we’re at high risk for fires."

    spat "Everything around is telling us to leave."

    spat "We either stay here and die from sickness…"

    spat "Or burn to death…"

    spat "Or… we could…"

    spat "Leave?"

    spat "Sure, we have nothing, but it's better than staying, right?"

    spat "Staying here feels like a trap for death."

    play sound "audio/dog whimper arf.mp3" volume 0.5
    paws "*whimpers*"

    spat "I’m tired and hungry…"

    spat "But I don’t want to go back either…"

    spat "I need to make a decision…"

    spat "or else- !!"
    $ quick_menu = False
    jump choices_5vA

label choices_5vA:
menu:
    "Go home":
        jump choices5_vA
    "Stay and think":
        jump choices5_vB

label choices5_vA:
    $ quick_menu = True
    
    spat "We….."

    spat "We can’t stay."

    spat "We’re going to die here either way."

    spat "At least out there, we have a chance!"

    spat "We’ll start over!"

    spat "We have lots of things to sell, I’m sure we can earn enough till we get a job right?"
    play sound "audio/dog happy arf.mp3" volume 0.5
    paws "Arf!"

    spat "Attaboy Paws!"

    spat "W-we… We’re not dying here!"
    play sound "audio/dog happy arf.mp3" volume 0.5
    paws "Arf!"
    play sound "audio/dog happy arf.mp3" volume 0.5
    paws "Arf!"
    stop music fadeout 2.0
    scene bg insidehousenoon with fade
    show spat verytired at defaultright with veryfastdissolve
    spat "Are… Are we sure about this?"
    show spat idle at defaultright with veryfastdissolve
    spat "I mean, what if we just stayed and did something to pass the time?"
    show spat likewise at defaultright with veryfastdissolve
    spat "You know… maybe make the house prettier?"
    hide spat likewise
    $ quick_menu = False
    jump goodorneutralending

label goodorneutralending:
menu:
    "Pack up and leave":
        jump good
    "Decorate the house":
        jump neutral

label good:
    $ quick_menu = True
    show spat sad at defaultright with veryfastdissolve
    spat "What am I thinking?"
    show spat idle at defaultright with veryfastdissolve
    spat "it would be stupid to stay here."
    show spat joyful at defaultright with veryfastdissolve
    spat "No turning back."
    show spat likewise at defaultright with veryfastdissolve
    spat "We're leaving Paws!"
    hide spat with moveoutright

    jump goodending
    # [*play good ending cutscene*]

    # [*show screen: Good Ending: You made the right decision*]

return

label neutral:
    $ quick_menu = True
    show spat verytired at defaultright with veryfastdissolve
    spat "I’m just overthinking things…"
    show spat tired at defaultright with veryfastdissolve
    spat "Yeah it's just scary now because of the chaos."
    show spat sad at defaultright with veryfastdissolve
    spat "It’ll pass. We’ll be fine."
    show spat idle at defaultright with veryfastdissolve
    spat "Let’s just fix up the house instead of thinking about bad things."
    hide spat idle
    show paws happy2 at defaultdog with veryfastdissolve
    play sound "audio/dog happy arf.mp3" volume 0.5
    paws "Arf! Arf!"
    
    # [*play neutral ending cutscene*]

    # [*show screen: neutral Ending: not too good, not too bad*]

    jump neutralending

return

label choices5_vB:
    $ quick_menu = True
    spat "If we stay, we might die."

    spat "But if we leave, we might have nothing to feed ourselves."

    spat "It’s either stay here and risk burning alive, or go out there and be left helpless."

    spat "None of these choices seem favorable…"

    spat "I don’t wanna think anymore…"

    spat "I-I… I need to lie down and think…"

    scene bg dumpsitesleep with dissolve

    spat "..."

    spat "I just wanna live comfortably…"

    spat "..........."

    spat "......."

    spat "..."
    stop music fadeout 2.0
    jump badending
    # [*scene fades to black*]
    # [*cricket sounds, owls hooting*]
    # [*play bad ending cutscene*]
    # [*show screen: Bad Ending: Decisions have their own consequences.*]

return

label choices5_b:
    $ quick_menu = True
    show elias idle at defaultright with veryfastdissolve
    elias "We’ve been in this dumpsite for a long time now, I’m sure it’ll pass."
    hide elias idle
    show basilio idle2 at defaultright with hpunch
    play sound "audio/coughing2.mp3" volume 0.5
    basilio "*coughs loudly*"
    hide basilio idle2
    show crisostomo idle2 at defaultright with hpunch
    play sound "audio/coughing1.mp3" volume 0.5
    crisostomo "*coughs blood*"
    hide crisostomo idle2
    show salvi idle at defaultright with veryfastdissolve
    salvi "I dont' know about that."
    show salvi idle2 at defaultright with veryfastdissolve
    salvi "I’m just worried that this disease will just continue to pass on to everyone but It’s not like I could leave this place either."
    hide salvi idle2
    show crispin idle at defaultright with veryfastdissolve
    crispin "Right, we have no place to go and I don’t think anyone is going to help us either."
    hide crispin idle
    show santiago idle at defaultright with veryfastdissolve
    santiago "Come on now, we’ve faced typhoons and fires."
    show santiago idle2 at defaultright with veryfastdissolve
    santiago "A common cold won’t kill us."
    hide santiago idl2
    show crisostomo idle at defaultright with veryfastdissolve
    crisostomo "I don’t think colds make you this sick."
    hide crisostomo idle at defaultright with veryfastdissolve
    show salvi idle at defaultright with veryfastdissolve
    salvi "We’ve lost so many people…"
    hide salvi idle
    show spat idle at defaultright with moveinright
    spat "What’s going on?"
    hide spat idle
    show basilio idle at defaultright with veryfastdissolve
    play sound "audio/coughing3.mp3" volume 0.5
    basilio "*coughs*"
    basilio "Hey kid."
    show basilio idle2 at defaultright with veryfastdissolve
    basilio "Just us adults deciding on what to do next…"
    hide basilio idle2
    show salvi idle at defaultright with veryfastdissolve
    salvi "Have you thought about what to do with your life yet?"
    show salvi idle2 at defaultright with veryfastdissolve
    salvi "Government and sickness and all…"
    hide salvi idle2
    $ quick_menu = False

label choices_5vB:
menu:
    "I think it'll pass":
        jump neutralchoice
    "I dont have much of a choice but to stay":
        jump bad
label neutralchoice:
    $ quick_menu = True
    show spat likewise at defaultright with veryfastdissolve
    spat "i think it’ll pass."
    hide spat likewise
    show elias idle2 at defaultright with veryfastdissolve
    elias "See, he gets it!"
    show elias idle at defaultright with veryfastdissolve
    elias "Nothing but ups and downs here in the dump, huh?"
    hide elias idle
    show spat idle at defaultright with veryfastdissolve
    pause 0.3
    show spat thumbsup at defaultright with veryfastdissolve
    spat "Yeah… It sure is."
    hide spat thumbsup
    show santiago idle2 at defaultright with veryfastdissolve
    santiago "Learn from the kid and grow a pair!"
    show santiago idle at defaultright with veryfastdissolve
    santiago "Getting scared over a cold and all."
    # [Residents laugh in unison]
    hide santiago
    show spat happy at defaultright with veryfastdissolve
    spat "(I feel more at ease now hearing how they think.)"
    show spat idle at defaultright with veryfastdissolve
    spat "(I should go home.)"
    hide spat idle at defaultright with moveoutright
    scene bg insidehouseday with fade

    jump neutral

label bad:
    $ quick_menu = True
    show spat verytired at defaultright with veryfastdissolve
    spat "(Ugh… I’m being put on the spot…)"
    show spat sad at defaultright with veryfastdissolve
    spat "(I need to say something…)"
    show spat likewise at defaultright with veryfastdissolve
    spat "I guess… I don’t have much of a choice but to stay."
    show spat idle at defaultright with veryfastdissolve
    spat "If we stay, we might die."
    show spat joyful at defaultright with veryfastdissolve
    spat "But there’s a chance we’ll also survive this."
    show spat sad at defaultright with veryfastdissolve
    spat "If we leave, we’ll have nothing to feed ourselves."
    show spat emotional at defaultright with veryfastdissolve
    spat "I’d rather stay here where my home is than be a beggar on the streets, begging for scraps."
    hide spat emotional
    show crisostomo idle2 at defaultright with veryfastdissolve
    crisostomo "Even a kid is more reasonable than you lot."
    hide crisostomo idle2
    show salvi idle at defaultright with veryfastdissolve
    salvi "Yeah, it’s not like we have a choice but to stay."
    show salvi idle2 at defaultright with veryfastdissolve
    salvi "But we at least have the right to fear for our lives."
    hide salvi idle2
    show spat sad at defaultright with veryfastdissolve
    spat "(I don’t think I’m confident with that answer of mine.)"
    show spat verytired at defaultright with veryfastdissolve
    spat "(People have died for God’s sake…)"
    show spat verysad at defaultright with veryfastdissolve
    spat "(A child like me will just be another corpse.)"
    show spat emotional at defaultright with veryfastdissolve
    spat "(I should go home.)"
    hide spat emotional at defaultright with moveoutright
    scene bg insidehouseday with fade
    show spat verysad at defaultright with veryfastdissolve
    spat "Staying here is still very scary…"
    show spat emotional at defaultright with veryfastdissolve
    spat "But I feel like I’ll die on the streets"
    show spat verytired at defaultright with veryfastdissolve
    spat "I’m nothing but a candidate for a corpse…"
    show spat sad at defaultright with veryfastdissolve
    spat "..."
    show spat tired at defaultright with veryfastdissolve
    spat "I don’t wanna think anymore…"
    show spat verytired at defaultright with veryfastdissolve
    spat "I-I… I need to lie down and think…"
    hide spat verytired with moveoutbottom
    spat "............"

    spat "I just wanna live comfortably…"

    spat "......."

    spat "....."

    spat "..."

    jump badending
    # [*scene fades to black*]
    # [*cricket sounds, owls hooting*]
    # [*play bad ending cutscene*]
    # [*show screen: Bad Ending: Decisions have their own consequences.*]

label badending:
    $ quick_menu = False
    scene bg blacklang with slowdissolve
    pause 1.0
    play sound "audio/bad ending sound.mp3" volume 0.6
    scene bg blacklang
    pause 17
    stop sound fadeout 8.0
    pause 3

    #*rumbling bgm*
    #*screaming sfx*
    #*crying sfx*
    #*crashing sfx*
    #*slow silence*
    
    play sound "audio/angry bark arf.mp3"
    paws "ARF! ARF ARF!"
    play sound "audio/angry bark arf.mp3"
    paws "ARF!!"
    play sound "audio/angry bark arf.mp3"
    paws "ARF ARF!!"
    
    spat "...pa...."

    spat "paw...ss...."
    play sound "audio/spat cough.mp3"
    spat "*coughs*"
    play music "audio/undertale ending.mp3" volume 0.6
    scene bg badending with slowdissolve
    # [*fades into spat dead; remove name boxes*]
    play sound "audio/paws crying.mp3" volume 0.7
    narrator "H-hey bud..."
    
    # [*dog whimpering sfx*]

    narrator "I don’t… think i can s-stay awake…"

    show black with dissolve
    pause 0.1
    hide black with dissolve
    pause 0.2
    show black with dissolve
    pause 0.3
    hide black with dissolve

    narrator "i-is it o-okay if i s… sleep?"

    # [*screen slow blinking to black*]

    narrator "D-dont wor..ry…"

    narrator "We’ll h-have…"

    narrator "Chicken and r-rice… tomorrow…"

    narrator "I-i’ll get u-us…"

    # [*screen slow blinking to black*]

    narrator "A chicken l-leg this t-...."
    
    scene bg blacklang with slowdissolve
    play sound "audio/paws howling.mp3" volume 0.8

    pause 9.0
   
    # [*screen fades to black*]

    # [*dog howling sfx* (play for 3-5 seconds)*]

    # [*fade to bad ending screen*]

    jump badcredits

return

label goodending:
    $ quick_menu = False
    scene bg blacklang with slowdissolve
    play music "audio/traffic noise.mp3" volume 0.5
    scene bg cityroad with dissolve
    
    # [bg *city view with spat and paws walking on the side of the road*]
    
    narrator "We’ll get through this together paws.."

    narrator "We have 1000 pesos and some leftover bread."

    narrator "This is enough to get us through till we get ourselves a job."

    narrator "I sense great things for us…"
    play sound "audio/dog happy arf.mp3" volume 0.5
    narrator "Arf! Arf!"

    # [*screen fades to black*]
    stop music fadeout 10
    scene bg blacklang with slowdissolve
    
    narrator "5 years later.."
    pause 1.0
    scene bg city with fade
    play music "audio/city ambience.mp3" volume 0.5 fadein 2.0

    # [*bgm: bustling city*]

    # [*show city view worms eye*]

    narrator "hmm..."

    narrator "Paws is running low on dogfood."

    narrator "I should drop by the store later."

    # [*scene change to id frame*]

    narrator "I have to go to work..."
    play sound "audio/climbing sound effect.mp3" volume 0.7
    pause 0.7
    scene bg city1 with veryfastdissolve
    pause 0.3
    scene bg city2 with veryfastdissolve
    pause 0.3
    scene bg city3 with veryfastdissolve
    pause 0.3
    scene bg city4 with veryfastdissolve
    pause 0.3
    scene bg city5 with veryfastdissolve
    pause 0.3
    play music "audio/postgood.mp3" volume 0.7
    scene bg blacklang with slowdissolve
    
    
    # [screen fade to black]

    # [*sfx: footsteps as screen is fading*]

    # This ends the game.
    jump goodcredits

label neutralending:
    $ quick_menu = False
    scene bg blacklang with slowdissolve
    play sound "audio/repair sound.mp3" volume 0.7
    pause 5.0
    stop sound fadeout 2.0
    pause 1.0
    # [*screen fades to black*]
    # [*bgm construction at spat’s house*]

    play sound "audio/bird chirping.mp3" volume 0.7
    scene bg skyday with slowdissolve
    pause 2.0
    scene bg blacklang with slowdissolve

    scene bg houseday with fade
    pause 0.3
    scene bg housenoon with fastdissolve
    pause 0.3
    scene bg housenight with fastdissolve
    pause 0.3
    scene bg houseday with fastdissolve
    pause 0.3
    scene bg housenoon with fastdissolve
    pause 0.3
    scene bg housenight with fastdissolve
    pause 0.3
    scene bg houseday with fastdissolve
    pause 0.3
    scene bg housenoon with fastdissolve
    scene bg blacklang with slowdissolve
    play sound "audio/earthquake rumble.mp3" volume 0.8
    scene bg housenight with fade 
    pause 2.0
    scene bg housenight at earthquake with veryfastdissolve
    pause 3.0
    show spat worried at defaultright with vpunch
    $ quick_menu = True
    spat "!!!!!"
    stop sound fadeout 2.0
    $ quick_menu = False
    scene bg housenightlight with dissolve
    pause 2.0
    show spat tired at defaultright with veryfastdissolve
    pause 0.5
    show spat exhausted at defaultright with veryfastdissolve
    pause 0.5
    show spat likewise at defaultright
    $ quick_menu = True
    spat "Good thing we reinforced the house huh?"
    hide spat likewise
    play sound "audio/dog whimper arf.mp3" volume 0.6
    show paws worried at defaultdog with veryfastdissolve
    paws "*Whimpers*"
    hide paws worried with moveoutright
    $ quick_menu = False
    scene bg blacklang with slowdissolve
    play sound "audio/bird chirping.mp3" volume 0.7
    scene bg skyday with fade
    $ quick_menu = True
    spat "Another day, another work."
    spat "Right buddy?"
    play sound "audio/dog happy arf.mp3" volume 0.5
    paws "Arf!"
    $ quick_menu = False
    scene bg blacklang with slowdissolve
    jump neutralcredits


label goodcredits:
    $ quick_menu = False
    scene bg postgood with slowdissolve
    pause 2.0
    show goodcredits with fade
    pause 150
    stop music fadeout 6
    pause 6
return

label badcredits:
    $ quick_menu = False
    scene bg postbad with slowdissolve
    pause 2.0
    stop music fadeout 2.0
    show credits with fade
    pause 156

return

label neutralcredits:
    $ quick_menu = False
    scene bg postneutral with slowdissolve
    pause 2.0
    show credits with fade
    pause 156

return
