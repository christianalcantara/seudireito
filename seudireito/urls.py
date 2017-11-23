"""seudireito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.utils.translation import ugettext_lazy as _

from seudireito import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    url(_(r'^login/$'), auth_views.login, name='login'),
    url(_(r'^logout/$'), auth_views.logout, name='logout'),
    url(r'', include('website.urls', namespace='website')),
    url(_(r'^lawyer/'), include('lawyer.urls', namespace='lawyer')),
    url(_(r'^company/'), include('company.urls', namespace='company')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
)

if settings.DEBUG:
    urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
