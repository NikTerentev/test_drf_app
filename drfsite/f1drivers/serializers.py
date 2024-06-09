import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Racer


# class RacerModel:
#    def __init__(self, title, content):
#        self.title = title
#        self.content = content


class RacerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Racer
        fields = "__all__"
