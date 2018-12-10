from django.conf.urls import url
from . import views

app_name = 'myapp'

urlpatterns = [url(r'^$', views.IndexView.as_view(), name='index'),]
