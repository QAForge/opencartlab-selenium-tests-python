from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://oc3032std.opencartlab.pl/")
assert "Sklep demonstracyjny" in driver.title
driver.quit()