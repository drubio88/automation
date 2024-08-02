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
# Note: for additional capabilities navigate to https://www.lambdatest.com/support/docs/test-settings-options/


class ViewMembershipTypes (unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor="http://{}:{}@hub.lambdatest.com/wd/hub".format(
                username, access_key
            ),
            options=options,
        )

    # """ You can write the test cases here """
   # Let's click on a element
        driver.find_element(By.NAME, "li1").click()
        location = driver.find_element(By.NAME, "li2")
        location.click()
        print("Clicked on the second element")

        # Take Smart UI screenshot
        # driver.execute_script("smartui.takeScreenshot")

        # Let's add a checkbox
        driver.find_element(By.ID, "sampletodotext").send_keys("LambdaTest")
        add_button = driver.find_element(By.ID, "addbutton")
        add_button.click()
        print("Added LambdaTest checkbox")

        # Find and fill the username field
username_field = driver.find_element(By.ID, "username")  # Adjust the identifier as needed
username_field.send_keys(username)

# Find and fill the password field
password_field = driver.find_element(By.ID, "password")  # Adjust the identifier as needed
password_field.send_keys(password)

# Find and click the login button
login_button = driver.find_element(By.ID, "loginButton")  # Adjust the identifier as needed
login_button.click()

# Wait for the page to load
time.sleep(5)  # Adjust the sleep time as needed

# Click on the Rewards section
rewards_link = driver.find_element(By.LINK_TEXT, "Rewards")  # Adjust the identifier as needed
rewards_link.click()

# Wait for the Rewards page to load
time.sleep(5)  # Adjust the sleep time as needed

# Verify membership types on the screen
# Replace 'membership-type' with the actual class, ID, or XPath of the membership elements
membership_elements = driver.find_elements(By.CLASS_NAME, "membership-type")

# Extract and print the membership types
for membership in membership_elements:
    print(membership.text)

# Verify the expected membership types
expected_membership_types = ["Gold", "Silver", "Bronze"]  # Add your expected membership types

        # Take Smart UI screenshot
        driver.execute_script("smartui.takeScreenshot")

        # Let

    # tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
