from django.db import models

# Create your models here.
class users(models.Model):
    id = models.CharField(max_length = 300)
    username = models.CharField(max_length = 300)
    last_login = models.CharField(max_length = 300)
    login_count = models.CharField(max_length = 300)
    project_count = models.CharField(max_length = 300)

    class Meta:
        verbose_name_plural = "users"

    def __str__(self):
        return self.name
