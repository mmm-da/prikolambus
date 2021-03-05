from django.conf.urls import url

from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import *


router = DefaultRouter()

router.register(r'anekdot', AnekdotViewSet, basename='anekdot')
router.register(r'rate', AnekdotRatingViewSet, basename='rate')
router.register(r'generate', AnekdotGeneratorViewSet, basename='generate')
router.register(r'register', UserViewSet, basename='register')

schema_view = get_schema_view(
    openapi.Info(
        title="API с приколом",
        default_version='v1'
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    url(r'^swagger/$', schema_view.with_ui('swagger',
                                           cache_timeout=0), name='schema-swagger-ui'),
    url(r'^token', TokenObtainPairView.as_view(), name="login"),
    url(r'^token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


urlpatterns += router.urls
