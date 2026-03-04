from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

wait = WebDriverWait(driver, 20)

# ==================================
# 1️⃣ Open Website
# ==================================
driver.get("https://the-internet.herokuapp.com/")
wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
print("✔ Homepage Loaded")

# ==================================
# 2️⃣ Click Form Authentication
# ==================================
driver.find_element(By.LINK_TEXT, "Form Authentication").click()
wait.until(EC.presence_of_element_located((By.ID, "login")))
print("✔ Login Page Opened")

# ==================================
# 3️⃣ Perform Login
# ==================================
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

wait.until(EC.presence_of_element_located((By.CLASS_NAME, "flash")))
print("✔ Login Successful")

# ==================================
# 4️⃣ Logout
# ==================================
driver.find_element(By.LINK_TEXT, "Logout").click()
wait.until(EC.presence_of_element_located((By.ID, "login")))
print("✔ Logout Successful")

# ==================================
# 5️⃣ Verify Title
# ==================================
assert "The Internet" in driver.title
print("✔ Title Verified")

driver.quit()

print("\n🎉 ALL TESTS PASSED SUCCESSFULLY")