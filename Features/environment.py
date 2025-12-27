from datetime import datetime

import allure
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

    defaultBrowserName=ConfigReader.read_configuration("basic info","browser")

    # Get browser from CLI parameter, default browser name get it from config.ini
    browserName = context.config.userdata.get("browser", defaultBrowserName).lower()

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
    if scenario.status == "failed":
        scenario_name = scenario.name.replace(" ", "_").replace('"', "").replace("'", "")   # Clean scenario name to avoid invalid file characters
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")                              # get current date time Timestamp
        file_path = f"screenshots/Failed_{scenario_name}_{timestamp}.png"                    # Final filename format
        context.driver.save_screenshot(file_path)

        # Attach screenshot to the Allure report
        with open(file_path, "rb") as f:
            allure.attach(
                f.read(),
                name=file_path,
                attachment_type=allure.attachment_type.PNG
            )



    context.driver.quit()



# def after_step(context, step):
#     if step.status == "failed":
#         safe_name = step.name.replace(" ", "_").replace('"', "").replace("'", "")
#         context.driver.save_screenshot(f"screenshots/{safe_name}.png")

# def after_step(context, step):
#     step_name = step.name.replace(" ", "_").replace('"', "").replace("'", "")
#     context.driver.save_screenshot(f"screenshots/{step_name}.png")

# def before_step(context, step):
#     print(f"Starting step:")
#
# def after_step(context, step):
#     print(f"Finished step:")
