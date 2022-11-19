

define turn = 0
define bet = 0

define T = Character("Teacher", image="teacher")
define S = Character("Student",image="student")
image Class = "Classroom.jpg"
 


 
  
    
    


label start:
    

    show Class
    pause
    "On a Sunny Wednesday Afternoon, an AP Statistics class is faced with a formidable task …"
    T sigh " Alright settle down class, as promised we'll be going over your new assignment for this unit!"
    S three "Ooh, sir, will this be weighed the same as the test?"
    T talk "Ah if you perform well, I might consider it..."
    T talk "Anyhow, let me introduce you to (insert name of game show)"
    S one "Finally, this looks really interesting!"
    T talk "However, to enter the games, you must pay an upfront fee of 5 percent of your cumulative mark!"
    S three "What!"
    "I knew this game had more to do than just marks, there's gotta be a twist here..."
    T talk "Keep in mind class, all these games revolve around probability, so if you play your odds right, you can end up with a higher mark!"
    T talk "Assuming luck is on your side of course..."

    scene Class
    with fade 
    "The very next day …"

    T talk "Welcome back class, I hope you all are ready for the first round of our very first (insert game show name)"
    T talk "Our first game is one you all probably have heard of, Blackjack"
    T talk "Blackjack in simple terms is a game where the objective is to receive a combination of playing cards that totals to 21"
    T talk "A dealer will provide the players with cards, who have the option of requesting another randomly-drawn card (hit) or keeping their current cards(stand). Remember the players aren't competing against each other, but rather against the dealer"
    T talk "Cards with numbers will have values of their number respectively. Face cards are all worth 10, and the Ace is worth either 1 or 11 depending on which favors you"
    T talk "Now that the game has been explained, we can begin playing!"
    T talk "Now of course, keep in mind class gambling is indeed illegal, so instead I will provide you with a fair chance of increasing your mark IF you win. If you lose, the opposite may occur."
    "I wonder if that chance really is fair…"
    S three "But sir! What if we get really unlucky! Won't that hurt our marks?"
    T talk "You're right, perhaps I should have explained that better."
    T talk "The way we will be playing Blackjack will be in groups of 4, with 5 different rounds"
    T talk "To bet marks, you will be allowed to bet up to 3 marks per round, if you win, that mark will be added to your game total (how many marks you earned that game). If you lose, that same amount will be deducted from your game total"
    T talk "For simplicity sake, I will be the dealer in each game."
    T talk "Are you all ready to play? Keep in mind that you want to take the fundamental concepts of this unit in mind. If you have any questions feel free to ask me."
    S three "Let's do this!"

    scene Class
    with fade

    

   
label round_1:
    $ deck = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    $ playerHand = []
    $ dealerHand = []
    $ earnings = 0
    $ cardAmount=0
    $ playerHand.append(renpy.random.choice(deck))
    $ dealerHand.append(renpy.random.choice(deck))
    $ dealerHand.append(renpy.random.choice(deck))
    $ deck.remove(dealerHand[0])
    $ deck.remove(dealerHand[1])
    $ deck.remove(playerHand[0])
    $ playerTotal = 0
    $ playerTotal += playerHand[0]
    $ cardAmount += 1
    $ dealerTotal = 0
    $ dealerTotal += dealerHand[0]
    $ dealerTotal += dealerHand[1]

    T talk "Before we begin playing, place your bet!"

    menu:
        "1":
            $ bet += 1
        "2":
            $ bet +=2
        "3":
            $ bet +=3

    T talk "Alright, let's begin, I'll start by dealing cards."



    "Dealer has [dealerHand[0]] and X."
    "You have [playerHand[0]]."

    T talk "Would you like to Stay or Hit?"
    
    menu:
        "Hit":
            $ playerHand.append(renpy.random.choice(deck)) 
            $ playerTotal += playerHand[1]
            $ cardAmount += 1
        "Stay":
            "your current card is [playerHand[0]]"
            jump reveal_hand1
            
            
   
    if playerTotal<21:
        "Would you like to..."
        menu:
            "Hit":
                $ value = renpy.random.choice(deck)
                $ playerHand.append(value) 
                $ playerTotal += value
                $ cardAmount += 1
            "Stay":
                    "Your total is [playerTotal]"
                    jump reveal_hand1
    else:
        jump reveal_hand1
   
       

