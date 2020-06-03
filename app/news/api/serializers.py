from datetime import datetime

from django.utils.timesince import timesince
from rest_framework import serializers

from news.models import Article, Journalist


class ArticleSerializer(serializers.ModelSerializer):

    time_since_publication = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'

    def get_time_since_publication(self, object):
        publication_data = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_data, now)

        return time_delta

    def validate(self, data):
        if data['title'] == data['description']:
            raise serializers.ValidationError(
                'Title and description must be different from one and other')

        return data

    def validate_title(self, value):
        if len(value) < 60:
            raise serializers.ValidationError(
                'Title has to be at least 60 chars')

        return value


class JournalistSerializer(serializers.ModelSerializer):
    articles = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='article-detail',
    )

    class Meta:
        model = Journalist
        fields = '__all__'
