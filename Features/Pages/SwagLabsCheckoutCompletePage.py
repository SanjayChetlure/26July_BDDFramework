from selenium.webdriver.common.by import By


class SwagLabsCheckoutCompletePage:

    def __init__(self, driver):
        self.driver = driver

    checkoutCompletePageLogoText = "//span[text()='Checkout: Complete!']"
    orderCompleteMsg = "//h2[text()='Thank you for your order!']"

    def getSwagLabsCheckoutCompletePageLogoTextVisible(self):
        return self.driver.find_element(By.XPATH, self.checkoutCompletePageLogoText).is_displayed()

    def getSwagLabsCheckoutCompletePageOrderCompleteMsgVisble(self):
        return self.driver.find_element(By.XPATH, self.orderCompleteMsg).is_displayed()