import pytest

invalid_creds = [
    ("invalid_email@gmail.com", "password"),
    ("invalid_email@gmail.com", "valid_password"),
    ("valid_email@gmail.com", "invalid_password")
]


@pytest.mark.regression
@pytest.mark.parametrize("email, password", invalid_creds)
def test_invalid_login(po, email, password):
    po.login_page.login_with_pass(email, password)
    creds_error = po.login_page.get_credentials_error()

    assert creds_error == "The user credentials were incorrect."
