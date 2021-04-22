from django.contrib.auth.models import User, Group

from rest_framework import serializers
from apirest.models import Printer


class PrinterSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(required=False, allow_blank=True, max_length=100)
    description = serializers.CharField(required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `Printer` instance, given the validated data.
        """
        return Printer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Printer` instance, given the validated data.
        """
        instance.name = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']