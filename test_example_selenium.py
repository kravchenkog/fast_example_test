import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import general_helper
import pytest

global driver
global gh

header_section = {
    By.CSS_SELECTOR: "section[class^='LoginHeader_container]"
}


def setup_module():
    pass


def teardown():
    driver.quit()


class TestGroup:
    driver = None
    gh = None

    def setup(self):
        if not self.driver:
            path = os.path.dirname(os.path.abspath(__file__))
            path = path + "/chromedriver"
            self.driver = webdriver.Chrome(executable_path=path)
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()
            self.driver.get("http://google.com/")
            self.gh = general_helper.GeneralHelper(driver=self.driver)

    def teardown(self):
        pass

    def test_example(self):
        assert self.gh.el_is_presented(header_section)
