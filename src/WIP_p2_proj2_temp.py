import math
from fractions import Fraction
from decimal import Decimal
from collections import OrderedDict


class NrsGlobalCache(OrderedDict):
    """This is a global nested dictionary for {(n,r,sig):calculated_properties:value}
        NrsGlobalCache= {(n,r,sig):
                          {interior_angle: value,
                           edge_length: value,
                           apothem: value,
                           area: value,
                           perimeter: value}
                        }
    """

    _instance = None

    @staticmethod
    def get_instance():
        """Static access method allows multiple handles for the same instance."""
        if NrsGlobalCache._instance is None:
            NrsGlobalCache()
        return NrsGlobalCache._instance

    def __init__(self):
        """Virtually private constructor."""
        if NrsGlobalCache._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            NrsGlobalCache._instance = self
            super().__init__()
            # self._cache = OrderedDict(dict())
            self._cache_limit = 100
            self._cache_size = len(self.keys())

    @property
    def cache_size(self):
        # current size of the cache
        return len(self.keys())

    # @cache_size.setter
    # def cache_size(self, length):
    #     return length

    @property
    def cache_limit(self):
        # maximum cache size default = 100
        return self._cache_limit

    @cache_limit.setter
    def cache_limit(self, limit):
        if self.cache_size > limit:
            while self.cache_size > (limit):
                # last=True -> FIFO remove the oldest items in the cache
                self.popitem(last=False)
                # self.cache_size(len(self.keys()))
                # set maximum cache size
        self._cache_limit = limit
        # return self._cache_limit

    @property
    def key_view(self):
        # view cached (n,r,Sig) keys
        return list(self.keys())

    def __missing__(self, key):
        # if key in self.keys():
        #     self.pop(key)
        val = self[key] = {}
        return val

    def cache_access(self, key, calc_prop, value):
        if key in self.keys():
            olditem = self.pop(key)
            newitem = {(str(calc_prop)): value}
            olditem.update(newitem)
            self.update({key: olditem})
        elif self.cache_size == self.cache_limit:
            self.popitem(last=False)
            self[key][calc_prop] = value
        else:
            self[key][calc_prop] = value

    def __repr__(self):
        return 'NrsGlobalCache()'

    #         # del self[key]
    #     OrderedDict.__setitem__(self, key, value)
    #     # let calc_prop be a dictionary {}
    #     super().__setitem__()
    #     self[key][calc_prop] = [value]
    #     # if self.cache_size > self.cache_limit:
    #     while self.cache_size > self.cache_limit:
    #         # last=True -> FIFO remove the oldest items in the cache
    #         self.popitem(last=False)
    #

    # def __getitem__(self, key, calc_prop, value):
    #     # return all calculated properties for a given (n,r,Sig) key
    #     # super(NrsGlobalCache, self).__getitem__(key, value, calc_prop)
    #     if value is None:
    #         return self[key]
    #     # return specific calculated property for a given (n,r,Sig) key
    #     else:
    #         return self[key][calc_prop]


