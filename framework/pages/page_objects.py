from demo.pages.login_page import LoginPage


class PageObjects:
    def __init__(self, page):
        self.page = page
        self._login = None

    """Lazy Initialization (On-Demand Object Creation)"""
    @property
    def login_page(self):
        self._login = self._login or LoginPage(self.page)
        return self._login
