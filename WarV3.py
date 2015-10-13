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

#create a function for War
def War(A,B,tempaCard,tempbCard):
    
    if A[tempaCard]%13 > B[tempbCard]%13:
        for i in range(3):
            A.append(B.pop(i))
            A.append(A.pop( i))
            print("A beat B")
    elif A[tempaCard]%13 < B[tempbCard]%13:
        for i in range(3):
            B.append(A.pop( i))
            B.append(B.pop( i))
            print("B beat A")
    else: 
            del A[0:3]
            del B[0:3]
            print("Everyone lost!")
            
#Create a function for the battle            
def Battle(aNum,bNum,rounds):
    
    if aNum%13 > bNum%13:
        A.append(B.pop(0))
        A.append(A.pop(0))
        print("A beat B")
        
    elif bNum%13 > aNum%13 : 
        B.append(A.pop(0))
        B.append(B.pop(0))
        print("B beat A")      
        
    else: 
        tempaCard = 3
        tempbCard = 3
        if len(A) <= 4:
            print ("B Wins, A did not have enough cards for war!")
            print("It took", rounds, "rounds!")
            exit()
        elif len(B) <= 4:
            print ("A Wins, B did not have enough cards for war!")
            print("It took", rounds, "rounds!")
            exit()
        else: 
            War(A,B,tempaCard,tempbCard)
    

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


    
