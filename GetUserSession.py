from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import urllib.parse as urlparse
from selenium.webdriver.chrome.options import Options


# =================Install below  python dependencies=================================================>
# pip install selenium
# pip install urllib3

# ==================================================================>


class ZerodhaAccessToken:
    def __init__(self):
        self.apiKey = 'xx_your_api_key'
        self.apiSecret = 'xx_your_api_secret'
        self.accountUserName = 'xx_your_zerodha_userid'
        self.accountPassword = 'xx_your_zerodha_password'
        self.securityPin = 'xx_your_pin'

    def getaccesstoken(self):
        try:
            login_url = "https://kite.trade/connect/login?v=3&api_key={apiKey}".format(apiKey=self.apiKey)

            ##change the chrome driver path
            chrome_driver_path = "chrome_driver_path\\your_machine\\chromedriver.exe"
            options = Options()

            ### By enabling below option you can run chrome without UI
            #options.add_argument('--headless')


            ## chrome driver object
            driver = webdriver.Chrome(chrome_driver_path, options=options)

            ## load the url into chrome
            driver.get(login_url)

            ## wait to load the site
            wait = WebDriverWait(driver, 20)

            ## Find User Id field and set user id
            wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="text"]')))\
                .send_keys(self.accountUserName)

            ## Find password field and set user password
            wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))\
                .send_keys(self.accountPassword)

            ## Find submit button and click
            wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))\
                .submit()

            ## Find pin field and set  pin value
            wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]'))).click()
            time.sleep(5)
            driver.find_element_by_xpath('//input[@type="password"]').send_keys(self.securityPin)

            ## Final Submit
            wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))).submit()

            ## wait for redirection
            wait.until(EC.url_contains('status=success'))

            ## get the token url after success
            tokenurl = driver.current_url
            parsed = urlparse.urlparse(tokenurl)
            driver.close()
            return urlparse.parse_qs(parsed.query)['request_token'][0]
        except Exception as ex:
            print(ex)


## Initialise the class object with required parameters
_ztoken = ZerodhaAccessToken()
actual_token = _ztoken.getaccesstoken()
## Final Token valid for the day ===========>
print(actual_token)
