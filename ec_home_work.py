import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


browser = webdriver.Chrome()
browser.get('https://hotline.ua/ua/yp/37946/?gclid=Cj0KCQjwj5mpBhDJARIsAOVjBdrkDkJVId07e64q8umHP9jsDT8VlHIYri6A8Gf5-CrfzpRMAnHcQ7QaAgwzEALw_wcB')

message = WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//p[@class="informer-translation-error__text informer-translation-error__text--first"]'))
    )
time.sleep(2)
