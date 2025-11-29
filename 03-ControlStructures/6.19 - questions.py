interested = input("Are you interested in computer science? (y/n): ") 
computer_games = input("Do you like playing computer games? (y/n): ")
instagram_account = input("Do you have an Instagram account? (y/n): ")

is_interested = (interested == "y")
likes_games = (computer_games == "y")
has_instagram = (instagram_account == "y")

if is_interested:
    print("Interested in computer science: Yes")
else:
    print("Interested in computer science: NO")

if likes_games:
 print("Playing computer games: Yes")
else:
  print("Playing computer games: NO")

if has_instagram:
 print("Has an Instagram account: Yes")
else:
 print("Has an Instagram account: NO")

