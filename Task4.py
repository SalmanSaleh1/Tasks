import os
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Get the absolute path of the APK using relative path
apk_path = os.path.abspath("resources/swaglabs.apk")

# Define desired capabilities using AppiumOptions
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "deviceName": "emulator-5554",  # Change to your actual device/emulator name
    "app": apk_path,  # ✅ Using relative path for the APK
    "automationName": "UiAutomator2"
})

# Initialize the Appium driver
driver = webdriver.Remote("http://localhost:4723", options=options)
time.sleep(5)  # Wait for app to load

try:
    print("✅ App launched successfully!")

    # First step: Click the menu icon to open the menu
    menu_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='open menu']/android.widget.ImageView"))
    )
    menu_icon.click()
    print("✅ Clicked on menu icon.")

    # Wait a little more to ensure the menu fully opens
    time.sleep(2)

    # Second step: Click on the "Log In" button using content-desc
    login_button_from_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='menu item log in']"))
    )
    login_button_from_menu.click()
    print("✅ Clicked on Log In button.")

    # Wait for the username field
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Username input field"))  # Use ACCESSIBILITY_ID if available
    )
    username_field.send_keys("bob@example.com")
    print("✅ Entered username.")

    # Wait for the password field
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Password input field"))  # Use ACCESSIBILITY_ID for password
    )
    password_field.send_keys("10203040")
    print("✅ Entered password.")

    # Wait for the login button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Login button"))  # Use ACCESSIBILITY_ID for login button
    )
    login_button.click()
    print("✅ Clicked login button.")

    # Validate successful login by checking the "PRODUCTS" page title
    products_title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Products"]'))
    )

    if products_title.is_displayed():
        print("🎉 Login Successful! PRODUCTS page is visible.")

except Exception as e:
    print(f"❌ Test failed: {e}")

finally:
    # Close the Appium session
    driver.quit()
    print("🚪 App closed.")
