"""gumi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers, permissions

# swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# swagger 정보 설정, 관련 엔드포인트 추가
# swagger 엔드포인트는 DEBUG Mode에서만 노출
schema_view = get_schema_view(
    openapi.Info(
        title="GumiTour API",
        default_version='v1',
        description="",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    url='https://k3d201.p.ssafy.io:8080',
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('accounts.urls')),
    path('tour/', include('tour.urls')),
    path('review/', include('review.urls')),

    # swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),

    # rest-auth
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/signup/', include('rest_auth.registration.urls')),
]
