from src import polygons_factory as pf
from pytest import raises


def test_polygons_factory_repr(test_poly_factory):
    # unit test: PolyFactory repr
    assert str(test_poly_factory) == \
           'PolyFactory(icount=10,clones=2,cloneamount=2,siderange=(3, 13),radrange=(1, 5),sig=1)'


def test_polygons_factory_icount_clone_value_error():
    with raises(ValueError):
        polyfactory = pf.PolyFactory(icount=10, clones=10, cloneamount=0, siderange=(3, 10), radrange=(1, 5), sig=0)
        return polyfactory


def test_polygons_factory_icount(test_poly_factory):
    assert test_poly_factory.icount == 10


def test_polygons_factor_icount_setter(test_poly_factory):
    test_poly_factory.icount = 3
    assert test_poly_factory.finalcount == 5
    with raises(ValueError):
        test_poly_factory.icount = 2


def test_polygons_factory_clones(test_poly_factory):
    assert test_poly_factory.clones == 2
    with raises(ValueError):
        test_poly_factory.icount = 1
        test_poly_factory.clones = 1


def test_polygons_factor_clones_setter(test_poly_factory):
    test_poly_factory.clones = 0
    assert test_poly_factory.finalcount == 10


def test_polygons_factor_clones_setter_value_error(test_poly_factory):
    with raises(ValueError):
        test_poly_factory.clones = 10


def test_polygons_factory_cloneamount(test_poly_factory):
    assert test_poly_factory.cloneamount == 2


def test_polygons_factor_cloneamount_setter(test_poly_factory):
    test_poly_factory.cloneamount = 3
    assert test_poly_factory.finalcount == 14


def test_polygons_factory_finalcount(test_poly_factory):
    assert test_poly_factory.finalcount == 12


def test_polygons_factory_siderange(test_poly_factory):
    assert test_poly_factory.siderange == (3, 13)


def test_polygons_factory_siderange_setter(test_poly_factory):
    test_poly_factory.siderange = (10,23)
    assert test_poly_factory.siderange == (10, 23)


def test_polygons_factory_radrange(test_poly_factory):
    assert test_poly_factory.radrange == (1, 5)


def test_polygons_factory_radrange_setter(test_poly_factory):
    test_poly_factory.radrange = (5,20)
    assert test_poly_factory.radrange == (5,20)


def test_polygons_factory_sig(test_poly_factory):
    assert test_poly_factory.sig == 1


def test_polygons_factory_sig_setter(test_poly_factory):
    test_poly_factory.sig = 2
    assert test_poly_factory.sig == 2


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
        assert str(pf.poly101) == 'Poly(12,4.9)'
        assert str(pf.poly102) == 'Poly(11,4.6)'
        assert pf.poly101 > pf.poly102


def test_polygons_factory_allcalc_funciton(test_poly_factory):
    assert hasattr(test_poly_factory, 'allcalc')
    assert len(test_poly_factory.allcalc) == 12
    return test_poly_factory.allcalc


def test_polygons_factory_sidevalues(test_poly_factory):
    assert hasattr(test_poly_factory, 'sidevalues')
    assert len(test_poly_factory.sidevalues) == 12
    return test_poly_factory.sidevalues


def test_polygons_factory_circumradiusvalues(test_poly_factory):
    assert hasattr(test_poly_factory, 'circumradiusvalues')
    assert len(test_poly_factory.circumradiusvalues) == 12
    return test_poly_factory.circumradiusvalues


def test_polygons_factory_vertexcalc(test_poly_factory):
    assert hasattr(test_poly_factory, 'vertexcalc')
    assert len(test_poly_factory.vertexcalc) == 12
    return test_poly_factory.vertexcalc


def test_polygons_factory_perimetercalc(test_poly_factory):
    assert hasattr(test_poly_factory, 'perimetercalc')
    assert len(test_poly_factory.perimetercalc) == 12
    return test_poly_factory.perimetercalc


def test_polygons_factory_apothemcalc(test_poly_factory):
    assert hasattr(test_poly_factory, 'apothemcalc')
    assert len(test_poly_factory.apothemcalc) == 12
    return test_poly_factory.apothemcalc


def test_polygons_factory_interioranglecalc(test_poly_factory):
    assert hasattr(test_poly_factory, 'interioranglecalc')
    assert len(test_poly_factory.interioranglecalc) == 12
    return test_poly_factory.interioranglecalc


def test_polygons_factory_edgelengthcalc(test_poly_factory):
    assert hasattr(test_poly_factory, 'edgelengthcalc')
    assert len(test_poly_factory.edgelengthcalc) == 12
    return test_poly_factory.edgelengthcalc


def test_polygons_factory_areacalc(test_poly_factory):
    assert hasattr(test_poly_factory, 'areacalc')
    assert len(test_poly_factory.areacalc) == 12
    return test_poly_factory.areacalc


def test_polygons_factory_instancerepr(test_poly_factory):
    assert hasattr(test_poly_factory, 'instancerepr')
    assert len(test_poly_factory.instancerepr) == 12
    return test_poly_factory.instancerepr


def test_polygons_factor_len_method(test_poly_factory):
    assert len(test_poly_factory) == 12
