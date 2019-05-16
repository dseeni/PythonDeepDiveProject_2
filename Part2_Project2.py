#Part2_Project2.py
import math
from fractions import Fraction
from decimal import Decimal
from collections import OrderedDict

class Poly:
    def __init__(self, n, r):

        # set private variables
        # check against ptype tuple data struct

        ptype = (int, float, Decimal, Fraction)

        if not (isinstance(n, ptype) and float(n).is_integer()):
            raise TypeError('Sides (n) = positive integer type Int/Float/Decimal/Fraction only')

        if n < 3:
            raise ValueError('At least 3 sides required')

        if not (isinstance(r, ptype) and r > 0):
            raise TypeError('r = Positive Int/Float/Decimal/Fraction only')

        self._n = int(n)
        self._r = float(r)
        self._ptype = (int, float, Decimal, Fraction)

    def __repr__(self):
        if self._r.is_integer():
            return 'Poly({0},{1})'.format(self._n, int(self._r))
        return 'Poly({0},{1})'.format(self._n, self._r)

    # math constants Pi etc
    Pi = math.pi
    abs_tolerance = .00001

    @property
    def vertex_count(self):
        return self._n

    @property
    def side_count(self):
        return self._n

    @property
    def circumradius(self):
        return self._r

    @property
    def interior_angle(self):
        return (self._n - 2) * (180 / self._n)

    @property
    def edge_length(self):
        return 2 * self._r * math.sin(self.Pi / self._n)

    @property
    def apothem(self):
        return self._r * (math.cos(self.Pi / self._n))

    @property
    def area(self):
        return .5 * self._n * self.edge_length * self.apothem

    @property
    def perimeter(self):
        return self._n * self.edge_length

    @property
    def listproperties(self):
        return (
            self.perimeter,
            self.area,
            self.apothem,
            self.edge_length,
            self.circumradius,
            self.interior_angle)

    def __setitem__(self, n, r):

            if not (isinstance(n, self._ptype) and float(n).is_integer()):
                raise TypeError('Sides (n) = positive integer type Int/Float/Decimal/Fraction only')

            if n < 3:
                raise ValueError('At least 3 sides required')

            if not (isinstance(r, self._ptype) and r > 0):
                raise TypeError('r = Positive Int/Float/Decimal/Fraction only')

            self._n = int(n)
            self._r = float(r)

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


class Polygons:
    def __init__(self, m, r):

        ptype = (int, float, Decimal, Fraction)

        if not (isinstance(m, ptype) and float(m).is_integer()):
            raise TypeError('Sides (m) = positive integer type Int/Float/Decimal/Fraction only')
        if m < 3:
            raise ValueError('At least 3 sides required')
        if not (isinstance(r, ptype) and r > 0):
            raise TypeError('r = Positive Int/Float/Decimal/Fraction only')

        self._m = int(m)
        self._r = float(r)
        self._polygons = [Poly(m, self._r) for m in range(3, m+1)]
        self._ptype = ptype

    def __len__(self):
        return self._m - 2

    def __repr__(self):
        if self._r.is_integer():
            return 'Polygons({0},{1})'.format(self._m, int(self._r))
        return 'Polygons({0},{1})'.format(self._m, self._r)

    def __getitem__(self, s):
        return self._polygons[s]

    def __setitem__(self, m, r):

        if not (isinstance(m, self._ptype) and float(m).is_integer()):
            raise TypeError('Sides (m) = positive integer type Int/Float/Decimal/Fraction only')
        if m < 3:
            raise ValueError('At least 3 sides required')
        if not (isinstance(r, self._ptype) and r > 0):
            raise TypeError('r = Positive Int/Float/Decimal/Fraction only')

        self._m = int(m)
        self._r = float(r)
        self._polygons = [Poly(m, self._r) for m in range(3, m+1)]

    @property
    def max_efficiency(self):
        sorted_polygons = sorted(self._polygons,
                                 key=lambda i: i.area/i.perimeter,
                                 reverse=True)
        print('Max Efficeny polygon:', sorted_polygons[0])
        return sorted_polygons[0].area / sorted_polygons[0].perimeter


