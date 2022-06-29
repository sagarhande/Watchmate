from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ["watchlist"]
        # fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    platform = serializers.CharField(source='platform.name')

    class Meta:
        model = WatchList
        fields = "__all__"

    def create(self, validated_data):
        return WatchList.objects.create(**validated_data)


class StreamPlatformSerializer(serializers.ModelSerializer):
    # below field is example of nested serialization
    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"



# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         """ Create and return a new `movie` instance, given the validated data."""
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """Update and return an existing movie instance, given the validated data."""
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#
    # def validate(self, data):
    #     """Check if name and Description is same"""
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Name and Description can't be same!")
    #     return data
    #
    # def validate_name(self, value):
    #     """Validate the name field"""
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!")
    #     return value
