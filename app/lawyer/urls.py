from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from . import views

urlpatterns = [
    url(_(r'^createaccount/$'), views.createaccount, name='create_account'),
    url(_(r'^proposals/$'), views.proposals, name='proposals'),
]
