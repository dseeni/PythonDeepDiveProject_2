from src import polygons_factory as Pf
from pytest import raises


def test_polygons_factory_repr(test_poly_factory):
    # unit test: PolyFactory repr
    assert str(test_poly_factory) == \
           'PolyFactory(icount=10,clones=2,cloneamount=2,siderange=(3, 13),radrange=(1, 5),sig=1)'


def test_polygons_factory_icount_clone_value_error():
    with raises(ValueError):
        polyfactory = Pf.PolyFactory(icount=10, clones=10, cloneamount=0, siderange=(3, 10), radrange=(1, 5), sig=0)
        return polyfactory


def test_polygons_factory_icount(test_poly_factory):
    assert test_poly_factory.icount == 10


def test_polygons_factory_clones(test_poly_factory):
    assert test_poly_factory.clones == 2


def test_polygons_factory_cloneamount(test_poly_factory):
    assert test_poly_factory.cloneamount == 2


def test_polygons_factory_finalcount(test_poly_factory):
    assert test_poly_factory.finalcount == 12


def test_polygons_factory_siderange(test_poly_factory):
    assert test_poly_factory.siderange == (3, 13)


def test_polygons_factory_radrange(test_poly_factory):
    assert test_poly_factory.radrange == (1, 5)


def test_polygons_factory_sample_ints(test_poly_factory):
    assert len(test_poly_factory.sample_ints) == 10
    assert test_poly_factory.sample_ints[0] == 12
    for i in test_poly_factory.sample_ints:
        assert isinstance(i, int)


def test_polygons_factory_sample_floats(test_poly_factory):
    assert len(test_poly_factory.sample_floats) == 10
    for i in test_poly_factory.sample_floats:
        assert isinstance(i, float)


def test_polygons_factory_nrfinal(test_poly_factory):
    if test_poly_factory.nrfinal():
        assert len(test_poly_factory.polydict) == 12
        assert len(test_poly_factory.polynames) == 12
        assert test_poly_factory.finallist == 12
        assert str(Pf.poly101) == 'Poly(12,4.9,1)'
        assert str(Pf.poly102) == 'Poly(11,4.6,1)'
        assert Pf.poly101 > Pf.poly102


def test_polygons_factory_allcalc_funciton(test_poly_factory):
    assert hasattr(test_poly_factory, 'allcalc')
    return test_poly_factory.allcalc


def test_polygons_factory_sidevalues(test_poly_factory):
    assert hasattr(test_poly_factory, 'sidevalues')
    return test_poly_factory.sidevalues


def test_polygons_factory_circumradiusvalues(test_poly_factory):
    assert hasattr(test_poly_factory, 'circumradiusvalues')
    return test_poly_factory.circumradiusvalues


def test_polygons_factory_vertexcalc(test_poly_factory):
    assert hasattr(test_poly_factory, 'vertexcalc')
    return test_poly_factory.vertexcalc


def test_polygons_factory_perimetercalc(test_poly_factory):
    assert hasattr(test_poly_factory, 'perimetercalc')
    return test_poly_factory.perimetercalc


def test_polygons_factory_apothemcalc(test_poly_factory):
    assert hasattr(test_poly_factory, 'apothemcalc')
    return test_poly_factory.apothemcalc


def test_polygons_factory_interioranglecalc(test_poly_factory):
    assert hasattr(test_poly_factory, 'interioranglecalc')
    return test_poly_factory.interioranglecalc


def test_polygons_factory_edgelengthcalc(test_poly_factory):
    assert hasattr(test_poly_factory, 'edgelengthcalc')
    return test_poly_factory.edgelengthcalc


def test_polygons_factory_areacalc(test_poly_factory):
    assert hasattr(test_poly_factory, 'areacalc')
    return test_poly_factory.areacalc


def test_polygons_factory_instancerepr(test_poly_factory):
    assert hasattr(test_poly_factory, 'instancerepr')
    return test_poly_factory.instancerepr


def test_polygons_factor_len_method(test_poly_factory):
    assert len(test_poly_factory) == 12
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
