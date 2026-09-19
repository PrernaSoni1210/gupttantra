from django.db import models


class Service(models.Model):

    title = models.CharField(max_length=200)

    title_hindi = models.CharField(
        max_length=200,
        blank=True
    )

    description = models.TextField()

    description_hindi = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to='services/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title