from django.contrib import admin
from models import UserProfile
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    fields = ('user', 'phone', 'photo', 'birthday', )


admin.site.register(UserProfile, UserProfileAdmin)