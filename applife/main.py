from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Replace '/path/to/chromedriver' with the actual path to your Chrome WebDriver executable
driver = webdriver.Chrome('/path/to/chromedriver')

# Open Google in the browser
driver.get('https://www.google.com')

# Get user input for name and school
name = input("Enter your name: ")
school = input("Enter your school: ")

# Find the search bar and enter the name
search_bar = driver.find_element_by_name('q')
search_bar.send_keys(name)
search_bar.send_keys(Keys.RETURN)

time.sleep(2)

try:
    # Locate the search result containing the school and extract the information
    search_result = driver.find_element_by_xpath('//div[@class="tF2Cxc"]/div[@class="yuRUbf"]/a/h3')
    search_result.click()

    # Wait for the page to load
    time.sleep(2)

    # Assuming the school information is in a specific element on the page
    school_element = driver.find_element_by_xpath('//div[@class="school-info"]/span')
    current_school = school_element.text

    # Compare the extracted school with the user-provided school
    if current_school.lower() == school.lower():
        print(f"Congratulations, {name}! Your current school matches the input: {current_school}")
    else:
        print(f"Sorry, {name}. The current school extracted from the search results doesn't match the input.")

except Exception as e:
    print("Failed to extract school information or perform comparison:", e)

driver.quit()
