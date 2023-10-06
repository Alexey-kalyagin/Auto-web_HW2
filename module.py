import yaml
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service  # импортирует драйвер непосредственно для chrom
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


with open("./testdata.yaml") as f: # подсасываем инфу из файла testdata.yaml
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]

#service = Service(testdata["driver_path"])
#options = webdriver.ChromeOptions()

class Site:
    def __init__(self,address):       # выполняем инициализацию
        if browser == "firefox":        # проверяет браузер и устанавливает драйвер
            service = Service(executable_path=GeckoDriverManager().install())
            options = options = webdriver.FirefoxOptions()
            self.driver = webdriver.Firefox(service=service, options=options)
        elif browser == "chrome":
            service = Service(executable_path=ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=service, options=options)

        #self.driver = webdriver.Chrome(service=service, options=options) # выполяем инициализацию драйвера
        self.driver.implicitly_wait(3) # задержка
        self.driver.maximize_window() # открывает сайт на весь экран
        self.driver.get(address)      # открываем адрес сайта
        time.sleep(testdata["sleep_time"]) # выжидаем заданное время

    def find_element(self, mode, path):
        if mode == "css":
            element = self.driver.find_element(By.CSS_SELECTOR, path)
        elif mode == "xpath":
            element = self.driver.find_element(By.XPATH, path)
        else:
            element = None
        return element
    
    def get_element_property(self, mode, path, property): 
        element = self.find_element(mode, path)
        return element.value_of_css_property(property)
    
    def close(self):
        self.driver.close()
            