#test 1: it compiles

#test 2: lineManage, lineSplash

import CarnivalLab
import random

def testLineManage(customers):
    lst = []
    for i in range(customers):
        lst.append(i)
    lst.append( "now that's a line!")
    return lst
    
def testLineSplash(customers):
    lst = []
    for i in range(customers):
        if i % 3 == 0:
            lst.append("splashed!")
        else:
            lst.append(i)
    return lst

def test_passed(test_feedback):
    gen1 = random.randrange(10, 25)
    gen2 = random.randrange(10, 25)
    
    lst1 = testLineManage(gen1)
    lst2 = testLineManage(gen2)
    lst3 = testLineSplash(gen1)
    lst4 = testLineSplash(gen2)

    student1 = CarnivalLab.lineManage(gen1)
    student2 = CarnivalLab.lineManage(gen2)
    student3 = CarnivalLab.lineSplash(gen1)
    student4 = CarnivalLab.lineSplash(gen2)
    if (lst1 == student1) and (lst2 == student2) and (lst3 == student3) and (lst4 == student4)):
        return true
    else:
        test_feedback.write('You incorrectly returned:\n{0}\n{1}\n{2}\n{3}\n\nExpected: {4}\n{5}\n{6}\n{7}'.format(student1,student2, student3, student4, lst1, lst2, lst3, lst4))
        return False



#test 3: connieCountdown, ringToss

import CarnivalLab
import random

def testRingToss(rolls, success):
    lst = []
    for roll in rolls:
        for s in success:
            if roll == s:
                lst.append("Success for {}".format(roll))
    return lst
    
def testConnieCountdown(num):
    lst = []
    for i in range(num, 0, -1): #alternatively, you can do standard for i in range(num) and alter what is appended
        lst.append(i)
    lst.append("Happy New Years!")
    return lst

def test_passed(test_feedback):
    rolls = []
    success = []
    for i in range(6):
        rolls.append(random.randrange(1, 21))
        success.append(random.randrange(1, 21))
    gen1 = random.randrange(5, 17)
    
    lst1 = testConnieCountdown(gen1)
    lst2 = testRingToss(rolls, success)

    student1 = CarnivalLab.countDown(gen1)
    student2 = CarnivalLab.ringToss(rolls, success)
    if (lst1 == student1) and (lst2 == student2):
        return true
    else:
        test_feedback.write('You incorrectly returned:\n{}\n{}\n\nExpected: {}\n{}\n'.format(student1,student2, lst1, lst2))
        return False



#test 4: dinerDance

import CarnivalLab
import random

def testDinerDance(start, numMoves):
    dance = []
    for i in range(numMoves):
        start = int((start * 2 + 4)/3)
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

def test_passed(test_feedback):
    gen1 = random.randrange(43, 107)
    gen2 = random.randrange(43, 107)
    gen3 = random.randrange(2, 6)
    gen4 = random.randrange(2, 6)
    
    lst1 = testDinerDance(gen1, gen3)
    lst2 = testDinerDance(gen2, gen4)
       
    student1 = CarnivalLab.dinerDance(gen1, gen3)
    student2 = CarnivalLab.dinerDance(gen2, gen4)
    if (lst1 == student1) and (lst2 == student2):
        return true
    else:
        test_feedback.write('You incorrectly returned:\n{}\n{}\n\nExpected: {}\n{}\n'.format(student1,student2, lst1, lst2))
        return False

