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
            while self.cache_size > limit:
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


class Poly:

    def __init__(self, n=None, r=None, sig=3):

        if Poly.polycheck(n, r, sig):
            self._n = int(n) if n is not None else None
            self._r = float(r) if r is not None else None
            self._sig = sig if sig is not None else None
            # Calculated Properties Start as None:
            self._perimeter = None
            self._area = None
            self._apothem = None
            self._edge_length = None
            self._interior_angle = None

    @staticmethod
    def polycheck(n=None, r=None, sig=None):
        # ptype = acceptable types for (n,r,sig)
        ptype = (int, float, Decimal, Fraction)

        if n is not None:
            if not (isinstance(n, ptype) and float(n).is_integer()):
                raise TypeError('Sides (n) = positive integer type Int/Float/Decimal/Fraction only')
            if n < 3:
                raise ValueError('At least 3 sides required')
        if r is not None:
            if not (isinstance(r, ptype) and r > 0):
                raise TypeError('r = Positive Int/Float/Decimal/Fraction only')
        if sig is not None:
            if not (isinstance(sig, int) and sig > 0):
                raise TypeError('Significant Digits (sig) must be of positive integer type only')
        
        return True

    def __repr__(self):
        if all(v is not None for v in (self._n, self._r, self._sig)):
            if float(self._r).is_integer():
                return 'Poly({0},{1},{2})'.format(self._n, int(self._r), self._sig)

        return 'Poly({0},{1},{2})'.format(self._n, self._r, self._sig)

    # math constants Pi etc
    Pi = math.pi
    abs_tolerance = .00001

    # local dictionary cache of (n,r,sig) key
    @property
    def nrskey(self):
        if any((_ is None for _ in (self._n, self._r, self._sig))):
            raise KeyError("n,r,s values = None")
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
        if self.polycheck(n, None, None):
            # print('Side Count Set')
            self._n = n
            # reset calculated properties
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
        if self.polycheck(None, r, None):
            # print('Radius Set')
            self._r = r
            # reset calculated properties
            self._perimeter = None
            self._area = None
            self._apothem = None
            self._edge_length = None
            self._interior_angle = None

    @property
    def sig(self):
        return self._sig

    @sig.setter
    def sig(self, sig):
        if self.polycheck(None, None, sig):
            # print('Sig Value Set')
            self._sig = sig
            # reset calculated properties
            self._perimeter = None
            self._area = None
            self._apothem = None
            self._edge_length = None
            self._interior_angle = None

    @property
    def interior_angle(self):
        if self._interior_angle is None:
            if all((_ is not None for _ in (self._n, self._sig))):
                # print('Calculating interior_angle...')
                self._interior_angle = round((self._n - 2) * (180 / self._n), self._sig)
            else:
                raise ValueError('Assign missing n, sig values')
        # else:
        #     # print('Retrieving interior_angle...')
        return self._interior_angle

    @property
    def edge_length(self):
        if self._edge_length is None:
            if all(_ is not None for _ in (self._r, self._n, self._sig)):
                # print('Calculating edge_length...')
                self._edge_length = round(2 * self._r * math.sin(self.Pi / self._n), self._sig)
            else:
                raise ValueError('Assign missing n,r,sig values')
        # else:
        #     # print('Retrieving edge_length...')
        return self._edge_length

    @property
    def apothem(self):
        if self._apothem is None:
            if all((_ is not None for _ in (self._n, self._r, self._sig))):
                # print('Calculating Apothem...')
                self._apothem = round(self._r * (math.cos(self.Pi / self._n)), self._sig)
            else:
                raise ValueError('Assign missing n,r,sig values')
        # else:
        #     print('Retrieving apothem...')
        return self._apothem

    @property
    def area(self):
        if self._area is None:
            if self.edge_length and self.apothem:
                # print('Calculating Area...')
                self._area = round(.5 * self._n * self.edge_length * self.apothem, self._sig)
        # else:
        #     print('Retrieving area...')
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            if all((_ is not None for _ in (self._n, self._r, self._sig))):
                # print('Calculating Perimeter...')
                self._perimeter = round(self._n * self.edge_length, self._sig)
        # else:
        #     print('Retrieving perimeter...')
        return self._perimeter

    # Calculate all properties...
    # @property
    def calcproperties(self):
        return [self.side_count,
                self.circumradius,
                self.vertex_count,
                self.perimeter,
                self.area,
                self.apothem,
                self.edge_length,
                self.interior_angle,
                self.sig]

    def __setitem__(self, n=None, r=None, sig=None):
        if Poly.polycheck(n, r, sig):
            n = n if n is not None else self._n
            r = r if r is not None else self._r
            sig = sig if sig is not None else self._sig

        if n:
            self._n = int(n)
        if r:
            self._r = float(r)
        if sig:
            self._sig = sig

        return self._n

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
        if isinstance(other, self.__class__):
            if math.isclose(self.area, other.area,
                            rel_tol=self.abs_tolerance,
                            abs_tol=self.abs_tolerance):
                return True
            else:
                return False

    def equal_perimeter(self, other):
        if isinstance(other, self.__class__):
            if math.isclose(self.perimeter, other.perimeter,
                            rel_tol=self.abs_tolerance,
                            abs_tol=self.abs_tolerance):
                return True
            else:
                return False


class Polygons:
    """Returns an iterable of generated Poly() objects from m(sides) down to len(m-2) sides"""
    @staticmethod
    def polyscheck(m=None, r=None):
        # ptype = acceptable types for (n,r,sig)
        ptype = (int, float, Decimal, Fraction)

        if m is not None:
            if not (isinstance(m, ptype) and float(m).is_integer()):
                raise TypeError('Sides (n) = positive integer type Int/Float/Decimal/Fraction only')
            if m < 3:
                raise ValueError('At least 3 sides required')
        if r is not None:
            if not (isinstance(r, ptype) and r > 0):
                raise TypeError('r = Positive Int/Float/Decimal/Fraction only')
        return True

    def __init__(self, m, r):
        if Polygons.polyscheck(m, r):
            self._m = int(m)
            self._r = float(r)
            self._polygons = [(m, self._r) for m in range(3, self._m+1)]
            print(self._polygons)

    def __len__(self):
        return self._m - 2

    def __iter__(self):
        # print('Calling Polygons instance __iter__')
        return self.PolyIterator(self)

    @property
    def max_efficiency(self):
        polylist = [Poly(self._polygons[i][0], self._polygons[i][1]) for i in range(len(self._polygons))]
        for i in polylist:
            i.calcproperties()
        sorted_polygons = sorted(polylist,
                                 key=lambda i: i.area/i.perimeter,
                                 reverse=True)
        # print('Max Efficeny polygon:', sorted_polygons[0])
        return sorted_polygons[0].area / sorted_polygons[0].perimeter

    def __repr__(self):
        if self._r.is_integer():
            return 'Polygons({0},{1})'.format(self._m, int(self._r))
        return 'Polygons({0},{1})'.format(self._m, self._r)

    class PolyIterator:
        def __init__(self, poly_obj):
            # poly_obj is the instance of Polygons iterable passed into the iterator
            # print('Calling PolyIterator __init__')
            self._poly_obj = poly_obj
            self._index = 0

        def __iter__(self):
            # print('Calling PolyIterator instance __iter__')
            return self

        def __next__(self):
            # print('Calling __next__')
            if self._index >= self._poly_obj.__len__():
                raise StopIteration
            else:
                item = Poly(self._poly_obj._polygons[self._index][0], self._poly_obj._polygons[self._index][1])
                self._index += 1
                return item
