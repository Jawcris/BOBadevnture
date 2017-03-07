# Git version - should use this one for now.
name= raw_input("What is your name: ")
raw_input("You are sitting in your living room, just checking your phone. There is nothing big happening around your area, it is very safe and peaceful here. Actually, this is why you chose live here, a small and quiet neighborhood, a lot better than the one you had.")
raw_input("But today is too quiet...")
raw_input("You do not see Mr. B walking his dogs toady, they walk pass you every day. You like his dogs, and they also seem to like you.")
raw_input("...")
raw_input("One hour has passed, you feel like you are at the bottom of the sea. You tried to text some friend, who you have not talked to since last year.")
raw_input("...")
raw_input("No reply.")
raw_input("...")
raw_input("You fall asleep.")
raw_input("...")
raw_input("You sit right next to someone, you cannot see her face. But you know you cherish her. She starts to run away from you, you desperately try to grab her hand. Yet, no matter how hard you try you just can't reach her.")
raw_input("...")
# the dream, forshadow something about the true end
raw_input("You are woken up by the buzzing of your phone. Someone is texting you, apparently, that person is really urgent. You have over 99 unread text message.")
for x in range(5):
    print "'Help'"
choice1= raw_input("You decide to: a. Ignore b. Reply...")
while choice1 !="b":
    print "The text messages do not seem to stop, may be if you reply the stranger, the texting will stop."
    choice1= raw_input("You decide to: a. Ignore b. Reply...")
if choice1 == "b":
    print "You replied the stranger. What do you want?"
raw_input("...")
raw_input("'Finally  someone replied me  Help  I was trapped in some place by this psycho'")
raw_input("'I stole his phone I can't call the police'")
raw_input("'I can't let him hear me'")
raw_input("'Please help me  he is about to find out  me he is gonna ki...'")
raw_input("...")
raw_input("The person stop texting you. You are worried, what if it is not a prank. Someone just told you that he or she is about to get killed")
raw_input("You decided to text the stranger. 'Are you alright?'")
raw_input("...")
raw_input("'Everything is going to be fine, " + name + ", as long as you cooperate. My name is BOB, I am not going to hurt anyone if you follow my instructions.'")
raw_input("...")
raw_input("You should be terrified. But you feel really calm, like you know what to do, what is going to happen on you.")
raw_input("Maybe you are just too bored about your peaceful life. Maybe small interlude won't be that bad.")
raw_input("Now let's start with a simple game.")
raw_input("...")
# choice 2 - play the game or not
choice2= raw_input("BOB is going to play a little game with you. You have no reason to accept, at the end, BOB and the victim may just be people who are trying to do those 'social experiment' on you. You decided to: a. Accept b. Reject...")
#while choice 2 != a and b
while choice2.lower() != "b" and choice2.lower()!="reject" and choice2.lower() != "a" and choice2.lower()!= "accept":
    print "You cannot always run away from making decison. It is your obligation to decide."
    choice2= raw_input("Now, pick one: a. Accept b. Reject...")
#reject to play
if choice2.lower() == "b" or choice2.lower()=="reject":
    raw_input("You reject BOB. There is no more text message coming, you are left alone again. You lay back to the couch, no one is going to bother you anymore.")
    raw_input("you are back in peace. You are safe again.")
    raw_input("...")
    raw_input("You fall asleep")
    raw_input("You sit right next to someone, you cannot see her face. But you know you cherish her. She starts to run away from you, you desperately try to grab her hand. Yet, no matter how hard you try you just can't reach her.")
    raw_input("...")
    raw_input("Someone opened your door. You can hear it. You walk to your front door.")
    raw_input("No one is there.")
    raw_input("Just to make sure you open the door. The sunlight is too bright, so weird it is already afternoon. You look down, you find a package.")
    raw_input("...")
    raw_input("It is soaked in blood.")
    raw_input("...")
    raw_input("You are sitting in the interrogation room. It looks like the one you have seen in movies. Grey wall, grey wall seems to crush you.")
    raw_input("...")
    raw_input("Do you recognize the ring on her finger? Who were you with before you received the package? Do you recognize these faces?")
    raw_input("These are the works done by that serial killer who already killed 28 people, of course, how could you not know, the news is everywhere!")
    raw_input("We have to protect you, maybe we could also catch that infamous killer. But the choice is still in your hand, you decide whether we will send people to be around you or not.")
    raw_input("...")
    #choice 3- have protection or not
    choice3 = raw_input("Now, you know BOB is an extremely dangerous person, your blood is pumping faster, a sense of livliness in your plain life. You decided to: a. Accept b. Reject...")
    while choice3.lower() != "b" and choice3.lower()!="reject" and choice3.lower() != "a" and choice3.lower()!= "accept":
        print "You cannot always run away from making decison. It is your obligation to decide."
        choice3= raw_input("Now, pick one: a. Accept b. Reject...")
