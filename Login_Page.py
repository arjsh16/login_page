
#use this for making the login page using otp for authentication of mail id
import random as rd                      #for generatng OTP
from tkinter import *                    #to create the UI
from email.message import EmailMessage   #to structure the mail in code
import ssl                               #to create a context for protocol
import smtplib                           #to create a protocol (protocol to send a mail)
#otp generator
otp=rd.randint(1000,9999)
#making a login screen
root=Tk()
root.title("Login")
root.resizable(width=False,height=False)
root.geometry("400x240+0+0")
root.configure(background = '#EEEEEE')
#taking mail for sending otp generated
L1=Label(root,text="Enter your email(eg: xyz@abc.com)",fg="#00ADB5",bg="#EEEEEE")
L1.pack()
e1=Entry(root,fg="#00ADB5",bg="#EEEEEE")
e1.pack()
#defining the command for the button that sends the otp
def OnClick():
    #details to make the code
    email_sender=''    #Give the mail id from which you want to send the otp
    email_password=''  #not the normal password,the password generated from of the given mail id myaccounts.google.com/u/4/apppassword
    #this should be a 16 digit with 3 spaces in the format-> abcd efgh ijkl mnop
    email_reciever=e1.get()
    #To define the subject and the body of the mail
    subject=f'OTP=>{otp}'
    body=f"Your OTP is {otp}"
    #creating the mail
    em=EmailMessage()

    em['From'] = email_sender
    em['To'] = email_reciever
    em['Subject'] = subject
    em.set_content(body)
    #creating protocol
    context=ssl.create_default_context()
    
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        #the protocol
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_reciever,em.as_string())
#the button that sends the otp
but1=Button(root,text="Send OTP",command=OnClick,fg="#00ADB5",bg="#EEEEEE")
but1.pack()
#making an entry so that otp can be confirmed
L=Label(root,text="Enter the OTP(check the given mail)",fg="#00ADB5",bg="#EEEEEE")
L.pack()
e=Entry(root,fg="#00ADB5",bg="#EEEEEE")
e.pack()
#definig the command for the submit button
def OnButtonClick():
    i=e.get()  
    i=int(i) 
    if i==otp:
        #The code for the program that takes place when the otp is authenticated goes here
        lab=Label(root,text="The otp is correct",bg="#393E46",fg="#00ADB5")
        lab.pack()
        root.configure(background='#393E46')
        L.configure(bg='#393E46',fg="#00ADB5")
        L1.configure(bg='#393E46',fg="#00ADB5")
        e1.configure(bg='#393E46',fg="#00ADB5")
        e.configure(bg='#393E46',fg="#00ADB5")
        but.configure(bg='#393E46',fg="#00ADB5")
        but1.configure(bg='#393E46',fg="#00ADB5")
    else:
        #code for the time OTP is wrong
        root.destroy()
#creating the submit button
but=Button(root,text="Submit OTP",command=OnButtonClick,fg="#00ADB5",bg="#EEEEEE")
but.pack()
#Mainloop
root.mainloop()