class Poly:
    # These are temp default values to pass into polycheck(n,r,sig) / __init__:
    n = None
    r = None
    sig = 3

    def __init__(self, n=n, r=r, sig=sig):

        # These are temp variables to pass into polycheck()
        self.n = n
        self.r = r
        self.sig = sig
        # if (n,r,sig) are valid, this is the starting state:
        if Poly.polycheck():

            self._n = int(n) if self.n else None
            self._r = float(r) if self.r else None
            self._sig = self.sig if self.sig else None
            # Calculated Properties Start as None:
            self._perimeter = None
            self._area = None
            self._apothem = None
            self._edge_length = None
            self._interior_angle = None

        # query global dictionary if (n,r,sig) have been assigned:
        if self.nrskey:
            NrsGlobalCache[self.nrskey]['perimeter']
            NrsGlobalCache[self.nrskey]['area']
            NrsGlobalCache[self.nrskey]['apothem']
            NrsGlobalCache[self.nrskey]['edge_length']
            NrsGlobalCache[self.nrskey]['interior_ange']

    @classmethod
    def polycheck(n=n,r=r,sig=sig):
        ptype = (int, float, Decimal, Fraction)

        if n:
            if not (isinstance(n, ptype) and float(n).is_integer()):
                raise TypeError('Sides (n) = positive integer type Int/Float/Decimal/Fraction only')
            if n < 3:
                raise ValueError('At least 3 sides required')
        if r:
            if not (isinstance(r, ptype) and r > 0):
                raise TypeError('r = Positive Int/Float/Decimal/Fraction only')
        if sig:
            if not (isinstance(sig, int) and sig > 0):
                raise TypeError('Significant Digits (sig) must be of positive integer type only')

        return True

    def __repr__(self):
        if all(v for v in (self.n, self.r, self.sig)):
            if float(self._r).is_integer():
                return 'Poly({0},{1},{2})'.format(self._n, int(self._r), self._sig)

        return 'Poly({0},{1},{2})'.format(self._n, self._r, self._sig)

    # math constants Pi etc
    Pi = math.pi
    abs_tolerance = .00001


    # global dictionary cache of (n,r,sig) key
    @property
    def nrskey(self):
        if any((_ is None for _ in (self._n, self._r, self._sig))):
            return False
        return self._n, self._r, self._sig

    # vertex_count = side_count....
    @property
    def vertex_count(self):
        return self._n

    @property
    def side_count(self):
        return self._n

    # If side count changes, reset all calculated properties:
    @side_count.setter
    def side_count(self, n):
        self.n = n
        if self.polycheck():
            print('Side Count Set')
            self._n = n
            self._perimeter = None
            self._area = None
            self._apothem = None
            self._edge_length = None
            self._interior_angle = None

    @property
    def circumradius(self):
        return self._r

    # If radius changes, reset all calculated properties:
    @circumradius.setter
    def circumradius(self, r):
            if self.polycheck():
                print('Radius Set')
                self._r = r
                self._perimeter = None
                self._area = None
                self._apothem = None
                self._edge_length = None
                self._interior_angle = None
                return self._r

    @property
    def sigvalue(self):
        return self._sig

    @sigvalue.setter
    def sigvalue(self, sig):
        if self.polycheck(sig):
            print('Sig Value Set')
            self._sig = sig
            return self._sig

    @property
    def interior_angle(self):
        if self._interior_angle is None:
            if all((_ is not None for _ in (self._n, self._sig))):
                print('Calculating interior_angle...')
                self._interior_angle = round((self._n - 2) * (180 / self._n), self._sig)
        return self._interior_angle

    @property
    def edge_length(self):
        if self._edge_length is None:
            if all(_ is not None for _ in (self._r, self._n, self._sig)):
                print('Calculating edge_length...')
                self._edge_length = round(2 * self._r * math.sin(self.Pi / self._n), self._sig)
        return self._edge_length

    @property
    def apothem(self):
        if self._apothem is None:
            if all((_ is not None for _ in (self._n, self._r, self._sig))):
                print('Calculating Apothem...')
                self._apothem = round(self._r * (math.cos(self.Pi / self._n)), self._sig)
        return self._apothem

    @property
    def area(self):
        if self._area is None:
            if all((_ is not None for _ in (self._n, self._edge_length, self._apothem, self._sig))):
                print('Calculating Area...')
                self._area = round(.5 * self._n * self.edge_length * self.apothem, self._sig)
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            if all((_ is not None for _ in (self._n, self._r, self._sig))):
                print('Calculating Perimeter...')
                self._perimeter = round(self._n * self.edge_length, self._sig)
        return self._perimeter

    # Calculate all properties...
    @property
    def calcproperties(self):
        print(
            'Current Properties:', '\n',
            'Side Count:', self.side_count,'\n',
            'Cirumradius:', self.circumradius, '\n',
            'Vertex Count:', self.n, '\n',
            'Perimeter:', self.perimeter,'\n',
            'Area:', self.area,'\n',
            'Apothem:', self.apothem,'\n',
            'Edge Length:', self.edge_length,'\n',
            'Interior_angle:', self.interior_angle,'\n',
            'Sig Value:', self.sig
            )
        return 'All Properties Calculated'


    # def __setitem__(self, n=None, r=None, sig=None):
    #     n = n if n is not None else self._n
    #     r = r if r is not None else self._r
    #     sig = sig if sig is not None else self._sig
    #
    #     if not (isinstance(n, self._ptype) and float(n).is_integer()):
    #         raise TypeError('Sides (n) = positive integer type Int/Float/Decimal/Fraction only')
    #
    #     if n < 3:
    #         raise ValueError('At least 3 sides required')
    #
    #     if not (isinstance(r, self._ptype) and r > 0):
    #         raise TypeError('r = Positive Int/Float/Decimal/Fraction only')
    #
    #     if not isinstance(sig, int):
    #         raise TypeError('Significant Digits (sig) must be of integer type only')
    #     if n:
    #         self._n = int(n)
    #     if r:
    #         self._r = float(r)
    #     if sig:
    #         self._sig = sig
    #
    #     return self._n

    # adding it as self vs self.__class__ explained later (prob meta-class checking)
    # self.__class__ allows for non-hard-coded of names of objects/instances
    # remember isinstance(other, self)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._n == other._n and self._r == other._r
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.vertex_count > other.vertex_count
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, self.__class__):
            return self.vertex_count >= other.vertex_count
        else:
            return NotImplemented

    def equal_area(self, other):
        if math.isclose(self.area, other.area,
                        rel_tol=self.abs_tolerance,
                        abs_tol=self.abs_tolerance):
            return True
        else:
            return False

    def equal_perimeter(self, other):
        if math.isclose(self.perimeter, other.perimeter,
                        rel_tol=self.abs_tolerance,
                        abs_tol=self.abs_tolerance):
            return True
        else:
            return False


