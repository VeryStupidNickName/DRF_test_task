from rest_framework import serializers
from app.models import *


class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadModel
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultModel
        fields = ['username', 'spent_money', 'gems']