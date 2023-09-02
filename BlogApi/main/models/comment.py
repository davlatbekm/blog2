from django.db import models


class Comments(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    post_id = models.ForeignKey('main.post', on_delete=models.CASCADE)
    text = models.TextField(max_length=300)


    def __str__(self):
        return self.text
