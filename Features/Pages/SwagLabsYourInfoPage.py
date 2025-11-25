from selenium.webdriver.common.by import By

class SwagLabsYourInfoPage:

    def __init__(self,driver):
        self.driver=driver

    YourInfoPageLogoText="//span[text()='Checkout: Your Information']"
    FN = "//input[@id='first-name']"
    LN="//input[@id='last-name']"
    ZipCode = "//input[@id='postal-code']"
    continueBtn="//input[@id='continue']"

    def getSwagLabsYourInfoPageLogoTextVisible(self):
        return self.driver.find_element(By.XPATH,self.YourInfoPageLogoText).is_displayed()

    def inpSwagLabsYourInfoPageFN(self,firstName):
         self.driver.find_element(By.XPATH,self.FN).send_keys(firstName)

    def inpSwagLabsYourInfoPageLN(self,lastName):
         self.driver.find_element(By.XPATH,self.LN).send_keys(lastName)

    def inpSwagLabsYourInfoPagePostalCode(self,postalCode):
         self.driver.find_element(By.XPATH,self.ZipCode).send_keys(postalCode)

    def clickSwagLabsYourInfoPageContinueBtn(self):
        self.driver.find_element(By.XPATH,self.continueBtn).click()