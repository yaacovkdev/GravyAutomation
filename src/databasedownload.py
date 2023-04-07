from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from time import sleep

url = "https://www.ncbi.nlm.nih.gov/protein/?term=e6+Human+papillomavirus"
searchID1 = "ReportShortCut6"
searchText1 = "viewercontent1"

#You have to have Firefox installed, Alternatively use webdriver.Chrome().

op = Options()
#op.add_argument('-headless')

print("Loading Webdriver...")
driver = webdriver.Firefox(options=op)

print("Getting Url...")
driver.get(url)

input_elements = driver.find_elements_by_xpath("//input[id='"+searchID1+"']")
print(len(input_elements))

'''
link = driver.find_element(By.ID, searchID1)
link.click()

textfield = driver.find_element(By.ID, searchText1)
while(textfield.get_attribute('innerText')[0] != '>'):
    sleep(0.1)
    textfield = driver.find_element(By.ID, searchText1)
print(textfield.get_attribute('innerText'))

#driver.close()
#driver.quit()
'''