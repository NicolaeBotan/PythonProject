import datetime


def take_screenshot(driver):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"screenshots/screenshot_{timestamp}.png"
    driver.save_screenshot(file_name)
