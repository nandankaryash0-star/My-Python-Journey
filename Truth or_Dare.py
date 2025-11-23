import random

player = ("Yash","Priti","Saksham","Vedanti")
Truth = ("If you could be invisible for a day, what’s the first thing you would do?","What’s the biggest secret you’ve kept from your parents?","What’s the most embarrassing music you listen to?",
         "What’s one thing you love most about yourself?","Who is your secret crush?","Who is the last person you creeped on social media?",
         "When was the last time you wet the bed?","If a genie granted you three wishes, what would you ask for and why?",
         "What’s your biggest regret?","If you had to only ever watch rom-coms or only watch scary movies for the rest of your life, which would you choose and why?",
         "Where is the weirdest place you've ever gone to the bathroom?","Have you ever ghosted on someone?","Which player would survive a zombie apocalypse and which would be the first to go?",
         "Reveal all the details of your first kiss.","What excuse have you used before to get out plans?","What five things would you bring to a deserted island?"
         )
Dare = ("Pick someone in this room and (lovingly) roast them for one minute straight.","Let another person post an Instagram caption on your behalf.","Let another person post an Instagram caption on your behalf.",
        "Let the other players go through your phone for one minute.","Smell another player's armpit.","Smell another player's barefoot.","Eat a bite of a banana peel.",
        "Do an impression of another player until someone can figure out who it is.","Say pickles at the end of every sentence you say until it's your turn again.","Imitate a TikTok star until another player guesses who you're portraying.",
        "Act like a chicken until your next turn.","Talk in a British accent until your next turn.","Send a heart-eye emoji to your crush’s Instagram story.","Call a friend, pretend it's their birthday, and sing them Happy Birthday to You.",
        "Name a famous person that looks like each player in the room.","Show us your best dance moves.","Eat a packet of hot sauce straight.","Let another person draw a tattoo on your back with a permanent marker."
        )
running = True

player = random.choice(player)

print (player)

option = input(f"Truth or Dare (T/D):  ").lower()

if option == "t":
    Truth = random.choice(Truth)
    print(Truth)
elif option == "d":
    Dare = random.choice(Dare)
    print(Dare)