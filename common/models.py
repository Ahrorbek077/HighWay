from django.utils.translation import gettext_lazy as _
from django.db import models
from django_resized import ResizedImageField

class Video(models.Model):
    name = models.CharField(_("name"), max_length=100)
    video = models.FileField(_("video"), upload_to='video/', blank=True, null=True)

    class Meta:
        db_table = "video"
        verbose_name = _("video")
        verbose_name_plural = _("videos") 

    def __str__(self):
        return self.name


class Gallery(models.Model):
    name = models.CharField(_("name"), max_length=256)
    description = models.CharField(_("description"), max_length=256)
    image = ResizedImageField(_("image"), crop=['middle', 'center'], upload_to='Gallery/')

    class Meta:
        db_table = "gallery"
        verbose_name = _("gallery")
        verbose_name_plural = _("galleries")

    def __str__(self):
        return f"{self.name}"

