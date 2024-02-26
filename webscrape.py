import selenium
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains

# Series of methods to ensure that the developer version of Selenium and Chrome WebDriver work
# for the newest versions of Google Chrome.
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service = service, options = options)

# Function to open wordle and keep the tab open.
def openwordle():
    driver.get('https://wordlegame.org/') 
    time.sleep(1)

# Function that receives a guess, inputs it into the game, and then returns
def make_guess(guess_word):
    ActionChains(driver)\
        .send_keys(f"{guess_word}")\
        .send_keys(Keys.ENTER)\
        .perform()
    time.sleep(1)
    y = 1
    game_row = driver.find_element(By.XPATH, f"//*[@id='game-wrapper']/div[1]/div[{y}]")
    y += 1
    tiles = game_row.find_elements(By.CLASS_NAME, "Row-letter")
    evaluations = [result.get_attribute("Class") for result in tiles]
    result_string = ""
    i = 0
    while i < 5:
        if evaluations[i] == "Row-letter letter-absent":
            result_string += "0"
        elif evaluations[i] == "Row-letter letter-elsewhere":
            result_string += "1"
        elif evaluations[i] == "Row-letter letter-correct":
            result_string += "2"
        i += 1
    print(result_string)
    return(result_string)
    
to_guess = "salet"
openwordle()
make_guess(to_guess)


input("Press Enter to close the browser...")
driver.quit()


