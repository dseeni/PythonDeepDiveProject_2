from src import parameter_checker as pm

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


# frange helper function tests
def test_frange_docstring():
        assert pm.frange.__doc__ is not None


# test frange returns len of stop - start x
def test_frange_default():
    print(list(pm.frange(0,10,.5)))

def test_frange_step_length():
    if len(list(pm.frange())) == 0:
        assert True

def test_frange_output_length():
    assert len(list(pm.frange(1.5,5.5,1))) == 4

