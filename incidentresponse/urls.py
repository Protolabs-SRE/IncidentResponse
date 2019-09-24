from django.contrib import admin
from django.urls import path, include
import incidentresponse.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('slack/', include('response.slack.urls')),
    path('core/', include('response.core.urls')),
    path('', include('response.ui.urls')),
    path('', views.active_incidents, name='active_incidents'),
    path('active', views.active_incidents, name='active_incidents'),
    path('recent', views.recent_incidents, name='recent_incidents'),
]