# TODO Finish Polygons Iterator __next__(method)
# class Polygons:
#     """Returns an iterable of generated Poly() objects from m(sides) down to len(m-2) sides"""
#     def __init__(self, m, r):
#
#         ptype = (int, float, Decimal, Fraction)
#
#         if not (isinstance(m, ptype) and float(m).is_integer()):
#             raise TypeError('Sides (m) = positive integer type Int/Float/Decimal/Fraction only')
#         if m < 3:
#             raise ValueError('At least 3 sides required')
#         if not (isinstance(r, ptype) and r > 0):
#             raise TypeError('r = Positive Int/Float/Decimal/Fraction only')
#
#         self._m = int(m)
#         self._r = float(r)
#         self._polygons = [Poly(m, self._r) for m in range(3, m+1)]
#         self._ptype = ptype
#
#     def __len__(self):
#         return self._m - 2
#
#     def __repr__(self):
#         if self._r.is_integer():
#             return 'Polygons({0},{1})'.format(self._m, int(self._r))
#         return 'Polygons({0},{1})'.format(self._m, self._r)
#
#     def __getitem__(self, s):
#         return self._polygons[s]
#
#     def __setitem__(self, m, r):
#
#         if not (isinstance(m, self._ptype) and float(m).is_integer()):
#             raise TypeError('Sides (m) = positive integer type Int/Float/Decimal/Fraction only')
#         if m < 3:
#             raise ValueError('At least 3 sides required')
#         if not (isinstance(r, self._ptype) and r > 0):
#             raise TypeError('r = Positive Int/Float/Decimal/Fraction only')
#
#         self._m = int(m)
#         self._r = float(r)
#         self._polygons = [Poly(m, self._r) for m in range(3, m+1)]
#
#     @property
#     def max_efficiency(self):
#         sorted_polygons = sorted(self._polygons,
#                                  key=lambda i: i.area/i.perimeter,
#                                  reverse=True)
#         print('Max Efficeny polygon:', sorted_polygons[0])
#         return sorted_polygons[0].area / sorted_polygons[0].perimeter

