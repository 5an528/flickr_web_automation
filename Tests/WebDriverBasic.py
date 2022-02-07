from selenium import webdriver

driver = webdriver.Chrome(executable_path="F:/chromedriver.exe")

driver.get("http://www.flickr.com/")

driver.maximize_window()

print(driver.title)

print(driver.current_url)






