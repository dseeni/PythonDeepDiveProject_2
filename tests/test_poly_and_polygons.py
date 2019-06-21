from src import WIP_p2_proj2_temp as Pp
from pytest import raises
from pytest import mark
import math
# https://www.calculatorsoup.com/calculators/geometry-plane/polygon.php


def test_polygon_repr(test_poly):
    assert (test_poly['poly100']) == Pp.Poly(3, 13, 3), 'actual:{0}'.format(test_poly['poly100'])


def test_polygon_float_radius_repr():
    poly100 = Pp.Poly(3, 3, 3)
    assert poly100.__repr__() == "Poly(3,3,3)"
    poly100 = Pp.Poly(3, 3.1, 3)
    assert poly100.__repr__() == "Poly(3,3.1,3)"
    poly100 = Pp.Poly(3, 3.0, 3)
    assert poly100.__repr__() == "Poly(3,3,3)"


def test_polygon_rich_comparisons(test_poly):
    # unit test: rich comparisons
    assert test_poly['poly103'] < test_poly['poly104']

    assert test_poly['poly106'] > test_poly['poly103']

    assert test_poly['poly103'] >= test_poly['poly102']

    assert test_poly['poly101'] <= test_poly['poly104']

    assert test_poly['poly107'] != test_poly['poly108']

    assert test_poly['poly100'] == test_poly['poly112']


def test_polygon_rich_comparisons_not_implemented(test_poly):
    # unit test: rich comparison not implemented error
    with raises(TypeError):
        assert test_poly['poly106'] > test_poly['poly111']

    with raises(TypeError):
        assert test_poly['poly103'] >= test_poly['poly111']

    with raises(TypeError):
        assert test_poly['poly104'] >= test_poly['poly111']

    with raises(Exception):
        assert test_poly['poly107'] == test_poly['poly111']


def test_polygon_specific_value():
    # specific value unit test
    poly9 = Pp.Poly(6, 2)
    poly10 = Pp.Poly(4, 1)
    poly11 = Pp.Poly(4, 1)
    poly12 = Pp.Poly(4, 1)
    poly13 = Pp.Poly(1000, 1, 5)
    for i in range(9, 14):
        eval("poly{0}.calcproperties".format(i))
    assert math.isclose(poly9.apothem, 1.732, rel_tol=.001, abs_tol=.001)
    assert math.isclose(poly9.area, 10.392, rel_tol=.001, abs_tol=.001)
    assert math.isclose(poly9.perimeter, 12, rel_tol=.001, abs_tol=.001)
    assert math.isclose(poly9.interior_angle, 120, rel_tol=.001, abs_tol=.001)
    assert math.isclose(poly9.edge_length, 2, rel_tol=.001, abs_tol=.001)
    assert math.isclose(poly10.area, 2, rel_tol=.001, abs_tol=.001)
    assert poly10.equal_area(poly11)
    assert poly10.equal_perimeter(poly11)
    assert math.isclose(poly12.edge_length, math.sqrt(2), rel_tol=.001, abs_tol=.001)
    assert math.isclose(poly13.area, math.pi, rel_tol=.001, abs_tol=.001)


def test_polygon_set_item():
    # set item and recalculate of poly1
    poly1 = Pp.Poly(4, 5)
    poly1.__setitem__(10, 13.1)
    assert poly1 == Pp.Poly(10, 13.1, 3), 'actual:{0}'.format(poly1)


def test_polygon_calulate_properties_method():
    # poly1 list properties
    poly1 = Pp.Poly(4, 5)
    assert poly1.calcproperties


def test_polygon_sig_value_attribute(test_poly):
    assert test_poly['poly101'].sig == 3


def test_polygon_sig_value_setter(test_poly):
    test_poly['poly101'].sig = 4
    assert test_poly['poly101'].sig == 4


def test_polygon_circumradius_setter(test_poly):
    test_poly['poly101'].circumradius = 4
    assert test_poly['poly101'].circumradius == 4


def test_polygon_side_count_setter(test_poly):
    test_poly['poly101'].side_count = 4
    assert test_poly['poly101'].side_count == 4


@mark.xfail(reason="Sides (n) = integer type Int/Flot/Decimal/Fraction only")
def test_polygon_polycheck_n_type():
    Pp.Poly('string', 4, 3)


@mark.xfail(reason="At least 3 sides required")
def test_polygon_polycheck_n_positive():
    Pp.Poly(-4, 4, 3)


@mark.xfail(reason="r = Positive Int/Float/Decimal/Fraction only")
def test_polygon_polycheck_r_positive_type():
    Pp.Poly(4, -4, 3)


@mark.xfail(reason="Significant Digits (sig) must be of positive integer type only")
def test_polygon_polycheck_sig_positive_type():
    Pp.Poly(4, 4, -3)


def test_polygon_nrskey_valid():
    poly100 = Pp.Poly(4, 4, 2)
    assert poly100.nrskey == (4, 4, 2)


@mark.xfail(reason="n,r,s values = None")
def test_polygon_nrskey_invalid():
    poly100 = Pp.Poly()
    return poly100.nrskey

# Testing for Polygons Class #
# def test_polygons_repr(test_polygons):
#     # Polygons Class __repr__ test
#     assert str(test_polygons[0]) == 'Polygons(10,6.35)', '{0}'.format(polys)
#
#
# def test_polygons_max_efficencey_method(test_polygons):
#     # test the max efficencey formula
#     assert max([p.area/p.perimeter for p in test_polygons[1]]) == test_polygons[1].max_efficiency
#
#
# def test_polygons_sequence(test_polygons):
#     # Access the sequence type
#     assert test_polygons[0][1]
#
#
# def test_polygon_sequence_pi_area(test_polygons):
#     # calculate area of Pi
#     assert math.isclose(test_polygons[1][497].area, math.pi, abs_tol=.0001, rel_tol=.0001)

    # print('pp.Polygons Class setitem method testing...')
    #
    # polys2 = pp.Polygons(4, 20)
    # print('polys2', polys2)
    #
    # print('polys2 changing sides and radius...')
    # if not polys2.__setitem__(400, 1):
    #     print('polys2', polys2)
    #     print('pp.Polygons Class setitem method working')
    # print('Unit Testing Complete')
