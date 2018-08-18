from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0





# Create instance of a webdriver
driver = webdriver.Chrome('/Applications/chromedriver')

# Do some login

def logMeIn():
    url = 'https://hbf.com.au/myhbf/login'
    driver.get(url)
    assert "HBF" in driver.title
    memberNumber = X
    member = driver.find_element_by_id('MemberNumber')
    member.clear()
    member.send_keys(memberNumber)
    password = driver.find_element_by_id('loginPassword')
    password.clear()
    password.send_keys('X')
    login = driver.find_element_by_id('btnMyHbfLoginDesktop')
    login.submit()

    
logMeIn()
    
# Start a claim
def startClaim():
    element = driver.find_element_by_class_name('hbf-btn hbf-btn--solid primary')
    element.submit()

startClaim()

#=================
# FUNCTIONS
#=================
#Create Submit function
def submitButton():
    button = driver.find_element_by_class_name('hbf-btn hbf-btn--solid primary myhbfNextButton')
    button.submit()

# Drag & Drop pdf receipt

dropfile = driver.find_element_by_class_name('drop-box ng-pristine ng-untouched ng-valid ng-empty')
#dropfile.send_keys(/path/filename)

# Next button
submitButton()


# Submit a claim
submitButton()


# Close the browser
driver.quit()
