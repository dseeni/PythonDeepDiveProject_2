from Scripts_PDD2_Project2 import ParameterChecker as pm

# check_parameters tests
def test_check_parameters_docstring():
        if pm.check_parameters.__doc__ is None:
                assert False

def test_check_parameters_callable():
    print(pm.check_parameters())


# frange helper function tests
def test_frange_docstring():
        if pm.frange.__doc__ is None:
                assert False
# test frange returns len of stop - start x
def test_frange_default():
    print(list(pm.frange(0,10,.5)))

def test_frange_step_length():
    if len(list(pm.frange())) == 0:
        assert True

