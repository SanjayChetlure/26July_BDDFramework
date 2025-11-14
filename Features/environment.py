from selenium import webdriver

# def before_all(context):
#     print("Starting test execution: opening browser")
#     context.driver=webdriver.Firefox()
#
# def after_all(context):
#     print("Starting test execution: opening browser")
#     context.driver.quite()

def before_scenario(context, scenario):
    print("Starting test execution: opening browser")
    context.driver = webdriver.Firefox()
    context.driver.maximize_window()


def after_scenario(context, scenario):
    print("Starting test execution: opening browser")
    context.driver.quit()


# def before_step(context, step):
#     print(f"Starting step:")
#
# def after_step(context, step):
#     print(f"Finished step:")
