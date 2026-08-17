#message welcome
print("="*70)
print("☠️")
print("\nWELCOME TO MY ISLAND\n")
print("="*70)

#Begin the Game
#print("="*70)
door = input(
    "there are two door in front of you:🚪 a (red) door and 🚪 a (blue) door\nwhich door do you want to open?").lower()

if door == "red":
    print("\nGreat! you entred a room.")
    box = input(
        "you found three boxes:📦 a (black) and (white) and (green).\nwhich box do you want to open?").lower()
    if box =="black":
        print("\nyou open a box filled a snakes🐉🐉🐉!")
        print("Game over!")
    elif box == "white":
        print("\nyou open a box filed a spider🕸️🕸️🕸️")
        print("Game over!")
    elif box == "green":
        print("\nCongratulation! you found the treasure💰🏆🎆")
    else:
        print("invalid choice!❌")
    
elif door == "blue":
    print("oops! you open the crocodile door 🐊🐊🐊")
    print("Game Over!")
else:
    print("invalid choice!❌")
print("="*70)