# if accept protection
        if choice3.lower() == "a" or choice3.lower() == "accept":
            print "bo"
# if reject protection
        if choice3.lower() == "b" or choice3.lower() == "reject":
            raw_input("You reject the protection. Deeply in your mind you know that this sense of liveliness is going to lead you into something horrible.")
            raw_input("...")
            raw_input("You sit down in your cozy couch in your living room. You feel isolated once again. No one is going to intrude your life, you think confidently.")
            raw_input("...")
            raw_input("Your phone buzzes, you received a text message.")
            raw_input("'Hi! This is BOB! We haven't talked for so long, I am starting to miss you. Please come to The Great Park we shall have a face-to-face meeting there.'")
            raw_input("'And everything will be clear.'")
            raw_input("The Great Park, what a familiar name. Of course, everyone in this area know about this park, but there is something else about this park that triggers your feeling.")
            choice4= raw_input("You decide to: a. Accept b. Reject...")
            while choice4.lower() != "b" and choice4.lower()!="reject" and choice4.lower() != "a" and choice4.lower()!= "accept":
                print "You cannot always run away from making decison. It is your obligation to decide."
                choice4= raw_input("Now, pick one: a. Accept b. Reject...")
                while choice4 != "a" and choice4 != "accept":
                    print "You should go to the park! You can't let this strange sense of familiarity to be stuck in your brain forever!"
                    choice4= raw_input("Now, try again: a. Accept b. Reject...")
# go to the park
            if choice4.lower()== "a" or choice4.lower()== "accept":
                raw_input("...")
                raw_input("You arrive at the park, you do not like this place, but everything about this park is so familiar to you. You saw a bench under a huge oak tree, you want to sit on that bench.")
                raw_input("Someone is already sitting on that bench. You just stand and wait until he leaves.")
                raw_input("Now you are sitting on the bench under the oak tree. It is Spring right now; the sun is shining and warm wind is blowing across your face. You think BOB won't show up soon.")
                raw_input("You fall asleep.")
                raw_input("...")
                raw_input("You are hiding behind the bushes, she is walking on the natural path.  Leaves cover the ground, it must be Winter or Fall. You breathe heavily, looks like you are trying really hard to make sure she doesn't see you. When she walks pass a bench, you jumped out of the bushes. You grab her hand. She is resisting, and you try to calm her down...")
                raw_input("...")
                raw_input("'You are going to get sick if you sleep here, name. Wake up'")
                raw_input("You open your eyes, yet everything looks so blurry.")
                raw_input("'Don't worry, it is just some privacy protection mechanism. Your vision will be restored after you win the game. See, I just want to play a small game with you, you rejected me last time, so this time I bring a different game. I spend a lot of money on this by the way.'")
                choice5= raw_input("BOB wants to play a game with you decide to: a. Accept b. Reject...")
                while choice5.lower() != "b" and choice5.lower()!="reject" and choice5.lower() != "a" and choice5.lower()!= "accept":
                    print "You cannot always run away from making decison. It is your obligation to decide."
                    choice5= raw_input("Now, are you going to play with BOB: a. Accept b. Reject...")
#reject the game
                if choice5.lower() == "b" or choice5.lower() == "reject":
                    raw_input("'I remember I mentioned that your vision will be restored after you play this game with me. Since you are not playing it with me, just pray you are going to adapt to your blindness'")
                    raw_input("You are sitting on the bench, you can't go anywhere. BOB have already left, glad that he did not kill you.")
                    raw_input("While you are sitting, you feel extremely calm, now, without your vision, you are isolated from a lot of information of the outside world. You enter a simple and peaceful world. You stand up, and want to embrace this brand-new world...")
                    raw_input("BANG")
                    raw_input("You have been hit in the head by some metal rod, maybe a baseball bat. Warm liquid strains down your head. You lose conscious. It is har to believe you will wake up again.")
                    raw_input("I assume it is BOB, I guess you did not make the right choice.")
