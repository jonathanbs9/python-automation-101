
from swag.actions import login_with
import pytest


def test_login_swag_with_valid_credentials(py, login):
    assert py.contains('Products')

def test_user_can_logout(py, login):
    py.contains('Open Menu').click()
    py.contains('Logout').click(force=True)
    assert py.should().contain_url('https://www.saucedemo.com/')

examples = [
    ('invalid_user' , 'secret_sauce'    , 'Username and password do not match any user in this service'),
    ('standard_user', 'invalid_password', 'Username and password do not match any user in this service'),
    ('invalid_user' , 'invalid_password', 'Username and password do not match any user in this service'),
    (''            , 'secret_sauce'    , 'Username is required'),
    ('standard_user', ''                , 'Password is required'),
]

@pytest.mark.parametrize('username,password,message', examples)    
def test_login_with_invalid_credentials(py, username, password, message):
    login_with(py, username, password)
    assert py.get('[data-test="error"]').should().contain_text(message)