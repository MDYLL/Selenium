from selenium import webdriver
import pyautogui
import time
import os
import shutil


def action(element: str):
    while True:
        try:
            driver.find_element_by_css_selector('[class="' + element + '"]').click()
            break
        except:
            time.sleep(1)


firefoxProfile = webdriver.FirefoxProfile()
firefoxProfile.set_preference("browser.download.folderList", 2)
firefoxProfile.set_preference("browser.download.manager.showWhenStarting", False)
firefoxProfile.set_preference("browser.download.dir", '/home/dmitrii/Downloads1/')
firefoxProfile.set_preference("pdfjs.disabled", True)
firefoxProfile.set_preference("browser.helperApps.neverAsk.saveToDisk", "image/JPEG")
driver = webdriver.Firefox(firefoxProfile)

driver.get('http://toonme.com')
for i in range(8226, 8501):

    action('btn-upload-foto')
    time.sleep(2)
    pyautogui.write('/home/dmitrii/3/seed' + str(i) + '.png')
    time.sleep(1)
    pyautogui.press('enter')

    time.sleep(20)

    while True:
        try:
            driver.find_element_by_class_name('collage__tab_disney').click()
            break
        except:
            time.sleep(1)

    while True:
        try:
            driver.find_element_by_xpath('//button[contains(text(), "Скачать в HD качестве")]').click()
            break
        except:
            time.sleep(1)
    time.sleep(1)
    driver.find_element_by_xpath('//button[contains(text(), "Понятно")]').click()
    time.sleep(2)
    for file in os.listdir('/home/dmitrii/Downloads1/'):
        os.rename('/home/dmitrii/Downloads1/' + file, '/home/dmitrii/Downloads1/seed' + str(i) + '_0.jpeg')
        time.sleep(1)
        shutil.move('/home/dmitrii/Downloads1/seed' + str(i) + '_0.jpeg',
                    '/home/dmitrii/target/seed' + str(i) + '_0.jpeg')
    while True:
        try:
            driver.find_element_by_class_name('collage__tab_vector').click()
            break
        except:
            time.sleep(1)
    while True:
        try:
            driver.find_element_by_xpath('//button[contains(text(), "Скачать в HD качестве")]').click()
            break
        except:
            time.sleep(1)
    while True:
        try:
            driver.find_element_by_xpath('//button[contains(text(), "Понятно")]').click()
            break
        except:
            time.sleep(1)
    time.sleep(3)
    for file in os.listdir('/home/dmitrii/Downloads1/'):
        os.rename('/home/dmitrii/Downloads1/' + file, '/home/dmitrii/Downloads1/seed' + str(i) + '_1.jpeg')
        time.sleep(1)
        shutil.move('/home/dmitrii/Downloads1/seed' + str(i) + '_1.jpeg',
                    '/home/dmitrii/target/seed' + str(i) + '_1.jpeg')
    while True:
        try:
            driver.find_element_by_xpath('//button[contains(text(), "Загрузить другое фото")]').click()
            break
        except:
            time.sleep(1)
    time.sleep(3)
