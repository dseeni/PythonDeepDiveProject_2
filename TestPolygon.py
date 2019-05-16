from collections import OrderedDict
from random import randint, uniform
from copy import deepcopy
from P2_Proj2_Temp import Poly


def checkparameters (icount=10, clones=2, cloneamount=2, siderange=(3,10), radrange=(1,5), sig=2):

    """ Check Parameters takes in the input from
    PolyFactory(icount,clones,clneamount,siderange,radrage,sig)
    Returns verified parametrs or the least modified viable parameters
    """


    def frange(start, stop=None, step=None):
        # Returns floating point numbers in a step range (sig)
        if stop == None:
            stop = start + 0.0
            start = 0.0
        if step == None:
            step = 1.0
        while True:

            if step > 0 and start >= stop:
                break
            elif step < 0 and start <= stop:
                break
            yield ("%g" % start)  # return float number
            start = start + step
    if not isinstance(sig, int) or sig < 0:
        raise TypeError('Significant Digits (sig) must be of type Integer only')

    # set default values of s/zero
    s = '1'
    zeros = '0'
    zeros = zeros * sig
    s = int(s + zeros)
    incrementor = len(str(sig)) / s
    floatrandomtotal = len(list(frange(incrementor, radrange[1] - radrange[0], incrementor)))
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
    s = '0'
    # these amount of 0's to add
    s = str(s * sig)
    floatrange = '{0}'.format(round(radrange[1] - radrange[0], sig))
    floatrange = floatrange.replace('.','')
    # strip the decimal from the float to create a ""
    randomspossible = int(floatrange + s)
    # print('randomspossible=',randomspossible)

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
        return checkparameters(icount,clones,cloneamount,siderange,radrange, sig)

    if icount <= randomspossible:
        return (icount, clones, cloneamount, siderange, radrange, sig)



