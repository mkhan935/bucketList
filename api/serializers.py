from rest_framework import serializers
from .models import Bucketlist
from django.contrib.auth.models import User

class BucketlistSerializer(serializers.ModelSerializer):
    ''' turn the model into json '''
    owner = serializers.ReadOnlyField(source = 'owner.username')
    class Meta:
        model = Bucketlist
        fields = ('id', 'name', 'owner', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class UserSerializer(serializers.ModelSerializer):
    bucketlists = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Bucketlist.objects.all()
    )
    class Meta:
        model = User
        fields = ('id', 'username', 'bucketlists')
