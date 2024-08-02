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


class FirstSampleTest(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor="http://{}:{}@hub.lambdatest.com/wd/hub".format(
                username, access_key
            ),
            options=options,
        )

    # """ You can write the test cases here """
    def test_demo_site(self):
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

       # Find and fill the username field
username_field = driver.find_element(By.ID, "username")  # Adjust the identifier as needed
username_field.send_keys(username)

# Find and fill the password field
password_field = driver.find_element(By.ID, "password")  # Adjust the identifier as needed
password_field.send_keys(password)

# Find and click the login button
login_button = driver.find_element(By.ID, "loginButton")  # Adjust the identifier as needed
login_button.click()

# Wait for the page to load (you can use explicit waits for better reliability)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Rewards")))

# Click on the Rewards section
rewards_link = driver.find_element(By.LINK_TEXT, "Rewards")  # Adjust the identifier as needed
rewards_link.click()

# Wait for the Rewards page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "reward-type")))

# Verify reward types on the screen
# Replace 'reward-type' with the actual class, ID, or XPath of the reward elements
reward_elements = driver.find_elements(By.CLASS_NAME, "reward-type")

# Extract and print the reward types
for reward in reward_elements:
    print(reward.text)

# Define the expected reward types
expected_reward_types = [
    "Chips Rewards",
    "Your Product Rewards",
    "Discount",
    "Your Membership Rewards",
    "Your Contest Rewards"
]

# Get the text of actual reward types on the page
reward_texts = [reward.text for reward in reward_elements]

# Check if the expected reward types are displayed
for reward_type in expected_reward_types:
    assert reward_type in reward_texts, f"{reward_type} not found on the page"

print("All expected reward types are displayed.")

# Close the browser
driver.quit()")

    # tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
