// This is a function script that changes the sprite of the active talker to the player's texture.
function Active_talker_set_Rookie () {
    sprites.destroy(Active_Talker)
    Active_Talker = sprites.create(assets.image`Rookie Armoured 1`, SpriteKind.Player)
    Active_Talker.setPosition(110, 58)
    Active_Talker.setScale(3, ScaleAnchor.Middle)
}
// This is a function script that changes the sprite of the active talker to Evil Daniel's texture.
function Active_talker_set_Daniel_Grain () {
    sprites.destroy(Active_Talker)
    Active_Talker = sprites.create(assets.image`Evil Daniel Armoured 1`, SpriteKind.Player)
    Active_Talker.setPosition(110, 58)
    Active_Talker.setScale(3, ScaleAnchor.Middle)
}
// This is a function script that changes the sprite of the active talker to Will's texture.
function Active_talker_set_Will () {
    sprites.destroy(Active_Talker)
    Active_Talker = sprites.create(assets.image`Will Armoured 1`, SpriteKind.Player)
    Active_Talker.setPosition(110, 58)
    Active_Talker.setScale(3, ScaleAnchor.Middle)
}
// This is a function script that changes the sprite of the active talker to Dom's texture.
function Active_talker_set_Alex () {
    sprites.destroy(Active_Talker)
    Active_Talker = sprites.create(assets.image`Alex Armoured 1`, SpriteKind.Player)
    Active_Talker.setPosition(110, 58)
    Active_Talker.setScale(3, ScaleAnchor.Middle)
}
// This is a function script that changes the sprite of the active talker to Ruby's texture.
function Active_talker_set_Ruby () {
    sprites.destroy(Active_Talker)
    Active_Talker = sprites.create(assets.image`Ruby Armoured 2`, SpriteKind.Player)
    Active_Talker.setPosition(110, 58)
    Active_Talker.setScale(3, ScaleAnchor.Middle)
}
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    story.clearAllText()
})
// Most of the following chuncks of code are my way of switching the costume of the Active Talker sprite. There is probably a more effective way of doing this. But this is good enough for me.
// This is a function script that changes the sprite of the active talker to Daniel's texture.
function Active_talker_set_Daniel () {
    sprites.destroy(Active_Talker)
    Active_Talker = sprites.create(assets.image`Daniel Armoured 1`, SpriteKind.Player)
    Active_Talker.setPosition(110, 58)
    Active_Talker.setScale(3, ScaleAnchor.Middle)
}
// This is a function script that changes the sprite of the active talker to Louis' texture.
function Active_talker_set_Louis () {
    sprites.destroy(Active_Talker)
    Active_Talker = sprites.create(assets.image`Louis Armoured 1`, SpriteKind.Player)
    Active_Talker.setPosition(110, 58)
    Active_Talker.setScale(3, ScaleAnchor.Middle)
}
// This clears the active talker form the screen for when a completely blank screen is needed. such as during transitions.
function Active_talker_clear () {
    sprites.destroy(Active_Talker)
}
let Active_Talker: Sprite = null
let Gender = ""
let Version_Number = textsprite.create("Beta 0.1", 15, 13)
let Version_Code = textsprite.create("25W25A")
sprites.destroy(Version_Code)
Version_Number.setPosition(32, 10)
// This contains the first set of screens that show the title of the game and who made it, before it fades into the main menu
let i = textsprite.create("Daniel Good Presents:")
i.setPosition(90, 59)
pause(2000)
i.setText("Bushrangers")
pause(1000)
sprites.destroy(i, effects.halo, 500)
pause(1000)
music.setVolume(50)
music.play(music.createSong(assets.song`Menu 1`), music.PlaybackMode.LoopingInBackground)
scene.setBackgroundImage(assets.image`Earth`)
game.setDialogCursor(assets.image`Diologue select Icon`)
game.splash("Press Space to Start", "Right arrow to skip text")
scene.setBackgroundImage(assets.image`Background`)
music.stopAllSounds()
music.setVolume(100)
Active_talker_set_Daniel()
story.setSoundEnabled(true)
story.printCharacterText("Hi. Welcome to Blue Team! My name's Daniel and I'm the commander of this Squad.", "Daniel")
story.printCharacterText("If You Follow Me, I can introduce you to the team.", "Daniel")
story.printCharacterText("So, uhhh. I may or may not have forgotten your name. Could you remind me real quick?", "Daniel")
let UserName = game.askForString("What's Your name?")
// This checks for any slurs that may be put into the name. I haven't written all the slurs I can think of but here were the main ones that came up when I asked people to put a name in during testing.
if (UserName == "Nigger" || (UserName == "Fuck" || (UserName == "Shit" || (UserName == "Osama" || false)))) {
    story.printCharacterText("Hmmm. I don't think " + ("" + UserName) + " Is appropriate for this environment. Restart", "Daniel")
    pause(1000)
    game.reset()
}
story.printCharacterText("Hey! " + UserName + "! I knew it was something like that... definitely...", "Daniel")
story.printCharacterText("Alright, Let's introduce you to everyone.", "Daniel")
story.showPlayerChoices("Ok.", "Do I have to?")
if (story.checkLastAnswer("Do I have to?")) {
    story.printCharacterText("Well, I mean. The game won't really make sense if you don't know anyone.", "Daniel")
    story.printCharacterText("Actually. I won't have a Game at all.", "Daniel")
    story.printCharacterText("I guess that means we just have to stare at each other uncomfortably.", "Daniel")
    pause(2000)
    story.printCharacterText("I've never had a Rookie on the team before.", "Daniel")
    story.printCharacterText("Are you all this weird?", "Daniel")
    story.showPlayerChoices("Yes.", "I don't know. I just work here.", "No.")
    pause(2000)
    story.showPlayerChoices("This Is awkward.", "You have great eyes.")
    if (story.checkLastAnswer("This Is awkward.")) {
        story.printCharacterText("Yeah. It really is.", "Daniel")
        story.printCharacterText("I think you should just restart the game at this point.", "Daniel")
        game.setGameOverEffect(false, effects.starField)
        game.gameOver(false)
        game.setGameOverMessage(false, "Awkward Ending!")
    } else {
        story.printCharacterText("...", "Daniel")
        story.printCharacterText("Um", "Daniel")
        story.printCharacterText("Thanks?", "Daniel")
        story.printCharacterText("I Guess?", "Daniel")
        story.printCharacterText("I think you should just restart the game at this point.", "Daniel")
        game.setGameOverEffect(false, effects.starField)
        game.gameOver(false)
        game.setGameOverMessage(false, "Awkward Ending!")
    }
} else {
    story.printCharacterText("Great! First up is Blue 2. Will B-064.", "Daniel")
    story.printCharacterText("Will is the marksman of our team. He can hit just about anything with his rifle. ", "Daniel")
    story.printCharacterText("Hey Will!", "Daniel")
    Active_talker_set_Will()
    story.printCharacterText("Yeah? What?", "Will")
    story.printCharacterText("Oh!, Is this our new number 6?", "Will")
    Active_talker_set_Daniel()
    story.printCharacterText("Yep. His? Her? Wait, What gender are You?", "Will")
    story.showPlayerChoices("Male", "Female", "Attack Helicopter", "Other")
    if (story.getLastAnswer() == "Male") {
        Gender = story.getLastAnswer()
    } else if (story.getLastAnswer() == "Female") {
        Gender = story.getLastAnswer()
    } else if (story.getLastAnswer() == "Attack Helicopter") {
        Gender = story.getLastAnswer()
    } else {
        Gender = game.askForString("What do you Identify As?", 24)
    }
    story.printCharacterText("Right... so " + Gender + "'s Name is " + UserName, "Daniel")
    story.printCharacterText("" + UserName + " Was assigned to our team as a Rookie.", "Daniel")
    story.printCharacterText("Alright. So that was Will. Now lets move on.", "Daniel")
    story.printCharacterText("Next We Have Blue 3. Ruby B-115", "Daniel")
    story.printCharacterText("Ruby is by far the fastest one on our team. She can have a bit of a short fuse, but she's harmless if you're on the right side.", "Daniel")
    story.printCharacterText("Ruby!", "Daniel")
    Active_talker_set_Ruby()
    story.printCharacterText("What?", "Ruby")
    Active_talker_set_Daniel()
    story.printCharacterText("This is our new Rookie", "Daniel")
    Active_talker_set_Ruby()
    story.printCharacterText("Oh! Hi!", "Ruby")
    story.printCharacterText("My name's Ruby, and you are?...", "Ruby")
    story.showPlayerChoices(UserName, "The new Rookie.")
    if (story.checkLastAnswer("The new Rookie.")) {
        story.printCharacterText("Yeah, I know but what's your-", "Ruby")
        story.printCharacterText("Never mind.", "Ruby")
    } else {
        story.printCharacterText("" + UserName + "! Nice to meet you.", "Ruby")
    }
    story.printCharacterText("Alright. Well that's that. I should probably get back to training. Catch you later?", "Ruby")
    Active_talker_set_Daniel()
    story.printCharacterText("Nearly done! We've got two more people to go!", "Daniel")
    story.printCharacterText("Next is Blue 4. Louis B-820.", "Daniel")
    story.printCharacterText("Louis is the pilot. He is the one who gets us in and out of our missions.", "Daniel")
    story.printCharacterText("You usually find him tinkering with his bird.", "Daniel")
    story.printCharacterText("But he can get a bit-", "Daniel")
    scene.cameraShake(7, 500)
    story.printCharacterText("SHIT!", "Louis")
    Active_talker_set_Louis()
    story.printCharacterText("F#CKING SHIT!", "Louis")
    Active_talker_set_Daniel()
    story.printCharacterText("Non Family-Friendly...", "Daniel")
    story.printCharacterText("Hey! Louis!", "Daniel")
    Active_talker_set_Louis()
    story.printCharacterText("What?", "Louis")
    Active_talker_set_Daniel()
    story.printCharacterText("Our new Rookie's here, try and keep it PG and not use such a... colourful set of words please?", "Daniel")
    Active_talker_set_Louis()
    story.printCharacterText("Fine", "Louis")
    story.printCharacterText("Hi, How's it going?", "Louis")
    story.showPlayerChoices("Good.", "What happened back there?")
    if (story.checkLastAnswer("What happened back there?")) {
        story.printCharacterText("A fuel tank combusted while it was active.", "Louis")
    }
    scene.cameraShake(5, 500)
    story.printCharacterText("BANG!", "")
    story.printCharacterText("Shit.", "Louis")
    story.printCharacterText("I gotta go fix that.", "Louis")
    Active_talker_set_Daniel()
    story.printCharacterText("So Yeah. That's Louis...", "Daniel")
    story.printCharacterText("Anyway, Last one.", "Daniel")
    story.printCharacterText("Alex B-517", "Daniel")
    story.printCharacterText("The Demo man.", "Daniel")
    story.printCharacterText("He's the one that carries all of our ordnance. Explosives, heavy weapons, Spare ammunition, the works.", "Daniel")
    Active_talker_set_Alex()
    story.printCharacterText("Hey! You must be the new rookie! ", "Alex")
    story.printCharacterText("Got a question for ya.", "Alex")
    story.printCharacterText("How many kilos of explosives would I need to blow this facility sky high?", "Alex")
    story.showPlayerChoices("10", "50", "100", "Why do you ask?")
    if (story.checkLastAnswer("Why do you ask?")) {
        story.printCharacterText("No reason.", "Alex")
        story.printCharacterText("Ya'know, higher ups want a failsafe if this facility falls into the wrong hands.", "Alex")
        story.printCharacterText("Nothing too important", "Alex")
    }
    story.printCharacterText("Alright, thanks for the help. I gotta go now.", "Alex")
    story.printCharacterText("BANG!", "")
    scene.cameraShake(4, 500)
    Active_talker_set_Louis()
    story.printCharacterText("F#CK! ALEX! STOP LEAVING THE THERMAL CORD NEAR THE THRUSTERS!", "Louis")
    Active_talker_set_Daniel()
    story.printCharacterText("Yikes. That does not sound good. We should go check it out", "Daniel")
    story.printCharacterText("Louis!? What happened?", "Daniel")
    Active_talker_set_Louis()
    story.printCharacterText("Alex left his goddamn explosive thermal cord behind my thruster.", "Louis")
    story.printCharacterText("I activated the thrusters to test that they work, but it activates Alex's thermal cord and nearly blows the ship to the ninth realm!", "Louis")
    Active_talker_set_Alex()
    story.printCharacterText("What did I do?", "Alex")
    Active_talker_set_Louis()
    story.printCharacterText("You nearly killed me!", "Louis")
    story.printCharacterText("You left your thermal cord near my thrusters during testing!", "Louis")
    Active_talker_set_Alex()
    story.printCharacterText("WHAT!? NO! My thermal cord is right here!", "Alex")
    story.printCharacterText("It was right here...", "Alex")
    Active_talker_set_Louis()
    story.printCharacterText("I don't see it.", "Louis")
    Active_talker_set_Alex()
    story.printCharacterText("I swear! I had it on me!", "Alex")
    Active_talker_set_Daniel()
    story.printCharacterText("Alright! Chill.", "Daniel")
    story.printCharacterText("We'll have a meeting and discuss some problems.", "Daniel")
    story.printCharacterText("It will also be a good chance to show " + UserName + " how our team functions.", "Daniel")
    Active_talker_clear()
    game.splash("The Meeting", "Spacebar to continue")
    Active_talker_set_Daniel()
    story.printCharacterText("Ok.", "Daniel")
    story.printCharacterText("You have all been called here to discuss some issues that have been occouring.", "Daniel")
    story.printCharacterText("Now, I have received word from command that someone on our team has been working for the enemy.", "Daniel")
    story.printCharacterText("Before we start pointing fingers, we should all do some investigating to see if we can get a lead.", "Daniel")
    story.showPlayerChoices("*Stay Quiet*", "Blame Alex", "Blame Daniel", "Blame Will", "Blame Ruby")
    if (story.checkLastAnswer("Blame Daniel")) {
        story.printCharacterText("...", "Daniel")
        story.printCharacterText("What?", "Daniel")
        Active_talker_clear()
        game.splash("After the Meeting", "Press space to continue")
        Active_talker_set_Daniel()
        story.printCharacterText("Hmm. Didn't think the Rookie would catch onto me this early.", "Daniel")
        Active_talker_set_Daniel_Grain()
        story.printCharacterText("You know... It's really unfortunate that it has to end this way.", "Daniel")
        story.printCharacterText("I really enjoyed your time on the team.", "Daniel")
        story.printCharacterText("But the truth is...", "Daniel")
        story.printCharacterText("The game was rigged from the start.", "Daniel")
        Active_talker_clear()
        game.setGameOverEffect(false, effects.melt)
        game.setGameOverMessage(false, "You Died.")
        game.gameOver(false)
    } else if (story.checkLastAnswer("Blame Alex")) {
        Active_talker_set_Alex()
        story.printCharacterText("Why me?", "Alex")
        story.printCharacterText("Hmph.", "Alex")
        story.printCharacterText("I didn't do anything", "Alex")
        Active_talker_clear()
        game.splash("After the Meeting", "Press space to continue")
        Active_talker_set_Daniel()
        story.printCharacterText("Hey, I think you're on the right track with Alex.", "Daniel")
        story.printCharacterText("But it would have been better if you didn't call him out.", "Daniel")
        story.printCharacterText("Now he knows we're onto him, he's going to be a lot sneakier.", "Daniel")
    } else if (story.checkLastAnswer("Blame Will") || story.checkLastAnswer("Blame Ruby")) {
        Active_talker_set_Daniel()
        story.printCharacterText("Umm... Let's get some evidence first.", "Daniel")
        game.splash("After the Meeting", "Press Space to continue")
    } else {
        Active_talker_set_Daniel()
        story.printCharacterText("Alright! let's Scooby Doo this shit!", "Daniel")
        game.splash("After the Meeting", "Press Space to continue")
    }
    Active_talker_set_Daniel()
    story.printCharacterText("Alright! let's Scooby Doo this shit!", "Daniel")
    story.printCharacterText("Ok, " + UserName + ", I think it might be Alex.")
    story.printCharacterText("But we need proof.", "Daniel")
    story.printCharacterText("This is where you come in.", "Daniel")
    story.printCharacterText("Your job is to go around and ask the others questions and try to get evidence agains Alex.", "Daniel")
    story.printCharacterText("Go ask around and try to find Alex. I've got some things I need to do.", "Daniel")
    story.showPlayerChoices("Ask Will", "Ask Ruby", "Ask Louis")
    // This is a fork in the story that hopefully sways the players choice on the imposter at the end.
    if (story.checkLastAnswer("Ask Will")) {
        story.printCharacterText("Ok. Go see if will has noticed anything while you're there", "Daniel")
        Active_talker_set_Will()
        story.printCharacterText("Hey Rookie. What's up?", "Will")
        story.showPlayerChoices("Have you seen Alex?", "Who do you think the imposter is?")
        if (story.checkLastAnswer("Who do you think the imposter is?")) {
            story.printCharacterText("Honestly, ever since Alex showed up Daniel's been...", "Will")
            story.printCharacterText("Off...", "Will")
            story.printCharacterText("I- Well, I me- It's kinda hard to explain.", "Will")
            story.printCharacterText("He used to have this 'Flair' of sorts.", "Will")
            story.printCharacterText("I know it seems stupid, But he also seems luckier if that makes sense.", "Will")
            story.showPlayerChoices("How so?", "No, that makes a little sense.")
            if (story.checkLastAnswer("How so?")) {
                story.printCharacterText("He used to kind of have an omen I guess.", "Will")
                story.printCharacterText("During important moments, usually comedically bad thing would happen to him. ", "Will")
                story.printCharacterText("There was this one time where we were fending off a hoard of infected", "Will")
                story.printCharacterText("And in the middle of the battle,", "Will")
                story.printCharacterText("A.C.E told us all that Daniel had 5 seconds before his armour shut down for,", "Will")
                story.printCharacterText("I kid you not...", "Will")
                story.printCharacterText("A windows update.", "Will")
            }
            story.printCharacterText("Yeah. Basically, he seems luckier.", "Will")
            story.printCharacterText("Something else seems off as well, but I can't quite put my finger on it...", "Will")
            story.printCharacterText("Is there anything else you need?", "Will")
            Active_talker_set_Rookie()
            story.printCharacterText("Yeah, have you seen Alex at all?", UserName)
        }
        Active_talker_set_Will()
        story.printCharacterText("Yeah, he's just down the hall, to the left", "Will")
        story.printCharacterText("There will be a couple of rooms, he'll be in the one with a symbol of a bomb.", "Will")
    } else if (story.checkLastAnswer("Ask Ruby")) {
        story.printCharacterText("Alright, Go get 'em.", "Daniel")
        Active_talker_set_Ruby()
        story.printCharacterText("" + UserName + "! Whatcha need?", "Ruby")
        story.showPlayerChoices("I need to find Alex", "What are your thoughts on the spy?")
        if (story.checkLastAnswer("What are your thoughts on the spy?")) {
            story.printCharacterText("Oh...", "Ruby")
            story.printCharacterText("Y'know what? I can trust you.", "Ruby")
            story.printCharacterText("But you have to promise NOT to tell him. Ok?", "Ruby")
            story.showPlayerChoices("Actually, Never Mind.", "I promise.")
            if (story.checkLastAnswer("I promise.")) {
                story.printCharacterText("When Alex joined our team as our 5th member", "Ruby")
                story.printCharacterText("Louis started to get angrier easier.", "Ruby")
                story.printCharacterText("And it's in a way that almost makes it seem that the pair knew eachother previously ", "Ruby")
                story.printCharacterText("Unfortunately, I have a feeling that Louis might not be as reliable as the rest of the Team thinks.", "Ruby")
                story.printCharacterText("Anyway, moving on...", "Ruby")
                story.printCharacterText("I heard You're looking for Alex?", "Ruby")
                story.printCharacterText("Lucky, I know where he is. Because when he disappears, it gets hard to find him.", "Ruby")
            } else {
                story.printCharacterText("I appreciate your honesty", "Ruby")
                story.printCharacterText("If you're looking for Alex...", "Ruby")
            }
        }
        story.printCharacterText("Alex is in his locker room. It's down the Hall that way.", "Ruby")
        story.printCharacterText("The door has a bomb symbol on it. You can't miss it.", "Ruby")
    } else if (story.checkLastAnswer("Ask Louis")) {
        story.printCharacterText("Yeah, Louis might know where you can find Alex.", "Daniel")
        Active_talker_set_Louis()
        story.printCharacterText("Hey. How's it going?", "Louis")
        story.showPlayerChoices("Do you know where Alex is?", "Who do you think the mole is?")
        if (story.checkLastAnswer("Who do you think the mole is?")) {
            story.printCharacterText("Alex.", "Louis")
            story.printCharacterText("I don't even need to think about it.", "Louis")
            story.printCharacterText("Ever since he joined the team, He's been trying to get me killed.", "Louis")
            story.printCharacterText("I honestly don't know how no one has picked up on the little F#cker.", "Louis")
            story.printCharacterText("But that's enough of that. I heard You're looking for the little brat.", "Louis")
        }
        story.printCharacterText("He's over at the barracks. There'll be a door with a bomb on it. He'll be in there.", "Louis")
    }
}
Active_talker_clear()
i = textsprite.create("Thanks for Playing!")
i.setPosition(90, 59)
