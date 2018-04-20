from django.contrib import admin

# Register your models here.
from .models import UserProfile


# 管理器：命名，model+Admin
class UserProfileAdmin(admin.ModelAdmin):
    pass


# 将UserProfile注册进admin,并将它作为管理器
admin.site.register(UserProfile, UserProfileAdmin)
