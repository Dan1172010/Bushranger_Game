# Most of the following chuncks of code are my way of switching the costume of the Active Talker sprite. There is probably a more effective way of doing this. But this is good enough for me.
# This is a function script that changes the sprite of the active talker to Daniel's Beat up texture.
def Active_talker_set_Beat_Up_Daniel():
    global Active_Talker
    sprites.destroy(Active_Talker)
    Active_Talker = sprites.create(assets.image("""
            Daniel damaged Armoured 1
            """),
        SpriteKind.player)
    Active_Talker.set_position(110, 58)
    Active_Talker.set_scale(3, ScaleAnchor.MIDDLE)
# This is a function script that changes the sprite of the active talker to the player's texture.
def Active_talker_set_Rookie():
    global Active_Talker
    sprites.destroy(Active_Talker)
    Active_Talker = sprites.create(assets.image("""
            Rookie Armoured 1
            """),
        SpriteKind.player)
    Active_Talker.set_position(110, 58)
    Active_Talker.set_scale(3, ScaleAnchor.MIDDLE)
# This is a function script that changes the sprite of the active talker to Evil Daniel's texture.
def Active_talker_set_Daniel_Grain():
    global Active_Talker
    sprites.destroy(Active_Talker)
    Active_Talker = sprites.create(assets.image("""
            Evil Daniel Armoured 1
            """),
        SpriteKind.player)
    Active_Talker.set_position(110, 58)
    Active_Talker.set_scale(3, ScaleAnchor.MIDDLE)
# This is a function script that changes the sprite of the active talker to Will's texture.
def Active_talker_set_Will():
    global Active_Talker
    sprites.destroy(Active_Talker)
    Active_Talker = sprites.create(assets.image("""
            Will Armoured 1
            """),
        SpriteKind.player)
    Active_Talker.set_position(110, 58)
    Active_Talker.set_scale(3, ScaleAnchor.MIDDLE)
# This is a function script that changes the sprite of the active talker to Louis' texture.
def Active_talker_set_Louis_Dead():
    global Active_Talker
    sprites.destroy(Active_Talker)
    Active_Talker = sprites.create(assets.image("""
            Louis Killed 1
            """),
        SpriteKind.player)
    Active_Talker.set_position(110, 58)
    Active_Talker.set_scale(3, ScaleAnchor.MIDDLE)
# This is a function script that changes the sprite of the active talker to Dom's texture.
def Active_talker_set_Alex():
    global Active_Talker
    sprites.destroy(Active_Talker)
    Active_Talker = sprites.create(assets.image("""
            Alex Armoured 1
            """),
        SpriteKind.player)
    Active_Talker.set_position(110, 58)
    Active_Talker.set_scale(3, ScaleAnchor.MIDDLE)
# This is a function script that changes the sprite of the active talker to Ruby's texture.
def Active_talker_set_Ruby():
    global Active_Talker
    sprites.destroy(Active_Talker)
    Active_Talker = sprites.create(assets.image("""
            Ruby Armoured 2
            """),
        SpriteKind.player)
    Active_Talker.set_position(110, 58)
    Active_Talker.set_scale(3, ScaleAnchor.MIDDLE)

def on_right_pressed():
    story.clear_all_text()
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

# Most of the following chuncks of code are my way of switching the costume of the Active Talker sprite. There is probably a more effective way of doing this. But this is good enough for me.
# This is a function script that changes the sprite of the active talker to Daniel's kidnapped texture.
def Active_talker_set_Kidnapped_Daniel():
    global Active_Talker
    sprites.destroy(Active_Talker)
    Active_Talker = sprites.create(assets.image("""
            Daniel damaged Armoured 0
            """),
        SpriteKind.player)
    Active_Talker.set_position(110, 58)
    Active_Talker.set_scale(3, ScaleAnchor.MIDDLE)
# This is a function script that changes the sprite of the active talker to Louis' texture.
def Active_talker_set_Louis():
    global Active_Talker
    sprites.destroy(Active_Talker)
    Active_Talker = sprites.create(assets.image("""
            Louis Armoured 1
            """),
        SpriteKind.player)
    Active_Talker.set_position(110, 58)
    Active_Talker.set_scale(3, ScaleAnchor.MIDDLE)
# Most of the following chuncks of code are my way of switching the costume of the Active Talker sprite. There is probably a more effective way of doing this. But this is good enough for me.
# This is a function script that changes the sprite of the active talker to Daniel's texture.
def Active_talker_set_Disguised_Daniel():
    global Active_Talker
    sprites.destroy(Active_Talker)
    Active_Talker = sprites.create(assets.image("""
            Daniel Grain Armoured 1
            """),
        SpriteKind.player)
    Active_Talker.set_position(110, 58)
    Active_Talker.set_scale(3, ScaleAnchor.MIDDLE)
# This clears the active talker form the screen for when a completely blank screen is needed. such as during transitions.
def Active_talker_clear():
    sprites.destroy(Active_Talker)
