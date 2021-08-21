from rest_framework import serializers
from .models import UserModel

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id','first_name','last_name','email','password','weight','height','age','location','gender']
        extra_kwargs = {
                'password':{'write_only':True}
            }

    def create(self, validated_data):
        password = validated_data.pop('password',None)
        serializer = self.Meta.model(**validated_data)
        if password is not None:
            serializer.set_password(password)
        serializer.save()
        return serializer


class AuthorDetails(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'first_name', 'last_name']