#accept the game
                if choice5.lower() == "a" or choice5.lower() == "accept":
                    raw_input("'The game is really simple. Here put on this pair of glasses, after I start the game, you will enter a virtual reality. There will be three weapons lying infornt of you, just follow your heart and pick one. Then you just need to fight the monster using your weapon. There are three types of monter, you never know which monster you will encounter. If you win, I will bring peace back to your life... Now, game starts!")
                    raw_input("You are not sure about what will happen if you lose.")
                    import random
                    directions = {
                        ("bat", "little monster"): True,
                        ("gun", "little monster"): False,
                        ("poison", "little monster"): True,
                        ("bat", "medium monster"): True,
                        ("gun", "medium monster"): True,
                        ("posion'", "medium monster"): False,
                        ("bat", "big monster"): False,
                        ("gun", "big monster"): True,
                        ("poison", "big monster"): False
                    }
                    def game2(weapon, monster):
                        return directions[(weapon,monster)]
                    def monster():
                        return random.choice(["big monster", "medium monster", "small monster"])
                    weapon = raw_input("You find a bat, a gun , and a bottle of poison. You chose(just type the name of the weapon)...")
                    while weapon != "bat" and weapon != "gun" and weapon != " poison":
                        print "You just need to type: bat, gun, or poison. "
                        weapon= raw_input("Quick! Pick one: ")
                    monster = monster()
                    result = game2(weapon, monster)
                    if result is True:
                        print "Congradulation! You kill the monster! You receive a golden ring as a prize!"
                        raw_input("'Now take off your glasses.' You hear BOB talking to you. But you can't do what he says, there is no glasses on you.")
                        raw_input("'Ah, forget about the glasses now, it won't hurt you. Did you found anything when you killed the monster?")
                        raw_input("You tell him about the golden ring.")
                        raw_input("'Have you seen this ring before? Do you know the owner of this ring? Come on! You must remember something! There must be something left in your head!'")
                        raw_input("'No? Nothing? Oh forget about it! It is not the right path, your brain is not ready yet. Maybe next time, next time we will find something.'")
                        raw_input("'Restart the system, quick, we don't have much time left!'")
                        raw_input("You are sitting in your living room, just checking your phone. There is nothing big happening around your area, it is very safe and peaceful here. Actually, this is why you chose live here, a small and quiet neighborhood, a lot better than the one you had.")
                        raw_input("But today is too quiet...")
                        raw_input("You do not see Mr. B walking his dogs toady, they walk pass you every day. You like his dogs, and they also seem to like you.....")
                    if result is False:
                        print "You failed to kill by the monster. I guess you are not ready yet."
                        raw_input("You lay on the ground, it hurts. The pain caused by the attack of the monster feel so real, it feels like you are actually bleeding. 'Hey BOB, I failed the game, what will happen to me?' You ask BOB.")
                        raw_input("...")
                        raw_input("At least one hour had passed, you start to wonder how come no one walking pass you notices something is wrong with you. You try to take off the glasses, yet, it seems like the glasses have dissappeared.")
                        raw_input("'System reloading...' You say this infront of your eyes, apparently you are still in the virtual reality created by that glasses.")
                        raw_input("Suddenly, everything goes dark. After a few seconds, your vision becomes clearer and brighter.")
                        raw_input("You hear people talking... 'I guess our subject's brain is not ready yet'")
                        raw_input("'Apparently, that was not the right path to take.'")
                        raw_input("'I hope this time, we will find out the answer hidden in your head.'")
                        raw_input("You are sitting in your living room, just checking your phone. There is nothing big happening around your area, it is very safe and peaceful here. Actually, this is why you chose live here, a small and quiet neighborhood, a lot better than the one you had.")
                        raw_input("But today is too quiet...")
                        raw_input("You do not see Mr. B walking his dogs toady, they walk pass you every day. You like his dogs, and they also seem to like you.....")
