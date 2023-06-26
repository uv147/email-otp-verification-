from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse, redirect, render
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import randint, randrange

sender_email = 'uvthemonster147@gmail.com'
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = sender_email
smtp_password = 'ugpveoccoqjjbqfn' 

def handlelogin(request):
  return render(request,'login.html')
def handleForgetPassword(request):
  return render(request,'forget-password.html')


def handleOTPVerificationPage(request):
  if(request.method=='POST'):
      first=request.POST.get('first')
      second=request.POST.get('second')
      third=request.POST.get('third')
      fourth=request.POST.get('fourth')
      fifth=request.POST.get('fifth')
      otp=first+second+third+fourth+fifth
      print(otp)
  return render(request,'otp.html')

def handlesignup(request):
    if request.method=='POST':
        email=request.POST.get('email')
        sendOTPToUser(email=email)
        return redirect("/otp-verification")
    return render(request,'signup.html')
def handleseller(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        brand=request.POST.get('BrandName')
        pan=request.POST.get('PAN')
        password=request.POST.get('pass1')
    
        confirmpassword=request.POST.get('pass2')
        if password!=confirmpassword:
           messages.warning(request,"Password is Incorrect")
           return redirect('/seller')
         
          
        try:
           if User.objects.get(username=uname):
                messages.info(request,'UserName is Taken')
                return redirect('/seller')
        except:
           pass
        try:
           if User.objects.get(email=email):
                messages.info(request,'Email is Taken')
                return redirect('/seller')
        except:
           pass
        try:
           if User.objects.get(BrandName=brand):
                messages.info(request,'BrandName is Taken')
                return redirect('/seller')
        except:
           pass
        try:
           if User.objects.get(PAN=pan):
                messages.info(request,'Pan is Taken')
                return redirect('/seller')
        except:
           pass
        myuser= User.objects.create_user(uname, email, password)
        myuser.save()
        
        return HttpResponse('Seller Signup Success')

    return render(request,'seller.html')
def handlesellerlogin(request):
    if request.method=='POST':
       uname=request.POST.get('username')
      
       pass1=request.POST.get('pass1')
       myuser=authenticate(username=uname,password=pass1)
       if myuser is not None:
           login(request,myuser)
           messages.success(request,'login success')
           return redirect('/')
       else:
           messages.error(request,'Invalid Credentials')
           return redirect('/sellerlogin')
           
    return render(request,'sellerlogin.html')

def sendOTPToUser(email):
    subject = 'Email Verification'
    otp=randrange(10000, 99999)
    body = "Your one time password is:"+ str(otp)

    # Create a multipart message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = email
    message['Subject'] = subject

    # Add body to the email
    message.attach(MIMEText(body, 'plain'))
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, email, message.as_string())
        print('Email sent successfully!')

    except Exception as e:
        print('An error occurred while sending the email:', str(e))
    finally:
        server.quit()

