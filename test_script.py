import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome WebDriver using WebDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

# Open a website (Google as an example)
driver.get("https://www.google.com")
driver.maximize_window()

time.sleep(2)
# Print the title of the page
print("Current Title is " + driver.title)
print("Current URL is " + driver.current_url)

# Close the browser
driver.quit()
