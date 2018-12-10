from django.db import models

'''用户信息表'''


class User(models.Model):
    # 用户id
    uid = models.AutoField(max_length=50,primary_key=True)
    # 用户昵称
    nickname = models.CharField(verbose_name='用户昵称',max_length=50)
    # 用户头像
    avatarurl = models.CharField(verbose_name='用户头像',max_length=100)
    #微信的openid
    openid=models.CharField(max_length=100,blank=True)
    #用户名，使用手机号
    username=models.CharField(max_length=20,blank=True)
    #用户密码
    userpwd=models.CharField(max_length=50,blank=True)
    #宝宝id
    bid=models.ForeignKey('baby.BabyInfo',on_delete=models.CASCADE,related_name='babyinfo',related_query_name='babyinfo',null=True)


    def __str__(self):
        return self.nickname