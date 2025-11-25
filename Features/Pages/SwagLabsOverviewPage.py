from selenium.webdriver.common.by import By


class SwagLabsOverviewPage:

    def __init__(self,driver):
        self.driver=driver

    overviewPageLogoText="//span[text()='Checkout: Overview']"
    finish="//button[text()='Finish']"

    def getSawgLabsOverviewPageLogoTextVisible(self):
        return self.driver.find_element(By.XPATH,self.overviewPageLogoText).is_displayed()

    def clickSawgLabsOverviewPageFinishBtn(self):
         self.driver.find_element(By.XPATH,self.finish).click()

