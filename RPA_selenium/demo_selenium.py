from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()   # ✅ Correct
driver.get("https://demo.opencart.com/")
# driver.back                   # Navigations
# driver.forward
# driver.refresh

#finding elements
element = driver.find_elements(By.ID,"content")
element = driver.find_elements(By.XPATH, '//*[@id="content"]/h3')

#wait
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located(By.ID, "content"))

#interactions
# element.click()
# element.send_keys("ai tech")
# element.clear()

# #screenshots
# driver.screenshots("demo.png")





