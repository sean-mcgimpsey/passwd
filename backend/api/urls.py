# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views
from .views import retrieveSecretView

router = routers.DefaultRouter()
router.register(r'secrets', views.secretViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('retrieve/', retrieveSecretView.as_view(), name='retrieve-secret'),
]
