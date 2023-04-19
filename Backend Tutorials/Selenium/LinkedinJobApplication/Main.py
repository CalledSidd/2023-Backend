from selenium import webdriver

chrome_drive_path = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(executable_path = chrome_drive_path)

driver.get("https://linkedin.com")




driver.close()