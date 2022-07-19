import os
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now as timezone_now
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from django.urls import reverse
from myproject.apps.core.models import UrlBase

# Create your models here.
def upload_to(instance, filename):
    now = timezone_now()
    base, extension = os.path.splitext(filename)
    extension = extension.lower()
    return f"store/{now:%Y/%m}/{instance.pk}{extension}"

class Payment(models.Model):
    title = models.CharField(
        _("Title"),
        max_length=200,
    )

    number = models.CharField(
        _("Number"),
        max_length=200,
    )

    name = models.CharField(
        _("Name"),
        max_length=200,
    )

    def __str__(self):
        return self.title


class Product(UrlBase):
    title = models.CharField(
        _("Title"),
        max_length=200,
    )
    slug = models.SlugField(max_length=255)
    description = models.TextField(
        _("Description"),
    )
    price = models.IntegerField(
        _("Price"),
    )
    is_featured = models.BooleanField(
        default=False
    )
    picture = models.ImageField(
        _("Picture"), upload_to=upload_to, null=True,
    )
    picture_social = ImageSpecField(
        source="picture",
        processors=[ResizeToFill(1024, 512)],
        format="JPEG",
        options={"quality": 100},
    )
    picture_large = ImageSpecField(
        source="picture",
        processors=[ResizeToFill(800, 400)],
        format="PNG"
    )
    picture_thumbnail = ImageSpecField(
        source="picture",
        processors=[ResizeToFill(728, 250)],
        format="PNG"
    )


    class Meta:
        ordering = ("title",)

    def __str__(self):
        return self.title

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
        return reverse("store:product_detail", kwargs={
            "slug": self.slug,
        })
