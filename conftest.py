from pytest import fixture
from src import poly_and_polygons as p
from collections import OrderedDict
from src.poly_and_polygons import NrsGlobalCache as Ngc
from src.polygons_factory import PolyFactory as Pf
from random import seed


@fixture(scope='function')
def test_poly():
    n = [i for i in range(3, 13)]
    r = [i for i in range(13, 23)]

    nr = tuple(zip(n, r))

    name = tuple(('poly{0}'.format(n)) for n in range(100, 100+len(n)))

    polylist = [p.Poly(n, r) for n, r in nr]
    polydict = OrderedDict(zip(name, polylist))
    polydict['poly111'] = 'dummy_obj'
    polydict['poly112'] = p.Poly(3,13)

    # for k, v in polydict.items():
    #     print(k, v,
    #           'perimeter =', v.perimeter,"\n",
    #           'apothem =', v.apothem,"\n",
    #           'interior angle =', v.interior_angle,"\n",
    #           'edge_length =', v.edge_length,"\n",
    #           'area =', v.area
    #           )
    return polydict


@fixture(scope='function')
def test_polygons():
    polys = p.Polygons(10, 6.35)
    polys2 = p.Polygons(500, 1)
    two_iterables = (polys,polys2)
    return two_iterables


# test_global_cache fixtures
@fixture(autouse=True)
# auto-run function fixture to clear singleton
def reset_test_global_cache_singletons():
    # move this to the root conftest.py file
    Ngc._instance = None


@fixture(scope='function')
def test_global_cache():
    global_cache = Ngc()
    # this is the oldest item in the dictionary
    # key 1
    global_cache[(50, 50, .1)]['apothem'] = [100]
    global_cache[(50, 50, .1)]['area'] = [400]

    # key 2
    global_cache[(60, 50, .1)]['apothem'] = [200]
    global_cache[(60, 50, .1)]['area'] = [500]

    # key 3
    global_cache[(70, 50, .1)]['apothem'] = [300]
    global_cache[(70, 50, .1)]['area'] = [600]

    # this is the key 3 newest item in the dictionary
    global_cache[(70, 50, .1)]['interior angle'] = [300]
    return global_cache


@fixture(scope='function')
def test_poly_factory():
    seed(0)
    polyfactory = Pf()
    return polyfactory
