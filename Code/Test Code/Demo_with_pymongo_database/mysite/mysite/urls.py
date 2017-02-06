"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings

from clinicflow.views import manage, viewer, login, schedule, setting, schedulelists, singleschedule

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login', login, name='login'), 
    url(r'^manage$', manage, name='manage'), 
    url(r'^viewer$', viewer, name='viewer'),  
    url(r'^schedule$', schedule, name='schedule'),  
    url(r'^setting$', setting, name='setting'), 
    url(r'^schedulelists$', schedulelists, name='schedulelists'),
    url(r'^singleschedule$', singleschedule, name='singleschedule'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

    