#accept the game
if choice2.lower() == "a" or choice2.lower()== "accept":
    raw_input("'I'm glad that you agree, things will be really messed up if you reject me. After all, you could quit anytime you want, but I won't guarantee what will happen on you and the victim.'")
    raw_input("'The game is really simple, I will give you two riddles, you just have to find out the answer and send it to me. You will not be able to get the next riddle unless you answer the previous answer correctly.'")
    raw_input("Don't worry you will have three chances for each riddle, and the answers are all inside your head. Seems really fair, right?")
    raw_input("...")
    def end1():
        q1= raw_input("First question: What fastens two people yet touches only one? (2 words): ")
        for n in range(4):
            if q1.lower() == "wedding ring" and n <= 2:
                q2 = raw_input("Correct! See, I told you the answers are all in your brain. Next question: Almost everyone sees me without noticing me, For what is beyond is what he or she seeks. What am I? (1 word): ")
                break
            elif q1.lower() != "wedding ring" and n < 2:
                print "Your answer is not correct " + str(2-n) + " out of 3 chances left~"
                q1 = raw_input("What fastens two people yet touches only one? (2 words): ")
            elif q1.lower() != "wedding ring" and n == 2:
                print "Oh come on, the answer is inside your brain!"
        else:
            raw_input("'Opps~ There is no chance left'")
            raw_input("You feel something is pressed against your head")
            raw_input("Looks like your brain is not ready yet")
            print "You has been shot by someone, I assume it is BOB."
            return False
        for m in range(4):
            if q2.lower() == "window" and m <= 2:
                q3 = raw_input("Next question: Why was the photographer arrested? You don't have to give me the answer for this, if you don't know, just keep on going and hit Enter ;)")
                if q3 != "He shot his customers and blew them up":
                    print "'I know you will have a hard time answering this, I will just tell you the answer. The photographer shot the customers and blew them up!'"
                    return True
                elif q3 == "He shot his customers and blew them up":
                    print "Good job, I mean, the answers are all in your head. I just tried to make things easier for you."
                    return True
            elif q2.lower() != "window" and m < 2:
                print "Your answer is not correct " + str(2-m) + " out of 3 chances left~"
                q2 = raw_input("Almost everyone sees me without noticing me, For what is beyond is what he or she seeks. What am I? (1 word):  ")
            elif q2.lower() != "window" and m == 2:
                print "Oh come on, the answer is inside your brain!"
        else:
            raw_input("'Opps~ There is no chance left'")
            raw_input("You feel something is pressed against your head")
            raw_input("Looks like your brain is not ready yet")
            print "You has been shot by someone, I assume it is BOB."
            return False
#if player answer the riddle correctly
    if end1() is True:
        raw_input("'Ha! The last one is just a small joke to make you more relaxed. Tight nerves won't help anyone to get the answer. Now, I have another game for you. I promise this is the last one.'")
        raw_input("'I want you to go to your bed room, open the drawer right next to your bed, and find a six-sided dice.'")
        raw_input("You are surprised that BOB knows about the drawer and the dice.")
        raw_input("'Quick, the game need that dice to start!'")
        choice6= raw_input("Knowing that BOB knows about the structure and details of your house, you decide to: a. Accept b. Reject...")
        while choice6.lower() != "b" and choice6.lower()!="reject" and choice6.lower() != "a" and choice6.lower()!= "accept":
            print "You cannot always run away from making decison. It is your obligation to decide."
            choice6= raw_input("Quick, make a decision, we don't have that much time left: a. Accept b. Reject...")
        #if reject to find the dice
        if choice6.lower() == "b" or choice.lower() == "reject":
            raw_input("You reject BOB, you do not want other people to decide what you are going to do. You have free will, you have the ability to choose whatever path you want to take.")
            raw_input("There is no more text message coming from BOB. You think you are safe now.")
            raw_input("You feel tired, after all of the things that have happened today. You sit on the couch, turn on the television, and fall asleep.")
            raw_input("'Pause the operation!'")
            raw_input("'BOB fails to interact with the subject, guys, we are stuck.")
            raw_input("'I think we have encounter a BUG of this system, ha, those developers said they had removed all the BUGs. This is why I do not agree to cooperate with those people, we can do a much better job alone.'")
            raw_input("'Restart the system, quick! We don't have much time left, let's just hope next time, we will find the right path and the answer.'")
            raw_input("...")
            raw_input("You are sitting in your living room, just checking your phone. There is nothing big happening around your area, it is very safe and peaceful here. Actually, this is why you chose live here, a small and quiet neighborhood, a lot better than the one you had.")
            raw_input("But today is too quiet.......")
        if choice6.lower() == "a" or choice6.lower() == "accept":
            raw_input("You think the safest way right now is to what BOB says. You head toward your bed room.")
            raw_input("You are about to go pass your kitchen, there are knives in the kitchen...")
            choice7= raw_input("a. Get a knife it may be useful later b. Keep walking you are running out of time...")
            while choice7.lower() != "b" and choice7.lower() != "a":
                print "You cannot always run away from making decison. It is your obligation to decide."
                choice7= raw_input("Quick, make a decision, we don't have that much time left: a. Get the knife b. Keep going...")
            #go to kitch
            if choice7.lower() == "a":
                raw_input("You open the door of the kitchen, you hear the exhasut fan running.")
                raw_input("Weird, you do not remember when did you turn on the fan.")
                raw_input("You saw two people standing in your kitchen, you recognize one of them.")
                raw_input("'Sarah!' You yell at your ex-fiancee, but she doesn't seem to recognize you.")
                raw_input("They knock you down, 'The other one must be BOB', you realize")
                raw_input("They turn off the exhaust fan, you smell sulfur.")
                raw_input("BOB punches you in your stomach, you are going to loose consciousness. You know they are going to blow up your house.")
                raw_input("Your mind starts to wonder. You are confused why Sarah wants to kill you, you loved her so much that you even bought her a really expensive engagement ring.")
                raw_input("Maybe it is because she finds out your secret, the secret you hide from the world.")
                raw_input("If you could go back in time, before Sarah broke up with you in the park, things could end up differently...")
                raw_input("'This is by far the biggest clue we have found!'")
                raw_input("'Guys, I think we are on the right track, but we still need more information.'")
                raw_input("'We should try a slightly different path, maybe we will find a better answer...'")
