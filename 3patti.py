
import  random

suits=['♠', '♥', '♦', '♣']
ranks=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

deck=[]
for suit in suits:
    for rank in ranks:
        deck.append(f"{rank}{suit}")


random.shuffle(deck)
print("==============================================================================")
print(f"Player 1 cards are: {deck[0]} {deck[1]} {deck[2]}")
print(f"Player 2 cards are: {deck[3]} {deck[4]} {deck[5]}")
print(f"Player 3 cards are: {deck[6]} {deck[7]} {deck[8]}")
print("==============================================================================")
