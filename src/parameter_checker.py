def check_parameters(icount=10, clones=2, cloneamount=2, siderange=(3, 10), radrange=(1, 5), sig=2):
    """
    *** PolyFactory helper function ***
    
    check_parameters() takes in the input from Polyfactory

    (icount, clones, clneamount, siderange, radrage, sig)
    and returns verified parameters.

    If initial randomized instances to be generated (icount) exceed the possible  unique
    values within siderange and radrange's significant digit precision, check_parameters
    returns the minimum viable parameters to satisfy the initial randomized
    instance count (icount)
    """
    if clones < 0 or cloneamount < 0:
        raise ValueError('clones and cloneamount must be >= 0')

    if not isinstance(sig, int) or sig < 0:
        raise TypeError('significant digits (sig) must be of type integer only')

    # r can never be 0 or negative
    if radrange[0] <= 0:
        raise ValueError('radius sample range start must be greater than 0')
    # enforce a positive radius sample range
    if round(radrange[1] - radrange[0], sig) <= 0:
        raise ValueError('rounded radrange length must be a positive number')

    if siderange[0] < 3:
        raise ValueError('Sampling of siderange (sides) must begin at 3')

    if not all(isinstance(i, int) for i in siderange):
        raise ValueError('Side range sampling start/end must be integer type only')

    # ensures input parameter for unique numbers / elements to clone / clone amount are integers
    if not all(isinstance(i, int) for i in [icount, clones, cloneamount]):
        raise TypeError('icount/clones/cloneamount must all be integers')

    # set default values of str(s) and str(zeros)
    # increase zeros variable by sig
    zeros = '0' * sig
    # int(s) = concatenated strings of s zeros
    s = int('1' + zeros)

    # incrementer is the start and step values for frange(start=incrementer , stop=radrange[1], step=incrementer )
    floatrandomtotal = int((radrange[1] - radrange[0]) * s)
    # floatrandomtotal = len(list(frange(incrementer, radrange[1] - radrange[0], incrementer)))

    # these amount of 0's to add
    s = str('0' * sig)

    # float range computes the total possible floating point radii
    # float range is limited by significant digits (sig)
    floatrange = str(round(radrange[1] - radrange[0], sig))
    # we want to strip out any potential decimal values
    floatrange = floatrange.replace('.', '')
    # randoms possible
    randomspossible = int(floatrange + s)

    possibleside = siderange[1] - siderange[0]
    if icount > possibleside:
        siderange = (siderange[0], siderange[1] + (icount - possibleside))

    while icount >= floatrandomtotal:
        sig += 1
        return check_parameters(icount, clones, cloneamount, siderange, radrange, sig)

    if icount <= randomspossible:
        return icount, clones, cloneamount, siderange, radrange, sig

help(check_parameters)
