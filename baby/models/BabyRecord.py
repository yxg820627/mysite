from django.db import models
from django.utils import timezone

'''喂养记录表'''


class BabyRecord(models.Model):
    FEEDTYPE = (('A', '母乳'), ('B', '奶粉'), ('C', '拉臭臭'), ('D', '换尿不湿'), ('E', '睡觉'))
    # 主键id
    id = models.AutoField(max_length=20, primary_key=True)
    # 记录类型，1为母乳，2为奶粉，3为拉臭臭，4为换尿不湿，5为睡觉
    type = models.CharField(verbose_name='记录类型',max_length=10, choices=FEEDTYPE, default='A')
    # 喂养量,type为4或5时，该字段为空
    volume = models.CharField(verbose_name='喂养量',max_length=50, blank=True,)
    # 开始时间
    starttime = models.DateTimeField(verbose_name='开始时间')
    # 结束时间
    endtime = models.DateTimeField(verbose_name='结束时间')
    # 记录时间
    recordtime = models.DateTimeField(verbose_name='记录时间',default=timezone.now)
    # BabyInfo表bid
    bid = models.ForeignKey('baby.BabyInfo', on_delete=models.CASCADE, related_name='baby', related_query_name='baby',verbose_name="宝宝姓名")
    # 记录人
    uid = models.ForeignKey('baby.User', on_delete=models.CASCADE, related_name='user', related_query_name='user',verbose_name='记录人')

    def __str__(self):
        return str(self.recordtime).format('%Y-%m-%d %H:%M:%S') + " -- " + self.get_type_display()
