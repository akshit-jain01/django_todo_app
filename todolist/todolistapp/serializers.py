from rest_framework import serializers
from .models import Task


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    taskTitle = serializers.CharField(required=False, allow_blank=True, max_length=100)
    taskDescription = serializers.CharField(style={'base_template': 'textarea.html'})
    bookmark = serializers.BooleanField(required=False)
    # language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    # style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.taskTitle = validated_data.get('taskTitle', instance.taskTitle)
        instance.taskDescription = validated_data.get('taskDescription', instance.taskDescription)
        instance.bookmark = validated_data.get('bookmark', instance.bookmark)
        # instance.language = validated_data.get('language', instance.language)
        # instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
