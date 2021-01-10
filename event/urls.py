"""events URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^addUser/$', views.add_user_view, name='addUser'),
    url(r'^login/$', views.login_user_view, name='login'),
    url(r'^getEvents/$', views.all_events_view, name='getEvents'),
    url(r'^addEvent/$', views.add_event_view, name='addEvent'),
    url(r'^editEvent/$', views.edit_event_view, name='editEvent'),
    url(r'^editEvent/$', views.edit_event_view, name='editEvent'),
    url(r'^removeEvent/$', views.delete_event_view, name='removeEvent'),
    url(r'^getCategory/$', views.category_event_view, name='getCategory'),
    url(r'^getTipology/$', views.tipology_event_view, name='getTipology'),
]