# Most of the following chuncks of code are my way of switching the costume of the Active Talker sprite. There is probably a more effective way of doing this. But this is good enough for me.
# This is a function script that changes the sprite of the active talker to Daniel's Beat up texture.
def Active_talker_set_Dead_daneil():
    global Active_Talker
    sprites.destroy(Active_Talker)
    Active_Talker = sprites.create(assets.image("""
            Daniel dead 1
            """),
        SpriteKind.player)
    Active_Talker.set_position(110, 58)
    Active_Talker.set_scale(3, ScaleAnchor.MIDDLE)
# Most of the following chuncks of code are my way of switching the costume of the Active Talker sprite. There is probably a more effective way of doing this. But this is good enough for me.
# This is a function script that changes the sprite of the active talker to Daniel's kidnapped texture.
def Active_talker_set_Battle_damaged_Daniel():
    global Active_Talker
    sprites.destroy(Active_Talker)
    Active_Talker = sprites.create(assets.image("""
            Daniel damaged Armoured 2
            """),
        SpriteKind.player)
    Active_Talker.set_position(110, 58)
    Active_Talker.set_scale(3, ScaleAnchor.MIDDLE)
Active_Talker: Sprite = None
Gender = ""
Version_Number = textsprite.create("Beta 0.2", 15, 13)
Version_Code = textsprite.create("25W26A")
sprites.destroy(Version_Code)
Version_Number.set_position(32, 10)
# This contains the first set of screens that show the title of the game and who made it, before it fades into the main menu
i = textsprite.create("Daniel Good Presents:")
i.set_position(90, 59)
pause(2000)
i.set_text("Bushrangers")
pause(1000)
sprites.destroy(i, effects.halo, 500)
pause(1000)
music.set_volume(50)
music.play(music.create_song(assets.song("""
        Menu 1
        """)),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)
scene.set_background_image(assets.image("""
    Earth
    """))
game.set_dialog_cursor(assets.image("""
    Diologue select Icon
    """))
game.splash("Press Space to Start", "Right arrow to skip text")
scene.set_background_image(assets.image("""
    Background
    """))
music.stop_all_sounds()
music.set_volume(100)
Active_talker_set_Disguised_Daniel()
story.set_sound_enabled(True)
story.print_character_text("Hi. Welcome to Blue Team! My name's Daniel and I'm the commander of this Squad.",
    "Daniel")
story.print_character_text("If You Follow Me, I can introduce you to the team.",
    "Daniel")
story.print_character_text("So, uhhh. I may or may not have forgotten your name. Could you remind me real quick?",
    "Daniel")
UserName = game.ask_for_string("What's Your name?")
# This checks for any slurs that may be put into the name. I haven't written all the slurs I can think of but here were the main ones that came up when I asked people to put a name in during testing.
if UserName == "Nigger" or (UserName == "Fuck" or (UserName == "Shit" or (UserName == "Osama" or False))):
    story.print_character_text("Hmmm. I don't think " + ("" + str(UserName)) + " Is appropriate for this environment. Restart",
        "Daniel")
    pause(1000)
    game.reset()
story.print_character_text("Hey! " + UserName + "! I knew it was something like that... definitely...",
    "Daniel")
story.print_character_text("Alright, Let's introduce you to everyone.", "Daniel")
story.show_player_choices("Ok.", "Do I have to?")
if story.check_last_answer("Do I have to?"):
    story.print_character_text("Well, I mean. The game won't really make sense if you don't know anyone.",
        "Daniel")
    story.print_character_text("Actually. I won't have a Game at all.", "Daniel")
    story.print_character_text("I guess that means we just have to stare at each other uncomfortably.",
        "Daniel")
    pause(2000)
    story.print_character_text("I've never had a Rookie on the team before.", "Daniel")
    story.print_character_text("Are you all this weird?", "Daniel")
    story.show_player_choices("Yes.", "I don't know. I just work here.", "No.")
    pause(2000)
    story.show_player_choices("This Is awkward.", "You have great eyes.")
    if story.check_last_answer("This Is awkward."):
        story.print_character_text("Yeah. It really is.", "Daniel")
        story.print_character_text("I think you should just restart the game at this point.",
            "Daniel")
        game.set_game_over_effect(False, effects.star_field)
        game.game_over(False)
        game.set_game_over_message(False, "Awkward Ending!")
    else:
        story.print_character_text("...", "Daniel")
        story.print_character_text("Um", "Daniel")
        story.print_character_text("Thanks?", "Daniel")
        story.print_character_text("I Guess?", "Daniel")
        story.print_character_text("I think you should just restart the game at this point.",
            "Daniel")
        game.set_game_over_effect(False, effects.star_field)
        game.game_over(False)
        game.set_game_over_message(False, "Awkward Ending!")
