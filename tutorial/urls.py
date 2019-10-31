"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path

# jwt插件导入的包。
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# 第一种设计而导入的包。
# from django.conf.urls import url, include
# from django.contrib.auth.models import User
# from rest_framework import serializers, viewsets, routers

# 第二种设计而导入的包。
from django.urls import include, path
from rest_framework import routers
from tutorial.quickstart import views

# 第一种设计创建序列化、视图集和路由。
# # Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']
#
#
# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# # Routers provide a way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

# # 第二种设计创建路由。
# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
# # 以下用法有待学习。
# # router.register(r'test_func', views.test_func())
# # router.register(r'test', views.Test)
#
# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),

    # 在主路由设置url认证和在app路由中设置url认证都行。
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # 在项目的主路由中，把app中的snippets的路由包含进来。
    path('', include('snippets.urls')),

    # jwt插件的token路由。
    # 获取token路由
    path(r'api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # 刷新token路由
    path(r'api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # 验证token路由
    path(r'api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # url(r'^', include(router.urls)),
#     # path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
# ]
