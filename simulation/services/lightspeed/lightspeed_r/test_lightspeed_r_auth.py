from services.lightspeed.lightspeed_r.lightspeed_r_auth import *
import pytest

def test_get_headers():
    get_header = get_headers()
    print(get_header)