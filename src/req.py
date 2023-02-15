from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.bioinformatics.org/sms2/protein_gravy.html"
searchterm = "textarea"
buttonname = "main_submit"

#TODO: Find a better browser to communicate with, such as the one that doesnt use a GUI, so the server usage can be minimized

#You have to have Firefox installed, Alternatively use webdriver.Chrome().
driver = webdriver.Firefox()

driver.get(url)

sbox = driver.find_element(By.TAG_NAME, searchterm)
sbox.clear()
sbox.send_keys(">sample sequence 2\nSEIIDNIYSVKAYCWESAMEKMIENLREVELKMTRKAAYMRFFTSSAFFFSGFFVVFLSVLPYTVINGIVLRKIFTTISFCIVLRMSVTRQFPTAVQIWYDSFGMIRKIQDFLQKQEYKVLEYNLMTTGI")


button = driver.find_element(By.NAME, buttonname).click()
driver.switch_to.window(driver.window_handles[1])

#Displays the output of Gravy
print(driver.find_element(By.CLASS_NAME, 'main').text)

#close double windows
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.close()
