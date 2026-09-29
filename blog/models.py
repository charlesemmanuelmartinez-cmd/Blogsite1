from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(model.Model):

    class Status(models.TextChoices):
        DRAFT ='Draft'
        PUBLISHED = 'PB', 'Published'
        title =models.CharField(max_leght=250)
        slug =models.SlugField(max_leght=250)
        author =models.ForeignKey(User , on delete=models.CASCADE,related_name='blog_posts')

        body = models.TextField()
        publish = models.DateTimeField(default=timezone.now)
        created = models.DateTimeField(auto_now_add=True)
        status = models.CharField(max_leght=2,choices=Status.choices,default=Status.DRAFT)

Hello
        class Meta:
            ordering = ['-publish']
            indexes = [
                models.Index(field=['-publish'])
            ]

        def _str_(self):
                return self.title


