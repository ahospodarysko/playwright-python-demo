import allure


class AllureHelper:

    @staticmethod
    def take_screenshot(item):
        """Attach screenshot to Allure report"""
        page = item.funcargs.get("page")  # Get Playwright 'page' fixture
        if page:
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)
            allure.attach.file(screenshot_path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
