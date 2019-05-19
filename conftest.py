from pytest import fixture
from Scripts_PDD2_Project2 import Poly_and_Polygons as p
import Ordereddict

@fixture(scope='module')
def test_polygon():

    n = [i for i in range(3, 13)]
    r = [i for i in range(13, 23)]

    nr = tuple(zip(n, r))

    name = tuple(('poly{0}'.format(n)) for n in range(100, 100+len(n)))

    # same as the for loop below
    polylist = [p.Poly(n, r) for n, r in nr]

    test_polygon.polydict = Ordereddict(zip(name, polylist))

    globals().update(test_polygon.polydict)

    for k, v in test_polygon.polydict.items():
        print(k, v,
              'perimeter =', v.perimeter
              'apothem =', v.apothem,
              'interior angle =', v.interior_angle,
              'edge_length =', v.edge_length,
              'area =', v.area
              )
