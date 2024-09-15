from django.contrib import admin
from .models import item


admin.site.site_header ="test"
admin.site.site_title ='fooddata'
# Register your models here.
admin.site.register(item)