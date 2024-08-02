import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions

username = os.getenv("deviwantchips")  # Replace the username
access_key = os.getenv("rCwsX06TpX04mFPmuNHIApqIr7iOyffmCvMouATAGMFAAZHQjY")  # Replace the access key


# paste your capibility options below

options = ChromeOptions()
options.browser_version = "latest"
options.platform_name = "win10"
lt_options = {}
lt_options["deviwantchips"] = username
lt_options["rCwsX06TpX04mFPmuNHIApqIr7iOyffmCvMouATAGMFAAZHQjY"] = access_key
lt_options["video"] = True
lt_options["resolution"] = "1920x1080"
lt_options["network"] = True
lt_options["build"] = "test_build"
lt_options["project"] = "unit_testing"
lt_options["smartUI.project"] = "test"
lt_options["name"] = "basic_unit_selinium"
lt_options["w3c"] = True
lt_options["plugin"] = "python-python"
options.set_capability("LT:Options", lt_options)


# Steps to run Smart UI project (https://beta-smartui.lambdatest.com/)
# Step - 1 : Change the hub URL to @beta-smartui-hub.lambdatest.com/wd/hub
# Step - 2 : Add "smartUI.project": "<Project Name>" as a capability above
# Step - 3 : Run "driver.execute_script("smartui.takeScreenshot")" command wherever you need to take a screenshot


class Login(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor="http://{}:{}@hub.lambdatest.com/wd/hub".format(
                username, access_key
            ),
            options=options,
        )

    # """ You can write the test cases here """
    def Login (self):
        # try:
        driver = self.driver
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)
        driver.set_window_size(1920, 1080)

        # Url
        print("Loading URL")
        driver.get(
            "https://v2-revamp-ui.d3c6j7b9bod0wf.amplifyapp.com/get-started"
        )

        # Click on Login
        driver.find_element(By.NAME, "li1").click()
        location = driver.find_element(By.NAME, "li2")
        location.click()
        print("Clicked on the sign up")

        # Take Smart UI screenshot
        driver.execute_script("smartui.takeScreenshot")

        # Enter Email
        driver.find_element(By.ID, "email").send_keys("doug@iwantchips.com")
        add_button = driver.find_element(By.ID, "addbutton")
        add_button.click()
        print("Entered email as doug@iwantchips.com")

        # Enter Password
        search = driver.find_element(By.CSS_SELECTOR, "password)
        assert search.is_displayed(), "Test123!"
        print(search.text)
        search.click()
        driver.implicitly_wait(3)

        # Click Login
        heading = driver.find_element(By.CSS_SELECTOR, "login")
        if heading.is_displayed():
            heading.click()
            driver.execute_script("lambda-status=passed")
            print("Logged In successfull")
        else:
            driver.execute_script("lambda-status=failed")

    # tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
