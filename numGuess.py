import random

my_num=random.randint(1, 100)

life=5

life_to_emoji = {
   
    5: "💖💖💖💖💖",
    4: "💖💖💖💖",
    3: "💖💖💖",
    2: "💖💖",
    1: "💖",
    0: "❌"
}

while life>0:

    print(f"You have {life_to_emoji[life]} lives left.")
    user_num=int(input("Enter a number between 1 and 100: "))

    if user_num==my_num:
        print("You guessed it right!")
        break
    elif user_num<my_num:
        print("Your guess is low.")
    else:
        print("Your guess is high.")
    life-=1
    if life==0:
        print(f"You've run out of lives. The correct number was {my_num}.")     

