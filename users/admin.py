from django.contrib import admin
from .models import Profile
# Register your models here.
admin.site.site_header ="test"
admin.site.site_title ='fooddata'
admin.site.register(Profile)
