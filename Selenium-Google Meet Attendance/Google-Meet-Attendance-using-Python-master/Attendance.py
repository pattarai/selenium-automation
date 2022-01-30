# web driver imports
# installing packages import
import os
# time import
import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# The function directly installs the required libraries
def install(package):
    os.system("pip install " + str(package))
    print("Installed", package.upper())

if __name__ == '__main__':
    install("selenium")
    gmail_id = input('Enter your gmail id: ')
    gmail_password = input('Enter your gmail password: ')
    meet_link = input('Paste the link of the Google Meet: ')

    # Some necessary things for automation with google driver
    opt = Options()
    opt.add_argument("--disable-infobars")
    opt.add_argument("start-maximized")
    opt.add_extension('C:\\webdriver\\attendance_tracker.crx')

    # This part allows the notifications, mic and camera permissions
    # Pass the argument 1 to allow and 2 to block
    opt.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 1,
        "profile.default_content_setting_values.notifications": 1
    })

    # Sign in to google
    driver = webdriver.Chrome(options=opt,
                              executable_path="C:\webdriver\chromedriver.exe")  # eg. r"C:\Users\hp\Downloads\chromedriver_win32\chromedriver.exe"
    driver.get('https://myaccount.google.com/')
    driver.find_element_by_xpath('/html/body/header/div[1]/div[5]/ul/li[2]/a').click()  # signing in with google
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys(
        gmail_id)  # entering the gmail id
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()
    sleep(2)
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(
        gmail_password)  # entering the password
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()
    sleep(2)

    driver.get('https://meet.google.com/')

    # Enter the meeting
    # Case when logged in with personal gmail account
    driver.find_element_by_css_selector('input#i3').send_keys(meet_link)  # Enter a code or link
    sleep(1)
    driver.find_element_by_css_selector(
        'button.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.ksBjEc.lKxP2d.cjtUbb').click()  # join
    sleep(1)
    driver.find_element_by_xpath(
        '/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()
    driver.find_element_by_xpath(
        '/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div').click()
    sleep(2)
    driver.find_element_by_css_selector('div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()  # join now
    sleep(2)
    driver.find_element_by_xpath(
        '/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[10]/div[3]/div[3]/div/div/div[2]/span/button').click()  # participant list
    sleep(1)
    driver.find_element_by_xpath(
        '/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[10]/div[1]/div/div/div/button').click()
    sleep(4)
    driver.find_element_by_xpath(
        '/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[10]/div[1]/div/div/div/button').click()
    chwnd = driver.window_handles[1]
    driver.switch_to.window(chwnd)

    sleep(5)
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/table[1]/tbody[1]/tr/td[8]/a/button').click()
    sleep(3)
    driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[1]/button').click()
    sleep(3)

    print('Attendance taken successfully!')
