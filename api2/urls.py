from urllib.parse import urlparse
from django.urls import URLPattern, include, path
from .views import Api2_list
urlpatterns = [
    path("Api_list/", Api2_list),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]