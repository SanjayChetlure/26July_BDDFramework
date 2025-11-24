from selenium.webdriver.common.by import By

#pom class2
class SwagLabHomePage:

    def __init__(self,driver):
        self.driver=driver


    logoTextXpath="//div[@class='app_logo']"
    addToCartBtn = "(//button[text()='Add to cart'])[1]"
    removeBtn = "//button[text()='Remove']"
    allProducts="//div[@class='inventory_item_name ']"
    SauceLabsBackPackProductPrice = "(//div[@class='inventory_item_price'])[1]"
    cartLink="//a[@class='shopping_cart_link']"


    def getSwagLabHomePageLogoText(self):
        actLogoText=self.driver.find_element(By.XPATH,self.logoTextXpath).text
        return actLogoText

    def getSwagLabHomePageLogoTextVisble(self):
        logoTextVisble=self.driver.find_element(By.XPATH,self.logoTextXpath).is_displayed()
        return logoTextVisble

    def clickSwagLabHomePageAddToCart(self):
        self.driver.find_element(By.XPATH,self.addToCartBtn).click()

    def getSwagLabHomePageRemoveBtnVisibleOrNot(self):
        actResult=self.driver.find_element(By.XPATH,self.removeBtn).is_displayed()
        return actResult

    def getSwagLabHomePageAllProductCount(self):
        actProduct=self.driver.find_elements(By.XPATH,self.allProducts)
        allProductsCount=len(actProduct)
        return allProductsCount

    def getSwagLabHomePageSauceLabsBackPackProductPrice(self):
        actProductPrice=self.driver.find_element(By.XPATH,self.SauceLabsBackPackProductPrice).text  #  $29.99
        actProductPrice=actProductPrice[1:]           #   29.99
        return actProductPrice

    def clickSwagLabHomePageCartLink(self):
        self.driver.find_element(By.XPATH, self.cartLink).click()
