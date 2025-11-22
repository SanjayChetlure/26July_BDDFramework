from selenium import webdriver

from Utilities import ConfigReader


# def before_all(context):
#     print("Starting test execution: opening browser")
#     context.driver=webdriver.Firefox()
#
# def after_all(context):
#     print("Starting test execution: opening browser")
#     context.driver.quite()

def before_scenario(context, scenario):
    print("Starting test execution: opening browser")

    browserName=ConfigReader.read_configuration("basic info","browser")

    if browserName=="chrome":
        context.driver = webdriver.Chrome()
    elif browserName=="firefox":
        context.driver = webdriver.Firefox()
    elif browserName=="edge":
        context.driver = webdriver.Edge()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


def after_scenario(context, scenario):
    print("Starting test execution: opening browser")
    context.driver.quit()


def after_step(context, step):
    if step.status == "failed":
        context.driver.save_screenshot(f"screenshots/{step.name}.png")

# def before_step(context, step):
#     print(f"Starting step:")
#
# def after_step(context, step):
#     print(f"Finished step:")
