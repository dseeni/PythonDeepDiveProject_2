from collections import OrderedDict
from pytest import mark

from src.WIP_p2_proj2_temp import NrsGlobalCache as NCacheGlobal


# xfail = "expected to fail test"
@mark.xfail(reason="NrsGlobalCache is not a Singleton!")
def test_nrsg_cache_is_singleton(test_global_cache):
    Another_Singleton = NCacheGlobal()


def test_nrsg_cache_size(test_global_cache):
    assert test_global_cache.cache_size == len(test_global_cache._cache.keys())

def test_nrsg_cache_view(test_global_cache):
    # viewable cached (n,r,sig) keys
    assert isinstance(test_global_cache.cache_view, list)

def test_nrsg_key_caclculated_property(test_global_cache):
    # key contains a nested dictionary as a value
    assert all(isinstance(i,dict) for i in (test_global_cache._cache.values()))

