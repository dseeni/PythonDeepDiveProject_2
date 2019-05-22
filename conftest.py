from pytest import fixture
from Scripts_PDD2_Project2 import Poly_and_Polygons as p
from collections import OrderedDict


# @fixture(scope='function')
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

# @fixture(scope='function')
# def make_customer_record():
#
#     def _make_customer_record(name):
#         return {
#             "name": name,
#             "orders": []
#         }
#
#     return _make_customer_record
#
#
# def test_customer_records(make_customer_record):
#     customer_1 = make_customer_record("Lisa")
#     customer_2 = make_customer_record("Mike")
#     customer_3 = make_customer_record("Meredith")
