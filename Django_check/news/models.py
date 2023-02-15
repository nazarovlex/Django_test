from django.db import models


# Create your models here.
class Articles(models.Model):
    title = models.CharField("Title", max_length=50, null=True)
    anons = models.CharField("Announce", max_length=250, null=True)
    full_text = models.TextField("Post", null=True)
    date = models.DateTimeField("Time of publishing", null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/news/{self.id}"

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
