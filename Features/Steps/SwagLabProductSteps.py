import time

from behave import when, then

from Features.Pages.Home import SwagLabHomePage


@when(u'user wait for "{timeInSec}" sec')
def step_impl(context,timeInSec):
    time.sleep(int(timeInSec))


@when(u'user click on addToCart btn')
def step_impl(context):
    context.homePage = SwagLabHomePage(context.driver)
    context.homePage.clickSwagLabHomePageAddToCart()


@then(u'remove btn is visible')
def step_impl(context):
    actResult=context.homePage.getSwagLabHomePageRemoveBtnVisibleOrNot()
    assert actResult,"Failed-Remove btn is not visible"



