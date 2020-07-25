from django.contrib import admin


# Register your models here.
from android.models import Users
from android.models import Games

admin.site.register(Users)
admin.site.register(Games)

