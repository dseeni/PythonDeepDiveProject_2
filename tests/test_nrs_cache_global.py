from src.WIP_p2_proj2_temp import NrsGlobalCache as NCacheGlobal
import pytest


def test_nrsg_cache_singleton():
    with pytest.raises(Exception) as e_info:
        s = NCacheGlobal()  # Ok
        another_singleton = NCacheGlobal()


