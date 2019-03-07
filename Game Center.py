print ("welcome to Game Center")
print (" would you like to play Sebastian's Trivia game on sports? press 1 or if you want to play Carel's BlackJack game, press 2, then finally if you want to play Pablo's movie/shows trivia game, press 3.")
game_choice = input()
if game_choice == "1" or game_choice == "one": 
    import threading
    import time
    import sys
    points=0
    count=0











    print("Hey this is a trivia game on sports")
    time.sleep(3)
    print("You will have a minute to try to answer all six questiones")
    time.sleep(3)
    print("You will know when your minute is up when it tells you did not make it  on  time")
    time.sleep(5)
    print("Even though you didn't finish on time you can still continue answering the  questiones")
    time.sleep(5)



    print("Who has scored the most points in NBA history")
    print("A.)Kareem Abdul-Jabbar")
    print("B.)Michael Jordan")
    print("C.)Karl Malone")
    print("D.)Kobe Bryant")

    nba= input()
    if nba=="a":
     points=points +1
     print("That is correct")
    elif nba=="A":
      points=points +1
      print("This is correct")
    else:
     print("That is incorrect")

    print("What soccer team has the most champion league trophies")
    print("A.)Barcelona")
    print("B.)Manchester United")
    print("C.)Real Madrid")
    print("D.)Liverpool")

    soccer=input()
    if soccer=="c":
     points=points +1
     print("That is correct")
    elif soccer=="C":
      points=points +1
      print("This is correct")
    else:
     print("That is incorrect")

    print("Who has the most Home runs in MLB history")
    print("A.)Barry Bonds")
    print("B.)Paul Goldshmit")
    print("C.)Randy Johnson")
    print("D.)Sammy Sosa")

    runs=input()
    if runs=="a":
     points=points +1
     print("That is correct")
    elif runs=="A":
      points=points +1
      print("This is correct")
    else:
     print("That is incorrect")

    print("What team in NBA history has the most championships")
    print("A.)Chicago Bulls")
    print("B.)Los Angeles Lakers")
    print("C.)Golden State Warriors")
    print("D.)Boston Celtics")

    team=input()
    if team== "d":
     points=points +1
     print("That is correct")
    elif team== "D":
      points=points +1
      print("This is correct")
    else:
     print("That is incorrect")

    print("Who has scored the most goals in Championes league history")
    print("A.)Lionel Messi")
    print("B.)Ronaldinho")
    print("C.)Cristiano Ronaldo")
    print("D.)Javier Hernandez")

    player=input()
    if player=="c":
     points=points +1
     print("That is correct")
    elif player=="C":
      points=points +1
      print("This is correct")
    else:
     print("This is incorrect")

    print("What team has won the most world series")
    print("A.)Arizona Diamondbacks")
    print("B.)New York Yankees")
    print("C.)Los Angeles Dodgers")
    print("D.)Chicago White Soxs")

    baseball=input()
    if baseball=="b":
     points=points +1
     print("This is correct")
    elif baseball=="B":
      points=points +1
      print("This is correct")

    else:
     print("This is incorrect")

    print("Your score is" ,points, "out of 6")
