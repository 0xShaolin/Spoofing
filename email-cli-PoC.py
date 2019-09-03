import smtplib

while True:
    try:
        print """
Shaolin's Email Spoofing Client!
Please make sure you have a mail.com account.
----------------------------------------------
"""
        email = raw_input("email> ")
        password = raw_input("password> ")
        server = smtplib.SMTP('smtp.mail.com', 587)
        server.login(email, password)
        print "Login successful!\n"
        break
    except Exception:
        print "Login failed.. please try again."
        exit(1)
        
    try:
        print "Now we will gather information for the target."
        target = raw_input("target's email> ")
        print "Now for the sender settings (YOU- the attacker)."
        name = raw_input("sender's name> ")
        sender = raw_input("sender's email> ")
        print "Now to write the email:"
        subject = raw_input("subject> ")
        message = raw_input("message> ")
    except KeyboardInterrupt:
        exit("Email canceled..")

    try:
        server.sendmail(
            "%s <%s>" % (name, email),
            target,
            subject,
            message)
    except Exception as e:
        print "Error sending email..."
        exit(1)
    finally:
        server.quit()
        exit("Message sent!")
