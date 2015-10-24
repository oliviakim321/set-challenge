import time
from itertools import combinations as comb

syms = [{'a', 'A', '@'}, {'h', 'H', '#'}, {'s', 'S', '$'}]
shades = [{'a', 'h', 's'}, {'A', 'H', 'S'}, {'@', '#', '$'}]


def find_set(cards):
    cards = process_cards(cards)
    # ignore num of cards
    subsets = []
    # finding subsets
    for subset in comb(cards[1:], 3):
        if is_set(subset):
            subsets.append(list(subset))
    print len(subsets)

    print subsets
    l = [[1, 2, 3], [3, 6, 8], [4, 9], [6, 11]]

    for set in combine(l):
         print set
    for set in combine(subsets):
        print set

def combine(input, list = [], lset = set()):
    if list:
        yield list
    for i, el in enumerate(input):
        if lset.isdisjoint(el):
            for out in combine(input[i+1:], list + [el], lset | set(el)):
                yield out


def process_cards(cards):
    cards = cards.split('\n')
    # skip the number of cards
    for i in xrange(1, len(cards)):
        cards[i] = cards[i].split(' ')
    return cards


def is_set(triplet):
    # check for color - the string color
    s = {triplet[0][0], triplet[1][0], triplet[2][0]}
    if len(s) == 2:
        return False

    # check for shading - # of symbols
    s = {len(triplet[0][1]), len(triplet[1][1]), len(triplet[2][1])}
    if len(s) == 2:
        return False

    # check for shading - # upper lower or symbol
    to_compare = []
    # loop through syms to compare
    for i in xrange(3):
        # loop through shade types
        for j in xrange(3):
            if triplet[i][1][0] in shades[j]:
                to_compare.append(j)
                break
    s = {to_compare[0], to_compare[1], to_compare[2]}
    if len(s) == 2:
        return False

    # check for symbol - A S or H
    # loop through syms to compare
    to_compare = []
    for i in xrange(3):
        # loop through sym types
        for j in xrange(3):
            if triplet[i][1][0] in syms[j]:
                to_compare.append(j)
                break
    s = {to_compare[0], to_compare[1], to_compare[2]}
    if len(s) == 2:
        return False

    return True


input1 = "\
15\n\
blue #\n\
green $\n\
blue AA\n\
yellow @\n\
blue @@@\n\
green A\n\
yellow $$$\n\
yellow @@@\n\
yellow HHH\n\
yellow #\n\
yellow @@\n\
blue a\n\
blue sss\n\
green a\n\
green @"

input2 = "\
28\n\
blue hhh\n\
yellow @\n\
green ##\n\
yellow ###\n\
blue AA\n\
green SSS\n\
blue ###\n\
yellow s\n\
yellow ##\n\
blue H\n\
green A\n\
blue $\n\
green SS\n\
green ###\n\
blue ss\n\
yellow $\n\
green aaa\n\
green AA\n\
yellow sss\n\
green aa\n\
green S\n\
green HH\n\
yellow AA\n\
yellow ss\n\
green h\n\
blue $$\n\
blue aa\n\
green sss"


start_time = time.time()
find_set(input1)
print ("seconds: %s" % (time.time()-start_time))