if game_choice == "2" or game_choice == "two":
    import random
    
    cards = [1,2,3,4,5,6,7,8,9,10,10,10]
    player = 0

    dealer = random.choice (cards)
    dealer2 = random.choice (cards)
    player = random.choice (cards) 
    player2 = random.choice (cards) 
    total = player + player2
    dealer_total = dealer + dealer2
    print (" let me explain how the cards will diplay. I will automatically give you two cards and show you the dealer's up card. From there you can either decide to 'hit' or 'stay'. if you decide to 'hit' then it will display the total of the first two cards then the number under that is the random card that you were given and then the number shown under that is the sum of the two numbers displayed above")
    print ("do you want to play black jack? yes/no ")
    answer1= input()
    if answer1 == "yes" or answer1 == "Yes" or answer == "YES": 
        print ("your two cards are:" )
        print (player,"and", player2) 
        print("Dealers upcard is:")
        print (dealer)
        answer = input ("do you want to hit? or stay")
        while answer == "hit" or answer == "yes" or answer == "Hit":
            if player > 21:
                print(" you went over 21! you loose")
                break
            player1 = total
            print (player1)
            player = player + player2
            player3 =random.choice(cards)
            print(player3) 
            total = player + player3
            print(total)
            if player == 21:
                print (" you won!" )
                break
            if player > 21:
                print(" you went over 21! you loose")
                break

            answer = input ("do you want to hit? or stay")

        if answer == "stay" or answer == "Stay" or answer == "No":
            print ("remember your total is:")
            print (total)
            print ("These are the dealers cards:") 
            print (dealer, "and", dealer2)
            print ("the dealers total:")
            print (dealer_total)
            while dealer_total <= 17:
                dealer3= random.choice(cards)
                print ("this is the dealer's new card")
                print (dealer3)
                dealer_total = dealer_total + dealer3
                print ("this is the dealer's new total")
                print(dealer_total)
        print ("your total is:")
        print (total)
        print ("The dealer's total is:")
        print (dealer_total)
