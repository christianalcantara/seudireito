from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(_(r'^quotations/$'), views.quotations, name='quotations'),
    url(_(r'^quotation/(?P<pk>[0-9]+)/$'), views.quotation, name='quotation'),
]
