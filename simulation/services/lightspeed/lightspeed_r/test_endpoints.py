from services.lightspeed.lightspeed_r.endpoints import *
import pytest

def test_can_get_account_info():
    info = account_info()
    print(info)
    # with pytest.raises(OverflowError):
    #     pass
