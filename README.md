# uoftScripts
Automatic Course Enrollment using rosi.<br />
Script checks each course in list repeatedly and autoenrolls if a section is open and sends email when it does so.<br />
Also auto-completes captcha challenges using 2captcha.<br />


# instructions
You need the following apis:<br />
--splinter<br />
--BeautifulSoup<br />


# how to configure and run
Add course codes to check in the variable 'courses'<br />
Add rosi login info in 'ID' and 'psw'<br />
Add email from to and login info for 'from' address if you want to use email *must be gmail*. Otherwise just write 'return' right after the sendMail function (line 14)<br />

Run courseAdd.py file<br />
