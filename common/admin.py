from django.contrib import admin
from common import models

admin.site.register(models.Video)

@admin.register(models.Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("name", )
