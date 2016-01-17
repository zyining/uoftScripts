import time
from splinter import Browser


def monitor():
    browser = Browser('Chrome')

    url = "https://sws.rosi.utoronto.ca/sws/"
    browser.visit(url)

    if browser.is_text_present('Sign In to SWS'):
        # login
        ID = input('id: ')
        psw = input('pass: ')

        browser.fill('personId', ID)
        browser.fill('pin', psw)

        loginButton = browser.find_by_value('Login')

        loginButton.click()

    # data
    courses = ['csc321h1', 'csc336h1']
    d = {'csc321h1': 'a', 'csc334h1': 'b'}
    section = 's'

    # check each course
    for course in courses:

        courseMenu = browser.find_by_text('Course Enrolment')
        courseMenu.click()
        courseManage = browser.find_by_text('Manage Courses').last
        courseManage.click()

        browser.fill('code', course)
        browser.fill('sectionCode', section)
        browser.find_by_value('Submit').click()
        if d.get(course, 'N/A') != browser.html:
            d[course] = browser.html
            print('updated %s' % course)
        else:
            print('no change %s' % course)
            # email(course)
        time.sleep(5)

monitor()
