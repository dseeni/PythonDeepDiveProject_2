from src import poly_and_polygons as Pp
from pytest import raises
import math
# https://www.calculatorsoup.com/calculators/geometry-plane/polygon.php


def test_polygon_repr(test_poly):
    # unit test: Polygon repr
    assert str(test_poly['poly100']) == 'Poly(3,13,3)'


def test_polygon_float_radius_repr():
    # unit test: Polygon radius float/int repr
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
    assert math.isclose(poly12.edge_length, math.sqrt(2), rel_tol=.001, abs_tol=.001)
    assert math.isclose(poly13.area, math.pi, rel_tol=.001, abs_tol=.001)
    # test equality
    assert poly10.equal_area(poly11)
    assert poly10.equal_perimeter(poly11)
    # test equality exceptions
    with raises(Exception):
        assert poly13.equal_area(poly9)
    with raises(Exception):
        assert poly13.equal_perimeter(poly9)


def test_polygon_set_item():
    # set item and recalculate of poly1
    poly1 = Pp.Poly(4, 5)
    poly1.__setitem__(10, 13.1)
    assert str(poly1) == 'Poly(10,13.1,3)'


def test_polygon_interior_angle_value_error():
    poly = Pp.Poly(None, None, None)
    with raises(ValueError):
        return poly.interior_angle


def test_polygon_interior_angle_value_calculates_without_radius():
    poly = Pp.Poly(3, None, 3)
    return poly.interior_angle


def test_polygon_interior_angle_cache():
    poly = Pp.Poly(5, 5, 3)
    if poly.interior_angle:
        assert poly.interior_angle
    poly.sig = 1
    assert poly._interior_angle is None
    poly.circumradius = 1
    assert poly._interior_angle is None
    poly.side_count = 3
    assert poly._interior_angle is None


def test_polygon_edge_length_cache():
    poly = Pp.Poly(5, 5, 3)
    if poly.edge_length:
        assert poly.edge_length
    poly.sig = 1
    assert poly._edge_length is None
    poly.circumradius = 1
    assert poly._edge_length is None
    poly.side_count = 3
    assert poly._edge_length is None


def test_polygon_apothem_cache():
    poly = Pp.Poly(5, 5, 3)
    if poly.apothem:
        assert poly.apothem
    poly.sig = 1
    assert poly._apothem is None
    poly.circumradius = 1
    assert poly._apothem is None
    poly.side_count = 3
    assert poly._apothem is None


def test_polygon_area_cache():
    poly = Pp.Poly(5, 5, 3)
    if poly.area:
        assert poly.area
    poly.sig = 1
    assert poly._area is None
    poly.circumradius = 1
    assert poly._area is None
    poly.side_count = 3
    assert poly._area is None


def test_polygon_perimeter_cache():
    poly = Pp.Poly(5, 5, 3)
    if poly.perimeter:
        assert poly.perimeter
    poly.sig = 1
    assert poly._perimeter is None
    poly.circumradius = 1
    assert poly._perimeter is None
    poly.side_count = 3
    assert poly._perimeter is None


def test_polygon_perimeter_value_error():
    with raises(ValueError):
        poly1 = Pp.Poly()
        return poly1.perimeter



def test_polygon_edge_length_value_error():
    poly = Pp.Poly(None, None, None)
    with raises(ValueError):
        return poly.edge_length


def test_polygon_apothem_value_error():
    poly = Pp.Poly(None, None, None)
    with raises(ValueError):
        return poly.apothem


def test_polygon_area_value_error():
    poly = Pp.Poly(None, None, None)
    with raises(ValueError):
        return poly.area


def test_polygon_calculate_properties_method():
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


def test_polygon_polycheck_n_type():
    with raises(Exception):
        Pp.Poly('string', 4, 3)


def test_polygon_polycheck_n_positive():
    with raises(Exception):
        Pp.Poly(-4, 4, 3)


def test_polygon_polycheck_r_positive_type():
    with raises(Exception):
        Pp.Poly(4, -4, 3)


def test_polygon_polycheck_sig_positive_type():
    with raises(Exception):
        Pp.Poly(4, 4, -3)


def test_polygon_nrskey_valid():
    poly100 = Pp.Poly(4, 4, 2)
    assert poly100.nrskey == (4, 4, 2)


def test_polygon_nrskey_returns_none():
    # with raises(Exception):
    poly100 = Pp.Poly()
    return poly100.nrskey


# Testing for Polygons Class
def test_polygons_repr(test_polygons):
    # Polygons Class __repr__ test
    assert str(test_polygons[0]) == 'Polygons(10,6.35)'


def test_polygons_radius_as_integer_repr():
    polygons = Pp.Polygons(4, 3.0)
    assert str(polygons) == 'Polygons(4,3)'


def test_polygons_type_error_sides():
    with raises(TypeError):
        polys = Pp.Polygons("string", 1)
        return polys


def test_polygons_value_error_sides():
    with raises(ValueError):
        polys = Pp.Polygons(0, 1)
        return polys


def test_polygons_type_error_radius():
    with raises(TypeError):
        polys = Pp.Polygons(10, "string")
        return polys


def test_polygons_len(test_polygons):
    assert len(test_polygons[0]) == 8


def test_polygons_returns_iterator(test_polygons):
    assert '__iter__' in dir(test_polygons[0]) and iter(test_polygons[0])


def test_polygons_max_efficencey_method(test_polygons):
    # test the max efficencey formula
    # assert max([p.area/p.perimeter for p in test_polygons[1]]) == test_polygons[1].max_efficiency
    assert test_polygons[1].max_efficiency == Pp.Poly(500, 1, 3)


def test_polygons_iterator_returns_self():
    polys = Pp.Polygons(10, 3)
    polysiterator = iter(polys)
    assert id(polysiterator) == id(iter(polysiterator))


