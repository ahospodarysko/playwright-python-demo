from framework.helpers.logger_helper import LoggerHelper


class LoginPage:

    def __init__(self, page):
        self._page = page

    def login_with_pass(self, user_email, user_pass):
        LoggerHelper.log_step(f"login with user - {user_email}")
        self._page.fill("#email", user_email)
        self._page.fill("#password", user_pass)
        self._page.get_by_role("button", name="Sign in").click()

    def get_credentials_error(self):
        LoggerHelper.log_step("get credentials error text")
        return self._page.locator("p.text-danger-500").inner_text()
