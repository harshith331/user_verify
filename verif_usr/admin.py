from django.contrib import admin
from .models import *
# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name','state','fav_gnr_writing', 'ready')
admin.site.register(user,userAdmin)