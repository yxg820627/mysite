from django.db import models
from django.utils import timezone

class BabyPhoto(models.Model):
    pid = models.AutoField(max_length=20, primary_key=True)
    bid = models.ForeignKey('baby.BabyInfo', on_delete=models.CASCADE)
    imageurl = models.CharField(max_length=500)
    imagepath = models.CharField(max_length=200)
    createtime = models.DateTimeField(default=timezone.now)
    uid=models.ForeignKey('baby.User',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.createtime
