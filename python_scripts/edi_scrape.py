import selenium

driver = selenium.webdriver.Chrome()

driver.get("https://edi.evc-net.com/")

username_input = driver.find_element_by_id("username")
username_input.send_keys("bartland@gmail.com")

password_input = driver.find_element_by_id("password")
password_input.send_keys("!Hu2Su5!@WTyzhP")

login_button = driver.find_element_by_class_name("btn-primary")
login_button.click()
