# This file is notes

from random import randint, uniform
from copy import deepcopy


def sample_floats(low, high, k=1):
    """ Return a k-length list of unique random floats
        in the range of low <= x <= high
    """
    result = []
    seen = set()
    for i in range(k):
        x = round(uniform(low, high), 2)
        while x in seen:
            x = round(uniform(low, high), 2)
        seen.add(x)
        result.append(x)
    return result


def sample_ints(low, high, k=1):
    """ Return a k-length list of unique random integers
        in the range of low <= x <= high
    """
    result = []
    seen = set()
    for i in range(k):
        while x in seen:
            x = randint(low, high)
        seen.add(x)
        result.append(x)
    return result


# lists are mutable data structures
# so use deepcopy (copy is a shallow copy and thus is a pass by reference)
# deep copy is a pass by value instantiating a new list
pcount = 100

nrvalslist = list(zip(sorted(sample_ints(1, 100, pcount), reverse=True),
                      sorted(sample_floats(1, 100, pcount), reverse=True)))


print('nrvalslist', nrvalslist)

# we want x number of different items to be duplicated
amountdup = 4
# we want to duplicate items y number of times (at least 2 times)
instances = 0




nrdups = deepcopy(nrvalslist[0:amountdup] * instances)
print('nrdups', len(nrdups), nrdups)

nrRemainder = deepcopy(nrvalslist[amountdup:])
print('nrRemainder', len(nrRemainder), nrRemainder)

nrFinal = deepcopy(nrdups + nrRemainder)
print('nrFinal', len(nrFinal), nrFinal)


nrTotalLength = (len(nrvalslist)- amountdup) + (amountdup*instances)

print(nrTotalLength)



assert (id(nrvalslist) != id(nrdups) != id(nrRemainder) != id(nrFinal))
print('unique list mem ids established')
