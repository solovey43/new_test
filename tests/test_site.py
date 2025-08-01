from selenium.webdriver.common.by import By
import time



def test_open_s6(driver):
    driver.get('https://demoqa.com/')
    link_1 = driver.find_element(By.CLASS_NAME, 'banner-image')
    link_1.click()
    button = driver.find_element(By.XPATH,'//h5[text()="Elements"]/parent::div')
    assert button.text == 'Elements'

def test_cost(driver):
    driver.get('https://demoqa.com/')
    button1 = driver.find_element(By.XPATH, '//div[@class="avatar mx-auto white"]')
    button1.click()
    time.sleep(3)
    buttons = driver.find_elements(By.CLASS_NAME,'btn btn-light')
    assert len(buttons) == 6





