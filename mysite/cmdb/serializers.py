# -*-coding:utf-8 -*-

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from cmdb.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class DeptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dept
        fields = ('url', 'name', 'ownername','ownerid','ownermail','status','memo')