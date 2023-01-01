from services.lightspeed.lightspeed_r.endpoints import *
import pytest

def test_can_get_account_info():
    account_id = account_info()
    print(account_id)
    assert isinstance(account_id, int), 'Argument of wrong type!'
    



