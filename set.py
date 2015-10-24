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

    #finding max disjoint
    sets = process_sets(subsets)

    max_disjoint = []
    for set in combine_recurse(sets):
        if len(set) > len(max_disjoint):
            max_disjoint = set
    print len(max_disjoint), "\n"

    for card in max_disjoint:
        for i in xrange(3):
            print card[i]
        # to separate lines
        print " "


def combine_recurse(sets, curr_list=[], list_sets=set()):
    if curr_list:
        yield curr_list
    for i, s in enumerate(sets):
        if list_sets.isdisjoint(s):
            for disjoint in combine_recurse(sets[i+1:], curr_list + [s], list_sets | set(s)):
                yield disjoint


def process_cards(cards):
    cards = cards.split('\n')
    # skip the number of cards
    for i in xrange(1, len(cards)):
        cards[i] = cards[i].split(' ')
    return cards


def process_sets(sets):
    for i in xrange(len(sets)):
        sets[i] = [' '.join(sets[i][0][0:2]), ' '.join(sets[i][1][0:2]), ' '.join(sets[i][2][0:2])]
    return sets


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
21\n\
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
green S"

input3 = "\
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
find_set(input3)
print ("seconds: %s" % (time.time()-start_time))

