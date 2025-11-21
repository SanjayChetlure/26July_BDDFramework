from selenium.webdriver.common.by import By

#pom class2
class SwagLabHomePage:

    def __init__(self,driver):
        self.driver=driver


    logoTextXpath="//div[@class='app_logo']"
    addToCartBtn = "(//button[text()='Add to cart'])[1]"
    removeBtn = "//button[text()='Remove']"


    def getSwagLabHomePageLogoText(self):
        actLogoText=self.driver.find_element(By.XPATH,self.logoTextXpath).text
        return actLogoText

    def clickSwagLabHomePageAddToCart(self):
        self.driver.find_element(By.XPATH,self.addToCartBtn).click()

    def getSwagLabHomePageRemoveBtnVisibleOrNot(self):
        actResult=self.driver.find_element(By.XPATH,self.removeBtn).is_displayed()
        return actResult
