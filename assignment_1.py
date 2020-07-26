import random
correct_answer=random.randint(1,100)
turn=1


while turn < 11:
   guess=int(input("input your number")) 
   if guess==correct_answer:
       print("YOU WIN! YOU GUESSED THE CORRECT NUMBER IN %s TURNS." %str(turn))
   elif guess < correct_answer:
       print("TOO LOW. GUESS AGAIN ")
   elif guess > correct_answer:
       print("TOO HIGH. GUESS AGAIN ")
   
   turn+=1
   
if turn > 10:
    print("you lose")