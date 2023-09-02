from django.db import models


class Post(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media')
    description = models.TextField(max_length=500)

    def __str__(self):
        return F"{self.pk}"