else:
    story.print_character_text("Great! First up is Blue 2. Will B-064.", "Daniel")
    story.print_character_text("Will is the marksman of our team. He can hit just about anything with his rifle. ",
        "Daniel")
    story.print_character_text("Hey Will!", "Daniel")
    Active_talker_set_Will()
    story.print_character_text("Yeah? What?", "Will")
    story.print_character_text("Oh!, Is this our new number 6?", "Will")
    Active_talker_set_Disguised_Daniel()
    story.print_character_text("Yep. His? Her? Wait, What gender are You?", "Will")
    story.show_player_choices("Male", "Female", "Attack Helicopter", "Other")
    if story.get_last_answer() == "Male":
        Gender = story.get_last_answer()
    elif story.get_last_answer() == "Female":
        Gender = story.get_last_answer()
    elif story.get_last_answer() == "Attack Helicopter":
        Gender = story.get_last_answer()
    else:
        Gender = game.ask_for_string("What do you Identify As?", 24)
    story.print_character_text("Right... so " + Gender + "'s Name is " + UserName, "Daniel")
    story.print_character_text("" + UserName + " Was assigned to our team as a Rookie.",
        "Daniel")
    story.print_character_text("Alright. So that was Will. Now lets move on.", "Daniel")
    story.print_character_text("Next We Have Blue 3. Ruby B-115", "Daniel")
    story.print_character_text("Ruby is by far the fastest one on our team. She can have a bit of a short fuse, but she's harmless if you're on the right side.",
        "Daniel")
    story.print_character_text("Ruby!", "Daniel")
    Active_talker_set_Ruby()
    story.print_character_text("What?", "Ruby")
    Active_talker_set_Disguised_Daniel()
    story.print_character_text("This is our new Rookie", "Daniel")
    Active_talker_set_Ruby()
    story.print_character_text("Oh! Hi!", "Ruby")
    story.print_character_text("My name's Ruby, and you are?...", "Ruby")
    story.show_player_choices(UserName, "The new Rookie.")
    if story.check_last_answer("The new Rookie."):
        story.print_character_text("Yeah, I know but what's your-", "Ruby")
        story.print_character_text("Never mind.", "Ruby")
    else:
        story.print_character_text("" + UserName + "! Nice to meet you.", "Ruby")
    story.print_character_text("Alright. Well that's that. I should probably get back to training. Catch you later?",
        "Ruby")
    Active_talker_set_Disguised_Daniel()
    story.print_character_text("Nearly done! We've got two more people to go!", "Daniel")
    story.print_character_text("Next is Blue 4. Louis B-820.", "Daniel")
    story.print_character_text("Louis is the pilot. He is the one who gets us in and out of our missions.",
        "Daniel")
    story.print_character_text("You usually find him tinkering with his bird.", "Daniel")
    story.print_character_text("But he can get a bit-", "Daniel")
    scene.camera_shake(7, 500)
    story.print_character_text("SHIT!", "Louis")
    Active_talker_set_Louis()
    story.print_character_text("F#CKING SHIT!", "Louis")
    Active_talker_set_Disguised_Daniel()
    story.print_character_text("Non Family-Friendly...", "Daniel")
    story.print_character_text("Hey! Louis!", "Daniel")
    Active_talker_set_Louis()
    story.print_character_text("What?", "Louis")
    Active_talker_set_Disguised_Daniel()
    story.print_character_text("Our new Rookie's here, try and keep it PG and not use such a... colourful set of words please?",
        "Daniel")
    Active_talker_set_Louis()
    story.print_character_text("Fine", "Louis")
    story.print_character_text("Hi, How's it going?", "Louis")
    story.show_player_choices("Good.", "What happened back there?")
    if story.check_last_answer("What happened back there?"):
        story.print_character_text("A fuel tank combusted while it was active.", "Louis")
    scene.camera_shake(5, 500)
    story.print_character_text("BANG!", "")
    story.print_character_text("Shit.", "Louis")
    story.print_character_text("I gotta go fix that.", "Louis")
    Active_talker_set_Disguised_Daniel()
    story.print_character_text("So Yeah. That's Louis...", "Daniel")
    story.print_character_text("Anyway, Last one.", "Daniel")
    story.print_character_text("Alex B-517", "Daniel")
    story.print_character_text("The Demo man.", "Daniel")
    story.print_character_text("He's the one that carries all of our ordnance. Explosives, heavy weapons, Spare ammunition, the works.",
        "Daniel")
    Active_talker_set_Alex()
    story.print_character_text("Hey! You must be the new rookie! ", "Alex")
    story.print_character_text("Got a question for ya.", "Alex")
    story.print_character_text("How many kilos of explosives would I need to blow this facility sky high?",
        "Alex")
    story.show_player_choices("10", "50", "100", "Why do you ask?")
    if story.check_last_answer("Why do you ask?"):
        story.print_character_text("No reason.", "Alex")
        story.print_character_text("Ya'know, higher ups want a failsafe if this facility falls into the wrong hands.",
            "Alex")
        story.print_character_text("Nothing too important", "Alex")
    story.print_character_text("Alright, thanks for the help. I gotta go now.", "Alex")
    story.print_character_text("BANG!", "")
    scene.camera_shake(4, 500)
    Active_talker_set_Louis()
    story.print_character_text("F#CK! ALEX! STOP LEAVING THE THERMAL CORD NEAR THE THRUSTERS!",
        "Louis")
    Active_talker_set_Disguised_Daniel()
    story.print_character_text("Yikes. That does not sound good. We should go check it out",
        "Daniel")
    story.print_character_text("Louis!? What happened?", "Daniel")
    Active_talker_set_Louis()
    story.print_character_text("Alex left his goddamn explosive thermal cord behind my thruster.",
        "Louis")
    story.print_character_text("I activated the thrusters to test that they work, but it activates Alex's thermal cord and nearly blows the ship to the ninth realm!",
        "Louis")
    Active_talker_set_Alex()
    story.print_character_text("What did I do?", "Alex")
    Active_talker_set_Louis()
    story.print_character_text("You nearly killed me!", "Louis")
    story.print_character_text("You left your thermal cord near my thrusters during testing!",
        "Louis")
    Active_talker_set_Alex()
    story.print_character_text("WHAT!? NO! My thermal cord is right here!", "Alex")
    story.print_character_text("It was right here...", "Alex")
    Active_talker_set_Louis()
    story.print_character_text("I don't see it.", "Louis")
    Active_talker_set_Alex()
    story.print_character_text("I swear! I had it on me!", "Alex")
    Active_talker_set_Disguised_Daniel()
    story.print_character_text("Alright! Chill.", "Daniel")
    story.print_character_text("We'll have a meeting and discuss some problems.", "Daniel")
    story.print_character_text("It will also be a good chance to show " + UserName + " how our team functions.",
        "Daniel")
    Active_talker_clear()
    game.splash("The Meeting", "Spacebar to continue")
    Active_talker_set_Disguised_Daniel()
    story.print_character_text("Ok.", "Daniel")
    story.print_character_text("You have all been called here to discuss some issues that have been occouring.",
        "Daniel")
    story.print_character_text("Now, I have received word from command that someone on our team has been working for the enemy.",
        "Daniel")
    story.print_character_text("Before we start pointing fingers, we should all do some investigating to see if we can get a lead.",
        "Daniel")
    story.show_player_choices("*Stay Quiet*",
        "Blame Alex",
        "Blame Daniel",
        "Blame Will",
        "Blame Ruby")
    if story.check_last_answer("Blame Daniel"):
        story.print_character_text("...", "Daniel")
        story.print_character_text("What?", "Daniel")
        Active_talker_clear()
        game.splash("After the Meeting", "Press space to continue")
        Active_talker_set_Disguised_Daniel()
        story.print_character_text("Hmm. Didn't think the Rookie would catch onto me this early.",
            "Daniel")
        Active_talker_set_Daniel_Grain()
        story.print_character_text("You know... It's really unfortunate that it has to end this way.",
            "Daniel")
        story.print_character_text("I really enjoyed your time on the team.", "Daniel")
        story.print_character_text("But the truth is...", "Daniel")
        story.print_character_text("The game was rigged from the start.", "Daniel")
        Active_talker_clear()
        game.set_game_over_effect(False, effects.melt)
        game.set_game_over_message(False, "You Died.")
        game.game_over(False)
    elif story.check_last_answer("Blame Alex"):
        Active_talker_set_Alex()
        story.print_character_text("Why me?", "Alex")
        story.print_character_text("Hmph.", "Alex")
        story.print_character_text("I didn't do anything", "Alex")
        Active_talker_clear()
        game.splash("After the Meeting", "Press space to continue")
        Active_talker_set_Disguised_Daniel()
        story.print_character_text("Hey, I think you're on the right track with Alex.",
            "Daniel")
        story.print_character_text("But it would have been better if you didn't call him out.",
            "Daniel")
        story.print_character_text("Now he knows we're onto him, he's going to be a lot sneakier.",
            "Daniel")
    elif story.check_last_answer("Blame Will") or story.check_last_answer("Blame Ruby"):
        Active_talker_set_Disguised_Daniel()
        story.print_character_text("Umm... Let's get some evidence first.", "Daniel")
        game.splash("After the Meeting", "Press Space to continue")
    else:
        Active_talker_set_Disguised_Daniel()
        game.splash("After the Meeting", "Press Space to continue")
    Active_talker_set_Disguised_Daniel()
    story.print_character_text("Alright! let's Scooby Doo this shit!", "Daniel")
    story.print_character_text("Ok, " + UserName + ", I think it might be Alex.")
    story.print_character_text("But we need proof.", "Daniel")
    story.print_character_text("This is where you come in.", "Daniel")
    story.print_character_text("Your job is to go around and ask the others questions and try to get evidence agains Alex.",
        "Daniel")
    story.print_character_text("Go ask around and try to find Alex. I've got some things I need to do.",
        "Daniel")
    story.show_player_choices("Ask Will", "Ask Ruby", "Ask Louis")
    # This is a fork in the story that hopefully sways the players choice on the imposter at the end.
    if story.check_last_answer("Ask Will"):
        story.print_character_text("Ok. Go see if will has noticed anything while you're there",
            "Daniel")
        Active_talker_set_Will()
        story.print_character_text("Hey Rookie. What's up?", "Will")
        story.show_player_choices("Have you seen Alex?", "Who do you think the imposter is?")
        if story.check_last_answer("Who do you think the imposter is?"):
            story.print_character_text("Honestly, ever since Alex showed up Daniel's been...",
                "Will")
            story.print_character_text("Off...", "Will")
            story.print_character_text("I- Well, I me- It's kinda hard to explain.", "Will")
            story.print_character_text("He used to have this 'Flair' of sorts.", "Will")
            story.print_character_text("I know it seems stupid, But he also seems luckier if that makes sense.",
                "Will")
            story.show_player_choices("How so?", "No, that makes a little sense.")
            if story.check_last_answer("How so?"):
                story.print_character_text("He used to kind of have an omen I guess.", "Will")
                story.print_character_text("During important moments, usually comedically bad thing would happen to him. ",
                    "Will")
                story.print_character_text("There was this one time where we were fending off a hoard of infected",
                    "Will")
                story.print_character_text("And in the middle of the battle,", "Will")
                story.print_character_text("A.C.E told us all that Daniel had 5 seconds before his armour shut down for,",
                    "Will")
                story.print_character_text("I kid you not...", "Will")
                story.print_character_text("A windows update.", "Will")
            story.print_character_text("Yeah. Basically, he seems luckier.", "Will")
            story.print_character_text("Something else seems off as well, but I can't quite put my finger on it...",
                "Will")
            story.print_character_text("Is there anything else you need?", "Will")
            Active_talker_set_Rookie()
            story.print_character_text("Yeah, have you seen Alex at all?", UserName)
        Active_talker_set_Will()
        story.print_character_text("Yeah, he's just down the hall, to the left", "Will")
        story.print_character_text("There will be a couple of rooms, he'll be in the one with a symbol of a bomb.",
            "Will")
    elif story.check_last_answer("Ask Ruby"):
        story.print_character_text("Alright, Go get 'em.", "Daniel")
        Active_talker_set_Ruby()
        story.print_character_text("" + UserName + "! Whatcha need?", "Ruby")
        story.show_player_choices("I need to find Alex", "What are your thoughts on the spy?")
        if story.check_last_answer("What are your thoughts on the spy?"):
            Active_talker_set_Ruby()
            story.print_character_text("Unfortunately...", "Ruby")
            story.print_character_text("I think it's Louis.", "Ruby")
            story.print_character_text("Ever since Alex showed up, he's gotten angrier, easier.",
                "Ruby")
            story.print_character_text("And I'd rather leave it at that.", "Ruby")
            story.print_character_text("Also, If you're looking for Alex,", "Ruby")
        story.print_character_text("He's down the hall in the room that has a bomb on the door.",
            "Ruby")
    elif story.check_last_answer("Ask Louis"):
        story.print_character_text("Yeah, Louis might know where you can find Alex.", "Daniel")
        Active_talker_set_Louis()
        story.print_character_text("Hey. How's it going?", "Louis")
        story.show_player_choices("Do you know where Alex is?",
            "Who do you think the mole is?")
        if story.check_last_answer("Who do you think the mole is?"):
            pass
        else:
            pass
        story.print_character_text("He's over at the barracks. There'll be a door with a bomb on it. He'll be in there.",
            "Louis")
    else:
        story.print_character_text("He's over at the barracks. There'll be a door with a bomb on it. He'll be in there.",
            "Louis")
    Active_talker_set_Alex()
    story.print_character_text("Hey.", "Alex")
    story.show_player_choices("Hey", "Who do you think the boogey is?")
    if story.check_last_answer("Who do you think the boogey is?"):
        story.print_character_text("Honestly...", "Alex")
        story.print_character_text("I'm not sure", "Alex")
        Active_talker_set_Rookie()
        story.print_character_text("a lot of people think it's you", UserName)
    Active_talker_set_Alex()
    story.print_character_text("Hmm.", "Alex")
    story.print_character_text("Actually, follow me.", "Alex")
    story.show_player_choices("*stay quiet*", "Where are we going?")
    if story.check_last_answer("Where are we going?"):
        story.print_character_text("To find answers.", "Alex")
    game.splash("The Database", "Space to continue")
    story.print_character_text("Here.", "Alex")
    story.print_character_text("This is where the Dossier is held.", "Alex")
    Active_talker_set_Rookie()
    story.print_character_text("What's the Dossier?", UserName)
    Active_talker_set_Alex()
    story.print_character_text("The Dossier is an archive of everything recorded by the UNPD.",
        "Alex")
    story.print_character_text("Including info on everyone on our team.", "Alex")
    story.print_character_text("This will hopefully help us find who the imposter is.",
        "Alex")
    story.print_character_text("But we only have time to search 1 Bio, so look into who you think the Boogey is.",
        "Alex")
    story.print_character_text("Daniel's just requested we all meet him at the briefing room",
        "Alex")
    story.print_character_text("Alright, who are we choosing?", "Alex")
    story.show_player_choices("Search Daniel",
        "Search Will",
        "Search Ruby",
        "Search Louis")
    if story.check_last_answer("Search Daniel"):
        Active_talker_set_Rookie()
        story.print_character_text("Ok...", UserName)
        story.print_character_text("It says here that Daniel has a blue nametag on the right part of his chest plate.",
            UserName)
        story.print_character_text("His Reactor is a blue hexagon in the middle of his chest.",
            UserName)
        Active_talker_set_Alex()
        story.print_character_text("Is there anything else?", "Alex")
        Active_talker_set_Rookie()
        story.print_character_text("It says here he was born in Yorkshire, England", UserName)
        Active_talker_set_Alex()
        story.print_character_text("Ok, we gotta go.", "Alex")
    elif story.check_last_answer("Search Will"):
        Active_talker_set_Rookie()
        story.print_character_text("Alright.", UserName)
        story.print_character_text("Will, Will, Will...", UserName)
        story.print_character_text("Will has a modified visor attachment that improves his accuracy and sight drastically.",
            UserName)
        story.print_character_text("His reactor is a green diamond on his chest plate.",
            UserName)
        Active_talker_set_Alex()
        story.print_character_text("That all?", "Alex")
        Active_talker_set_Rookie()
        story.print_character_text("He was also born in Austin, Texas in the United States.",
            UserName)
        Active_talker_set_Alex()
        story.print_character_text("Ok. That's all we can do. Daniel wants us up there now.",
            "Alex")
    elif story.check_last_answer("Search Ruby"):
        Active_talker_set_Rookie()
        story.print_character_text("Alright Ruby, Let's see what you're hiding...", UserName)
        story.print_character_text("Ruby's got a red circular reactor in the middle of her chest piece.",
            UserName)
        story.print_character_text(" and a set of thruster jets hidden behind the plating on the back of her calves",
            UserName)
        Active_talker_set_Alex()
        story.print_character_text("Well that doesn't help. we are in a game where we can't even see our legs. ",
            "Alex")
        story.print_character_text("In fact, I didn't even know we had any", "Alex")
        story.print_character_text("What else can you find?", "Alex")
        Active_talker_set_Rookie()
        story.print_character_text("Umm...", UserName)
        story.print_character_text("She was born in Alice Springs, Australia", UserName)
        Active_talker_set_Alex()
        story.print_character_text("That's all we have time for. We've gotta go to that meeting.",
            "Alex")
    elif story.check_last_answer("Search Louis"):
        Active_talker_set_Rookie()
        story.print_character_text("Louis. The only non-PG character here. That's gotta mean something.",
            UserName)
        story.print_character_text("His reactor in the middle of his chest plate is a yellow square.",
            UserName)
        story.print_character_text("And he was born in cape town in South Africa.", UserName)
        Active_talker_set_Alex()
        story.print_character_text("Hey. Daniel's calling us up to the meeting room. We need to go now.",
            "Alex")
    game.splash("The Meeting", "Space to continue")
    Active_talker_set_Disguised_Daniel()
    story.print_character_text("Ok.", "Daniel")
    story.print_character_text("Command has told me that getting the Boogey of the team is a top priority.",
        "Daniel")
    story.print_character_text("And that we need to get it done at any cost.", "Daniel")
    story.print_character_text("Even if that means getting rid of one of us right now...",
        "Daniel")
    story.print_character_text("I have had " + UserName + " go around and investigate you lot.",
        "Daniel")
    story.print_character_text("And I believe he has found who the Boogey is.", "Daniel")
    story.print_character_text("" + UserName + " is going to tell us who the imposter is, and we will then have them removed from the team.",
        "Daniel")
    story.print_character_text("Ok, " + UserName + ". Who's the Boogey", "Daniel")
    story.show_player_choices("Daniel", "Will", "Ruby", "Louis")
    if story.check_last_answer("Daniel"):
        Active_talker_set_Disguised_Daniel()
        story.print_character_text("What?!", "Daniel")
        story.print_character_text("Why me?!", "Daniel")
        Active_talker_set_Will()
        story.print_character_text("Sorry man. Gotta agree with the Rookie on this one.",
            "Will")
        Active_talker_set_Ruby()
        story.print_character_text("What? He's our Leader?", "Ruby")
        Active_talker_set_Louis()
        story.print_character_text("And he's been with us since the start.", "Louis")
        story.print_character_text("In fact, he was the first Bushranger.", "Louis")
        Active_talker_set_Will()
        story.print_character_text("Yeah, It's just...", "Will")
        story.print_character_text("Something's off...", "Will")
        Active_talker_set_Ruby()
        story.print_character_text("The hell's that supposed to mean?!", "Ruby")
        Active_talker_clear()
        story.print_character_text("HMMM!", "???")
        Active_talker_set_Louis()
        story.print_character_text("Uhhhh. Wha-", "Louis")
        Active_talker_clear()
        story.print_character_text("HHMPHHMM! HMMMPH!", "???")
        Active_talker_set_Disguised_Daniel()
        story.print_character_text("Oh no...", "Daniel?")
        Active_talker_clear()
        story.print_character_text("IT'S NOT ME!", "???")
        Active_talker_set_Alex()
        story.print_character_text("It's coming from over there!", "Alex")
        Active_talker_set_Kidnapped_Daniel()
        story.print_character_text("Guys!", "???")
        story.print_character_text("It's Me! Daniel!", "???")
        story.print_character_text("Get me outa here!", "Daniel")
        Active_talker_set_Alex()
        story.print_character_text("Ruby, Get the bag off his head.", "Alex")
        Active_talker_set_Beat_Up_Daniel()
        story.print_character_text("Ah!", "Daniel")
        story.print_character_text("Guys! It's me!", "Daniel")
        Active_talker_set_Louis()
        story.print_character_text("Woah! What happened to you?", "Daniel")
        Active_talker_set_Beat_Up_Daniel()
        story.print_character_text("I can't remember...", "Daniel")
        story.print_character_text("But that... Thing.", "Daniel")
        story.print_character_text("It's not me...", "Daniel")
        Active_talker_set_Daniel_Grain()
        story.print_character_text("Hmm. Wondered if any of you would figure it out.",
            "Evil Daniel")
        story.print_character_text("Turns out, of all of you. It was the Rookie that caught me.",
            "Evil Daniel")
        Active_talker_set_Will()
        story.print_character_text("psst. Daniel.", "Will")
        story.print_character_text("Here's your helmet. It's a little banged up, but we can fix itlater.",
            "Will")
        Active_talker_set_Battle_damaged_Daniel()
        story.print_character_text("Thanks.", "Daniel")
        story.print_character_text("Hey, you must be the Rookie.", "Daniel")
        Active_talker_set_Rookie()
        story.print_character_text("Yes sir.", UserName)
        Active_talker_set_Battle_damaged_Daniel()
        story.print_character_text("Don't worry about the formalities. Just call me Daniel.",
            "Daniel")
        Active_talker_set_Ruby()
        story.print_character_text("Hate to break up the introduction, But where'd that 'thing' go?",
            "Daniel")
    elif story.check_last_answer("Will"):
        Active_talker_set_Will()
        story.print_character_text("What?", "Will")
        story.print_character_text("I don't- wha- How? Why?", "Will")
        story.print_character_text("It's not me!", "Will")
        Active_talker_set_Disguised_Daniel()
        story.print_character_text("Look, I wish it wasn't you, but the Rookie did his investigating.",
            "Daniel")
        story.print_character_text("The Evidence doesn't lie.", "Daniel")
        Active_talker_set_Louis()
        story.print_character_text("Are we sure It's Will?", "Louis")
        Active_talker_set_Rookie()
        story.print_character_text("Yeah.", UserName)
        story.print_character_text("It all matches up.", UserName)
        Active_talker_set_Will()
        story.print_character_text("*sigh*", "Will")
        story.print_character_text("I understand.", "Will")
        story.print_character_text("I just want you all to know...", "Will")
        story.print_character_text("I guarentee you I'm not the boogey.", "Will")
        Active_talker_clear()
        game.splash("1 Week Later", "Space to continue")
        Active_talker_set_Alex()
        story.print_character_text("Hey.", "Alex")
        Active_talker_set_Rookie()
        story.print_character_text("What if it wasn't him?", UserName)
        Active_talker_set_Alex()
        story.print_character_text("Don't think like that.", "Alex")
        story.print_character_text("You did all you could.", "Alex")
        Active_talker_clear()
        pause(100)
        Active_talker_set_Alex()
        pause(100)
        Active_talker_clear()
        pause(500)
        Active_talker_clear()
        story.print_character_text("Ummm.", "Alex")
        story.print_character_text("Who turned the lights off?", "Alex")
        story.print_character_text("Ummm. Guys?", "Ruby")
        story.print_character_text("You might want to come and see this!", "Ruby")
        story.print_character_text("What is it?", "Alex")
        story.print_character_text("Has anyone got a torch?", "Alex")
        story.print_character_text("Yeah, here.", "Louis")
        Active_talker_set_Dead_daneil()
        story.print_character_text("Oh no...", "Ruby")
        story.print_character_text("Oooohhhh.", "Louis")
        story.print_character_text("Yeah, He's dead...", "Louis")
        Active_talker_set_Alex()
        story.print_character_text("I take it back Rookie. I don't think we got him...", "Alex")
        Active_talker_set_Rookie()
        story.print_character_text("This means, He's still here.", UserName)
        Active_talker_set_Ruby()
        story.print_character_text("Uh oh.", "Ruby")
        Active_talker_set_Louis()
        story.print_character_text("What?", "Louis")
        Active_talker_set_Ruby()
        story.print_character_text("All appliances are disconnected. Nothing has power.",
            "Ruby")
        Active_talker_set_Alex()
        story.print_character_text("You don't say.", "Alex")
        Active_talker_set_Ruby()
        story.print_character_text("I mean everything. Doors included.", "Ruby")
        story.print_character_text("We're stuck in here...", "Ruby")
        Active_talker_set_Louis()
        story.print_character_text("I think this might be an appropriate time.", "Louis")
        Active_talker_set_Ruby()
        story.print_character_text("For what?", "Ruby")
        Active_talker_set_Rookie()
        story.print_character_text("A Son of a Bitch moment.", UserName)
        Active_talker_set_Louis()
        story.print_character_text("Exactly. A very big Son of a Bitch moment.", "Louis")
        Active_talker_clear()
        story.print_character_text("Ohh. This is definately a Son of a Bitch moment.", "???")
        story.print_character_text("Son of a Bitch.", "Louis")
        story.print_character_text("Enough sons of a bitches!", "Ruby")
        story.print_character_text("You just said it.", "Louis")
        story.print_character_text("Oh shut up.", "Ruby")
    elif story.check_last_answer("Ruby"):
        Active_talker_set_Ruby()
        story.print_character_text("No!", "Ruby")
        story.print_character_text("Bullshit!", "Ruby")
        story.print_character_text("What evidence do you have?!", "Ruby")
        Active_talker_set_Louis()
        story.print_character_text("He's clearly got enough to blame you!", "Louis")
        Active_talker_set_Ruby()
        story.print_character_text("Well I don't know what their source is. Because I'm not the Boogey.",
            "Ruby")
        story.print_character_text("If anything it's you.", "Ruby")
        Active_talker_set_Louis()
        story.print_character_text("F#CK OFF!", "Louis")
        Active_talker_set_Ruby()
        story.print_character_text("What?! You're the one who started to get mad when Alex showed up!",
            "Ruby")
        Active_talker_set_Disguised_Daniel()
        story.print_character_text("Louis, Put the gun down.", "Daniel")
        Active_talker_set_Louis()
        story.print_character_text("Make me.", "Louis")
        Active_talker_set_Disguised_Daniel()
        story.print_character_text("LOUIS! PUT THE GUN DOW-", "Daniel")
        Active_talker_set_Ruby()
        scene.camera_shake(4, 100)
        story.print_character_text("*Ruby shoots Louis in the head*")
        story.print_character_text("Done.", "Ruby")
        Active_talker_set_Disguised_Daniel()
        story.print_character_text("Ok...", "Daniel")
        story.print_character_text("Let's all calm down.", "Daniel")
        story.print_character_text("Holster our guns.", "Daniel")
        story.print_character_text("And hope Ruby just killed the Boogey.", "Daniel")
        Active_talker_set_Rookie()
        story.print_character_text("Are we going to need to replace him?", UserName)
        Active_talker_set_Disguised_Daniel()
        story.print_character_text("I...", "Daniel")
        story.print_character_text("Don't know.", "Daniel")
    elif story.check_last_answer("Louis"):
        Active_talker_set_Louis()
        story.print_character_text("Yeah? well F#ck you too.", "Louis")
        story.print_character_text("I can't believe you've actually listened to him, you idiot.",
            "Louis")
        Active_talker_set_Rookie()
        story.print_character_text("What do you mean?", UserName)
        Active_talker_set_Louis()
        story.print_character_text("Couldn't you tell? Why do you think Alex tried to kill me earlier?",
            "Louis")
        story.print_character_text("He's been trying to destroy this facility since he got here.",
            "Louis")
        Active_talker_set_Alex()
        story.print_character_text("Nuh Uh.", "Alex")
        story.print_character_text("Command ordered me to set up a failsafe for if the Boogey takes over the facility.",
            "Alex")
        Active_talker_set_Louis()
        story.print_character_text("Yeah,", "Louis")
        story.print_character_text("and command told me to set up 2 metric tonnes of explosives to blow your ass sky high if you try anything. ",
            "Louis")
        Active_talker_set_Alex()
        story.print_character_text("You wouldn't.", "Alex")
        Active_talker_set_Louis()
        story.print_character_text("You really want to gamble your life on a guess?", "Louis")
        Active_talker_set_Alex()
        story.print_character_text("Don't have to because I ha-", "Alex")
        Active_talker_set_Louis()
        scene.camera_shake(4, 500)
        story.print_character_text("BOOM!")
        Active_talker_set_Will()
        story.print_character_text("Woah! What have you done?!", "Will")
        Active_talker_set_Louis()
        story.print_character_text("He had a primed grenade in his hand. He was about to kill us all!",
            "Louis")
        Active_talker_set_Disguised_Daniel()
        story.print_character_text("That didn't give you the clearance to kill him!", "Daniel")
        Active_talker_set_Louis()
        story.print_character_text("It was either I kill him, or he was going to kill us!",
            "Louis")
        Active_talker_set_Rookie()
        story.print_character_text("Hey. Did any of you lock the doors?", UserName)
        Active_talker_clear()
        story.print_character_text("Yeah. That would be me...", "???")
Active_talker_clear()
i = textsprite.create("Thanks for Playing!")
i.set_position(90, 59)