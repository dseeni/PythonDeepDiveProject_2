from Scripts_PDD2_Project2 import Poly_and_Polygons as Pp
import math
from conftest import test_polys

globals().update(test_polys())
# https://www.oalculatorsoup.com/calculators/geometry-plane/polygon.php


def test_polygon_repr():
    assert str(poly100) == 'Poly(3,13)', 'actual:{0}'.format(poly100)


def test_polygon_rich_comparisons():
    # unit test: rich comparisons
    assert poly103 < poly104, 'actual:{0}'.format(poly101 < poly104)
    assert poly106 > poly103, 'actual:{0}'.format(poly106 > poly103)
    assert poly103 >= poly102, 'actual:{0}'.format(poly103 >= poly102)
    assert poly104 >= poly101, 'actual:{0}'.format(poly104 >= poly101)
    assert poly107 != poly108, 'actual:{0}'.format(poly107 != poly108)


def test_polygon_specific_value():
    # specific value unit test
    poly9 = Pp.Poly(6, 2)
    poly10 = Pp.Poly(4, 1)
    poly11 = Pp.Poly(4, 1)
    poly12 = Pp.Poly(4, 1)
    poly13 = Pp.Poly(1000, 1)

    assert math.isclose(poly9.apothem, 1.732, rel_tol=.0001, abs_tol=.0001)
    assert math.isclose(poly9.area, 10.392, rel_tol=.0001, abs_tol=.0001)
    assert math.isclose(poly9.perimeter, 12, rel_tol=.0001, abs_tol=.0001)
    assert math.isclose(poly9.interior_angle, 120, rel_tol=.0001, abs_tol=.0001)
    assert math.isclose(poly9.edge_length, 2, rel_tol=.0001, abs_tol=.0001)
    assert math.isclose(poly10.area, 2, rel_tol=.0001, abs_tol=.0001)
    assert poly10.equal_area(poly11)
    assert poly10.equal_perimeter(poly11)
    assert math.isclose(poly12.edge_length, math.sqrt(2), rel_tol=.0001, abs_tol=.0001)
    assert math.isclose(poly13.area, math.pi, rel_tol=.0001, abs_tol=.0001)


def test_polygon_set_item():
    # set item and recalculate of poly1
    poly1 = Pp.Poly(4, 5)
    poly1.__setitem__(10, 13.1)
    assert str(poly1) == 'Poly(10,13.1)', 'actual:{0}'.format(poly1)


def test_polygon_list_properties():
    # poly1 list properties
    poly1 = Pp.Poly(4, 5)
    assert poly1.listproperties


# def test_polygons():
#     # Unit Tests for p.Polygons Class
#     print('POLYGONS CLASS TESTING:')
#
#     polys = p.Polygons(10, 6.35)
#     polys2 = p.Polygons(500, 1)
#
#     # p.Polygons Class __repr__ test
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
#         print('p.Polygons Class Pi test passed')
#
#     print('p.Polygons Class setitem method testing...')
#
#     polys2 = p.Polygons(4, 20)
#     print('polys2', polys2)
#
#     print('polys2 changing sides and radius...')
#     if not polys2.__setitem__(400, 1):
#         print('polys2', polys2)
#         print('p.Polygons Class setitem method working')
#     print('Unit Testing Complete')

