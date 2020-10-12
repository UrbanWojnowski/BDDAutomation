from selenium.webdriver import Chrome

# def before_feature(context,feature):
# def before_scenario(context, scenario):
# before_tag, before_step


def before_all(context):
    path = 'C:\\Python38\\chromedriver.exe'
    context.driver = Chrome(executable_path=path)

# def after_feature(context,feature):
# def after_scenario(context,scenario):


def after_all(context):
    context.driver.close()
