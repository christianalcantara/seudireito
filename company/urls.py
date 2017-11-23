from django.conf.urls import url
from . import views
from django.utils.translation import ugettext_lazy as _


urlpatterns = [
    url(_(r'^createaccount/$'), views.createaccount, name='create_account'),
    url(_(r'^quotations/$'), views.quotations, name='quotations'),
    url(_(r'^quotation/create/$'), views.quotation_create, name='quotation_create'),
    url(_(r'^quotation/(?P<pk>[0-9]+)/proposals/$'), views.quotation_proposals, name='quotation_proposals'),
]
