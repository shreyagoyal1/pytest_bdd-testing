import pytest_bdd
import pytest
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

# Constants
OPENMRS_HOME = 'https://demo.openmrs.org/openmrs'

@pytest.fixture
def browser():
  driver = Firefox()
  driver.implicitly_wait(10)
  yield driver
  driver.quit()

# Scenarios
@pytest_bdd.scenario('incorrect_userpas.feature','incorrect userpas attempts', features_base_dir='', strict_gherkin=False)
def test_incorrect_password():
    pass

# Given Steps
@pytest_bdd.given('the OpenMRS home page is displayed')
def demo_home(browser):
    browser.get(OPENMRS_HOME)
    
@pytest.fixture(scope='function')
def context():
    return {}

# When Steps
@pytest_bdd.when('the attacker tries to login with invalid "user" and invalid "pas"')

def login_username(browser):
    temp=0
    fail=0
    z=0.55
    p=0.77
    k=0.85
    w=0.85
    o=0.56
    i=0.56
    q=0.56
    ISS = 1-((1-o) * (1-i) * (1-q))
    Impact = 6.42 * ISS
    
    user = ['hwjk', 'dxgd', 'efds', 'gtefdsc', 'evfdw', 'gewfds', 'hrgsfd', 'hgrtrfs', 'hrgts', 'user', 'admin']

    pas = ['hwjk', 'dxgd', 'efds', 'gtefdsc', 'evfdw', 'gewfds', 'tgrsf', 'juytfh', 'hygfe', 'fgfjbm','Admin123']
    for i in range(len(pas)):
        search_input = browser.find_element_by_id('username')
        search_input.send_keys(user[i])
        
        search_input = browser.find_element_by_id('password').send_keys((pas[i]) + Keys.TAB) 
        login_button = browser.find_element_by_id('loginButton')
        login_button.click()

        
        if browser.current_url == 'https://demo.openmrs.org/openmrs/referenceapplication/home.page':
            temp=temp+1
            break
        
        else:
            fail+=1
            
        if fail<=9:
            p = 0.44
            Exploitability = 8.22*z*p*k*w
            Base_score = 1
            if Impact<= 0:
                Base_score = 0
            else:
                Base_score = min((Impact + Exploitability), 10)
                Base_score1 = round(Base_score, 2)
                Base_score2 = round(Base_score1, 1)
           
        elif fail>9:
            p = 0.77
            Exploitability = 8.22*z*p*k*w
            round(Exploitability, 2)
            Base_score = 1
            if Impact<= 0:
                Base_score = 0
            else:
                Base_score = min((Impact + Exploitability), 10)
                Base_score1 = round(Base_score, 2)
                Base_score2 = round(Base_score1, 1)

        
    print("CVSS Score:", Base_score2)    
    
# Then Steps
@pytest_bdd.then('check after 10 incorrect attempts, the systems allows to login with correct credentials or not')
def login_results(browser):
    assert browser.current_url == 'https://demo.openmrs.org/openmrs/referenceapplication/home.page'
