## Selenium with Python Automation Framework

# Git clone

Clone the project

`$ git clone https://github.com/Vinodkumar545/Elegant.git`

Checkout to the branch.

`$ git checkout test_framework`

# Installation

Create a Virtual Environment, activate it and install the libraries from requirement file 

```
$ virtualenv -p python3.6 venv
$ venv\Scripts\activate.bat
$ pip install -r requirements.txt
```

# Host Selenium Standalone Server

`
$ java -jar selenium-server-standalone-3.141.59.jar
`

Verify the server(Selenium grid) is hosted by using this link 

`http://127.0.0.1:4444/wd/hub/static/resource/hub.html`

# Framework settings
Setting for this framewortk is located in `Utilities > settings.py`

## Application related
Application URL and respective username and password are provided here.

## Framework related
Framework related details is used to setup tox installation

## Email Configuration
For Authenticating with Gmail refer this Article [stackabuse](`https://stackabuse.com/how-to-send-emails-with-gmail-using-python/`)

1. Provide the list of recepients in **MAIL_TO**
2. Provide your personal gmail id  in **SMTP_USERNAME**
3. Provide your gmail password in **SMTP_PASSWORD**

# Run the test suite
`$ tox`
