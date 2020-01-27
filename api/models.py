from django.db import models
# Create your models here.


class users(models.Model):
    username = models.CharField(max_length = 300)

    class Meta:
        verbose_name_plural = "users"

    def __str__(self):
        return self.username
