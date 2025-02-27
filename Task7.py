import os
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Get the absolute path of the APK
apk_path = os.path.abspath("resources/swaglabs.apk")

# Define Appium options
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "deviceName": "emulator-5554",  # Change based on your device/emulator
    "app": apk_path,
    "automationName": "UiAutomator2"
})

# Initialize Appium driver
driver = webdriver.Remote("http://localhost:4723", options=options)
time.sleep(5)  # Allow app to load

try:
    print("✅ App launched successfully!")

    # Step 1: Open the menu
    menu_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='open menu']/android.widget.ImageView"))
    )
    menu_icon.click()
    print("✅ Opened menu.")

    time.sleep(2)

    # Step 2: Click "Log In"
    login_button_from_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='menu item log in']"))
    )
    login_button_from_menu.click()
    print("✅ Clicked Log In.")

    # Step 3: Enter login details
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Username input field"))).send_keys("bob@example.com")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Password input field"))).send_keys("10203040")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Login button"))).click()
    print("✅ Logged in.")

    # Validate login success
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Products"]')))
    print("🎉 Logged in successfully!")

    # Step 4: Add a product to the cart
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='store item']"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Add To Cart button"))).click()
    print("✅ Product added to cart.")

    # Step 5: Go to cart and proceed to checkout
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "cart badge"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Proceed To Checkout button"))).click()
    print("✅ Navigated to checkout.")

    # Step 6: Enter shipping details (handle stale element exception)
    shipping_fields = {
        "Full Name* input field": "Bob Smith",
        "Address Line 1* input field": "123 Main Street",
        "City* input field": "Los Angeles",
        "Zip Code* input field": "90001",
        "Country* input field": "USA"
    }

    for field, value in shipping_fields.items():
        input_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, field))
        )
        input_element.clear()  # Ensure field is empty before input
        input_element.send_keys(value)
        print(f"✅ Entered {field}: {value}")

    # Click 'To Payment' button
    to_payment_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "To Payment button"))
    )
    to_payment_btn.click()
    print("✅ Proceeded to Payment.")

    # Step 7: Enter payment details
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Full Name* input field"))).send_keys("Bob Smith")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Card Number* input field"))).send_keys("4111111111111111")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Expiration Date* input field"))).send_keys("12/28")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Security Code* input field"))).send_keys("123")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Review Order button"))).click()
    print("✅ Entered payment details.")

    # Step 8: Review order and place it
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Review your order"]')))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Place Order button"))).click()
    print("✅ Order placed.")

    # Step 9: Validate order confirmation
    confirmation_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Your new swag is on its way"]'))
    )
    if confirmation_message.is_displayed():
        print("🎉 Order placed successfully!")

    # Step 10: Continue shopping
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Continue Shopping button"))).click()
    print("✅ Continued shopping.")

except Exception as e:
    print(f"❌ Test failed: {e}")

finally:
    driver.quit()
    print("🚪 App closed.")