if game_choice == "3" or game_choice == "three":
    import time

    print("Hi, Welcome to The Trivia. What's your Name?")
    name = input()
    print("Nice to meet you " +name+ " let's get started.")

    print("Before You Start, Here's are Example:")
    print("The First Trivia Question Is Gonna Be About Movie's.")
    print("Then In The Second Trivia Qusetion Is Gonna Be About Video Games.")
    print("When You Answer Corretly, You get 10 Points")
    print("When You Answer Incorrectly, You get -10 Points")
    print("You Might want to use the Caps Lock While Answering the questions.")

    print("Good Luck ;)")



    score = 0

    print("Who was the Actor That Does Cameo in All Marvel Movies?")

    print("A.Adam West")
    print("B.Stan Lee")
    print("C.Torou Iwatani")
    Answer = input()
    if Answer == "A":
       score = score -10
       print("YOU REALLY GOTTA WATCH SOME MARVEL MOVIES!! The Correct answer is B, Stan Lee")
    if Answer == "B":
       score = score +10  
       print("That is Correct, Also We Will See Him In the Stars,EXCElSIOR 1922-2018.")
    if Answer == "C":
       score = score -10
       print("YOU REALLY GOTTA WATCH SOME MARVEL MOVIES!! The Correct answer is B, Stan Lee")
    print("Your Score is: " ,score)

    print("In Pixels,Who is the video game character That The wonder kid is in love with?")

    print("A.Lady Lisa")
    print("B.Rosalina")
    print("C.Zelda")
    Answer = input()
    if Answer == "A":
       score = score +10 
       print("That is Correct, Also The Wonder Kid Got His Wish.")
    if Answer == "B":
       score = score -10
       print("WOW!!!! was that Your Bset Guess? The Correct answer is A, Lady Lisa")
    if Answer == "C":
       score = score -10
       print("WOW!!!! was that Your Bset Guess? The Correct answer is A, Lady Lisa")
    print("Your Score is: " ,score)


    print("Who Narrates as Bailey In A Dog's Purpose?")

    print("A.Morgan Freeman")
    print("B.Josh Brolin")
    print("C.Josh Gad")
    Answer = input()
    if Answer == "A":
       score = score -10
       print("WERE YOU NOT LISTENING TO THAT NARRATOR???? The Correct answer is C, Josh Gad")
    if Answer == "B":
       score = score -10
       print("WERE YOU NOT LISTENING TO THAT NARRATOR???? The Correct answer is C, Josh Gad")
    if Answer == "C":
       score = score +10 
       print("That is Correct, Also His Narration is Pretty Good.=)")
    print("Your Score is: " ,score)


    print("In Netflix Series Skylander Academy Who Played as Cy The Imaginator Skylander?")

    print("A.Dantdm")
    print("B.Markiplier")
    print("C.Jacksepticeye")
    Answer = input()
    if Answer == "A":
       score = score +10 
       print("That is Corret, Also Who Ever Thought That YouTuber Voice Is Him.")
    if Answer == "B":
       score = score -10
       print("NOT EVEN CLOSE! The Correct answer is A, Dantdm")
    if Answer == "C":
       score = score -10
       print("NOT EVEN CLOSE! The Correct answer is A, Dantdm")
    print("Your Score is: " ,score)


    print("In Pixels, Who was The Voide of Q*Bert?")

    print("A.Tom Kenny")
    print("B.Billy West")
    print("C.Seth Rogan")
    Answer = input()
    if Answer == "A":
       score = score -10
       print("YOU REALLY THOUGHT OF THAT ANSWER???? The Correct answer is B, Billy West")
    if Answer == "B":
       score = score +10 
       print("That is Correct, Also He Sounds Funny As Q*Bert.")
    if Answer == "C":
       score = score -10
       print("YOU REALLY THOUGHT OF THAT ANSWER???? The Correct answer is B, Billy West")
    print("Your Score is: " ,score)


    print("In The Movie The Minions, What is Their Quest?")

    print("A.Find Love")
    print("B.Find a Friend")
    print("C.Find Their New Boss")
    Answer = input()
    if Answer == "A":
       score = score -10
       print("WERE YOU NOT LISTEN TO KEVIN'S SPEECH???? The Correct answer is C, Find Their New Boss")
    if Answer == "B":
       score = score -10
       print("WERE YOU NOT LISTEN TO KEVIN'S SPEECH???? The Correct answer is C, Find Their New Boss")
    if Answer == "C":
       score = score +10 
       print("If  You Guess Find Their New Boss, That is Correct")
    print("Your Score is: " ,score)








    print("Okay,Let's Move On To The New Topic")


    print("Let's Talk About Video Game Topic.")



    print("What does Mario jumps on after completing a level?")

    print("A.Flag Pole")
    print("B.On the Bed")
    print("C.On the Trampoline")
    Answer = input()
    if Answer == "A":
       score = score +10 
       print("That is Correct, He jumps on the Flag Pole")
    if Answer == "B":
       score = score -10
       print("HAVE YOU NOT PLAY IT ON NINTENDO???? The Correct answer is A, Flag Pole")
    if Answer == "C":
       score = score -10
       print("HAVE YOU NOT PLAY IT ON NINTENDO???? The Correct answer is A, Flag Pole")
    print("Your Score is: " ,score)


    print("What does NES stand for?")

    print("A.Nintendo Excitment System")
    print("B.Nintendo Entertainment System")
    print("C.Nintendo Emergency System")
    Answer = input()
    if Answer == "A":
       score = score -10
       print("OOOOOHHHHH THAT WAS CLOSE! The Correct answer is B,Nintendo Entertainment System")
    if Answer == "B":
       score = score +10 
       print("That is Correct, it Stand for Nintendo Entertainment System.")
    if Answer == "C":
       score = score -10
       print("OOOOOHHHHH THAT WAS CLOSE! The Correct answer is B,Nintendo Entertainment System")
    print("Your Score is: " ,score)


    print("What is the name of the princess whom Mario repeatedly stops Boswer from kidnapping?")

    print("A.Princess Daisy")
    print("B.Princess Rosalina")
    print("C.Princess Peach")
    Answer = input()
    if Answer == "A":
       score = score -10
       print("Well You were Close. The Correct answer is C, Princess Peach")
    if Answer == "B":
       score = score -10
       print("Well You were Close. The Correct answer is C, Princess Peach") 
    if Answer == "C":
       score = score +10 
       print("That is Correct, Through Out Gaming History He Always Kidnapp Peach")
    print("Your Score is: " ,score)


    print("What's the color of the wings of Dragon in Spyro?")

    print("A.Orange")
    print("B.Red")
    print("C.Orchoid")
    Answer = input()
    if Answer == "A":
       score = score +10 
       print("That is Correct, You Gotta Play Spyro Someday.")
    if Answer == "B":
       score = score -10
       print("WRONG COLOR! The Correct Answer is A, Orange")
    if Answer == "C":
       score = score -10
       print("WRONG COLOR! The Correct Answer is A, Orange")
    print("Your Score is: " ,score)


    print("Name the character abused by Mario?")

    print("A.Wario")
    print("B.Donkey Kong")
    print("C.Waluigi")
    Answer = input()
    if Answer == "A":
       score = score -10
       print("Not Even Close, The Correct Answer is B, Donkey Kong")
    if Answer == "B":
       score = score +10 
       print("That is Correct, The Level 1 Is Even Better")
    if Answer == "C":
       score = score -10
       print("Not Even Close, The Correct Answer is B, Donkey Kong")
    print("Your Score is: " ,score)


    print("Most of us have played Atari games. What does Atari means?")

    print("A.Failure")
    print("B.Victory")
    print("C.Success")
    Answer = input()
    if Answer == "A":
       score = score -10
       print("Not Quite, The Correct Answer is C, Success")
    if Answer == "B":
       score = score -10
       print("Not Quite, The Correct Answer is C, Success")
    if Answer == "C":
       score = score +10
       print("That is Correct, Nintendo Also Made A Big Success.")
    print("Your Score is: " ,score)


    print("Which year the Minecraft was released?")

    print("A.2009")
    print("B.2010")
    print("C.2012")
    Answer = input()
    if Answer == "A":
       score = score +10
       print("That is Correct, And That's When the Alvin the The chipmunks 2 was made.;D")
    if Answer == "B":
       score = score -10
       print("Well you're close, The Correct Answer is A, 2009")
    if Answer == "C":
       score = score -10
       print("Well you're close, The Correct Answer is A, 2009")
    print("Your Score is: " ,score)


    print("What's the color of Pacman in Pacman256?")

    print("A.Blue")
    print("B.Yellow")
    print("C.Pink")
    Answer = input()
    if Answer == "A":
       score = score -10
       print("WRONG COLOR!, The Correct Answer is B, Yellow")
    if Answer == "B":
       score = score +10
       print("That is Correct, He's Always Yellow.")
    if Answer == "C":
       score = score -10
       print("WRONG COLOR!, The Correct Answer is B, Yellow")
    print("Your Score is: " ,score)



    print("Time for the Bonus Round")
    print("Between 1,or 2 Questions Earns 15 points")
    print("and this time I'll give you Hints.")

    print("God Luck ;)")


    print("BONUS 1: Throghout The Chipmunk Movies Who was The Voice of Alvin Sevllie?")
    print("Hint: He Voiced From Alpha & Omega, Planet 51, Walking With The Dinosaur, and Skylander Academy")


    print("A.Justin Long")
    print("B.Matthew Guleb Grey")
    print("C.Jesse Mcarthy")
    Answer = input()
    if Answer == "A":
       score = score +15
       print("If you thought Justin Long voice, That is Correct, You really need to listen to his real voice to chipmunk voice ;)")
    if Answer == "B":
       score = score -15
       print("Well You're Close. The Correct Answer is A, Justin Long")
    if Answer == "C":
       score = score -15
       print("Well You're Close. The Correct Answer is A, Justin Long")  
    print("Your Bonus Score is: " ,score)


    print("Get Ready for the Next Question, and this one is a Movie Based On the Cartoon")


    print("BONUS 2: In The My Little Pony: The Movie, Who was The voice of Princess Twilight Sparkle Based on The Show?")
    print("Hint: she Voiced From The Fairly OddParents, The Rugrats, Ben 10, Transformers Animated, and Uniktty series")


    print("A.Andrea Libman")
    print("B.Ashleigh Ball")
    print("C.Tara Strong")
    Answer = input()
    if Answer == "A":
       score = score -15
       print("OOOOHHHH SO CLOSE, The Correct Answer is C, Tara Strong")
    if Answer == "B":
       score = score -15
       print("OOOOHHHH SO CLOSE, The Correct Answer is C, Tara Strong")
    if Answer == "C":
       score = score +15
       print("That is Correct, 5 Stars to Tara With her Master of her voice.;)<3")
    print("Your Bonus Score is: " ,score)   





    print("CONGRADULATIONS! You did The Good Triva Guess.")
    print("Your Best Score is: " ,score)


    print("Want to Play Again?")
    Answer = input()
    if Answer == "yes":
        print("okay then, restart the program")
    else:
       print("Well It's Been Fun, See You Later ;)")

    time.sleep(150)    
