import smtplib

try: # container for entire program
    while True:
        print """
Welcome to my SMS Spoofer! Make sure
you have a mail.com email set up!
-------------------------------------
"""
        try:
            email = raw_input("email> ")
            password = raw_input("password> ")
            server = smtplib.SMTP('smtp.mail.com', 587)
            server.login(email, password)
            break
        except:
            print "Error Logging in.., please try again!"

    try:
        print "Type your target's phone number into freesmsgateway.info, then copy the line that says 'SMS Gateway Address'."
        target = raw_input("target> ")
        print "Now type your message. Please limit to 150 characters."
        message = raw_input("message> ")
        print "Finally, type the number you would like to text as!"
        print "ex. 444-555-6666, 911, 611-27"
        spoofas = raw_input("number> ")
        server.sendmail(
            spoofas,
            target,
            message,)
        server.quit()
        print "Message sent!"
        exit(0)
    except Exception as e:
        print "Error sending the message: %s" % e
        server.quit()
except KeyboardInterrupt:
    exit(0)
