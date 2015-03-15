from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from weatherapp import views

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'station', views.StationViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', 'weatherapp.views.home', name='home'),
)
