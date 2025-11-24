import time
from behave import when, then

from Features.Pages.SwagLabsYourCartPage import SwagLabYourCartPage


@when(u'user is on SwagLab yourCart page')
def step_impl(context):
    context.youCart=SwagLabYourCartPage(context.driver)
    assert context.youCart.getSwagLabYourCartPageLogoTextVisible(), "Failed-yourCart page not visible"

@when(u'user click on checkout button')
def step_impl(context):
    context.youCart.clickSwagLabYourCartPagecheckoutBtn()


# @when(u'user is on SwagLab checkout yourInfo page')
# def step_impl(context):
#
#
#
# @when(u'user enter FN as "{firstName}"')
# def step_impl(context,firstName):
#
#
# @when(u'user enter LN as "{lastName}"')
# def step_impl(context,lastName):
#
#
#
# @when(u'user enter ZipCode "{ZipCode}"')
# def step_impl(context,ZipCode):
#
#
#
# @when(u'user click on continue button')
# def step_impl(context):
#
# @when(u'user is on SwagLab checkout Overview page')
# def step_impl(context):
#
#
# @when(u'user click on finish button')
# def step_impl(context):
#
#
# @when(u'user is on SwagLab checkout complete page')
# def step_impl(context):
#
#
# @then(u'order placed message visible')
# def step_impl(context):
#
