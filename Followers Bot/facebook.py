from selenium import webdriver 
from time import sleep 
import numpy as np
from random import randint
import random
import string
sz="devilfrommars"
us="21321"
pas="Niko213"
im = np.loadtxt('imie.npy', dtype=str)
nz = np.loadtxt('nazw.npy', dtype=str)
imy = randint(0,81)
nzy = randint(0,13)
nal=im[imy] + " " + nz[nzy] 
def create_str(str_length):
    return random.sample(string.ascii_letters, str_length)
x = create_str(int(12))

rmail =''.join(x) + "@wp.pl"
driver = webdriver.Chrome() 
driver.get('https://www.instagram.com/accounts/emailsignup/?hl=pl') 
print ("Opened facebook") 
sleep(1) 
  
username_box = driver.find_element_by_name('emailOrPhone') 
username_box.send_keys(rmail)  

nal_box = driver.find_element_by_name('fullName')
nal_box.send_keys(nal)
sleep(5)


use_box = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[5]/div/div/div/button')
use_box.click()

pas_box = driver.find_element_by_name('password')
pas_box.send_keys(pas)

login_box = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[7]/div/button') 
login_box.click()
sleep(3)
pel_box = driver.find_element_by_css_selector('#igCoreRadioButtonageRadioabove_18')
pel_box.click()

dalej_box = driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div._0GT5G > div > button')
dalej_box.click()
sleep(7)

notnow_box = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]') 
notnow_box.click()
sleep(1)
szukaj_box = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
szukaj_box.send_keys()
sleep(2)
klik_box = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]')
klik_box.click()