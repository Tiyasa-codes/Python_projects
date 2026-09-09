import random
while(not want):
   dice_roll=random.randint(1,6)
   print(dice_roll)
   want=bool(input("Do you want to play again?"))  
