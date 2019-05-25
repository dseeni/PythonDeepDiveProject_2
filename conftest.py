from pytest import fixture
from src import poly_and_polygons as p
from collections import OrderedDict
from src.WIP_p2_proj2_temp import NrsGlobalCache as Ngc

@fixture(scope='function')
def test_poly():
    n = [i for i in range(3, 13)]
    r = [i for i in range(13, 23)]

    nr = tuple(zip(n, r))

    name = tuple(('poly{0}'.format(n)) for n in range(100, 100+len(n)))

    polylist = [p.Poly(n, r) for n, r in nr]
    polydict = OrderedDict(zip(name, polylist))

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



@fixture(autouse=True)
# auto-run function fixture to clear singleton
def reset_test_global_cache_singletons():
    # move this to the root conftest.py file
    Ngc._instance = None

@fixture(scope='function')
def test_global_cache():
    global_cache = Ngc()
    global_cache.__setitem__((50, 50, .1), 'apothem', 100)
    global_cache.__setitem__((60, 50, .1), 'apothem', 200)
    global_cache.__setitem__((70, 50, .1), 'apothem', 300)
    return global_cache
#
# @pytest.fixture
# def mocked_key_response(mocker):
#   mocker.patch.object(credentials.KeyHandler, '_retrieve_parameter', return_value=key_response)
#
# def test_keys_initialize(mocked_key_response):
#   key_handler = credentials.KeyHandler('some_key')
#

