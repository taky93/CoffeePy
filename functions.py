import time
from constants import *
import playsound




def header():
    print("*********************************************************")
    print("*******************COFFEE MACHINE************************")
    print("*********************************************************")
    time.sleep(0.5)


def select():
    print("1.COFFEE  2.ESPRESSO  3.TEA  4.LATTE")
    selection = int(input("Select a Drink: "))
    if selection == 1:
        print("COFFEE SELECTED AND THE PRICE IS " + str(COFFEE))
        price(COFFEE)
    elif selection == 2:
        print("ESPRESSO SELECTED AND THE PRICE IS " + str(ESPRESSO))
        price(ESPRESSO)

    elif selection == 3:
        print("TEA SELECTED AND THE PRICE IS " + str(TEA))
        price(TEA)

    elif selection == 4:
        print("LATTE SELECTED AND THE PRICE IS " + str(LATTE))
        price(LATTE)

    else:
        print("WRONG INPUT")

def price(content):
    money = int(input("AMOUNT OF MONEY INSERTED: "))
    if money == content:
        print("ENOUGH MONEY INSERTED")
        time.sleep(1)
        print("YOUR DRINK IS ON THE WAY")
        time.sleep(1)
        playsound._playsoundNix('sound.wav',True)
        print("FINISHED")
    else:
        print("NOT ENOUGH MONEY INSERTED")



