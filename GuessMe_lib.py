import random


def check(rand_no, value):
    # print "Random No:" + str(rand_no)
    # print "Value: " + str(value)
    if rand_no == value:
        return True
    else:
        return False


def set_game(lvl, lvl_chances):

        if lvl == 1:
            rand_no = random.randrange(1, int(lvl_chances))
            attempts_left = 5

            # print "Random No: " + str(rand_no)
            # print "Level 1"
            # print "Level Chances: " + str(lvl_chances)

        if lvl == 2:
            rand_no = random.randrange(1, int(lvl_chances))
            attempts_left = 10

            # print "Random No: " + str(rand_no)
            # print "Level 1"
            # print "Level Chances: " + str(lvl_chances)
        return int(rand_no), int(attempts_left)


def check(rand_no, value):
    # print "Random No:" + str(rand_no)
    # print "Value: " + str(value)
    if rand_no == value:
        return True, str("equal")
    if rand_no > value:
        return False, str("less")
    if rand_no < value:
        return False, str("greater")
