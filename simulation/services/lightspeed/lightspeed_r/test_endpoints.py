from services.lightspeed.lightspeed_r.endpoints import *
import pytest

def test_can_get_account_info():
    account_infos = account_info()
    print(account_infos)
    assert isinstance(account_infos[0], int), 'account_id of wrong type!'
    assert isinstance(account_infos[1], str), 'name of wrong type'
    


