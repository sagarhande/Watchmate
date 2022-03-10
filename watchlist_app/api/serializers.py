from rest_framework import serializers
from watchlist_app.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    # Below is for custom method to know more read DRF docs- API guide-> serializer fields
    name_len = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "__all__"
        # fields = ['id','name','description']          # only few fields added
        # exclude = ['active']                            # if need to exclude few from many fields

        def get_name_len(self, object):
            """This is custom method to return len of name field"""
            return len(object.name)

        def validate(self, data):
            """Check if name and Description is same"""
            if data['name'] == data['description']:
                raise serializers.ValidationError("Name and Description can't be same!")
            return data

        def validate_name(self, value):
            """Validate the name field"""
            if len(value) < 2:
                raise serializers.ValidationError("Name is too short!")
            return value

#
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
