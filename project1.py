name = input("Hey Type you name here : ")

print("Hello" +name+ "welcome to my Game!")

Should_we_play = input("Do you want to play?. ").lower()

if Should_we_play == 'y' or Should_we_play == "yes":
    print("We are gonna Play!")

    direction = input("Do you want to go left or right.? (left/right)").lower()

    if direction == "left":
        print("You went left and fell of a cliff, game over, try again.")
    elif direction == "right":
        choice = input("Okay, You now see a bridge, do you want to swim under it or cross it? (swim/cross)")
        if choice == "swim":
            print("You Got eaten by an alligator, you die, the end!")

        else:
            print("You found the gold tressure and won!")
    else:
        print("Sorry not a valid reply, you die!")
else:
    print("we are not Playing")
