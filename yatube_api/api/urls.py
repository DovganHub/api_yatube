from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import PostViewSet, CommentViewSet, GroupViewSet

v1_router = DefaultRouter()
v1_router.register('posts', PostViewSet)
v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, 'post_id')
v1_router.register(r'^groups', GroupViewSet, basename="groups")

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/api-token-auth/', obtain_auth_token),
]
