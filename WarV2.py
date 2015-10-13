_author_ = "Ethan Richards"
# CIS 125
#War
# WarV1.py
#Simulates a game of War. 

import random 

#build the full deck and decks for each player
Deck = []
A = []
B = []
rounds = 0

for i in range(52):
    Deck.append(i)
    
random.shuffle(Deck)

for card in range(26):
   A.append(Deck.pop())
   B.append(Deck.pop())


    #create a function that battles the two cards that were on top.
def Battle(aNum,bNum,rounds):
    
    if aNum%13 > bNum%13:
        A.append(A.pop(0))
        B.pop(0)
        print("A beat B")
    elif bNum%13 > aNum%13 : 
        B.append(B.pop(0))
        A.pop(0)
        print("B beat A")      
    else: 
        A.pop(0)
        B.pop(0)

     #Create a loop that calls the battle function until one person is out of cards.  
while len(A) > 0 and len(B) > 0:
    rounds += 1
    Battle(A[0],B[0],rounds)
    if len(A) == 0 :
        print("B wins!")
        print("It took", rounds, "rounds!") 
    elif len(B) == 0 :
        print("A wins!")
        print("It took", rounds, "rounds!")


    
