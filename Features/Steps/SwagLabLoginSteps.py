from behave import given, when, then, Then
from Features.Pages.Home import SwagLabHomePage
from Features.Pages.Login import SwagLabLoginPage
from Utilities import ConfigReader


@given(u'user is on swagLab login page')
def step_impl(context):
    urlValue=ConfigReader.read_configuration("basic info","url")
    context.driver.get(urlValue)


@when(u'user enter username "{UN}" on swagLab login page')
def step_impl(context,UN):
    UNValue=ConfigReader.read_configuration("credentials", UN)
    context.loginPage=SwagLabLoginPage(context.driver)
    context.loginPage.inpSwagLabLoginPageUN(UNValue)

@when(u'user enter password "{PWD}" on swagLab login page')
def step_impl(context,PWD):
    PWDValue = ConfigReader.read_configuration("credentials", PWD)
    context.loginPage.inpSwagLabLoginPagePWD(PWDValue)


@when(u'user clicks login btn on swagLab login page')
def step_impl(context):
    context.loginPage.clickSwagLabLoginPageLoginBtn()


@then(u'user should be on swagLab home page with logoText "{expLogoText}"')
def step_impl(context,expLogoText):
    context.homePage=SwagLabHomePage(context.driver)
    actLogoText=context.homePage.getSwagLabHomePageLogoText()
    assert actLogoText==expLogoText, "Failed - act & exp logo text are diff"


@then(u'error message is visible')
def step_impl(context):
    actResult=context.loginPage.getSwagLabLoginPageErrorMsgDisplayed()
    assert actResult, "Failed- error msg not visible"

