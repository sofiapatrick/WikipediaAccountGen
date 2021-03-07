from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup, SoupStrainer
from twocaptcha import TwoCaptcha
import requests, random, string, time, json

solver = TwoCaptcha('key')
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=r'C:\users\cgsaw\chromedriver.exe')
driver.get("https://en.wikipedia.org/w/index.php?title=Special:CreateAccount%22)
html = driver.page_source
soup = BeautifulSoup(html, features="lxml")
lmao = []
for link in soup.find_all('img'):
    lmao.append(link.get('src'))
dd = "https://en.wikipedia.org/" + lmao[0]
r = requests.get(dd)
open("file.jpg", "wb").write(r.content)
result = solver.normal("file.jpg")
print(result)
result = result["code"]
chars = string.ascii_letters + string.digits
def rand(siz):
    return ''.join(random.choice(chars) for x in range(siz))
passs = rand(8)
user = rand(8)
driver.find_element_by_id("wpName2").send_keys(user)
driver.find_element_by_id("wpPassword2").send_keys(passs)
driver.find_element_by_id("wpRetype").send_keys(passs)
driver.find_element_by_id("mw-input-captchaWord").send_keys(result)
email = False
if email:
    driver.find_element_by_id("wpEmail").send_keys("email")
driver.find_element_by_id("wpCreateaccount").click()
print(user + ":" + passs)
html = driver.page_source
soup = BeautifulSoup(html, features="lxml")
open("the.txt", "a").write(user + ":" + passs)
