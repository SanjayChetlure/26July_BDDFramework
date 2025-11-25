import time
from behave import when, then

from Features.Pages.SwagLabsCheckoutCompletePage import SwagLabsCheckoutCompletePage
from Features.Pages.SwagLabsOverviewPage import SwagLabsOverviewPage
from Features.Pages.SwagLabsYourCartPage import SwagLabYourCartPage
from Features.Pages.SwagLabsYourInfoPage import SwagLabsYourInfoPage


@when(u'user is on SwagLab yourCart page')
def step_impl(context):
    context.youCart=SwagLabYourCartPage(context.driver)
    assert context.youCart.getSwagLabYourCartPageLogoTextVisible(), "Failed-yourCart page not visible"

@when(u'user click on checkout button')
def step_impl(context):
    context.youCart.clickSwagLabYourCartPagecheckoutBtn()


@when(u'user is on SwagLab checkout yourInfo page')
def step_impl(context):
    context.youInfo=SwagLabsYourInfoPage(context.driver)
    assert context.youInfo.getSwagLabsYourInfoPageLogoTextVisible(), "Failed-Your Info page not visible"


@when(u'user enter FN as "{firstName}"')
def step_impl(context,firstName):
    context.youInfo.inpSwagLabsYourInfoPageFN(firstName)

@when(u'user enter LN as "{lastName}"')
def step_impl(context,lastName):
    context.youInfo.inpSwagLabsYourInfoPageLN(lastName)

@when(u'user enter ZipCode "{ZipCode}"')
def step_impl(context,ZipCode):
    context.youInfo.inpSwagLabsYourInfoPagePostalCode(ZipCode)


@when(u'user click on continue button')
def step_impl(context):
    context.youInfo.clickSwagLabsYourInfoPageContinueBtn()

@when(u'user is on SwagLab checkout Overview page')
def step_impl(context):
    context.overview=SwagLabsOverviewPage(context.driver)
    assert context.overview.getSawgLabsOverviewPageLogoTextVisible(),"Failed-overview page not visible"


@when(u'user click on finish button')
def step_impl(context):
    context.overview.clickSawgLabsOverviewPageFinishBtn()


@when(u'user is on SwagLab checkout complete page')
def step_impl(context):
    context.checkoutComplete=SwagLabsCheckoutCompletePage(context.driver)
    assert  context.checkoutComplete.getSwagLabsCheckoutCompletePageLogoTextVisible(),"Failed-checkout complete page not visible"

@then(u'order placed message visible')
def step_impl(context):
    assert context.checkoutComplete.getSwagLabsCheckoutCompletePageOrderCompleteMsgVisble(),"failed-order complete msg not visible"

