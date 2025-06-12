# Population page contains locators and methods to interact with World Population Count webpage
# Importing By classes from selenium for locators
from selenium.webdriver.common.by import By
# To use the methods from base_page importing Class BasePage.
# from folder_name.file_name import Class_name
from pages.base_page import BasePage


# PopulationPage inherits BasePage.PopulationPage contains locators and methods to interact with locators.
class WorldPopulation(BasePage):


    # LOCATOR - POPULATION_COUNT uses XPATH to locate the element
    POPULATION_COUNT= (By.XPATH, '//div[@class="counter-ticker is-size-2-mobile"]')


    # METHOD-Uses find_element() from BasePage to locate the element and 'text' to access the value
    def world_count(self):
     return self.find_element(self.POPULATION_COUNT).text
