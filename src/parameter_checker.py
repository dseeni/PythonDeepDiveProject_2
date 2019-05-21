def frange(start=0.0, stop=0.0, step=1.0):
    """returns floating point numbers in a (stepped) range generator object"""
    while True:
        if step > 0 and start >= stop:
            break
        elif step < 0 and start <= stop:
            break
        yield ("%g" % start)  # return formatted float number
        start = start + step


def check_parameters(icount=10, clones=2, cloneamount=2, siderange=(3,10), radrange=(1,5), sig=2):
    """ check parameters takes in the input from
    Polyfactory(icount,clones,clneamount,siderange,radrage,sig)
    returns verified parameters or the least modified viable parameters
    """
    if not isinstance(sig, int) or sig < 0:
        raise TypeError('significant digits (sig) must be of type integer only')

    # set default values of str(s)/str(zeros)
    # increase zeros variable by sig
    zeros = '0' * sig
    # int(s) = concatenated strings of s/zeros
    s = int('1' + zeros)

    # incrementer is the start/step values for frange(start=incrementer , stop=radrange[1], step=incrementer )
    incrementer = len(str(sig)) / s
    # print(incrementer)
    floatrandomtotal = len(list(frange(incrementer, radrange[1] - radrange[0], incrementer)))
    # print(list(frange(incrementer, radrange[1] - radrange[0], incrementer)))
    # this function verifies the that icount amount of unique samples
    # are possible within specified radius range/sig
    # capture the original significant digits
    # r can never be 0 or negative
    if radrange[0] <= 0:
        raise ValueError('radius sample range start must be greater than 0')
    # enforce a positive radius sample range
    if round(radrange[1] - radrange[0], sig) <= 0:
        raise ValueError('rounded radrange length must be a positive number')

    # how many digits for sig
    # 1 + sig amount of 0

    # these amount of 0's to add
    s = str('0' * sig)

    # float range computes the total possible floating point radii
    # float range is limited by significant digits (sig)
    floatrange = str(round(radrange[1] - radrange[0], sig))
    # we want to strip out any potential decimal values
    floatrange = floatrange.replace('.','')
    # randoms possible
    randomspossible = int(floatrange + s)
    # print('randomspossible=', randomspossible)
    if siderange[0] < 3:
        raise ValueError('Sampling of siderange (sides) must begin at 3')

    if not all(isinstance(i, int) for i in siderange):
        raise ValueError('Side range sampling start/end must be integer type only')

    possibleside = siderange[1] - siderange[0]
    if icount > possibleside:
        siderange = (siderange[0], siderange[1] + (icount - possibleside + 1))

    # ensures input parameter for unique numbers / elements to clone / clone amount are integers
    if not all(isinstance(i, int) for i in [icount, clones, cloneamount]):
        raise TypeError('icount/clones/cloneamount must all be integers')

    while icount >= floatrandomtotal:
        sig+=1
        return check_parameters(icount,clones,cloneamount,siderange,radrange, sig)

    if icount <= randomspossible:
        return (icount, clones, cloneamount, siderange, radrange, sig)

