from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

url = "https://www.bioinformatics.org/sms2/protein_gravy.html"
searchterm = "textarea"
buttonname = "main_submit"

#You have to have Firefox installed, Alternatively use webdriver.Chrome().

op = Options()
op.add_argument('-headless')

print("Loading Webdriver...")
driver = webdriver.Firefox(options=op)

print("Getting Url...")
driver.get(url)

sbox = driver.find_element(By.TAG_NAME, searchterm)
sbox.clear()

print("Sending Protein...")
sbox.send_keys(">sample sequence 2\nSEIIDNIYSVKAYCWESAMEKMIENLREVELKMTRKAAYMRFFTSSAFFFSGFFVVFLSVLPYTVINGIVLRKIFTTISFCIVLRMSVTRQFPTAVQIWYDSFGMIRKIQDFLQKQEYKVLEYNLMTTGI")

button = driver.find_element(By.NAME, buttonname)
button.click()
driver.switch_to.window(driver.window_handles[1])

#Displays the output of Gravy
print(driver.find_element(By.CLASS_NAME, 'main').text)

#close double windows
driver.close()
driver.switch_to.window(driver.window_handles[0])

sbox.clear()
sbox.send_keys(">sample sequence 2\nSDNIYSVKAYCWESAMEKMIENLREVELKMTRKAAYMRFFTSSAFFFSGFFVVFLSVLPYTVINGIVLRKIFTTISFCIVLRMSVTRQFPTAVQIWYDSFGMIRKIQDFLQKQEYKVLEYNLMTTGI")
button.click()
driver.switch_to.window(driver.window_handles[1])

#Displays the output of Gravy
print(driver.find_element(By.CLASS_NAME, 'main').text)


driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.close()
driver.quit()
