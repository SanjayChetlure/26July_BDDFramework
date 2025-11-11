from selenium.webdriver.common.by import By

#pom/page class1
class SwagLabLoginPage:

    def __init__(self,driver):
        self.driver=driver               #convert local object/variable into class object/variable

    usernameXpath="//input[@id='user-name']"
    passwordXpath="//input[@id='password']"
    loginBtnXpath="//input[@id='login-button']"


    def inpSwagLabLoginPageUN(self):
        self.driver.find_element(By.XPATH,self.usernameXpath).send_keys("standard_user")

    def inpSwagLabLoginPagePWD(self):
        self.driver.find_element(By.XPATH,self.passwordXpath).send_keys("secret_sauce")

    def clickSwagLabLoginPageLoginBtn(self):
        self.driver.find_element(By.XPATH,self.loginBtnXpath).click()
