from rest_framework import serializers
from .models import Developer,Game,Review

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    developer = DeveloperSerializer(read_only=True)
    developer_id = serializers.PrimaryKeyRelatedField(queryset=Developer.objects.all(), source='developer', write_only=True)
    class Meta:
        model = Game
        fields = ['id', 'title', 'genre', 'release_date', 'developer', 'developer_id']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'