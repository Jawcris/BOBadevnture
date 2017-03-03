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
# describe the dream, forshadow something about the true end
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
    choice3 = raw_input("Now you know BOB is an extremely dangerous person, your blood is pumping faster, a sense of livliness in your plain life. You decided to: a. Accept b. Reject...")
# if accept protection
if choice3.lower() == "a" or choice3.lower() == "accept":
    print "bo"
# if reject protection
if choice3.lower() == "b" or choice3.lower() == "reject":
    print "bob"
#accept the game
if choice2.lower() == "a" or choice2.lower()== "accept":
    raw_input("'I'm glad that you agree, things will be really messed up if you reject me. After all, you could quit anytime you want, but I won't guarantee what will happen on you and the victim.'")
    raw_input("'The game is really simple, I will give you two riddles, you just have to find out the answer and send it to me. You will not be able to get the next riddle unless you answer the previous answer correctly.'")
    raw_input("Don't worry you will have three chances for each riddle, and the answers are all inside your head. Seems really fair, right?")
    raw_input("...")
    q1= raw_input("First question: What fastens two people yet touches only one? (2 words): ")
    count1=0
    for n in range(3):
        if q1.lower() == "wedding ring":
            q2 = raw_input("Correct! See, I told you the answers are all in your brain. Next question: Almost everyone sees me without noticing me, For what is beyond is what he or she seeks. What am I? (1 word): ")
            break
        else:
            print "Your answer is not correct " + str(2-n) + " out of 3 chances left~"
            q1 = raw_input("What fastens two people yet touches only one? (2 words): ")
    for n in range(3):
        if q2.lower() == "window":
            q3 = raw_input("Next question: Why was the photographer arrested?")
            break
        else:
            print "Your answer is not correct " + str(2-n) + " out of 3 chances left~"
            q2 = raw_input("Almost everyone sees me without noticing me, For what is beyond is what he or she seeks. What am I? (1 word):  ")
    if q3 != "He shot his customers and blew them up":
        print "'I know you will have a hard time answering this, I will just tell you the answer. The photographer shot the customers and blew them up!"




