print("Welcome to my First Game")
name = input("What is your name? : ")
age = int(input("What is your age? : "))

print("Hello ",name," you are ",age," years old")

health = 10



if age >= 18:
  print("You are old enough to play!")

  wants_to_play = input("Do you want to play?").lower()
  if wants_to_play=="yes":
    ("You are starting with ",health,"health")
    print("Let's play")

    left_or_right = input("First choice... left or right(left/right)? ")
    if left_or_right=="left":
      ans = input("you follow the path and reach a lake...Do you swim across or go go around (across/around)? ")

      if ans == "around":
        print("You went around and reached to the other side of the lake")
      elif ans == "across":
        print("You managed to get across but were bit by a fish and lost 5 health")
        health -= 5

   

  else:
    print("cya.....")
else:
  print("You are not old enough to play!")

