from django.urls import path
from . import views

urlpatterns = [
    # path('gen_otp',views.gen_otp, name="index"),
    # path('verif_email',views.verif_email, name="verif_otp"),
    # path("send_mail",views.send_email,name="send_mail"),
    path("wait",views.wait,name="index"),
    path('user_data_entry',views.user_data_entry, name="index"),
    path('verif_email_pswd',views.verif_email_pswd, name="verif_email_pswd"),
    path('verif_email_otp',views.verif_email_otp, name="verif_email_otp"),
    path("upload",views.upload,name="upload"),
    path("ready_check",views.ready_check,name="send_mail"),
    path("update_url",views.update_url,name="update_url"),
]