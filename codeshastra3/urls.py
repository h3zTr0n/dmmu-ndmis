# -*- coding: utf-8 -*-
"""codeshastra3 URL Configuration

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


    url(r'^classify/', cviews.index, name='index'),
    url(r'^(?P<testtweet_id>\d+)/tag/$', cviews.tag, name='tag'),
    url(r'^analysis/(?P<keyword>.+)$', cviews.analysis_keyword, name='analysis_keyword'),
    url(r'^analysis$', cviews.analysis_keyword, name='analysis_keyword'),
    url(r'^map$', cviews.osmap, name='osmap'),

"""
from django.conf.urls import url, include
from django.contrib import admin

from app import views
from classifier import views as cviews
from controlcenter.views import controlcenter

#
# import xadmin
# xadmin.autodiscover()
#
# from xadmin.plugins import xversion
# xversion.register_models()


urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    # url(r'xadmin/', include(xadmin.site.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^admin/dashboard/', controlcenter.urls),
    url(r'^$', views.home),
    url(r'^heatmap/', views.heatmap),
    url(r'^classifier/', include('classifier.urls')),
    #  (r'^forms/', include('form_designer.urls')),
    url(r'^report_builder/', include('report_builder.urls')),
]

admin.site.site_header = "NDMIS ADMINISTRATION"
admin.site.site_title = "National Disaster Management Information System"
# admin.site.site_header = "National Disaster Management Information System"
