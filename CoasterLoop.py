#Step 0
#input: num -- an int
#output: lst -- a list of ints from 0 to num-1
def basicLoop(num):
    lst = []
    for i in range(num):
        lst.append(i)
    return lst


#Step 1
#input: customers -- the number of customers in line for the ride
#output: lst -- a list full of the numbers from 0 to customers-1 and the string "now that's a line!"
def lineManage(customers):
    lst = []
    #student code here
    for i in range(customers):
        lst.append(i)
    lst.append("now that's a line!")
    return lst
print("TESTING lineManage", lineManage(5))

#Step 2
#input: customers -- the number of customers in line for the ride
#output: lst -- a list full of the numbers from 0 to customers-1, with the splashed customers replaced by "splashed!"
def lineSplash(customers):
    lst = []
    #student code here
    for i in range(customers):
        if i == 0 or (i % 3 == 0):
            lst.append("splashed")
        else:
            lst.append(i)
    return lst
print("TESTING lineSplash", lineSplash(5))

#Step 3
#input: num -- some starting int number
#output: lst -- a list from num to 1 and the string "Happy New Years!"
def connieCountdown(num):
    lst = []
    #student code here
    for i in range(num, 0, -1):
        lst.append(i)
    lst.append("Happy New Years!")
    return lst
print("TESTING connieCountdown", connieCountdown(10))

#Step 4
#input: rolls -- a list of the player's rolls. success -- a list of Connie's rolls
#output: any time one of player's rolls matches one of Connie's, append to lst "Success for [number]"
def ringToss(rolls, success):
    lst = []
    #student code here
    for i in rolls:
        for j in success:
            if i == j:
                lst.append(f'Success for {i}')
    return lst
print("TESTING ringToss", ringToss([10, 3, 5, 7, 20, 19], [19, 3, 18, 12, 15, 1]))

#Step 5
#input: start -- random starting number numMoves -- the number of moves that should go into the dance list
#output: dance -- a list full of dance moves based on numMoves and start
def dinerDance(start, numMoves):
    dance = []
    #student code here
    for i in range(numMoves):
        start = int((start * 2 + 4) / 3)
        if start % 3 == 0:
            dance.append("spin")
        elif start % 4 == 0:
            dance.append("side step")
        elif start % 5 == 0:
            dance.append("shake hips")
        elif start % 2 == 0:
            dance.append("freestyle")
        else:
            dance.append("hop")
    return dance
print("TESTING dinerDance", dinerDance(50, 4))

def main():
    print("Basic Loop returns: {}".format(basicLoop(3)))
    return

if __name__ == "__main__":
    main()

