from collections import OrderedDict
from pytest import mark

from src.WIP_p2_proj2_temp import NrsGlobalCache as NCacheGlobal


# xfail = "expected to fail test"
@mark.xfail(reason="NrsGlobalCache is not a Singleton!")
def test_global_cache_is_singleton(test_global_cache):
    Another_Singleton = NCacheGlobal()


def test_global_cache_subclassed_ordered_dict(test_global_cache):
    # confirm NrsGlobalCache is a subclass of OrderedDict
    print(type(NCacheGlobal))
    assert issubclass(NCacheGlobal, OrderedDict)


def test_global_cache_size(test_global_cache):
    # working size w/add, change, pop
    test_global_cache[(20,20,.001)]: {'apothem': 100}
    assert test_global_cache.cache_size == len(test_global_cache.key_view)


def test_global_cache_key_view(test_global_cache):
    # viewable cached (n,r,sig) keys
    assert isinstance(test_global_cache.key_view, list)
    assert len(test_global_cache.key_view) == len(test_global_cache.keys())


def test_global_cache_contains_dict(test_global_cache):
    # key contains a nested dictionary as a value
    for i in test_global_cache.keys():
        print(test_global_cache.values())
        print(type(test_global_cache))
        all(isinstance(test_global_cache[i], dict))


def test_global_cache_add_item(test_global_cache):
    # clear cache of keys / values / calculated properties
    test_global_cache.clear()
    test_global_cache.__setitem__((50, 50, .1), 'apothem', 100)
    # print(test_global_cache.cache_size)
    print(test_global_cache.keys())
    assert test_global_cache.cache_size == 1


def test_global_cache_clear(test_global_cache):
    # add cache of keys / values / calculated properties
    test_global_cache.clear()
    test_global_cache.__setitem__((50, 50, .1), 'apothem', 100)
    assert test_global_cache.cache_size == 1
    # clear cache of keys / values / calculated properties
    test_global_cache.clear()
    assert test_global_cache.cache_size == 0


def test_global_cache_set_size(test_global_cache):
    # set cache size to key size
    test_global_cache.cache_limit = 200
    assert test_global_cache.cache_limit == 200


# def test_global_cache_oldest_item(test_global_cache):
#     test_global_cache.
# def test_global_cache_update_item(test_global_cache):
    # update an existing key and values
    # test_global_cache.se
    
# TODO get the latest item in stash
# TODO get the oldest item in stash
# TODO update an existing key more values
# TODO updating a key makes key recent item
# TODO cache_size respects cachce limit, old keys are discarded
