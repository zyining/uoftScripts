# uoftScripts
Automatic Course Enrollment using rosi.
Script checks each course in list repeatedly and autoenrolls if a section is open and sends email when it does so.
Also auto-completes captcha challenges using 2captcha.


# instructions
You need the following apis:
  splinter
  BeautifulSoup


# how to configure and run
Add course codes to check in the variable 'courses'
Add rosi login info in 'ID' and 'psw'
Add email from to and login info for 'from' address if you want to use email *must be gmail*. Otherwise just write 'return' right after the sendMail function (line 14)

Run courseAdd.py file
