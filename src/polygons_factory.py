from collections import OrderedDict
from random import randint, uniform
from copy import deepcopy
from src import poly_and_polygons as pp
from src import parameter_checker as pm


class PolyFactory:

    """
    This class generates randomized instances of Poly(n,r):

            icount = intital unique values of (n,r) to generate
            clones = how many of those values will have frequency > 1
            cloneamount = frequency of reoccuring (n,r)
            siderange = (x,y] interval range for side sampling
            radrange = (x,y] interval range of radius sampling
            sig = floating point precision for radrange (x,y] and float display rounding

            self.nrfinal = Generates randomized instances of Poly(n,r)
            self.name = last recent Poly(n,r) object names in a list
            self.finallist = length of the list of recently created Poly(n,r)
            self.finalcount = Total count of last generated Poly(n,r)
            self.allcalc = caculate allcalc for each instance of Poly(n,r)
            self.sidevalues = caculate sidevalues for each instance of Poly(n,r)
            self.circumradiusvalues = caculate circumradiusvalues for each instance of Poly(n,r)
            self.vectexcalc = caculate vectexcalc for each instance of Poly(n,r)
            self.perimetercalc = caculate perimetercalc for each instance of Poly(n,r)
            self.apothemcalc = caculate apothemcalc for each instance of Poly(n,r)
            self.interioranglecalc = caculate interioranglecalc for each instance of Poly(n,r)
            self.edgelengthcalc = caculate edgelengthcalc for each instance of Poly(n,r)
            self.areacalc = caculate areacalc for each instance of polygon
            self.instancerepr = dispaly instancerepr for each instance of Poly(n,r)
    """

    def __init__(self, icount=10, clones=2, cloneamount=2, siderange=(3, 10), radrange=(1, 5), sig=1):

        params = pm.check_parameters(icount, clones, cloneamount, siderange, radrange, sig)

        self._icount = params[0]
        self._clones = params[1]
        self._cloneamount = params[2]
        self._siderange = params[3]
        self._radrange = params[4]
        self._sig = params[5]
        self._finalcount = (self._icount - self._clones) + (self._clones * self._cloneamount)
        if self._finalcount <= clones * cloneamount and all(x >= 0 for x in (icount, clones, cloneamount)):
            raise ValueError('Error: Total Output Polgyons < Total Desired Clones!')
        self.polynames = '{0}, Generate Polygons with nrfinal method'.format(None)

    @property
    def icount(self):
        """ intital count of unique values of (n,r) to generate"""
        return self._icount

    @icount.setter
    def icount(self, icount):
        params = pm.check_parameters(icount=icount, clones=self._clones, cloneamount=self._cloneamount,
                                     siderange=self._siderange, radrange=self._radrange, sig=self._sig)
        self._icount = params[0]
        self._clones = params[1]
        self._cloneamount = params[2]
        self._siderange = params[3]
        self._radrange = params[4]
        self._sig = params[5]
        self._finalcount = (self._icount - self._clones) + (self._clones * self._cloneamount)
        if self._finalcount <= self._clones * self._cloneamount and all(x >= 0 for x in (self._icount, self._clones,
                                                                                         self._cloneamount)):
            raise ValueError('Error: Total Output Polgyons < Total Desired Clones!')
        self.polynames = '{0}, Generate Polygons with nrfinal method'.format(None)

    @property
    def clones(self):
        """ clones = how many of those values will have frequency > 1"""
        return self._clones

    @clones.setter
    def clones(self, clones):
        params = pm.check_parameters(icount=self._icount, clones=clones, cloneamount=self._cloneamount,
                                     siderange=self._siderange, radrange=self._radrange, sig=self._sig)
        self._icount = params[0]
        self._clones = params[1]
        self._cloneamount = params[2]
        self._siderange = params[3]
        self._radrange = params[4]
        self._sig = params[5]
        self._finalcount = (self._icount - self._clones) + (self._clones * self._cloneamount)
        if self._finalcount <= self._clones * self._cloneamount \
                and all(x >= 0 for x in (self._icount, self._clones, self._cloneamount)):
            raise ValueError('Error: Total Output Polgyons < Total Desired Clones!')
        self.polynames = '{0}, Generate Polygons with nrfinal method'.format(None)

    @property
    def cloneamount(self):
        """frequency of reoccuring (n,r)"""
        return self._cloneamount

    @cloneamount.setter
    def cloneamount(self, cloneamount):
        params = pm.check_parameters(icount=self._icount, clones=self._clones, cloneamount=cloneamount,
                                     siderange=self._siderange, radrange=self._radrange, sig=self._sig)
        self._icount = params[0]
        self._clones = params[1]
        self._cloneamount = params[2]
        self._siderange = params[3]
        self._radrange = params[4]
        self._sig = params[5]
        self._finalcount = (self._icount - self._clones) + (self._clones * self._cloneamount)
        # if self._finalcount <= self._clones * self._cloneamount and all(x >= 0 for x in (self._icount, self._clones,
        #                                                                                  self._cloneamount)):
        #     raise ValueError('Error: Total Output Polgyons < Total Desired Clones!')
        self.polynames = '{0}, Generate Polygons with nrfinal method'.format(None)

    @property
    def finalcount(self):
        """Total count of last generated Poly(n,r)"""
        return self._finalcount

    @property
    def siderange(self):
        """(x,y] interval range for side sampling"""
        return self._siderange

    @siderange.setter
    def siderange(self, siderange):
        params = pm.check_parameters(icount=self._icount, clones=self._clones, cloneamount=self._cloneamount,
                                     siderange=siderange, radrange=self._radrange, sig=self._sig)
        self._icount = params[0]
        self._clones = params[1]
        self._cloneamount = params[2]
        self._siderange = params[3]
        self._radrange = params[4]
        self._sig = params[5]
        # self._finalcount = (self._icount - self._clones) + (self._clones * self._cloneamount)
        # if self._finalcount <= self._clones * self._cloneamount and all(x >= 0 for x in (self._icount, self._clones,
        #                                                                                  self._cloneamount)):
        #     raise ValueError('Error: Total Output Polgyons < Total Desired Clones!')
        self.polynames = '{0}, Generate Polygons with nrfinal method'.format(None)

    @property
    def radrange(self):
        """(x,y] interval range of radius sampling"""
        return self._radrange

    @radrange.setter
    def radrange(self, radrange):
        params = pm.check_parameters(icount=self._icount, clones=self._clones, cloneamount=self._cloneamount,
                                     siderange=self._siderange, radrange=radrange, sig=self._sig)
        self._icount = params[0]
        self._clones = params[1]
        self._cloneamount = params[2]
        self._siderange = params[3]
        self._radrange = params[4]
        self._sig = params[5]
        # self._finalcount = (self._icount - self._clones) + (self._clones * self._cloneamount)
        # if self._finalcount <= self._clones * self._cloneamount and all(x >= 0 for x in (self._icount, self._clones,
        #                                                                                  self._cloneamount)):
        #     raise ValueError('Error: Total Output Polgyons < Total Desired Clones!')
        self.polynames = '{0}, Generate Polygons with nrfinal method'.format(None)

    @property
    def sig(self):
        """"floating point precision for radrange (x,y]"""
        return self._sig

    @sig.setter
    def sig(self, sig):
        params = pm.check_parameters(icount=self._icount, clones=self._clones, cloneamount=self._cloneamount,
                                     siderange=self._siderange, radrange=self._radrange, sig=sig)
        self._icount = params[0]
        self._clones = params[1]
        self._cloneamount = params[2]
        self._siderange = params[3]
        self._radrange = params[4]
        self._sig = params[5]
        # self._finalcount = (self._icount - self._clones) + (self._clones * self._cloneamount)
        # if self._finalcount <= self._clones * self._cloneamount and all(x >= 0 for x in (self._icount, self._clones,
        #                                                                                  self._cloneamount)):
        #     raise ValueError('Error: Total Output Polgyons < Total Desired Clones!')
        self.polynames = '{0}, Generate Polygons with nrfinal method'.format(None)

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

    def nrfinal(self):
        """ nrfinal generates instances of Poly(n,r) objects from specified parameters"""
        # Unique n list + Unique r list of length icount
        # lists are mutable data structures
        # so use deepcopy (copy is a shallow copy and thus is a pass by reference)
        # deep copy is a pass by value instantiating a new list

        nrvalslist = list(zip(sorted(self.sample_ints, reverse=True),
                              sorted(self.sample_floats, reverse=True)))
        # print('Initial Unique Values:', len(nrvalslist), nrvalslist)

        nrdups = deepcopy(nrvalslist[0:self._clones] * self._cloneamount)
        # print('Clones To Append:', len(nrdups), nrdups)

        nrremainder = deepcopy(nrvalslist[self._clones:])
        # print('Remaining Unique Values:', len(nrremainder) , nrremainder)

        finallist = deepcopy(nrdups + nrremainder)

        # print(finallist)

        # print('Final Values of (n,r) for Poly Generation:', len(finallist), finallist)

        # print('POLYGON CLASS TESTING:')

        name = tuple(('poly{0}'.format(n)) for n in range(101, 101+self._finalcount))
        # print('Newly Created Object Names:', len(name), name)

        # polylist instantiates Poly objects
        polylist = [pp.Poly(n, r) for n, r in finallist]
        polydict = OrderedDict(zip(name, polylist))

        self.polydict = polydict

        globals().update(polydict)

        self.finallist = len(finallist)
        """ self.polynames = list of names for newly created Poly(n,r) objects """
        self.polynames = name
        return """Process Complete"""

    @property
    def allcalc(self):
        """Calculates all properties for each instance of Poly(n,r)"""
        self.nrfinal()
        final_allcalc = []
        for v in self.polynames:
            final_allcalc.append((v,
                                  'Side Count =', eval('{0}.side_count'. format(v)),
                                  'Circumradius =', round(eval('{0}.circumradius'. format(v)), self._sig),
                                  'Vertex Count =', eval('{0}.vertex_count'. format(v)),
                                  'Perimeter =', round(eval('{0}.perimeter'. format(v)), self._sig),
                                  'Apothem =', round(eval('{0}.apothem'. format(v)), self._sig),
                                  'Interior Angle =', round(eval('{0}.interior_angle'. format(v)), self._sig),
                                  'Edge Length =', round(eval('{0}.edge_length'. format(v)), self._sig),
                                  'Area =', round(eval('{0}.area'. format(v)), self._sig)
                                  ))

        return final_allcalc

    @property
    def sidevalues(self):
        """Returns side counts for each instance of Poly(n,r)"""
        self.nrfinal()
        final_sidevalues = []
        for v in self.polynames:
            final_sidevalues.append((v,
                                     'Side Count =', eval('{0}.side_count'. format(v))))
        return final_sidevalues

    @property
    def circumradiusvalues(self):
        """Returns circumradius for each instance of Poly(n,r)"""
        self.nrfinal()
        final_circumradiusvalues = []
        for v in self.polynames:
            final_circumradiusvalues.append((v, 'Circumradius =', eval('{0}.circumradius'. format(v))))
        return final_circumradiusvalues

    @property
    def vertexcalc(self):
        """Returns vertex count for each instance of Poly(n,r)"""
        self.nrfinal()
        final_vertexcalc = []
        for v in self.polynames:
            final_vertexcalc.append((v, 'Vertex Count =', eval('{0}.vertex_count'. format(v))))
        return final_vertexcalc

    @property
    def perimetercalc(self):
        """Returns caculated perimeter for each instance of Poly(n,r)"""
        self.nrfinal()
        final_perimetercalc = []
        for v in self.polynames:
            final_perimetercalc.append((v, 'Perimeter =', eval('{0}.perimeter'. format(v))))
        return final_perimetercalc

    @property
    def apothemcalc(self):
        """Returns caculated apothem for each instance of Poly(n,r)"""
        self.nrfinal()
        final_apothemcalc = []
        for v in self.polynames:
            final_apothemcalc.append((v, 'Apothem =', eval('{0}.apothem'. format(v))))
        return final_apothemcalc

    @property
    def interioranglecalc(self):
        """Returns caculated interior angle for each instance of Poly(n,r)"""
        self.nrfinal()
        final_angle = []
        for v in self.polynames:
            final_angle.append((v, 'Interior Angle =', eval('{0}.interior_angle'. format(v))))
        return final_angle

    @property
    def edgelengthcalc(self):
        """Returns caculated side length for each instance of Poly(n,r)"""
        self.nrfinal()
        final_edgelengths = []
        for v in self.polynames:
            final_edgelengths.append((v, 'Edge Length =', eval('{0}.edge_length'. format(v))))
        return final_edgelengths

    @property
    def areacalc(self):
        """Returns calculated area for each instance of Poly(n,r)"""
        final_areas = []
        self.nrfinal()
        for v in self.polynames:
            final_areas.append((v, 'Area =', eval('{0}.area'. format(v))))
        return final_areas

    @property
    def instancerepr(self):
        """Returns each instance representation of Poly(n,r):"""
        self.nrfinal()
        finalrepr = []
        for v in self.polynames:
            finalrepr.append((v, '=', eval('{0}'. format(v))))
        return finalrepr

    def __len__(self):
        return self.finalcount

    def __repr__(self):
        return 'PolyFactory(icount={0},clones={1},cloneamount={2},siderange={3},radrange={4},sig={5})'\
            .format(self._icount,
                    self._clones,
                    self._cloneamount,
                    self._siderange,
                    self._radrange,
                    self._sig)

