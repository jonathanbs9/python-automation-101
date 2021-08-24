from swag.actions import login_with
import pytest

@pytest.fixture
def login(py):
    login_with(py, 'standard_user', 'secret_sauce')
