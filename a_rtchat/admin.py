from django.contrib import admin
from .models import ChatGroup, GroupMessage, UserChannel


admin.site.register(ChatGroup)
admin.site.register(GroupMessage)
admin.site.register(UserChannel)