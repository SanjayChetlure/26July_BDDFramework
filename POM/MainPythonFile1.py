import time
from selenium import webdriver
import Login
import Home


driver=webdriver.Firefox()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

login=Login.SwagLabLoginPage(driver)
login.inpSwagLabLoginPageUN("standard_user")
login.inpSwagLabLoginPagePWD("secret_sauce")
login.clickSwagLabLoginPageLoginBtn()
time.sleep(3)
home=Home.SwagLabHomePage(driver)
actLogoText=home.getSwagLabHomePageLogoText()
expLoloText="Swag Labs"

if actLogoText==expLoloText:
    print("PASS")
else:
    print("FAIL")

time.sleep(3)
driver.quit()




