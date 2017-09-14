import random

cards = [[random.sample(xrange(1,15), 5) for i in xrange(5)] for i in xrange(5)]
matchcards = [[False for i in xrange(5)] for j in xrange(5)]

nums = range(1,5)

print "Before"
print cards

random.shuffle(nums)

print "Numbers"
print nums

for i in nums:
    
    for icard in cards:
        for icol in icard:
            for inum in icol:
                if inum == i:
                    print inum, i
                    
print "After"
print cards
