from src import poly_and_polygons as Pp
from src import polygons_factory as Pf
from pytest import raises
import math


# TODO: Refactor the below code as test cases

def test_polygons_factory_repr(test_poly_factory):
    # unit test: PolyFactory repr
    assert str(test_poly_factory) == \
           'PolyFactory(icount=10,clones=2,cloneamount=2,siderange=(3, 13),radrange=(1, 5),sig=1)'

# gen_polys = PolyFactory()

# print(gen_polys.nrfinal)
# # print(gen_polys.finallist)
# # print(gen_polys.polynames)
# # help(gen_polys)
# # gen_polys.__setitem__(cloneamount=50, sig=3)
# # print(gen_polys)
# # gen_polys.nrfinal
# # print(gen_polys.polynames)
# # print(gen_polys.allcalc)
# # gen_polys.nrfinal
# # gen_polys.polynames
# #
# # print(gen_polys)
# # print(gen_polys.polynames)
# # gen_polys.nrfinal
# # print(gen_polys.polynames)
# # gen_polys.apothemcalc
# #
# # help(checkparameters)
# # help(PolyFactory)
# #
# # print(len(gen_polys))
# # gen_polys.__setitem__(siderange=(100,300))
# # gen_polys.allcalc
# # gen_polys.__setitem__(sig=5)
# # print(gen_polys.polynames)
# # # gen_polys.__setitem__(radrange=(100,200),siderange=(200,400),sig=3)
# # # gen_polys.allcalc
# # print(gen_polys)
# # gen_polys.__setitem__(sig=5)
# # print(gen_polys)
# # # gen_polys.__setitem__(sig=1000)
# print(gen_polys.instancerepr)


# pf = PolyFactory()
# print(pf.nrfinal)
# print(pf.finallist)
# print(pf.finalcount)
