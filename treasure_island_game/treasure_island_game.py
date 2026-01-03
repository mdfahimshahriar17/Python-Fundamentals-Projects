from treasure_box_ASCII import treasure_box
print(treasure_box)
print("Welcome to Treasure Island\nYour mission is find the treasure.")

choice1 = input("You're at a cross road. Where do you want to go?").lower()


if choice1 == "left":
   choice2 = input("You've come to a lake. There is an island in the middle of the lake. Type \"Wait\" to wait for a boat. Type \"Swim\" to swim across. ").lower()

   if choice2 == "wait":
      choice3 = input("You arrive at the island unharmed. There is house with 3 doors. One Red, One Yellow and One Blue").lower()

      if choice3 == "red":
          print("It's a room full of fire. Game Over")
      elif choice3 == "yellow":
          print("You found the treasure. You Win!")
      elif choice3 == "blue":
          print("You enter a room of beasts. Game Over.")
      else:
          print("You choose the door that doesn't exist. Game Over")

   else:
       print("You got attacked by an angry trout. Game Over.")

else:
    print("You fell in to a hole, Game Over.")