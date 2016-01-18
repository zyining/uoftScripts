# uoftScripts
Automatic Course Enrollment using rosi.<br />
Script checks each course in list repeatedly and autoenrolls if a section is open and sends email when it does so.<br />
Also auto-completes captcha challenges using 2captcha.<br />


# Instructions
You need the following APIs:<br />
--splinter<br />
--BeautifulSoup<br />


# How to configure and run
Edit variable 'courses' to be an array of the course codes you want to check <br />
Add rosi login info in 'ID' and 'psw'<br />

Run courseAdd.py file<br />

(Optional)Enable email by deleting line 15 in courseAdd.py. Add email 'from', 'to' and login info for 'from' address *'from' must be gmail*. 
