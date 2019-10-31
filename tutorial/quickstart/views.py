from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer
from django.shortcuts import redirect, HttpResponse, reverse


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# 不知道为什么不行
class Test(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    print("this is test_class.")


def test_func():
    return HttpResponse("this is test_func.")