label reveal_hand1:

    T talk "Time to reveal the hands..."
    "Dealer had [dealerHand[0]] and [dealerHand[1]]"
    
    if cardAmount == 1:
        "You have [playerHand[0]]."
    elif cardAmount == 2:
        "You have [playerHand[0]] and [playerHand[1]]."
    elif cardAmount == 3:
        "You have [playerHand[0]] and [playerHand[1]] and [playerHand[2]]."
    elif cardAmount == 4:
        "You have [playerHand[0]] and [playerHand[1]] and [playerHand[2]] and [playerHand[3]]."

    if playerTotal > 21: 
        "You bust! The dealer won."
        "You lost [bet]"
        $ earnings -= bet
        "Your winnings/losses so far is [earnings]"
        jump round_2
    elif playerTotal == 21:
        "BlackJack! You Won!"
        "You won [bet]"
        $ earnings += bet
        "Your winnings/losses so far is [earnings]"
        jump round_2

    
    if dealerTotal>playerTotal:
        "The dealer won!"
        "You lost [bet]"
        $ earnings -= bet
        "Your winnings/losses so far is [earnings]"
        jump round_2
    else:
        "You won!"
        $ bet *= 2
        "You won [bet]"
        $ earnings += bet
        "Your winnings/losses so far is [earnings]"
        jump round_2

label round_2:
  
    $ playerHand2 = []
    $ dealerHand2 = []
    $ cardAmount2=0
    $ playerHand2.append(renpy.random.choice(deck))
    $ dealerHand2.append(renpy.random.choice(deck))
    $ dealerHand2.append(renpy.random.choice(deck))
    $ deck.remove(dealerHand2[0])
    $ deck.remove(dealerHand2[1])
    $ deck.remove(playerHand2[0])
    $ playerTotal2 = 0
    $ playerTotal2 += playerHand2[0]
    $ cardAmount2 += 1
    $ dealerTotal2 = 0
    $ bet2 = 0
    $ dealerTotal2 += dealerHand2[0]
    $ dealerTotal2 += dealerHand2[1]

    T talk "Let's begin round 2, place your bet!"

    menu:
        "1":
            $ bet2 += 1
        "2":
            $ bet2 +=2
        "3":
            $ bet2 +=3

    T talk "Alright, let's begin, I'll start by dealing cards."



    "Dealer has [dealerHand2[0]] and X."
    "You have [playerHand2[0]]."

    T talk "Would you like to Stay or Hit?"
    
    menu:
        "Hit":
            $ playerHand2.append(renpy.random.choice(deck)) 
            $ playerTotal2 += playerHand2[1]
            $ cardAmount2 += 1
        "Stay":
            "your current card is [playerHand2[0]]"
            jump reveal_hand2
            
            
   
    if playerTotal2<21:
        "Would you like to..."
        menu:
            "Hit":
                $ value = renpy.random.choice(deck)
                $ playerHand2.append(value) 
                $ playerTotal2 += value
                $ cardAmount2 += 1
            "Stay":
                    "Your total is [playerTotal2]"
                    jump reveal_hand2
    else:
        jump reveal_hand2   

