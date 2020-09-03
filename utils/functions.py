from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions


def browserOptionSwitcher(i: int):
    switcher = {
        1: connectFirefox,  # 1 - Firefox
        2: connectChrome,  # 2 - Chrome
    }
    return switcher.get(i, "Opção inválida")()


def connectChrome():
    options = ChromeOptions()
    options.add_argument("--headless")  # Não abre o navegador e faz as operações no background
    chrome_driver_path = ChromeDriverManager().install()
    driver = webdriver.Chrome(chrome_driver_path, chrome_options=options)
    print("Chrome Headless Browser Invoked")
    return driver


def connectFirefox():
    options = FirefoxOptions()
    options.add_argument("--headless")  # Não abre o navegador e faz as operações no background
    gecko_driver = GeckoDriverManager().install()
    driver = webdriver.Firefox(gecko_driver, firefox_options=options)
    print("Firefox Headless Browser Invoked")
    return driver
