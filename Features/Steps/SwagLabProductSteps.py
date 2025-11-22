import time

from behave import when, then

from Features.Pages.Home import SwagLabHomePage


@when(u'user wait for "{timeInSec}" sec')
def step_impl(context,timeInSec):
    time.sleep(int(timeInSec))


@when(u'user is on SwagLab home page')
def step_impl(context):
    context.homePage = SwagLabHomePage(context.driver)
    assert context.homePage.getSwagLabHomePageLogoTextVisble(), "Failed-Home page not visible"


@when(u'user click on addToCart btn')
def step_impl(context):
    context.homePage.clickSwagLabHomePageAddToCart()


@then(u'remove btn is visible')
def step_impl(context):
    actResult=context.homePage.getSwagLabHomePageRemoveBtnVisibleOrNot()
    assert actResult,"Failed-Remove btn is not visible"


@then(u'verify total "{expProductCount}" products are available on home page')
def step_impl(context,expProductCount):
    actProductCount=context.homePage.getSwagLabHomePageAllProductCount()
    assert actProductCount==int(expProductCount), "Failed-act & exp product count"


@then(u'verify price of product Sauce Labs Backpack is "{expProductPrice}"')
def step_impl(context,expProductPrice):
    actProductPrice=context.homePage.getSwagLabHomePageSauceLabsBackPackProductPrice()
    assert actProductPrice==expProductPrice,"Failed-Remove btn is not visible"



