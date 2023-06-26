
from django.urls import  path 
from app import views

urlpatterns = [ 

    path('login',views.handlelogin,name='handlelogin'),
    path('signup',views.handlesignup,name='handlesignup'),
    path('otp-verification',views.handleOTPVerificationPage,name='handleOTPVerificationPage'),
    path('seller',views.handleseller,name='handleseller'),
    path('forget-password',views.handleForgetPassword,name='handleForgetPassword'),
    path('sellerlogin',views.handlesellerlogin,name='handlesellerlogin'),
]
    
   