label reveal_hand2:

    T talk "Time to reveal the hands..."
    "Dealer had [dealerHand2[0]] and [dealerHand2[1]]"
    
    if cardAmount2 == 1:
        "You have [playerHand2[0]]."
    elif cardAmount2 == 2:
        "You have [playerHand2[0]] and [playerHand2[1]]."
    elif cardAmount2 == 3:
        "You have [playerHand2[0]] and [playerHand2[1]] and [playerHand2[2]]."
    elif cardAmount2 == 4:
        "You have [playerHand2[0]] and [playerHand2[1]] and [playerHand2[2]] and [playerHand2[3]]."

    if playerTotal2 > 21: 
        "You bust! The dealer won."
        "You lost [bet2]"
        $ earnings -= bet2
        "Your winnings/losses so far is [earnings]"
        jump round_2
    elif playerTotal2 == 21:
        "BlackJack! You Won!"
        "You won [bet2]"
        $ earnings += bet2
        "Your winnings/losses so far is [earnings]"
        jump round_3

    
    if dealerTotal2>playerTotal2:
        "The dealer won!"
        "You lost [bet2]"
        $ earnings -= bet2
        "Your winnings/losses so far is [earnings]"
        jump round_3
    else:
        "You won!"
        $ bet *= 2
        "You won [bet2]"
        $ earnings += bet2
        "Your winnings/losses so far is [earnings]"
        jump round_3


label round_3:
    $ playerHand3 = []
    $ dealerHand3 = []
    $ cardAmount3=0
    $ playerHand3.append(renpy.random.choice(deck))
    $ dealerHand3.append(renpy.random.choice(deck))
    $ dealerHand3.append(renpy.random.choice(deck))
    $ deck.remove(dealerHand3[0])
    $ deck.remove(dealerHand3[1])
    $ deck.remove(playerHand3[0])
    $ playerTotal3 = 0
    $ playerTotal3 += playerHand3[0]
    $ cardAmount3 += 1
    $ dealerTotal3 = 0
    $ bet3 = 0
    $ dealerTotal3 += dealerHand3[0]
    $ dealerTotal3 += dealerHand3[1]

    T talk "Let's begin the final round, place your bet!"

    menu:
        "1":
            $ bet3 += 1
        "2":
            $ bet3 +=2
        "3":
            $ bet3 +=3

    T talk "Alright, let's begin, I'll start by dealing cards."



    "Dealer has [dealerHand3[0]] and X."
    "You have [playerHand3[0]]."

    T talk "Would you like to Stay or Hit?"
    
    menu:
        "Hit":
            $ playerHand3.append(renpy.random.choice(deck)) 
            $ playerTotal3 += playerHand3[1]
            $ cardAmount3 += 1
        "Stay":
            "your current card is [playerHand3[0]]"
            jump reveal_hand3
            
            
   
    if playerTotal3<21:
        "Would you like to..."
        menu:
            "Hit":
                $ value = renpy.random.choice(deck)
                $ playerHand3.append(value) 
                $ playerTotal3 += value
                $ cardAmount3 += 1
            "Stay":
                    "Your total is [playerTotal3]"
                    jump reveal_hand3
    else:
        jump reveal_hand3

label reveal_hand3:

    T talk "Time to reveal the hands..."
    "Dealer had [dealerHand3[0]] and [dealerHand3[1]]"
    
    if cardAmount3 == 1:
        "You have [playerHand3[0]]."
    elif cardAmount3 == 2:
        "You have [playerHand3[0]] and [playerHand3[1]]."
    elif cardAmount3 == 3:
        "You have [playerHand3[0]] and [playerHand3[1]] and [playerHand3[2]]."
    elif cardAmount3 == 4:
        "You have [playerHand3[0]] and [playerHand3[1]] and [playerHand3[2]] and [playerHand3[3]]."

    if playerTotal3 > 21: 
        "You bust! The dealer won."
        "You lost [bet3]"
        $ earnings -= bet3
        "Your winnings/losses so far is [earnings]"
        jump transition1
    elif playerTotal3 == 21:
        "BlackJack! You Won!"
        "You won [bet3]"
        $ earnings += bet3
        "Your winnings/losses so far is [earnings]"
        jump transition1

    
    if dealerTotal3>playerTotal3:
        "The dealer won!"
        "You lost [bet3]"
        $ earnings -= bet3
        "Your winnings/losses so far is [earnings]"
        jump transition1
    else:
        "You won!"
        $ bet3 *= 2
        "You won [bet3]"
        $ earnings += bet3
        "Your winnings/losses so far is [earnings]"
        jump transition1 

label transition1:
    pass

    return
