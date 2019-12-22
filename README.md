# ZerodhaRequestToken
Zerodha Request Token is a python script built using selenium to automate the zerodha login process in order to get the 
request_token which will be further used to get the access_token.

Currently you need to login manually to get request token from URL, as per exchange policy, 
auto-login is not allowed. Access token is valid through the day, until you log-out/destroy the session. 
In order to automate this process I have developed this script.

Zerodha Documentation :- https://kite.trade/docs/connect/v3/user/


## Installing
You can directly install below packages using pip.
    
    pip install selenium
    
    pip install urllib3

Or

You can create python virtual enviornment and install dependencies using requirement.txt.

    pip install -r requirement.txt


## Getting Started

Set the below variables with your own values inside the GetUserSession.py file ZerodhaAccessToken class init.
        
        self.apiKey = 'xx_your_api_key' 
        
        self.apiSecret = 'xx_your_api_secret'
        
        self.accountUserName = 'xx_your_zerodha_userid'
        
        self.accountPassword = 'xx_your_zerodha_password'
        
        self.securityPin = 'xx_your_pin'

Download Chrome Driver (depending on your chrome version) https://chromedriver.chromium.org/downloads and 
set the chrome driver path variable inside the getaccesstoken function to your local machine driver path. 

    
    chrome_driver_path = "chrome_driver_path\\your_machine\\chromedriver.exe"
  

### Usage 

      _ztoken = ZerodhaAccessToken() 
   
      actual_token = _ztoken.getaccesstoken()


### Prerequisites

1) Python - 3.6
2) Chrome Driver (depending on your chrome version) 
    url - https://chromedriver.chromium.org/downloads

