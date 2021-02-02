import random

class die:
  num = 0
    # getter method for subject
  def get_num(self): 
      return self.num
  # setter method for subject
  def set_num(self, x): 
      self.num = x 

  def roll(self):
    rand_roll = random.randint(1, 6)
    self.set_num(rand_roll)
    print("Dice Roll = " + str(self.get_num()))
    self.print_die()
    return self.get_num()

  def print_die(self):
    if(self.get_num()==1):
      print("+-----+")
      print("|     |")
      print("|  o  |")
      print("|     |")
      print("+-----+")
    elif(self.get_num()==2):
      print("+-----+")
      print("| o   |")
      print("|     |")
      print("|   o |")
      print("+-----+")
    elif(self.get_num()==3):
      print("+-----+")
      print("|o    |")
      print("|  o  |")
      print("|    o|")
      print("+-----+")
    elif(self.get_num()==4):
      print("+-----+")
      print("|o   o|")
      print("|     |")
      print("|o   o|")
      print("+-----+")
    elif(self.get_num()==5):
      print("+-----+")
      print("|o   o|")
      print("|  o  |")
      print("|o   o|")
      print("+-----+")
    elif(self.get_num()==6):
      print("+-----+")
      print("|o   o|")
      print("|o   o|")
      print("|o   o|")
      print("+-----+")
    

class dice_roller_game:
  dice1 = die()
  dice2 = die()
  dice3 = die()

  def get_dice1(self): 
    return self.dice1
  def set_dice1(self, x): 
    self.dice1 = x

  def get_dice2(self): 
    return self.dice2
  def set_dice2(self, x): 
    self.dice2 = x 
  
  def get_dice3(self): 
    return self.dice3
  def set_dice3(self, x): 
    self.dice3 = x

  def add_rolls3(self):
    #returns number from roll
    dice_roll1 = self.get_dice1().roll()
    dice_roll2 = self.get_dice2().roll()
    dice_roll3 = self.get_dice3().roll()
    
    self.get_dice1().set_num = dice_roll1
    self.get_dice2().set_num = dice_roll2
    self.get_dice3().set_num = dice_roll3
    
    sum = self.get_dice1().get_num() + self.get_dice2().get_num() + self.get_dice3().get_num()
    print("The role sum is:", sum)
    #return sum
  
  def add_rolls2(self):
    #returns number from roll
    dice_roll1 = self.get_dice1().roll()
    dice_roll2 = self.get_dice2().roll()
       
    self.get_dice1().set_num = dice_roll1
    self.get_dice2().set_num = dice_roll2
    
    sum = self.get_dice1().get_num() + self.get_dice2().get_num() 
    print("The role sum is:", sum)
    #return sum

  def add_rolls1(self):
    #returns number from roll
    dice_roll1 = self.get_dice1().roll()
    self.get_dice1().set_num = dice_roll1 
    sum = self.get_dice1().get_num() 
    print("The role sum is:", sum)
    #return sum



  # --------------------------------------------------

dice_game = dice_roller_game()
#dice_game.add_rolls1()
#dice_game.add_rolls2()


choice = 0
the_sum = 10
game_run = True
print("1) One Die\n2) Two Dice\n3) Three Dice")

#tried creating loop to have game keep running
#ran into error:"TypeError 'int' object is not callable"
# probably means that you are trying to call a method when a property with the same name is available.................
#line 14 cuasing error:::    self.set_num(rand_roll)

# while game_run == True:
#   choice = input("How many dice to roll? Choice: ")
#   choice = int(choice)
#   if choice == 1:
#     print("11111")
#     dice_game.add_rolls1()
#   elif choice == 2:
#     dice_game.add_rolls2()
#   elif choice == 3:
#     dice_game.add_rolls3()
#   else:
#     break

choice = input("How many dice to roll? Choice: ")
choice = int(choice)
if choice == 1:
  dice_game.add_rolls1()
elif choice == 2:
  dice_game.add_rolls2()
elif choice == 3:
  dice_game.add_rolls3()

#dice_game.add_rolls1()

#print("FInal: The roll sum is: " + str(the_sum))
# the_sum = 

# Note: remove paranthesis from if statements. Unecessary typing
# Note: remember input answers are strings 
# Note: find out hour paranthesis affects method calls ( )
