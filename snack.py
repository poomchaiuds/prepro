"""vending machine"""
def main():
    """rge"""
    money = int(input())
    water = int(input())
    ttsnack_1 = int(input())
    ttsnack_2 = int(input())
    ttsnack_3 = int(input())
    change_1 = money - water
    change_12 = change_1 % 3
    if change_12 == 0:
        snack_1 = 10
    elif change_12 == 1:
        snack_1 = 15
    else: snack_1 = 20
    change_2 = change_1 - (snack_1*ttsnack_1)
    change_22 = change_2 % 3
    if change_22 == 0:
        snack_2 = 12
    elif change_22 == 1:
        snack_2 = 15
    elif change_22 == 2:
        snack_2 = 18
    change_3 = change_2 - (snack_2*ttsnack_2)
    change_32 = change_3 % 3
    if change_32 == 0:
        snack_3 = 5
    elif change_32 == 1:
        snack_3 = 7
    elif change_32 == 2:
        snack_3 = 9
    lastchange = change_3 - (snack_3*ttsnack_3)
    if lastchange < 0:
        print("Now you have %d left."%money)
        print("You don't have enough money!")
    elif lastchange >= 0:
        print("Now you have %d left."%lastchange)
        print("Here's your order!")
        print("Water: %d baht"%water)
        print("Snack number 1: %d baht"%(snack_1*ttsnack_1))
        print("Snack number 2: %d baht"%(snack_2*ttsnack_2))
        print("Snack number 3: %d baht"%(snack_3*ttsnack_3))
main()