# TODO nrsdictglobal maybe in a seperate file as a seperate global cache
# # https://www.calculatorsoup.com/calculators/geometry-plane/polygon.php
# # UNIT TESTING #######################################################
# # ####################################################################
# # ####################################################################
#
#
# class TestPolygon:
#     def __init__(self, pcount):
#
#         # pcount generates at least 6 polygons for our test case
#
#         if not isinstance(pcount, int):
#             raise TypeError('pcount (polygons to generate) must be of type(int)')
#         if pcount < 6:
#             raise ValueError('at least 6 polygons must be generated')
#         self._pcount = pcount
#
#     def __repr__(self):
#         return 'TestPolygon({0})'.format(self._pcount)
#
#     @property
#     def polycount(self):
#         return self._pcount
#
#     def __setitem__(self, pcount):
#         if not isinstance(pcount, int):
#             raise TypeError('pcount (polygons to generate) must be of type(int)')
#         if pcount < 6:
#             raise ValueError('at least 6 polygons must be generated')
#         self._pcount = pcount
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#     def sample_floats(low, high, k=1):
#         """ Return a k-length list of unique random floats
#             in the range of low <= x <= high
#         """
#         result = []
#         seen = set()
#         for i in range(k):
#             x = round(uniform(low, high), 2)
#             while x in seen:
#                 x = round(uniform(low, high), 2)
#             seen.add(x)
#             result.append(x)
#         return (result)
#
#     def sample_ints(low, high, k=1):
#         """ Return a k-length list of unique random integers
#             in the range of low <= x <= high
#         """
#         result = []
#         seen = set()
#         for i in range(k):
#             x = randint(low, high)
#             while x in seen:
#                 x = randint(low, high)
#             seen.add(x)
#             result.append(x)
#         return result
#
#     # lists are mutable data structures
#     # so use deepcopy (copy is a shallow copy and thus is a pass by reference)
#     # deep copy is a pass by value instantiating a new list
#
#
#
#     nrvalslist = list(zip(sorted(sample_ints(3, 100, pcount), reverse=True),
#                           sorted(sample_floats(1, 100, pcount), reverse=True)))
#
#     print('nrvalslist', nrvalslist)
#
#     # we want 2 duplicate items
#     amountdup = 2
#     instances = 3
#
#     nrdups = deepcopy(nrvalslist[0:amountdup] * instances)
#     print('nrdups', nrdups)
#
#     nrRemainder = deepcopy(nrvalslist[amountdup:])
#     print('nrRemainder', nrRemainder)
#
#     nrFinal = deepcopy(nrdups + nrRemainder)
#     print('nrFinal', len(nrFinal), nrFinal)
#
#     assert (id(nrvalslist) != id(nrdups) != id(nrRemainder) != id(nrFinal))
#     print('unique list mem ids established')
#
#
#     print('POLYGON CLASS TESTING:')
#
#     # n = [i for i in range(3, 13)]
#     # r = [i for i in range(13, 23)]
#     #
#     # nr = tuple(zip(n, r))
#
#     name = tuple(('poly{0}'.format(n)) for n in range(100, 101+len(nrFinal)))
#
#     # same as the for loop below
#     polylist = [Poly(n, r) for n, r in nrFinal]
#
#     test_polygon.polydict = OrderedDict(zip(name, polylist))
#
#     globals().update(test_polygon.polydict)
#
#     for k, v in test_polygon.polydict.items():
#         print(k, v,
#               'perimeter =', v.perimeter,
#               'apothem =', v.apothem,
#               'interior angle =', v.interior_angle,
#               'edge_length =', v.edge_length,
#               'area =', v.area
#               )
#
#     # unit test: __repr__
#     assert str(poly100) == 'Poly(3,13)', 'actual:{0}'.format(poly100)
#
#     # Unit Test: Radius repr float vs int
#     polyA = Poly(5, 13.3)
#     polyB = Poly(5, 13)
#     print(polyA, polyB)
#
#     # unite test: rich comparisons
#     assert poly101 < poly104, 'actual:{0}'.format(poly101 < poly104)
#     assert poly106 > poly103, 'actual:{0}'.format(poly106 > poly103)
#     assert poly103 >= poly102, 'actual:{0}'.format(poly103 >= poly102)
#     assert poly104 >= poly101, 'actual:{0}'.format(poly104 >= poly101)
#     assert poly107 != poly108, 'actual:{0}'.format(poly107 != poly108)
#
#     # specific value test
#     poly9 = Poly(6, 2)
#     poly10 = Poly(4, 1)
#     poly11 = Poly(4, 1)
#     poly12 = Poly(4, 1)
#     poly13 = Poly(1000, 1)
#
#     assert math.isclose(poly9.apothem, 1.732, rel_tol=.0001, abs_tol=.0001)
#     assert math.isclose(poly9.area, 10.392, rel_tol=.0001, abs_tol=.0001)
#     assert math.isclose(poly9.perimeter, 12, rel_tol=.0001, abs_tol=.0001)
#     assert math.isclose(poly9.interior_angle, 120, rel_tol=.0001, abs_tol=.0001)
#     assert math.isclose(poly9.edge_length, 2, rel_tol=.0001, abs_tol=.0001)
#     assert math.isclose(poly10.area, 2, rel_tol=.0001, abs_tol=.0001)
#     assert poly10.equal_area(poly11)
#     assert poly10.equal_perimeter(poly11)
#     assert math.isclose(poly12.edge_length, math.sqrt(2), rel_tol=.0001, abs_tol=.0001)
#     if math.isclose(poly13.area, math.pi, rel_tol=.0001, abs_tol=.0001):
#         print('Pi Test Passed')
#     # set item and recalculate of poly1
#     poly1 = Poly(4, 5)
#     poly1.__setitem__(10, 13.1)
#
#     # poly1 list properties
#     print('Poly1', poly1, poly1.calcproperties)
#
#
# def test_polygons():
#     # Unit Tests for Polygons Class
#     print('POLYGONS CLASS TESTING:')
#
#     polys = Polygons(10, 6.35)
#     polys2 = Polygons(500, 1)
#
#     # Polygons Class __repr__ test
#     assert str(polys) == 'Polygons(10,6.35)', '{0}'.format(polys)
#
#     # test the max efficacy formula
#     assert max([p.area/p.perimeter for p in polys]) == polys.max_efficiency
#
#     print('Iterable Type Check:')
#
#     print('get the 2nd item in polys........{0}'.format(polys[3]))
#     print('get the third item polys2........{0}'.format(polys2[4]))
#
#     if math.isclose(polys2[-1].area, math.pi, abs_tol=.0001, rel_tol=.0001):
#         print('Polygons Class Pi test passed')
#
#     print('Polygons Class setitem method testing...')
#
#     polys2 = Polygons(4, 20)
#     print('polys2', polys2)
#
#     print('polys2 changing sides and radius...')
#     if not polys2.__setitem__(400, 1):
#         print('polys2', polys2)
#         print('Polygons Class setitem method working')
#     print('Unit Testing Complete')
#
#
# test_polygon()
# test_polygons()
# gg = Poly(4,4,1)
# print(gg)

# gg.side_count = 100
# print(gg)



# print(gg.perimeter)
# print(gg.apothem)
# print(gg.edge_length)


# print('Retriving cache values...')
# print(gg.apothem)
# print(gg.edge_length)


# g3 = Poly()

# print(type(g3))

# g2 = Poly()
# print(g2)
# print(g2.nrskey)
# print(g2)
# print(g2.calcproperties)
# print(g2.calcproperties)
#
# g2.circumradius = None
# print(g2.calcproperties)
#
# g2.circumradius = 21312
# print(g2)
# g2.side_count = 12
# print(g2)
# g2.sigvalue = 0
# print(g2)
