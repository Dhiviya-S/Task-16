# Test Classes contains test scripts and calling actions
# Importing pytest and time
import pytest
import time
# Importing Class WorldPopulation from population_page under pages folder
from pages.population_page import WorldPopulation


# # To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestLogin:


    # test_population prints the population count which dynamically changes every second.
    # Printing stops when user presses Ctrl+C
    def test_population(self,setup):

        # This line creates an instance of the WorldPopulation class,and passes the WebDriver instance (self.driver) to it.
        population_count=WorldPopulation(self.driver)

        # 'try' block prints the population and when interruption occurs it moves to 'except' block
        try:
            # 'while' is used to print 'n' iterations
            while True:

               # population_count object calls world_count() to find the element 'World Population'
               # Value is stored in variable 'population' and prints the live value of population
               population=population_count.world_count()
               print(f"World Population Count:{population}")

               # time.sleep() is used to pause for 0.4seconds
               time.sleep(0.4)

        # When user presses Ctrl+C in Terminal the Keyboard interruption occurs so the printing stops
        except KeyboardInterrupt:
            print("User pressed Ctrl+C to exit")

#To generate HTML Report of Pytest cases:pytest -v -s tests/test_population.py --html=report.html
#report.html(to be opened in Browser)







