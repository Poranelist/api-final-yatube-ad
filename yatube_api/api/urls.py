from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from api.views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

app_name = 'api'
router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register('follow', FollowViewSet, basename='follows')
comment_router = routers.DefaultRouter()
comment_router.register(r'comments', CommentViewSet, basename='comments')
urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/posts/<int:post_id>/', include(comment_router.urls)),
    path('v1/jwt/create/',
         jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/jwt/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('v1/jwt/verify/',
         jwt_views.TokenVerifyView.as_view(),
         name='token_verify'),
]