class PolyFactory:

    """
    This class generates randomized instances of Poly(n,r,sig):

            icount = intital unique values of (n,r,sig) to generate
            clones = how many of those values will have frequency > 1
            cloneamount = frequency of reoccuring (n,r,sig)
            siderange = (x,y] interval range for side sampling
            radrange = (x,y] interval range of radius sampling
            sig = significant digits for caclulated properties / radius sample range Poly(n,r,sig)

            self.nrfinal = Generates randomized instances of Poly(n,r,sig)

            self.name = last recent Poly(n,r,sig) object names in a list
            self.finallist = length of the list of recently created Poly(n,r,sig)
            self.finalcount = Total count of last generated Poly(n,r,sig)
            self.allcalc = caculate allcalc for each instance of Poly(n,r,sig)
            self.sidevalues = caculate sidevalues for each instance of Poly(n,r,sig)
            self.circumradiusvalues = caculate circumradiusvalues for each instance of Poly(n,r,sig)
            self.vectexcalc = caculate vectexcalc for each instance of Poly(n,r,sig)
            self.perimetercalc = caculate perimetercalc for each instance of Poly(n,r,sig)
            self.apothemcalc = caculate apothemcalc for each instance of Poly(n,r,sig)
            self.interioranglecalc = caculate interioranglecalc for each instance of Poly(n,r,sig)
            self.edgelengthcalc = caculate edgelengthcalc for each instance of Poly(n,r,sig)
            self.areacalc = caculate areacalc for each instance of polygon
            self.instancerepr = dispaly instancerepr for each instance of Poly(n,r,sig)
    """

    def __init__(self, icount=10, clones=2, cloneamount=2, siderange=(3,10), radrange=(1,5), sig=2):

        params = checkparameters(icount,clones,cloneamount,siderange,radrange,sig)

        self._icount = params[0]
        self._clones = params[1]
        self._cloneamount = params[2]
        self._siderange = params[3]
        self._radrange = params[4]
        self._sig = params[5]
        self._finalcount = (self._icount - self._clones) + (self._clones * self._cloneamount)
        if self._finalcount < clones * cloneamount and all(x > 0 for x in (icount, clones, cloneamount)):
            raise ValueError('Error: Total Output Polgyons < Total Desired Clones!')
        self.polynames = '{0}, Generate Polygons with nrfinal method'.format(None)
    @property
    def icount(self):
        """ intital count of unique values of (n,r,sig) to generate"""
        return self._icount
    @property
    def clones(self):
        """ clones = how many of those values will have frequency > 1"""
        return self._clones
    @property
    def cloneamount(self):
        """frequency of reoccuring (n,r,sig)"""
        return self._cloneamount
    @property
    def finalcount(self):
        """Total count of last generated Poly(n,r,sig)"""
        return self._finalcount

    @property
    def siderange(self):
        """(x,y] interval range for side sampling"""
        return self._siderange

    @property
    def radrange(self):
        """(x,y] interval range of radius sampling"""
        return self._radrange

    @property
    def sample_ints(self):
        """ Return a k-length list of unique random integers
            in the range of low <= x <= high
        """

        result = []
        seen = set()
        for i in range(self._icount):
            x = randint(*self._siderange)
            while x in seen:
                x = randint(*self._siderange)
            seen.add(x)
            result.append(x)
        return result

    @property
    def sample_floats(self):
        """ Return a k-length list of unique random floats
            in the range of low <= x <= high fdas
        """
        result = []
        seen = set()
        for i in range(self._icount):
            x = round(uniform(*self._radrange), self._sig)
            while x in seen:
                x = round(uniform(*self._radrange), self._sig)
            seen.add(x)
            result.append(x)
        return result
    @property
    def nrfinal(self):
        """ nrfinal generates instances of Poly(n,r,sig) objects from specified parameters"""
        # Unique n list + Unique r list of length icount
        # lists are mutable data structures
        # so use deepcopy (copy is a shallow copy and thus is a pass by reference)
        # deep copy is a pass by value instantiating a new list

        nrvalslist = list(zip(sorted(self.sample_ints, reverse=True),
                              sorted(self.sample_floats, reverse=True)))
        print('Initial Unique Values:', len(nrvalslist), nrvalslist)

        nrdups = deepcopy(nrvalslist[0:self._clones] * self._cloneamount)
        print('Clones To Append:', len(nrdups), nrdups)

        nrremainder = deepcopy(nrvalslist[self._clones:])
        print('Remaining Unique Values:', len(nrremainder) , nrremainder)

        if len(deepcopy(nrdups + nrremainder)) == 0:
            finallist = deepcopy(nrvalslist)
        else:
            finallist = deepcopy(nrdups + nrremainder)
        finallistsig = []
        for i in finallist:
            finallistsig.append([i[0], i[1]])
        for i in finallistsig:
            i.append(self._sig)

        print(finallistsig)

        print('Final Values of (n,r,sig) for Poly Generation:', len(finallistsig), finallistsig)

        print('POLYGON CLASS TESTING:')

        name = tuple(('poly{0}'.format(n)) for n in range(101, 101+self._finalcount))
        print('Newly Created Object Names:', len(name), name)

        # polylist instantiates Poly objects
        polylist = [Poly(n, r, s) for n, r, s in finallistsig]
        polydict = OrderedDict(zip(name, polylist))

        self.polydict = polydict

        globals().update(polydict)

        self.finallist = len(finallist)
        """ self.polynames = list of names for newly created Poly(n,r,sig) objects """
        self.polynames = name
        return """Process Complete"""

    @property
    def allcalc(self):
        """Calculates all properties for each instance of Poly(n,r,sig)"""
        self.nrfinal
        for v in self.polynames:
            print(v,
                  'Side Count =', eval('{0}.side_count'. format(v)),
                  'Circumradius =', eval('{0}.circumradius'. format(v)),
                  'Vertex Count =',eval('{0}.vertex_count'. format(v)),
                  'Perimeter =', eval('{0}.perimeter'. format(v)),
                  'Apothem =', eval('{0}.apothem'. format(v)),
                  'Interior Angle =', eval('{0}.interior_angle'. format(v)),
                  'Edge Length =', eval('{0}.edge_length'. format(v)),
                  'Area =',eval('{0}.area'. format(v)),
                  'Significant Digits =',eval('{0}.sig'. format(v)),
                  )

    @property
    def sidevalues(self):
        """Returns side counts for each instance of Poly(n,r,sig)"""
        self.nrfinal
        for v in self.polynames:
            print(v, 'Side Count =', eval('{0}.side_count'. format(v)))



    @property
    def circumradiusvalues(self):
        """Returns circumradius for each instance of Poly(n,r,sig)"""
        self.nrfinal
        for v in self.polynames:
            print(v, 'Circumradius =', eval('{0}.side_count'. format(v)))


    @property
    def vectexcalc(self):
        """Returns vertex count for each instance of Poly(n,r,sig)"""
        self.nrfinal
        for v in self.polynames:
            print(v, 'Vertex Count =',eval('{0}.side_count'. format(v)))


    @property
    def perimetercalc(self):
        """Returns caculated perimeter for each instance of Poly(n,r,sig)"""
        self.nrfinal
        for v in self.polynames:
            print(v, 'Perimeter =', eval('{0}.side_count'. format(v)))

    @property
    def apothemcalc(self):
        """Returns caculated apothem for each instance of Poly(n,r,sig)"""
        self.nrfinal
        for v in self.polynames:
            print(v,'Apothem =', eval('{0}.side_count'. format(v)))


    @property
    def interioranglecalc(self):
        """Returns caculated interior angle for each instance of Poly(n,r,sig)"""
        self.nrfinal
        for v in self.polynames:
            print(v, 'Interior Angle =', eval('{0}.edge_length'. format(v)))


    @property
    def edgelengthcalc(self):
        """Returns caculated side length for each instance of Poly(n,r,sig)"""
        self.nrfinal
        for v in self.polynames:
            print(v, 'Edge Length =', eval('{0}.side_count'. format(v)))


    @property
    def areacalc(self):
        """Returns calculated area for each instance of Poly(n,r,sig)"""
        self.nrfinal
        for v in self.polynames:
            print(v, 'Area =',eval('{0}.side_count'. format(v)))

    @property
    def instancerepr(self):
        """Returns each instance representation of Poly(n,r,sig)lf):"""
        self.nrfinal
        for v in self.polynames:
            print(v, 'Poly() Instance Names =',eval('{0}'. format(v)))


    def __len__(self):
        return self.finalcount
    #
    def __repr__(self):
        return 'PolyFactory(icount={0},clones={1},cloneamount={2},siderange={3},radrange={4},sig={5})'.format(self._icount,
                                                             self._clones,
                                                             self._cloneamount,
                                                             self._siderange,
                                                             self._radrange,
                                                             self._sig)

    def __setitem__(self, icount=None, clones=None, cloneamount=None, siderange=None, radrange=None, sig=None):

        icount = icount if icount is not None else self._icount
        clones = clones if clones is not None else self._clones
        cloneamount = cloneamount if cloneamount is not None else self._cloneamount
        siderange = siderange if siderange is not None else self._siderange
        radrange = radrange if radrange is not None else self._radrange
        sig = sig if sig is not None else self._sig

        params = checkparameters(icount, clones, cloneamount, siderange, radrange, sig)

        self._icount = params[0]
        self._clones = params[1]
        self._cloneamount = params[2]
        self._siderange = params[3]
        self._radrange = params[4]
        self._sig = params[5]
        self._finalcount = (self._icount - self._clones) + (self._clones * self._cloneamount)
        if self._finalcount < clones * cloneamount and all(x > 0 for x in (icount, clones, cloneamount)):
            raise ValueError('Error: Total Output Polgyons < Total Desired Clones!')
        self.nrfinal




# gen_polys = PolyFactory()

# print(gen_polys.nrfinal)
# # print(gen_polys.finallist)
# # print(gen_polys.polynames)
# # help(gen_polys)
# # gen_polys.__setitem__(cloneamount=50, sig=3)
# # print(gen_polys)
# # gen_polys.nrfinal
# # print(gen_polys.polynames)
# # print(gen_polys.allcalc)
# # gen_polys.nrfinal
# # gen_polys.polynames
# #
# # print(gen_polys)
# # print(gen_polys.polynames)
# # gen_polys.nrfinal
# # print(gen_polys.polynames)
# # gen_polys.apothemcalc
# #
# # help(checkparameters)
# # help(PolyFactory)
# #
# # print(len(gen_polys))
# # gen_polys.__setitem__(siderange=(100,300))
# # gen_polys.allcalc
# # gen_polys.__setitem__(sig=5)
# # print(gen_polys.polynames)
# # # gen_polys.__setitem__(radrange=(100,200),siderange=(200,400),sig=3)
# # # gen_polys.allcalc
# # print(gen_polys)
# # gen_polys.__setitem__(sig=5)
# # print(gen_polys)
# # # gen_polys.__setitem__(sig=1000)
# print(gen_polys.instancerepr)