from selenium import webdriver

def get_webdriver():
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return webdriver.Chrome("C:/Work/courses/webscraper/chromedriver.exe", options=options)
