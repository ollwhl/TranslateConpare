from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def google(source,target,text):
    driver = webdriver.Chrome()
    driver.set_window_size(600, 800)
    driver.get("https://translate.google.co.jp/?sl="+source+"&tl="+target+"&text="+text+"&op=translate")
    time.sleep(2)
    try:
        transtext=driver.find_element_by_class_name("ryNqvb").text
    except Exception as e:
        transtext = text
    driver.close()
    return transtext
def deepl(source,target,text):
    driver = webdriver.Chrome()
    driver.set_window_size(600, 800)
    driver.get("https://www.deepl.com/translator#"+source+"/"+target+"/"+text)
    time.sleep(7)
    try:
        transtext=driver.find_element_by_id("target-dummydiv").get_attribute("textContent")
    except Exception as e:
        transtext = text
    driver.close()
    return transtext.splitlines()[0]
def mirai(source,target,text):
    driver = webdriver.Chrome()
    driver.set_window_size(600, 800)
    driver.get("https://miraitranslate.com/trial/")
    textaera=driver.find_element_by_id("source-input")
    textaera.send_keys(text)
    time.sleep(1)
    textaera.send_keys(Keys.CONTROL,Keys.ENTER)
    time.sleep(5)
    return  driver.find_element_by_id("translation-input").get_attribute("textContent")
def weblio(source,target,text):
    driver = webdriver.Chrome()
    driver.get("https://translate.weblio.jp")
    textaera=driver.find_element_by_id("originalTextArea")
    textaera.send_keys(text)
    if(source=="en"):
        btn=driver.find_element_by_id("EJB")
        btn.click()
        time.sleep(1)
        try:
            transtext=driver.find_element_by_xpath("//*[@id=\"transResultMainLn\"]/ol/li[1]/span[1]").get_attribute("textContent")
        except Exception as e:
            transtext = text
    elif(source=="jp"):
        btn=driver.find_element_by_id("JEB")
        driver.execute_script("arguments[0].click();",btn)
        time.sleep(1)
        transtext=driver.find_element_by_id("translatedText").get_attribute("value")
    driver.close()
    return transtext.splitlines()[0]






