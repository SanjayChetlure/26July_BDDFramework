import time
from selenium import webdriver
import Login
import Home

driver=webdriver.Firefox()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

loginObj=Login.SwagLabLoginPage(driver)
loginObj.inpSwagLabLoginPageUN("standard_user")
loginObj.inpSwagLabLoginPagePWD("ckbsdvdsv")
loginObj.clickSwagLabLoginPageLoginBtn()
time.sleep(1)
actResult=loginObj.getSwagLabLoginPageErrorMsgDisplayed()

if actResult:
    print("PASS- Error msg present")
else:
    print("FAIL- Error msg not present")


time.sleep(5)


