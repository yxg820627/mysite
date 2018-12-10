from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^myset/', admin.site.urls),
    # url(r'^polls/', include('polls.urls')),
    # url(r'^myapp/',include('myapp.urls')),
    url(r'^baby/',include('baby.urls')),
]