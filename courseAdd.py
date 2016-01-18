import time
import random
from splinter import Browser
from captcha2upload import CaptchaUpload
import smtplib
import urllib.request
from bs4 import BeautifulSoup


browser = Browser('chrome')
browser.driver.set_page_load_timeout(10)  # 10 seconds


def sendMail(msg):
    return # disable email function by default, remove this line and fill following fieds to use gmail
    fromaddr = ''
    toaddrs = ''

    # Credentials (if needed)
    username = ''
    password = ''

    try:
        # The actual mail send
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
    except:
        print('email error')
        server.quit()


def isCap():
    if browser.is_text_present('Verification Before You Proceed'):
        try:
            if browser.is_element_present_by_id('recaptcha_challenge_image', wait_time=5):

                soup = BeautifulSoup(browser.html)
                images = soup('img')

                path = images[0]['src']
                # print(path)
                answer = solveCap(path)
                browser.fill('recaptcha_response_field', answer)
                browser.find_by_id('process_0').click()
                print('captcha solved')
                browser.visit('https://sws.rosi.utoronto.ca/sws/reg/course/edit.do?editCourse.dispatch')
        except:
            print('captcha error')
            sendMail('captcha error')


def solveCap(path):
    key = 'b727fcc73349f3ed88be668d0010903d'
    captcha = CaptchaUpload(key)
    urllib.request.urlretrieve(path, "captcha.jpg")
    return captcha.solve('captcha.jpg')


def monitor():

    url = "https://sws.rosi.utoronto.ca/sws/"
    browser.visit(url)

    while (1):
        if browser.is_text_present('SWS Unavailable'):
            time.sleep(5*60)
            browser.visit(url)
        else:
            break

    if browser.is_text_present('Sign In to SWS'):
        # login
        ID = ''  # input('id: ')
        psw = ''  # input('pass: ')

        browser.fill('personId', ID)
        browser.fill('pin', psw)

        loginButton = browser.find_by_value('Login')
        loginButton.click()

        courseMenu = browser.find_by_text('Course Enrolment')
        courseMenu.click()

        isCap()

        courseManage = browser.find_by_text('Manage Courses').last
        courseManage.click()

    # data
    courses = ['csc336h1', 'ece311h1', 'csc343h1']
    d = {'default': 'N/A'}
    section = 's'

    while (1):
        interval = random.randint(0, 4)
        time.sleep(interval)
        # check each course
        for course in courses:
            try:
                browser.visit('https://sws.rosi.utoronto.ca/sws/reg/course/edit.do?editCourse.dispatch')

                browser.fill('code', course)
                browser.fill('sectionCode', section)
                browser.find_by_value('Submit').click()
                # check for changes?
                if (
                    d.get(course, 'N/A') != browser.html and
                    d.get(course, 'N/A') != 'N/A'
                ):
                    if (not browser.is_text_present('Verification Before You Proceed')):
                        d[course] = browser.html
                        print('updated %s' % course)
                        sendMail('updated %s' % course)

                else:
                    d[course] = browser.html
                    # print('no change %s' % course)

                if browser.is_text_present('add meeting sections'):
                    # add section!
                    print('added %s' % course)
                    browser.find_by_value('Add Meeting Sections').click()
                    courses.remove(course)
                    sendMail('Added %s' % course)

            except:
                isCap()
                print('exception?')

monitor()
