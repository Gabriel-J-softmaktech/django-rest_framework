from rest_framework import routers
from django.urls import path, include
from quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewset)

# wire up our API using automatic URL routing.
# additionally, we include login URLs for browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path("api-auth/", include('rest_framework.urls', namespace='rest_framework')),
    path("", include('snippets.urls', namespace="snippets")),
]
