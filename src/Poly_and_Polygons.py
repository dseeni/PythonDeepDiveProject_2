import math
from fractions import Fraction
from decimal import Decimal

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

