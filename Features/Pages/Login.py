from selenium.webdriver.common.by import By

#pom/page class1
class SwagLabLoginPage:

    def __init__(self,driver):
        self.driver=driver               #convert local object/variable into class object/variable

    usernameXpath="//input[@id='user-name']"
    passwordXpath="//input[@id='password']"
    loginBtnXpath="//input[@id='login-button']"
    loginFailedErrorMsg="//h3[contains(text(),'Username and password do not match')]"


    def inpSwagLabLoginPageUN(self,UN):
        self.driver.find_element(By.XPATH,self.usernameXpath).send_keys(UN)

    def inpSwagLabLoginPagePWD(self,PWD):
        self.driver.find_element(By.XPATH,self.passwordXpath).send_keys(PWD)

    def clickSwagLabLoginPageLoginBtn(self):
        self.driver.find_element(By.XPATH,self.loginBtnXpath).click()

    def getSwagLabLoginPageErrorMsgDisplayed(self):
        result=self.driver.find_element(By.XPATH,self.loginFailedErrorMsg).is_displayed()
        return result
