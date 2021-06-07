"""hawkpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('pages.urls')),
    url(r'^accounts/profile/', include('dashboard.urls')),
    url(r'^sudashboard/', include('sudashboard.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^payment/', include('payment.urls')),
]

urlpatterns += i18n_patterns(
    url(r'^', include('pages.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
)

'''
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
'''