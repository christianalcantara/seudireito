from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^createaccount/$', views.createaccount, name='create_account'),
]
