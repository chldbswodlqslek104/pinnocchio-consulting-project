from django.urls import path, include
from .views import index
from .views import Api2_list 

urlpatterns = [
    path('', index, name='index.html'),
    path("Api_list/", Api2_list),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]