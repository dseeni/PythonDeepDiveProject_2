import math
from fractions import Fraction
from decimal import Decimal
from collections import OrderedDict


class NrsGlobalCache(OrderedDict):
    """This is a global nested dictionary for {(n,r):calculated_properties:value}
        NrsGlobalCache= {(n,r):
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

    @property
    def cache_size(self):
        # current size of the cache
        return len(self.keys())

    @property
    def cache_limit(self):
        # maximum cache size default = 100
        return self._cache_limit

    @cache_limit.setter
    def cache_limit(self, limit):
        if self.cache_size > limit:
            while self.cache_size > limit:
                # last=False -> FIFO removes the oldest items in the cache
                self.popitem(last=False)
        self._cache_limit = limit

    @property
    def key_view(self):
        # view cached (n,r) keys
        return list(self.keys())

    def __missing__(self, key):
        val = self[key] = {}
        return val

    def setter(self, key, calc_prop, value):
        if key in self.keys():
            olditem = self.pop(key)
            newitem = {(str(calc_prop)): value}
            olditem.update(newitem)
            self.update({key: olditem})
        else:
            self[key][calc_prop] = value
            if self.cache_size > self.cache_limit:
                self.popitem(last=False)
                self[key][calc_prop] = value

    def getter(self, key, calc_prop):
        if key in self.keys():
            pop = self.pop(key)
            for k, v in pop.items():
                self.setter(key, k, v)

        return self[key][calc_prop]
    
    def __repr__(self):
        return 'NrsGlobalCache()'


CacheGlobal = NrsGlobalCache()


class Poly:

    """
    Poly(n, r) is a mutable Polygon object with n sides and radius r
    Calculated Properties:
        - interior angle
        - side length
        - apothem
        - area
        - perimeter
    """
    def __init__(self, n=None, r=None):

        if Poly.polycheck(n, r):
            self._n = int(n) if n is not None else None
            self._r = float(r) if r is not None else None
            # Calculated Properties Start as None:
            self._perimeter = None
            self._area = None
            self._apothem = None
            self._edge_length = None
            self._interior_angle = None

    @staticmethod
    def polycheck(n=None, r=None):
        # ptype = acceptable types for (n,r)
        ptype = (int, float, Decimal, Fraction)

        if n is not None:
            if not (isinstance(n, ptype) and float(n).is_integer()):
                raise TypeError('Sides (n) = positive integer type Int/Float/Decimal/Fraction only')
            if n < 3:
                raise ValueError('At least 3 sides required')
        if r is not None:
            if not (isinstance(r, ptype) and r > 0):
                raise TypeError('r = Positive Int/Float/Decimal/Fraction only')
        
        return True

    def __repr__(self):
        if all(v is not None for v in (self._n, self._r)):
            if float(self._r).is_integer():
                return 'Poly({0},{1})'.format(self._n, int(self._r))

        return 'Poly({0},{1})'.format(self._n, self._r)

    # math constants Pi etc
    abs_tolerance = .00001
    Pi = math.pi

    # local dictionary cache of (n,r) key
    @property
    def nrkey(self):
        if any((_ is None for _ in (self._n, self._r))):
            return None
        return self._n, self._r

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
        if self.polycheck(n, None):
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
        if self.polycheck(None, r):
            # print('Radius Set')
            self._r = r
            # reset calculated properties
            self._perimeter = None
            self._area = None
            self._apothem = None
            self._edge_length = None
            self._interior_angle = None

    @property
    def interior_angle(self):
        if self._n is None:
            # Radius is not required for interior_angle
            raise ValueError('Assign missing n')

        def calc_interior_angle():
            # print('Calculating interior_angle...')
            self._interior_angle = (self._n - 2) * (180 / self._n)

        if self._interior_angle is None:
            # check CacheGlobal for exiting calculation
            if self._interior_angle is None and self.nrkey is not None:
                try:
                    self._interior_angle = CacheGlobal.getter(self.nrkey, 'interior_angle')
                    # print('Pinged CacheGlobal for interior_angle')
                except KeyError:
                    calc_interior_angle()
                    CacheGlobal.setter(self.nrkey, 'interior_angle', self._interior_angle)
                    # print('Stored caculated property in CacheGlobal')
            else:
                # just in case interior_angle is None but radius is also None so its not in cache...
                calc_interior_angle()

        # else:
            # print('Retrieving interior_angle')
        return self._interior_angle

    @property
    def edge_length(self):
        if any(_ is None for _ in (self._r, self._n)):
            raise ValueError('Assign missing n,r')
        if self._edge_length is None:
            try:
                self._edge_length = CacheGlobal.getter(self.nrkey, 'edge_length')
                # print('Pinged CacheGlobal for edge_length')
            except KeyError:
                # print('Calculating edge_length...')
                self._edge_length = (2 * self._r * math.sin(Poly.Pi / self._n))
                CacheGlobal.setter(self.nrkey, 'edge_length', self._edge_length)
                # print('Stored caculated property in CacheGlobal')
        # else:
            # print('Retrieving edge_length...')
        return self._edge_length

    @property
    def apothem(self):
        if any(_ is None for _ in (self._n, self._r)):
            raise ValueError('Assign missing n,r')
        if self._apothem is None:
            try:
                self._apothem = CacheGlobal[self.nrkey]['apothem']
                # print('Pinged CacheGlobal for apothem')
            except KeyError:
                # print('Calculating Apothem...')
                self._apothem = self._r * (math.cos(Poly.Pi / self._n))
                CacheGlobal.setter(self.nrkey, 'apothem', self._apothem)
                # print('Stored caculated property in CacheGlobal')
    # else:
        # print('Retrieving apothem...')
        return self._apothem

    @property
    def area(self):
        if any((_ is None for _ in (self._n, self._r))):
            raise ValueError('Assign missing n,r')
        if self._area is None:
            try:
                self._area = CacheGlobal[self.nrkey]['area']
                # print('Pinged CacheGlobal for area')
            except KeyError:
                # print('Calculating Area...')
                self._area = .5 * self._n * self.edge_length * self.apothem
                CacheGlobal.setter(self.nrkey, 'area', self._area)
                # print('Stored caculated property in CacheGlobal')
        # else:
            # print('Retrieving area...')
        return self._area

    @property
    def perimeter(self):
        if any((_ is None for _ in (self._n, self._r))):
            raise ValueError('Assign missing n,r')

        if self._perimeter is None:
            try:
                self._perimeter = CacheGlobal[self.nrkey]['perimeter']
                # print('Pinged CacheGlobal for perimeter')
            except KeyError:
                # print('Calculating Perimeter...')
                self._perimeter = self._n * self.edge_length
                CacheGlobal.setter(self.nrkey, 'perimeter', self._perimeter)
                # print('Stored caculated property in CacheGlobal')
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
                self.interior_angle]

    def __setitem__(self, n=None, r=None):
        if Poly.polycheck(n, r):
            n = n if n is not None else self._n
            r = r if r is not None else self._r

        if n:
            self._n = int(n)
        if r:
            self._r = float(r)

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
        # ptype = acceptable types for (n,r)
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
            self.polygons = [(m, self._r) for m in range(3, self._m + 1)]
            self._max_efficiency_polygon = None

    def __len__(self):
        return self._m - 2

    def __iter__(self):
        # print('Calling Polygons instance __iter__')
        return self.PolyIterator(self)

    @property
    def max_efficiency(self):
        if self._max_efficiency_polygon is None:
            polylist = [Poly(self.polygons[i][0], self.polygons[i][1]) for i in range(len(self.polygons))]
            sorted_polygons = sorted(polylist,
                                     key=lambda i: i.area/i.perimeter, reverse=True)
            self._max_efficiency_polygon = sorted_polygons[0]
        return self._max_efficiency_polygon

    def __repr__(self):
        if self._r.is_integer():
            return 'Polygons({0},{1})'.format(self._m, int(self._r))
        return 'Polygons({0},{1})'.format(self._m, self._r)

    class PolyIterator:
        def __init__(self, poly_obj):
            # poly_obj is the instance of Polygons iterable passed into the iterator
            # print('Calling PolyIterator __init__')
            self.poly_obj = poly_obj
            self._index = 0

        def __iter__(self):
            # print('Calling PolyIterator instance __iter__')
            return self

        def __next__(self):
            # print('Calling __next__')
            if self._index >= self.poly_obj.__len__():
                raise StopIteration
            else:
                item = Poly(self.poly_obj.polygons[self._index][0], self.poly_obj.polygons[self._index][1])
                self._index += 1
                return item


