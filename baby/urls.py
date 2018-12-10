from django.conf.urls import url
from . import views
from .view import BabyRecordView,BabyView,UserView

app_name='baby'

urlpatterns=[
    # url(r'^$', views.index, name='index'),
    url(r'^getBabyById$',BabyView.getBabyById,name='getBabyById'),
    url(r'^record$',BabyRecordView.record,name='record'),
    url(r'^wxLogin$', UserView.wxLogin, name='wxLogin'),
    url(r'^userLogin$', UserView.userLogin, name='userLogin'),
]