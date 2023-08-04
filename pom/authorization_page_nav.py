"""authorization_page_nav.py."""
from base.seleniumbase import SeleniumBase


class AuthorizationPageNav(SeleniumBase):
    """AuthorizationPageNav."""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__user_name = "#i0116"
        self.__password = "#i0118"
        self.__login_button = "#idSIButton9"
        self.inline_block = "#idBtn_Back"

    def get_input_username(self):
        """Get input username."""
        return self.is_visible("css", self.__user_name, "input_username")

    def get_input_password(self):
        """Get input password."""
        return self.is_visible("css", self.__password, "input_password")

    def get_button_login(self):
        """Get button login."""
        return self.is_visible("css", self.__login_button, "button_login")

    def inline_block(self):
        """Inline block."""
        return self.is_visible("css", self.inline_block, "inline_block")
