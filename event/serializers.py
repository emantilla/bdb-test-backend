from rest_framework import serializers

from event.models import Tipology, Category, Event, User


class TipologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipology
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


