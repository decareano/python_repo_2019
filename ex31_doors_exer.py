print("you enter a dark room with two doors. you want door 1 or 2?")

door = input("> ")

if door == "1":
    print("there is a giant bear here eating a cheese cake. what do you do?")
    print("1. take the cake")
    print("2. scream at the bear")


    bear = input("> ")

    if bear == "1":
        print("the bear eats your face off. Good job")
    elif bear == "2":
        print("bear eats your legs off")
    else:
        print("well doing %s is probably better. Bear runs away" % bear)

elif door == "2":
    print("you stare into the endless retina")
    print("1. blueberries")
    print("2. yellow jacket clothespins")
    print("3. understanding revolvers yelling melodies")

    insanity = input("> ")

    if insanity == "1" or insanity == '2':
        print("your body survives")
    else:
        print("the insanity rots your eyes into a pool of muck")

else:
    print("you stumble around a knife and die")
