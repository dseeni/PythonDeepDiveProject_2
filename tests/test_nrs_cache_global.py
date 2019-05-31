from collections import OrderedDict
from pytest import mark
from src.WIP_p2_proj2_temp import NrsGlobalCache as NCacheGlobal


# NrsGlobalCache docstring test
def test_global_cache_docstring(test_global_cache):
    assert test_global_cache.__doc__ is not None


def test_global_cache_repr(test_global_cache):
    assert test_global_cache.__repr__() == 'NrsGlobalCache()'


@mark.xfail(reason="NrsGlobalCache is not a Singleton!")
def test_global_cache_is_singleton(test_global_cache):
    # xfail = "expected to fail test"
    NCacheGlobal()


def test_global_cache_get_instance_method(test_global_cache):
    assert test_global_cache._instance is not None
    assert NCacheGlobal.get_instance() == test_global_cache


def test_global_cache_get_instance_as_none():
    assert NCacheGlobal._instance is None
    assert NCacheGlobal.get_instance() == NCacheGlobal._instance


def test_global_cache_is_subclass_of_ordered_dict(test_global_cache):
    # confirm NrsGlobalCache is a subclass of OrderedDict
    # print(type(NCacheGlobal))
    assert issubclass(NCacheGlobal, OrderedDict)


def test_global_cache_size(test_global_cache):
    # working size w/add, change, pop
    test_global_cache[(20, 20, .001)]['apothem'] = [100]
    assert test_global_cache.cache_size == len(test_global_cache.key_view)


def test_global_cache_key_view(test_global_cache):
    # viewable cached (n,r,sig) keys
    assert isinstance(test_global_cache.key_view, list)
    assert len(test_global_cache.key_view) == len(test_global_cache.keys())


def test_global_cache_contains_dict(test_global_cache):
    # key contains a nested dictionary as a value
    assert isinstance(type(test_global_cache[(50, 50, .1)].values()), type(dict))


def test_global_cache_add_item(test_global_cache):
    # clear cache of keys / values / calculated properties
    test_global_cache.clear()
    test_global_cache.cache_access((90, 50, .1), 'apothem', 100)
    assert test_global_cache.cache_size == 1


def test_global_cache_clear(test_global_cache):
    # add cache of keys / values / calculated properties
    test_global_cache.clear()
    test_global_cache[(50, 50, .1)]['apothem'] = [100]
    assert test_global_cache.cache_size == 1
    test_global_cache.clear()
    assert test_global_cache.cache_size == 0


def test_global_cache_set_cache_limit(test_global_cache):
    # set cache size to key size
    test_global_cache.cache_limit = 200
    assert test_global_cache.cache_limit == 200


def test_global_cache_get_oldest_item(test_global_cache):
    assert ((test_global_cache.popitem(last=False)) ==
            ((50, 50, 0.1), {'apothem': [100], 'area': [400]}))


def test_global_cache_get_newest_item(test_global_cache):
    assert ((test_global_cache.popitem(last=True)) ==
            ((70, 50, 0.1), {'apothem': [300], 'area': [600], 'interior angle': [300]}))


def test_global_cache_add_calc_prop_to_existing_key(test_global_cache):
    test_global_cache[(50, 50, .1)]['interior_angle'] = [60]
    assert len(test_global_cache.values()) == 3


def test_global_cache_updating_key_makes_key_newest_item(test_global_cache):
    test_global_cache.cache_access((50, 50, .1), 'interior_angle', 60)
    assert next(reversed(test_global_cache)) == (50, 50, .1)


def test_global_cache_limit_respects_new_item(test_global_cache):
    print('test_global_cache.cache_size = ', test_global_cache.cache_size)
    test_global_cache.cache_limit = 1
    print('test_global_cache.cache_size = ', test_global_cache.cache_size)
    test_global_cache.cache_access((60, 60, .1), 'area', 100)
    # print('test_global_cache.cache_size(test_global_cache.keys()) = ',
    #       test_global_cache.cache_size(len(test_global_cache.keys())))
    # print('test_global_cache.items() = ', test_global_cache.items())
    assert test_global_cache.cache_size == 1
