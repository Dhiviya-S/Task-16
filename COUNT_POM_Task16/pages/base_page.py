# BASE PAGE FOR WORLD POPULATION COUNT LIVE
# Page classes represents the webpage.
# Importing WebDriverWait is used to explicitly wait for elements to appear, disappear,clickable
# Explicit wait is used to wait for specific condition to occur before proceeding to next.
from selenium.webdriver.support.ui import WebDriverWait
# Importing expected_conditions like url contains,presence of element,visibility of element
from selenium.webdriver.support import expected_conditions as EC


# BasePage class contains method to find the element
class BasePage:


    # Constructor method used to interact with Selenium Webdriver. Driver is passed from 'setup' code
    def __init__(self, driver):
        self.driver = driver


    # Finding the element using the locator with timeout of 5 seconds using explicit wait
    def find_element(self, locator, timeout=5):
        # Explicit wait until the element is located else raises TimeOutException
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