#keep walking
            if choice7.lower() == "b":
                raw_input("Forget about the knife, BOB is probably watching your action somewhere, you do not want to make him angry.")
                raw_input("You enter your bedroom.")
                raw_input("...")
                raw_input("There is no one in your bedroom, you thought BOB will be there.")
                raw_input("You open your drawer. Beside the from the dice, you also see a golden ring.")
                raw_input("That was your engagment ring, your fiancee just broke up with you. What a stupid way it is to break up in your favorite park.")
                raw_input("You text BOB: 'I have find the dice.")
                raw_input("...")
                raw_input("'Great! The game we are going to play is really simple. You just need to roll the dice and text me the number. I will also roll my six-sided dice, but my dice is slightly different than yours, there are only three different numbers. I can't tell you what those numbers are, but if the number you rolled out is the same with the number I rolled out, you will loose the game.'")
                choice8= raw_input("You decide to: a. Roll the dice b. Runaway...")
                while choice8.lower() != "b" and choice8.lower() != "a":
                    print "You cannot always run away from making decison. It is your obligation to decide."
                    choice8= raw_input("This is a really important! Make a decision!: a. Roll the dice b. Runaway...")
                if choice8.lower() == "b":
                    raw_input("You runaway, everything is insane! You have to get help!")
                    raw_input("BANG...")
                    raw_input("You have been shot. You fall on the floor. You saw two people, one is holding the gun, and the other one is Sarah, you ex-fiancee.")
                    raw_input("The one holding the gun must be BOB. You assumed that Sarah hires BOB to kill you, becasue she found out your deepest secret. You were planning to kill her and burry her, but she has already taken action before you do...")
                    raw_input("...")
                    raw_input("'It ends here?'")
                    raw_input("'These are enough to proof subject's intention, but we don't know where did the subject burry the victim")
                    raw_input("'Run the system again, we need to find a better path.")
                    raw_input("...")
                    raw_input("You are sitting in your living room, just checking your phone. There is nothing big happening around your area, it is very safe and peaceful here. Actually, this is why you chose live here, a small and quiet neighborhood, a lot better than the one you had.")
                    raw_input("But today is too quiet......")
                if choice8.lower() == "b":
                    import random
                    directions2 = {
                        ("1", "1"): True,
                        ("1", "2"): False,
                        ("1", "3"): False,
                        ("1", "4"): False,
                        ("1", "5"): False,
                        ("1", "6"): False,
                        ("2", "1"): False,
                        ("2", "2"): True,
                        ("2", "3"): False,
                        ("2", "4"): False,
                        ("2", "5"): False,
                        ("2", "6"): False,
                        ("6", "1"): False,
                        ("6", "2"): False,
                        ("6", "3"): False,
                        ("6", "4"): False,
                        ("6", "5"): False,
                        ("6", "6"): True,
                    }
                    def game3(bob, dice):
                        return directions2[(bob, dice)]
                    def bob():
                        return random.choice(["1","2","6"])









