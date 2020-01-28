#---------------------------------
#Arrays Final
#Sydney Loerzel
#January 24, 2020
#---------------------------------

#-------------Lists---------------

art_supplies = ["paint", "brushes", "paper", "canvas", "pencil", "tape"]
others = ["poster", "model cars", "books", "garbage", "bag"]

#--------------Dicts--------------
paint = {}
to_buy = {}

#-----------Functions-------------

def intro():
    print("You have a spare art room that has become a mess")
    print("You know you are going shopping later and can buy more supplies")
    print("BUT first. You need to clean the room and see what all you have in there")
    print("You start by putting everything into 2 piles. Supplies and other stuff")
    print("After a going through everything you look at what all is in each pile")
    print(art_supplies)
    print(others)
    print("You notice a random deck of cards and toss it into the other pile")
    others.append("cards")
    
def art_pile():
    print("You decide to deal with the art supplies pile first")
    print("You begin to put everything up onto the empty shelf")
    print("You notice the tape is the wrong kind of tape")
    print("It belongs not in your art room but in a junk drawer")
    print("You take it out of your room")
    art_supplies.remove("tape")
    print("You start a list to buy, adding painters tape. Maybe two rolls to have")
    to_buy["tape"] = "2"
    print("Once the art pile has been organized onto shelves you move onto the others")
    print("First you make a note of how many different art things you have")
    print(len(art_supplies))

def other_pile():
    print("This pile doesn't look fun at all...")
    print("Lets use a bag and get rid of all the garbage")
    others.remove("garbage")
    others.remove("bag")
    print("lets look at how many other things you have to deal with")
    num = len(others)
    print(num)
    print("That's", num, "too many")
    print("You decide to worry about that pile later and push it to the side")
    
def paints():
    print("Lets look at the paint you have")
    print("You see a lot of blues, reds, greens, and white. Plus one black")
    paint["blues"] = "6"
    paint["reds"] = "5"
    paint["greens"] = "7"
    paint["white"] = "4"
    paint["black"] = "1"
    print(paint)
    print("You should probably get some other colours and more black")
    print("A few purple, pink, and yellow should be good")
    print("Just a couple bottles of each. So 8 in total with the black")
    to_buy["paint"] = "8"
    
def canvas():
    print("To paint you need canvas'. You only have one")
    key = input("How many canvas' do you want to buy?")
    to_buy["canvas"] = key
    
def add_more():
    done = False
    while done == False:
        key = input("Would you like to add anything else? Type 'done' to exit.").lower()
        if key == "done":
            done = True
        elif key != "done":
            value = input("How many?")
            to_buy[key] = value
    
def items():
    print("Now you are at the store buying everything")
    print("You remember everything that you need to get")
    print("But you already forget how much stuff you need to get")
    for values in to_buy:
        buy = to_buy[values]
        print(buy)
        
def outro():
    print("Eventually you get everything and it is time to go home")
    print("Now time to put all the new things away....")
    
def main():
    intro()
    art_pile()
    other_pile()
    paints()
    canvas()
    print(to_buy)
    add_more()
    items()
    outro()
    
main()