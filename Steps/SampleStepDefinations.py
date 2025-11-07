from behave import given, when, then

@given('user open browser')
def step_impl(context):
    print("open browser")

@when('user enter url')
def step_impl(context):
    print("enter url")

@when('user enter username')
def step_impl(context):
    print("enter UN")

@when('user enter password')
def step_impl(context):
    print("enter pwd")

@when('user click on login btn')
def step_impl(context):
    print("click on login btn")

@then('user should be at home page')
def step_impl(context):
    print("home page visble")


@when('user enter invalid username')
def step_impl(context):
    print("enter invalid UN")


@when('user enter invalid password')
def step_impl(context):
    print("enter invalid PWD")


@then('user can see error msg')
def step_impl(context):
    print("login failed - error msg visible")

