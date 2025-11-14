from selenium.webdriver.common.by import By

#pom class2
class SwagLabHomePage:

    def __init__(self,driver):
        self.driver=driver


    logoTextXpath="//div[@class='app_logo']"


    def getSwagLabHomePageLogoText(self):
        actLogoText=self.driver.find_element(By.XPATH,self.logoTextXpath).text
        return actLogoText
