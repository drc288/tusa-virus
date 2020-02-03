# PSL Coding Challenge

The thesaurus virus has arrived in Colombia, so we created a software to be able to count the victims
this application is created in python and to install it you must have the following packages
first we must have installed pip in version 3, for this we do the following
```
apt-get install python3-pip
```

## Packages
### Flask
Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. 
```
pip3 install flask
```
### Firebase admin
The Firebase Admin Python SDK enables server-side (backend) Python developers to integrate Firebase into their services and applications.
```
pip3 install firebase-admin
```
### Selenium
Selenium WebDriver is a web automation framework that allows you to execute your tests against different browsers
```
pip3 install selenium
```
### Gunicorn
allows us to keep multiple web application processes running, as well as continuous communication between client and server
```
pip3 install gunicorn
```

## Run the service
Being in the directory of our application
```
gunicorn app:app
```
***
## Author
- [David Rosero Calle](https://www.linkedin.com/in/david-rosero-calle-1aa6a2126/)