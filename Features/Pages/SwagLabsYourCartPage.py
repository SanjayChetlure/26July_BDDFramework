from selenium.webdriver.common.by import By

#pom/page class1
class SwagLabYourCartPage:

    def __init__(self,driver):
        self.driver=driver

    CartPageLogoText="//span[text()='Your Cart']"
    checkout="//button[text()='Checkout']"

    def getSwagLabYourCartPageLogoTextVisible(self):
        return self.driver.find_element(By.XPATH,self.CartPageLogoText).is_displayed()

    def clickSwagLabYourCartPagecheckoutBtn(self):
        self.driver.find_element(By.XPATH,self.checkout).click()

