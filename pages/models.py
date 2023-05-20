from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.BinaryField(blank=True)
    about = models.TextField(blank=True)
    js = models.TextField(blank=True)
    css = models.TextField(blank=True)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
