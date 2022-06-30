import uuid
import contextlib
import os
from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now as timezone_now

from myproject.apps.core.models import UrlBase


def upload_to(instance, filename):
    now = timezone_now()
    base, extension = os.path.splitext(filename)
    extension = extension.lower()
    return f"webpage/{now:%Y/%m}/{instance.pk}{extension}"

class Testimoni(UrlBase):
    # fields, attributes, properties and methods...
    nama = models.CharField(max_length=255)
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    picture = models.ImageField(
        _("Picture"), upload_to=upload_to
    )
    picture_social = ImageSpecField(source="picture", processors=[ResizeToFill(1024, 512)], format="JPEG",
        options={"quality": 100},
    )
    picture_large = ImageSpecField(source="picture", processors=[ResizeToFill(800, 400)], format="PNG")
    picture_thumbnail = ImageSpecField(
        source="picture",
        processors=[ResizeToFill(728, 250)],
        format="PNG"
    )

    # other fields, properties, and  methods...
    def delete(self, *args, **kwargs):
        from django.core.files.storage import default_storage
        if self.picture:
            with contextlib.suppress(FileNotFoundError):
                default_storage.delete(
                    self.picture_social.path
                )
                default_storage.delete(
                    self.picture_large.path
                )
                default_storage.delete(
                    self.picture_thumbnail.path
                )
            self.picture.delete()
        super().delete(*args, **kwargs)

    def get_url_path(self):
        return reverse("testimoni_details", kwargs={
            "testimoni_id": str(self.pk),
        })