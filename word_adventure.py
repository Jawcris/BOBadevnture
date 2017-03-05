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
raw_input("You sit right next to someone, you cannot see her face. But you know you cherish her. She starts to run away from you, you desperately try to grab her hand. Yet no matter how hard you try you just can't reach her.")
raw_input("...")
# the dream, forshadow something about the true end, change the gender of the person in the dream next time
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
    raw_input("...")
    raw_input("Someone opened your door. You can hear it. You walk to your front door.")
    raw_input("No one is there.")
    raw_input("Just to make sure you open the door. The sunlight is too bright, so weird it is already afternoon. You look down, you find a package.")
    raw_input("...")
    raw_input("It is soaked in blood.")
    raw_input("...")
    raw_input("You are sitting in the interrogation room. It looks like the one you have seen in movies. Grey wall, grey wall seems to crush you.")
    raw_input("...")
    raw_input("Do you recognize the ring on her finger? Who were you with before you received the package? Do you know you are in big trouble?")
    raw_input("It is that serial killer who already killed 28 people, the news is everywhere, the one who received the package from that killer were all killed.")
    raw_input("We have to protect you, maybe we could also catch that infamous killer. But the choice is still in your hand, you decide whether we will send people to be around you or not.")
    raw_input("...")
    #choice 3- have protection or not
    choice3 = raw_input("Now you know BOB is an extremely dangerous person, your blood is pumping faster, a sense of livliness in your plain life. You decided to: a. Accept b. Reject...")
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
            raw_input("You sit down in your cozy couch in your living room. You feel isolated once again. No one is going to intrude your life, you think surprisingly confidently.")
            raw_input("...")
            raw_input("Your phone buzzes, you received a text message.")
            raw_input("'Hi! This is BOB! We haven't talked for so long, I am starting to miss you. Please come to The Great Park we shall have a face-to-face meeting there.'")
            raw_input("'And everything will be clear.'")
            raw_input("The Great Park what a familiar name. Of course, everyone in this area know about this park, but there is something else about this park that triggers you emotion.")
            choice4= raw_input("You decide to: a. Accept b. Reject...")
            while choice4.lower() != "b" and choice4.lower()!="reject" and choice4.lower() != "a" and choice4.lower()!= "accept":
                print "You cannot always run away from making decison. It is your obligation to decide."
                choice4= raw_input("Now, pick one: a. Accept b. Reject...")
                while choice4 != "a" and choice4 != "accept":
                    print "You should go to the park! You can't let this strange sense of familiarity to be stuck in your brain forever!"
                    choice4= raw_input("Now, pick one: a. Accept b. Reject...")
# go to the park
            if choice4.lower()== "a" or choice4.lower()== "accept":
                        print "bbb"
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
            return "You has been shot by someone, I assume it is BOB."
        for m in range(4):
            if q2.lower() == "window" and m <= 2:
                q3 = raw_input("Next question: Why was the photographer arrested?")
                if q3 != "He shot his customers and blew them up":
                    return "'I know you will have a hard time answering this, I will just tell you the answer. The photographer shot the customers and blew them up!"
            elif q2.lower() != "window" and m < 2:
                print "Your answer is not correct " + str(2-m) + " out of 3 chances left~"
                q2 = raw_input("Almost everyone sees me without noticing me, For what is beyond is what he or she seeks. What am I? (1 word):  ")
            elif q2.lower() != "window" and m == 2:
                print "Oh come on, the answer is inside your brain!"
        else:
            raw_input("'Opps~ There is no chance left'")
            raw_input("You feel something is pressed against your head")
            raw_input("Looks like your brain is not ready yet")
            return "You has been shot by someone, I assume it is BOB."
    print end1()




