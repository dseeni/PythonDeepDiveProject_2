from pytest import mark
from src import parameter_checker as pm


# frange helper function tests
def test_frange_docstring():
    assert pm.frange.__doc__ is not None

def test_frange_reverse_direciton():
    assert len(list(pm.frange(start=0.0, stop=-10.0, step=-1.0))) == 10

# test frange returns len of stop - start x
def test_frange_default():
    assert(len(list(pm.frange(0, 10, 1))) == 10)
    assert(len(list(pm.frange(0, 10, .5))) == 20)
    assert(len(list(pm.frange(0, 10, .25))) == 40)

# test frange returns len of stop - start x
def test_frange_step_length():
    assert len(list(pm.frange())) == 0

# test frange returns len of stop - start x
def test_frange_output_length():
    assert len(list(pm.frange(1.5,5.5,1))) == 4


# check_parameters tests
def test_check_parameters_docstring():
    assert pm.check_parameters.__doc__ is not None


def test_check_parameters_callable():
    assert (pm.check_parameters())

# check_parameters(icount=10, clones=2, cloneamount=2, siderange=(3,10), radrange=(1,5), sig=2)
def test_check_parameters_default_finalcount():
    returnvalues = pm.check_parameters()
    finalcount = (returnvalues[0] - returnvalues[1]) \
    + (returnvalues[1] * returnvalues[2])
    assert finalcount == 12


@mark.xfail(reason="sig must be an integer")
def test_check_parameters_sig_float_exception():
    pm.check_parameters(sig=.1)


@mark.xfail(reason="negative radius")
def test_check_parameters_negative_radius_exception():
    pm.check_parameters(radrange=(10,1))


@mark.xfail(reason="sig adjusted radius range must be positive")
def test_check_parameters_sig_adjusted_radius_range_exception():
    pm.check_parameters(radrange=(2,1), sig=0)


@mark.xfail(reason="adjust radius range must be positive")
def test_check_parameters_positive_radius_range_start_exception():
    pm.check_parameters(radrange=(-1,1))

@mark.xfail(reason="Side Range sampling must being at 3")
def test_check_parameters_3_side_range_start_exception():
    pm.check_parameters(siderange=(1,10))


@mark.xfail(reason="Side range sample range must be intergers")
def test_check_parameters_side_range_integer_exception():
    pm.check_parameters(siderange=(4.0,10.0))


@mark.xfail(reason="icount/clones/cloneamount must all be integers")
def test_check_paramters_icount_clones_cloneamount_integer_exception():
   pm.check_parameters(icount=4.3, clones=2.2, cloneamount=4.5)


def test_check_parameter_self_correction():
    assert pm.check_parameters(sig=0) == (10, 2, 2, (3,13), (1,5), 1)
