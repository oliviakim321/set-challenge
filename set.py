
from itertools import combinations as comb

# The different symbols: a group, h group or s group
syms = [{'a', 'A', '@'}, {'h', 'H', '#'}, {'s', 'S', '$'}]
# The different shades: lower, upper or symbol case
shades = [{'a', 'h', 's'}, {'A', 'H', 'S'}, {'@', '#', '$'}]


def find_sets(cards):
    """ Prints the number of unique sets of cards and the number of cards in
        the maximum disjoint set and prints the sets contained in the disjoint set.
        -:param cards -- The string listing the cards
    """
    cards = process_cards(cards)
    subsets = []
    # finding subsets
    for subset in comb(cards[1:], 3):
        if is_set(subset):
            subsets.append(list(subset))
    print len(subsets)

    #finding max disjoint
    subsets = process_sets(subsets)
    max_disjoint = []
    for set in combine_recurse(subsets):
        if len(set) > len(max_disjoint):
            max_disjoint = set

    print len(max_disjoint), "\n"
    for card in max_disjoint:
        for i in xrange(3):
            print card[i]
        # to separate lines
        print " "


def combine_recurse(sets, curr_list=[], list_set=set()):
    """ Recursively combines the subsets and checks to see if they overlap. Returns the disjoints of the sets.
        -:param sets -- the total set of sets of cards to work with
        -:param curr_list -- the current disjoint list of sets
        -:param list_sets -- the disjoint set of sets we use to compare with the next set in the list of sets
    """
    if curr_list:
        yield curr_list
    for i, s in enumerate(sets):
        # check for common elements in the list of sets with the new set
        if list_set.isdisjoint(s):
            for disjoint in combine_recurse(sets[i+1:], curr_list + [s], list_set | set(s)):
                yield disjoint


def process_cards(cards):
    """ Processes the cards into easier to access form - separates each card into a list. Returns the formatted
        list of cards.
        -:param cards -- The string listing the cards
    """
    cards = cards.split('\n')
    for i in xrange(1, len(cards)):
        cards[i] = cards[i].split(' ')
    return cards


def process_sets(sets):
    """ Processes the sets into a form that is readable by the combine_recurse function. Returns the of sets.
        -:param sets -- The list of sets that need to be formatted
    """
    for i in xrange(len(sets)):
        sets[i] = [' '.join(sets[i][0][0:2]), ' '.join(sets[i][1][0:2]), ' '.join(sets[i][2][0:2])]
    return sets


def is_set(triplet):
    """ Checks to see if three cards form a set. Returns True if they form a set, False otherwise
        -:param triplet -- The list of three cards to evaluate
    """
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


