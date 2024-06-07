from django.contrib import admin
from embed_video.admin import AdminVideoMixin

from .models import Video


class VideoAdmin(AdminVideoMixin ,admin.ModelAdmin):
    list_display = ('title', 'added', 'url')


class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
    pass




admin.site.register(Video, VideoAdmin)
