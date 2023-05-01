from django.db import models


class Magazines(models.Model):
    class Meta:
        verbose_name_plural = "magazines"

    name = models.CharField(max_length=48)

    def __str__(self):
        return self.name
