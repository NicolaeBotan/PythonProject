import utils
from base_webdriver import get_driver

driver = get_driver()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
print(driver.title)

driver.find_element_by_xpath("//input[@id='user-name']").send_keys("standard_user")
driver.find_element_by_xpath("//input[@id='password']").send_keys("secret_sauce")
driver.find_element_by_xpath("//input[@id='login-button']").click()

elements = driver.find_elements_by_xpath("//div[@class='inventory_item_name ']")
expected_text = "Sauce Labs Onesie"

for element in elements:
    if element.text.strip() == expected_text:
        element.click()
        break
driver.find_element_by_xpath("//button[@id='add-to-cart']").click()
driver.back()

utils.take_screenshot(driver)
driver.quit()
