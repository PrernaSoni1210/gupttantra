from django.db import models


class Video(models.Model):

    title = models.CharField(max_length=200)

    video_url = models.URLField(
        blank=True,
        null=True
    )

    video_file = models.FileField(
        upload_to='videos/',
        blank=True,
        null=True
    )

    thumbnail = models.ImageField(
        upload_to='video_thumbnails/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    @property
    def youtube_embed_url(self):

        if not self.video_url:
            return ""

        if "youtu.be/" in self.video_url:

            video_id = self.video_url.split(
                "youtu.be/"
            )[1].split("?")[0]

        elif "watch?v=" in self.video_url:

            video_id = self.video_url.split(
                "watch?v="
            )[1].split("&")[0]

        else:

            return self.video_url

        return f"https://www.youtube.com/embed/{video_id}"

    @property
    def youtube_thumbnail_url(self):

        if not self.video_url:
            return ""

        if "youtu.be/" in self.video_url:

            video_id = self.video_url.split(
                "youtu.be/"
            )[1].split("?")[0]

        elif "watch?v=" in self.video_url:

            video_id = self.video_url.split(
                "watch?v="
            )[1].split("&")[0]

        else:

            return ""

        return f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"

    def __str__(self):
        return self.title