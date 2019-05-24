from collections import OrderedDict
from pytest import mark

from src.WIP_p2_proj2_temp import NrsGlobalCache as NCacheGlobal


@mark.xfail(reason="NrsGlobalCache is not a Singleton!")
# xfail = "expected to fail test"
def test_global_cache_is_singleton(test_global_cache):
    Another_Singleton = NCacheGlobal()


def test_global_cache_size(test_global_cache):
    assert test_global_cache.cache_size == len(test_global_cache.key_view)


def test_global_cache_view(test_global_cache):
    # viewable cached (n,r,sig) keys
    assert isinstance(test_global_cache.key_view, list)
    assert len(test_global_cache.key_view) == len(test_global_cache._cache.keys())


def test_global_key_contains_dict(test_global_cache):
    # key contains a nested dictionary as a value
    assert all(isinstance(i, dict) for i in (test_global_cache._cache.values()))


def test_global_add_key_property_value(test_global_cache):
    # clear cache of keys / values / calculated propertes
    test_global_cache._cache['poly100'] = {'apothem': 100}
    assert test_global_cache.cache_size == 1


def test_global_clear_cache(test_global_cache):
    # add cache of keys / values / calculated properties
    # clear cache of keys / values / calculated properties
    test_global_cache._cache['poly100'] = {'apothem': 100}
    assert test_global_cache.cache_size == 1
    test_global_cache._cache.clear()
    assert test_global_cache.cache_size == 0


# @mark.skip(reason="WIP")
def test_global_set_cache_size(test_global_cache):
    # set cache size to key size
    test_global_cache.cache_limit = 200
    assert test_global_cache.cache_limit == 200

# TODO set cache size
# TODO append item in stash
# TODO get the last item in stash
# TODO get the oldest item in stash
