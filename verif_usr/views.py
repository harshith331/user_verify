from django.shortcuts import render
from .models import *
import json,math,random
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.


def generateOTP() : 
    digits = "0123456789"
    OTP = "" 
    for i in range(7) : 
        OTP += digits[math.floor(random.random() * 10)] 
  
    return OTP 

# def gen_otp(request):
#     if request.method == 'POST':
#         body_unicode = request.body.decode('utf-8')
#         body = json.loads(body_unicode)
#         email= body["email"]
#         try:
#             cur_user=user.objects.get(email=email)
#             return JsonResponse({'success': False,'error':"email already exists"})
#             # else:
#             #     otp=generateOTP()
#             #     cur_user.otp=otp
#             #     cur_user.save()
#             #     html_content = render_to_string('otp_mail.html', {'otp':otp}) 
#             #     text_content = strip_tags(html_content) # Strip the html tag. So people can see the pure text at least.
#             #     send_mail('VERIFICATION',text_content,settings.EMAIL_HOST_USER ,[email],fail_silently = False)
#             #     return JsonResponse({'success': True})

#         except:
#             otp=generateOTP()
#             user.objects.create(email=email,otp=otp)
#             # html_content = render_to_string('otp_mail.html', {'otp':otp}) 
#             # text_content = strip_tags(html_content) # Strip the html tag. So people can see the pure text at least.
#             # # send_mail('VERIFICATION',text_content,settings.EMAIL_HOST_USER ,[email],fail_silently = False)
#             return JsonResponse({'success': True})

def verif_email_otp(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        email= body["email"]
        given_otp= body["otp"]
        try:
            cur_user=user.objects.get(email=email)
            if cur_user.otp==given_otp:
                return JsonResponse({'success': True,'verified':True})
            else:
                return JsonResponse({'success': False,'verified':False,'error':"OTP doesnt match"})
        except:
            return JsonResponse({'success': False,'error':"email doesnt exist"})

def user_data_entry(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        mail=body["email"]
        try:
            cur_user=user.objects.get(email=mail)
            return JsonResponse({'success': False,"error":"user already exists"})
        except:
            user.objects.create(
            email=mail,
            first_name=body["first_name"],
            last_name=body["last_name"],
            date_of_birth=body["date_of_birth"],
            country_of_residence=body["country_of_residence"],
            state=body["state"],
            city_of_residence=body["city_of_residence"],
            phone_no=body["phone_no"],
            password=body["password"],
            fav_gnr_writing=body["fav_gnr_writing"],
            short_story=body["short_story"],
            )
            return JsonResponse({'success': True})


def ready_check(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        email= body["email"]
        try:
            cur_user=user.objects.get(email=email)
            ready=cur_user.ready
            return JsonResponse({'ready_check':ready})
        except:
            return JsonResponse({'success': False,'error':"email doesnt exist"})


def verif_email_pswd(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        email= body["email"]
        password= body["password"]
        try:
            cur_user=user.objects.get(email=email)
            if cur_user.password==password:
                return JsonResponse({'success': True,'verified':True})
            else:
                return JsonResponse({'success': False,'verified':False,'error':"wrong password"})
        except:
            return JsonResponse({'success': False,'error':"email doesnt exist"})            

def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return JsonResponse({"file_url":uploaded_file_url})

def update_url(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        mail=body["email"]
        url=body["url"]
        try:
            cur_user=user.objects.get(email=mail)
            if cur_user.registered==True:
                return JsonResponse({"success":False,"error":"File already uploaded"})
            else:
                cur_user.registered=True
                cur_user.doc_url=url
                cur_user.save()
                return JsonResponse({"success":True})
        except:
            return JsonResponse({"success":False,"error":"email dosent exist"})



        
