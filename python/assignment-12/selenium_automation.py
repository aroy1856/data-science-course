from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create WebDriver instance using webdriver.Chrome()
driver = webdriver.Chrome()

# Open web pages like Amazon using driver.get()
driver.get("https://www.amazon.in")

# Use driver.maximize_window() to maximize browser window
driver.maximize_window()

# Use time.sleep() for wait handling
time.sleep(5)
# Locate elements using locators like By.NAME, By.CLASS_NAME, By.LINK_TEXT, and By.XPATH
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
# Perform search operation using send_keys()
search_box.send_keys("iphone")

time.sleep(5)
# Click elements using click() method
driver.find_element(By.ID, "nav-search-submit-button").click()

# Refresh web page using driver.refresh()
time.sleep(5)
driver.refresh()

# Extract multiple elements using find_elements()
time.sleep(5)
titles = driver.find_elements(By.XPATH, "//h2[@class='a-size-medium a-spacing-none a-color-base a-text-normal']")


# Display extracted data in console using print()
for title in titles:
    print(title.get_attribute("aria-label"))

time.sleep(10)
# Close browser using driver.quit()
driver.quit()

