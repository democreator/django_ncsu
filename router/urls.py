from django.conf.urls import url, include

from rest_framework import routers

from .viewsets import RouterViewset

r = routers.DefaultRouter()
r.register(u'generate', RouterViewset, basename='api_generate')

urlpatterns = [
    url(r'^api/', include(r.urls)),
]
