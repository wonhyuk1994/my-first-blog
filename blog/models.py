from django.db import models

# Create your models here.
from django.utils import timezone


class Post(models.Model):   #models 떄문에 Post가 DB에 저장되야 댄다는걸 알게 됨
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
