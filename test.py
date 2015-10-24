
import time
from set import find_sets

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

# calculate the time it takes to run the program
start_time = time.time()
find_sets(input3)
print ("seconds: %s" % (time.time()-start_time))
