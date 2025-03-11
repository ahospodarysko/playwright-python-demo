import os


class BrowserHelper:

    @staticmethod
    def get_browser_type():
        """Get the browser type from environment variables (default: chromium)."""
        return os.getenv("BROWSER", "chromium").lower()

    @staticmethod
    def get_launch_options():
        """Return browser launch options dynamically based on environment variables."""
        return {
            "headless": os.getenv("HEADLESS", "false").lower() == "true",  # false - headed mode, true - headless mode
            "slow_mo": int(os.getenv("SLOW_MO", "0")),  # slows down Playwright operations
            "args": ["--start-maximized"]  # requires to add no_viewport=True to browser.new_page(no_viewport=True)
        }
