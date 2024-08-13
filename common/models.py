from django.utils import gettext_lazy as _
from django.db import models


class Gallery(models.Model):
    name = models.CharField("name", max_length=256)
    description = models.CharField("description", max_length=256)
    image = models.ImageField("image", upload_to="gallery/%Y/%m")

    class Meta:
        db_table = "gallery"
        verbose_name = _("gallery")
        verbose_name_plural = _("galleries")

    def __str__(self):
        return f"{self.name}"
