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

# Wait for the page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Rewards")))

# Click on the Rewards section
rewards_link = driver.find_element(By.LINK_TEXT, "Rewards")  # Adjust the identifier as needed
rewards_link.click()

# Wait for the Rewards page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Create New Award")))

# Click on Create New Award
create_new_award_button = driver.find_element(By.LINK_TEXT, "Create New Award")  # Adjust the identifier as needed
create_new_award_button.click()

# Wait for the Create New Award page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Chips")))

# Click on Chips
chips_button = driver.find_element(By.LINK_TEXT, "Chips")  # Adjust the identifier as needed
chips_button.click()

# Wait for the Chips Award form to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "consumer_user_radio")))

# Choose Consumer user radio button
consumer_user_radio = driver.find_element(By.ID, "consumer_user_radio")  # Adjust the identifier as needed
consumer_user_radio.click()

# Click "Buys" in "When User" dropdown
when_user_dropdown = driver.find_element(By.ID, "when_user_dropdown")  # Adjust the identifier as needed
when_user_dropdown.click()
buys_option = driver.find_element(By.XPATH, "//option[text()='Buys']")  # Adjust the XPath as needed
buys_option.click()

# Selecting Date
date_picker = driver.find_element(By.ID, "date_picker")  # Adjust the identifier as needed
date_picker.send_keys("2023-10-01")  # Adjust the date format as needed

# Selecting Location
location_dropdown = driver.find_element(By.ID, "location_dropdown")  # Adjust the identifier as needed
location_dropdown.click()
location_option = driver.find_element(By.XPATH, "//option[text()='Location Name']")  # Adjust the XPath as needed
location_option.click()

# Selecting Chip Quantity
chip_quantity = driver.find_element(By.ID, "chip_quantity")  # Adjust the identifier as needed
chip_quantity.send_keys("100")  # Enter the desired chip quantity

# Selecting Image
image_upload = driver.find_element(By.ID, "image_upload")  # Adjust the identifier as needed
image_upload.send_keys("/path/to/your/image.png")  # Enter the path to your image file

# Clicking Save
save_button = driver.find_element(By.ID, "save_button")  # Adjust the identifier as needed
save_button.click()

# Verify success message or redirect (optional)
# success_message = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "success-message"))  # Adjust the identifier as needed
# )
# assert "Award created successfully" in success_message.text

print("Award created successfully")

# Close the browser
driver.quit()

    # tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
