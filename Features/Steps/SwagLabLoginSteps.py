from behave import given, when, then
from Features.Pages.Home import SwagLabHomePage
from Features.Pages.Login import SwagLabLoginPage

@given(u'user is on swagLab login page')
def step_impl(context):
    context.driver.get("https://www.saucedemo.com")

@when(u'user enter username "{username}" on swagLab login page')
def step_impl(context,username):
    context.login=SwagLabLoginPage(context.driver)
    context.login.inpSwagLabLoginPageUN(username)

@when(u'user enter password "{password}" on swagLab login page')
def step_impl(context,password):
    context.login.inpSwagLabLoginPagePWD(password)


@when(u'user clicks login btn on swagLab login page')
def step_impl(context):
    context.login.clickSwagLabLoginPageLoginBtn()


@then(u'user should be on swagLab home page with logoText "{expLogoText}"')
def step_impl(context,expLogoText):
    home=SwagLabHomePage(context.driver)
    actLogoText=home.getSwagLabHomePageLogoText()
    assert actLogoText==expLogoText, "Failed-act & exp Logo text are different"


