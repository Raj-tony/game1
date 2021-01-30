def start():
    print("there are two doors ")
    print("select any door left or right")
    answer = input("<").lower()
    if "f" in answer:
        bear_room()
    elif "r" in answer:
        monster_room()
    else:
        game_over("don't you know how type!!")

def  bear_room():
     print("your in bear room,now the bear is eating tasty honey and there is door beside the bear")
     print("select one 1)go silently 2)take off that honey")
     answer = input()
     if "1" in answer:
        diamond_room()
     elif "2" in answer:
        game_over("you got killed by bear")
     else:
        game_over("dont you know how to type")

def monster_room():
    print("your in a monster room ,there is a monster sleeping infront of you ")
    print("you have two options 1)silently go through the door which is behind the monster")
    print("or 2)try to kill the monster")
    answer = input()
    if "1" in answer:
        diamond_room()
    elif "2" in answer:
        game_over("monster killed you")
    else:
        game_over("you dont know how to type")
def diamond_room():
    print("your in a diamond room full of diamonds now you have two options")
    print("choose one 1)pack all your diamonds in your bag 2)move silently to next door")
    answer = input()
    if "1" in answer:
        game_over("your dead cause all the diamonds are cursed stuff")
    elif "2" in answer:
        print("you win the game")
    else:
        game_over("bitch")
def game_over(reason):
    print("\n"+reason)
    print("Game over!")
    play_again()

def play_again():
    print("do u wanna start again y or n")
    answer = input()
    if "y" in answer:
        start()
    else:
        exit()
start()
