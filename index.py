import os,time
from selenium import webdriver
from selenium.webdriver.common.by import By
 


opt = webdriver.ChromeOptions()


opt.add_argument("--user-data-dir="+r"C:/Users/Administrator/AppData/Local/Google/Chrome/User Data/")
driver = webdriver.Chrome(chrome_options=opt)   # 打开chrome浏览器

# extension_path = r'D:\Downloads\steam inventury helper\1.11.1.3_0.crx'
# opt.add_extension(extension_path)


driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')
driver.maximize_window()
time.sleep(2)
 
# driver.find_element(By.CSS_SELECTOR, "input[class='MuiInputBase-input MuiInput-input']")
driver.find_element(By.CSS_SELECTOR, 'button[button btn--rounded btn-secondary]').click()

print('finish')
time.sleep(33)
driver.quit()
