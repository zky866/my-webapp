from django.conf.urls.i18n import urlpatterns
from django.urls import path
from . import views
app_name="urls"
urlpatterns=[
    path("",views.urls,name="urls")

]