# https://www.calculatorsoup.com/calculators/geometry-plane/polygon.php
# UNIT TESTING #######################################################
# ####################################################################
# ####################################################################

def test_polygon():

    print('POLYGON CLASS TESTING:')

    n = [i for i in range(3, 13)]
    r = [i for i in range(13, 23)]

    nr = tuple(zip(n, r))

    name = tuple(('poly{0}'.format(n)) for n in range(100, 100+len(n)))

    # same as the for loop below
    polylist = [Poly(n, r) for n, r in nr]

    test_polygon.polydict = OrderedDict(zip(name, polylist))

    globals().update(test_polygon.polydict)

    for k, v in test_polygon.polydict.items():
        print(k, v,
              'perimeter =', v.perimeter,
              'apothem =', v.apothem,
              'interior angle =', v.interior_angle,
              'edge_length =', v.edge_length,
              'area =', v.area
              )

    # unit test: __repr__
    assert str(poly100) == 'Poly(3,13)', 'actual:{0}'.format(poly100)

    # Unit Test: Radius repr float vs int
    polyA = Poly(5, 13.3)
    polyB = Poly(5, 13)
    print(polyA, polyB)

    # unite test: rich comparisons
    assert poly101 < poly104, 'actual:{0}'.format(poly101 < poly104)
    assert poly106 > poly103, 'actual:{0}'.format(poly106 > poly103)
    assert poly103 >= poly102, 'actual:{0}'.format(poly103 >= poly102)
    assert poly104 >= poly101, 'actual:{0}'.format(poly104 >= poly101)
    assert poly107 != poly108, 'actual:{0}'.format(poly107 != poly108)

    # specific value test
    poly9 = Poly(6, 2)
    poly10 = Poly(4, 1)
    poly11 = Poly(4, 1)
    poly12 = Poly(4, 1)
    poly13 = Poly(1000, 1)

    assert math.isclose(poly9.apothem, 1.732, rel_tol=.0001, abs_tol=.0001)
    assert math.isclose(poly9.area, 10.392, rel_tol=.0001, abs_tol=.0001)
    assert math.isclose(poly9.perimeter, 12, rel_tol=.0001, abs_tol=.0001)
    assert math.isclose(poly9.interior_angle, 120, rel_tol=.0001, abs_tol=.0001)
    assert math.isclose(poly9.edge_length, 2, rel_tol=.0001, abs_tol=.0001)
    assert math.isclose(poly10.area, 2, rel_tol=.0001, abs_tol=.0001)
    assert poly10.equal_area(poly11)
    assert poly10.equal_perimeter(poly11)
    assert math.isclose(poly12.edge_length, math.sqrt(2), rel_tol=.0001, abs_tol=.0001)
    if math.isclose(poly13.area, math.pi, rel_tol=.0001, abs_tol=.0001):
        print('Pi Test Passed')
    # set item and recalculate of poly1
    poly1 = Poly(4, 5)
    poly1.__setitem__(10, 13.1)

    # poly1 list properties
    print('Poly1', poly1, poly1.listproperties)


def test_polygons():
    # Unit Tests for Polygons Class
    print('POLYGONS CLASS TESTING:')

    polys = Polygons(10, 6.35)
    polys2 = Polygons(500, 1)

    # Polygons Class __repr__ test
    assert str(polys) == 'Polygons(10,6.35)', '{0}'.format(polys)

    # test the max efficacy formula
    assert max([p.area/p.perimeter for p in polys]) == polys.max_efficiency

    print('Iterable Type Check:')

    print('get the 2nd item in polys........{0}'.format(polys[3]))
    print('get the third item polys2........{0}'.format(polys2[4]))

    if math.isclose(polys2[-1].area, math.pi, abs_tol=.0001, rel_tol=.0001):
        print('Polygons Class Pi test passed')

    print('Polygons Class setitem method testing...')

    polys2 = Polygons(4, 20)
    print('polys2', polys2)

    print('polys2 changing sides and radius...')
    if not polys2.__setitem__(400, 1):
        print('polys2', polys2)
        print('Polygons Class setitem method working')
    print('Unit Testing Complete')


test_polygon()
test_polygons()
