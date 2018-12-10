from django.contrib import admin
from .models import BabyInfo,BabyRecord,User,BabyPhoto
import time

@admin.register(BabyInfo)
class BabyInfoAdmin(admin.ModelAdmin):
    def converBirthday(obj):
        return obj.birthday.strftime('%Y-%m-%d')
    converBirthday.short_description = '生日'

    list_display = ('bid','name','sex','age',converBirthday,'height','weight')
    search_fields = ['name']
    # list_filter = ['sex']

@admin.register(BabyRecord)
class BabyRecordAdmin(admin.ModelAdmin):

    def convertStrartTime(obj):
        return obj.starttime.strftime('%Y-%m-%d %H:%I:%S')

    convertStrartTime.short_description = '开始时间'

    def convertEndTime(obj):
        return obj.endtime.strftime('%Y-%m-%d %H:%I:%S')

    convertEndTime.short_description='结束时间'

    def convertRecordTime(obj):
        return obj.recordtime.strftime('%Y-%m-%d %H:%I:%S')

    convertRecordTime.short_description='记录时间'

    list_display = ('id','type','volume',convertStrartTime,convertEndTime,convertRecordTime,'bid','uid')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('uid','nickname','avatarurl','openid','username','userpwd','bid')

@admin.register(BabyPhoto)
class BabyPhotoAdmin(admin.ModelAdmin):
    list_display = ('pid','bid','imageurl','imagepath','createtime')


# admin.site.register(BabyInfo,BabyInfoAdmin)
# admin.site.register(BabyRecord,BabyRecordAdmin)
# admin.site.register(User)