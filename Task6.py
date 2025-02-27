import os
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, value):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((by, value))
        )

    def click(self, by, value):
        element = self.find_element(by, value)
        element.click()

    def send_keys(self, by, value, text):
        element = self.find_element(by, value)
        element.send_keys(text)


class GestureActions:
    def __init__(self, driver):
        self.driver = driver
        self.screen_size = self.driver.get_window_size()
        self.screen_width = self.screen_size['width']
        self.screen_height = self.screen_size['height']

    def validate_coordinates(self, x, y):
        if x < 0 or x > self.screen_width or y < 0 or y > self.screen_height:
            raise ValueError(
                f"Coordinates ({x}, {y}) are out of bounds for screen size ({self.screen_width}, {self.screen_height})")

    def swipe(self, start_x, start_y, end_x, end_y, duration=1000):
        self.validate_coordinates(start_x, start_y)
        self.validate_coordinates(end_x, end_y)
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def tap(self, x, y, duration=100):
        self.validate_coordinates(x, y)
        self.driver.tap([(x, y)], duration)

    def scroll(self, start_x, start_y, end_x, end_y, duration=1000):
        self.swipe(start_x, start_y, end_x, end_y, duration)


class MenuPage(BasePage, GestureActions):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        GestureActions.__init__(self, driver)


def get_driver():
    apk_path = os.path.abspath("resources/swaglabs.apk")
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "deviceName": "emulator-5554",  # Change to your actual device/emulator name
        "app": apk_path,
        "automationName": "UiAutomator2"
    })
    driver = webdriver.Remote("http://localhost:4723", options=options)
    time.sleep(5)
    return driver


def validate_item(driver, image_xpath, name_xpath, price_xpath):
    try:
        image = driver.find_element(AppiumBy.XPATH, image_xpath)
        name = driver.find_element(AppiumBy.XPATH, name_xpath)
        price = driver.find_element(AppiumBy.XPATH, price_xpath)
        print(f"✅ Item found: {name.text} - {price.text}")
    except Exception as e:
        print(f"❌ Error finding item details: {e}")


def load_and_validate_item(driver, image_xpath, name_xpath, price_xpath, swipe_coordinates):
    while True:
        swipe_coordinates()

        try:
            # Validate the specific item details
            validate_item(driver, image_xpath, name_xpath, price_xpath)
            break
        except Exception as e:
            print(f"❌ No item found: {e}")
            break


def main():
    driver = get_driver()
    try:
        print("✅ App launched successfully!")

        menu_page = MenuPage(driver)

        menu_page.swipe(100, 500, 100, 100)
        menu_page.tap(200, 300)

        time.sleep(2)

        # XPaths for the specific item
        image_xpath = "(//android.view.ViewGroup[@content-desc='store item'])[1]/android.view.ViewGroup[1]/android.widget.ImageView"
        name_xpath = "(//android.widget.TextView[@content-desc='store item text' and @text='Sauce Labs Backpack'])[1]"
        price_xpath = "(//android.widget.TextView[@content-desc='store item price' and @text='$29.99'])[1]"

        load_and_validate_item(driver, image_xpath, name_xpath, price_xpath,
                               lambda: menu_page.swipe(100, 500, 100, 100))

    except Exception as e:
        print(f"❌ Test failed: {e}")

    finally:
        driver.quit()
        print("🚪 App closed.")


if __name__ == "__main__":
    main()
