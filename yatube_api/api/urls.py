from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.apps import ApiConfig
from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = ApiConfig.name

router = DefaultRouter()
router.register('posts', PostViewSet, basename='Post')
router.register('groups', GroupViewSet, basename='Group')
router.register(
    'posts/(?P<post_id>[0-9]+)/comments',
    CommentViewSet,
    basename='Comment',
)
router.register('follow', FollowViewSet, basename='Follow')


urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
]
