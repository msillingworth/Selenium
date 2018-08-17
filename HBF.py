from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create instance of a webdriver
driver = webdriver.Chrome('/Applications/chromedriver')

# Get the relevant webpage
url = 'https://hbf.com.au'
driver.get(url)
assert "HBF" in driver.title

# Do some login

def logMeIn():
    url = 'htttps://hbf.com.au/myhbf/login'
    driver.get(url)
    assert "HBF" in driver.title
    userName = '18392520'
    password = 'Essendon2000'
    memberNumber = driver.find_element_by_id('memberNumber')
    user.clear()
    user.send_keys(memberNumber)
    password = driver.find_element_by_id('loginPassword')
    password.clear()
    password.send_keys(password)
    
    login = driver.find_element_by_id('btnMyHbfLoginDesktop')
    login.send_keys(Keys.Click)
    # assert "HBF" in driver.url
    
logMeIn()
    
# Start a claim
def startClaim():
    claimId = 'hbf-make-claim'
    claimElem = driver.find_element_by_id(claimId)
    claimElem.clear()
    claimElem.send_keys(Keys.Click)
    assert 'No results found' not in driver.page_source

startClaim()

#=================
# FUNCTIONS
#=================
#Create Submit function
def submitButton():
    button = driver.find_element_by_class_name('hbf-btn hbf-btn--solid primary myhbfNextButton')
    button.send_keys(Keys.Click)

# Drag & Drop pdf receipt

dropfile = driver.find_element_by_class_name('drop-box ng-pristine ng-untouched ng-valid ng-empty')
#dropfile.send_keys(/path/filename)

# Next button
submitButton()


# Submit a claim
submitButton()


# Close the browser
driver.quit()
