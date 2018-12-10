from django.db import models
from django.utils import timezone
'''宝宝信息表'''


class BabyInfo(models.Model):
    SEX=(('A','男'),('B','女'))
    # 主键id
    bid = models.AutoField(max_length=10, primary_key=True)
    # 姓名
    name = models.CharField(verbose_name='姓名',max_length=30)
    # 性别
    sex = models.CharField(verbose_name='性別',max_length=10,choices=SEX,default='A')
    # 年龄
    age = models.CharField(verbose_name='年龄',max_length=10)
    # 生日
    birthday = models.DateField(verbose_name='生日',max_length=10)
    #身高
    height=models.CharField(verbose_name='身高',max_length=20,blank=True)
    #体重
    weight=models.CharField(verbose_name='体重',max_length=20,blank=True)

    def __str__(self):
        return self.name



