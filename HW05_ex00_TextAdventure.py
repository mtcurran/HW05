#!/usr/bin/env python
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
import sys
from sys import exit

# Body


def infinite_stairway_room(user_name, count=0):
    print "%s walks through the door to see a dimly lit hallway." % str(user_name)
    print "At the end of the hallway is a", count * 'long ', 'staircase going towards some light'
    next = raw_input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print '%s takes the stairs' % str(user_name)
        if (count > 0):
            print "but %s is not happy about it" % str(user_name)
        infinite_stairway_room(user_name, count + 1)
    # option 2 == ?????
    elif next == "implode":
        dead("%s implodes." % str(user_name))
        pass
    elif next == "back":
        back_room(user_name)


def gold_room(user_name):
    print "This room is full of gold.  How much does %s take?" % str(user_name)

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, %s is not greedy, %s wins!" % (str(user_name), str(user_name))
        exit(0)
    else:
        print "%s is a greedy bastard! %s is banished to the infinite stairs." % (str(user_name), str(user_name))
        infinite_stairway_room(user_name, 0)

def bear_room(user_name):
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How is %s going to move the bear?" % str(user_name)
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take" or next == "honey":
            dead("The bear looks at %s then slaps %s's face off." % (str(user_name), str(user_name)))
        elif (next == "taunt") and not bear_moved:
            print "The bear has moved from the door. %s can go through it now." % str(user_name)
            bear_moved = True
        elif (next == "taunt") and bear_moved:
            dead("The bear gets pissed off and chews %s's leg off." % str(user_name))
        elif (next == "open" or "door") and bear_moved:
            gold_room(user_name)
        elif next == "back":
            back_room(user_name)
        else:
            print "I got no idea what that means."


def cthulhu_room(user_name):
    print "Here %s sees the great evil Cthulhu." % str(user_name)
    print "He, it, whatever stares at %s and %s goes insane." % (str(user_name), str(user_name))
    print "Does %s flee for %s's life or eat %s's head?" % (str(user_name), str(user_name), str(user_name))

    next = raw_input("> ")

    if "flee" in next:
        main()
    elif "head" in next:
        dead("Well that was tasty!")
    elif next == "back":
        back_room(user_name)
    else:
        cthulhu_room(user_name)

def back_room(user_name):
    print "%s enters a room full of awkward programmers. %s states %s's name, but nobody listens. %s soon starts programming python and never leaves." % (str(user_name), str(user_name), str(user_name), str(user_name))
    exit(0)

def dead(why):
    print why, "Good job!"
    exit(0)


##############################################################################
def main():
    # START the TextAdventure game
    user_name = sys.argv[1]

    print "%s is in a dark room." % str(user_name)
    print "There is a door to %s's right and left." % str(user_name)
    print "Which one does %s take?" % str(user_name)

    next = raw_input("> ")

    if next == "left":
        bear_room(user_name)
    elif next == "right":
        cthulhu_room(user_name)
    elif next == "back":
        back_room(user_name)
    else:
        dead("%s stumbles around the room until %s starves." % (str(user_name), str(user_name)))

if __name__ == '__main__':
    main()
