from rest_framework import serializers
from django.contrib.auth.models import User
from models.models import *


class AnekdotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anekdot
        fields = '__all__'


class AnekdotGenerationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anekdot
        fields = [
            'model_name',
            't',
            'p',
            'k',
            'rep_penalty',
        ]


class AnekdotRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anekdot
        fields = [
            'id',
            'rating'
        ]

class AnekdotNextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anekdot
        fields = ['id']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]


class InviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invite
        fields = ['code']
