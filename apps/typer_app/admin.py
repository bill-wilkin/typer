from django.contrib import admin
from .models import Target, Session
# Register your models here.

class TargetAdmin(admin.ModelAdmin):
    pass
admin.site.register(Target, TargetAdmin)

class SessionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Session, SessionAdmin)

