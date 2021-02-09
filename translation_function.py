import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

chromedriver_path = "/Users/.../chromedriver"
driver = webdriver.Chrome(chromedriver_path)


def translate(text, source_language, target_language):
    """Translate a text from a source_language to a target_language using deepl. Possible languages: German 'de',
    Chinese 'zh', English 'en', French 'fr', Italian 'it', Japanese 'ja', Dutch 'nl', Polish 'pl', Portuguese 'pt',
    Russian 'ru', Spanish 'es'."""
    driver.get(f'https://www.deepl.com/translator#{source_language}/{target_language}/{text}')
    translation_text_field_xpath = '//*[@id="dl_translator"]/div[5]/div[2]/div[3]/div[3]/div[1]/textarea'
    while True:
        text_field = WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, translation_text_field_xpath)))
        if (text_field.get_attribute('value') != ''):
            time.sleep(2)
            translation = text_field.get_attribute('value')
            break
    driver.quit()
    return translation


print(translate("Hello world", 'en', 'zh'))
