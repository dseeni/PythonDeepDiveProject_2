from src import parameter_checker as pm
from pytest import raises


# check_parameters tests
def test_check_parameters_docstring():
    assert pm.check_parameters.__doc__ is not None


def test_check_parameters_clones_value_error(test_poly_factory):
    with raises(ValueError):
        test_poly_factory.clones = -1


def test_check_parameters_cloneamount_value_error(test_poly_factory):
    with raises(ValueError):
        test_poly_factory.cloneamount = -1


def test_check_parameters_callable():
    assert (pm.check_parameters())


# check_parameters(icount=10, clones=2, cloneamount=2, siderange=(3,10), radrange=(1,5), sig=2)
def test_check_parameters_default_finalcount():
    returnvalues = pm.check_parameters()
    finalcount = (returnvalues[0] - returnvalues[1]) + (returnvalues[1] * returnvalues[2])
    assert finalcount == 12


def test_check_parameters_sig_float_exception():
    with raises(Exception):
        pm.check_parameters(sig=.1)


def test_check_parameters_negative_radius_exception():
    with raises(Exception):
        pm.check_parameters(radrange=(10, 1))


def test_check_parameters_sig_adjusted_radius_range_exception():
    with raises(Exception):
        pm.check_parameters(radrange=(2, 1), sig=0)


def test_check_parameters_positive_radius_range_start_exception():
    with raises(Exception):
        pm.check_parameters(radrange=(-1, 1))


def test_check_parameters_3_side_range_start_exception():
    with raises(Exception):
        pm.check_parameters(siderange=(1, 10))


def test_check_parameters_side_range_integer_exception():
    with raises(Exception):
        pm.check_parameters(siderange=(4.0, 10.0))


def test_check_paramters_icount_clones_cloneamount_integer_exception():
    with raises(Exception):
        pm.check_parameters(icount=4.3, clones=2.2, cloneamount=4.5)


def test_check_parameter_self_correction():
    assert pm.check_parameters(sig=0) == (10, 2, 2, (3, 13), (1, 5), 1)
