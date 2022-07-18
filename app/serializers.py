from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, ImageField, EmailField, IntegerField
from rest_framework.serializers import ModelSerializer, Serializer

from app.models import Posts, Comment


class PostSerializers(ModelSerializer):
    age = IntegerField()

    class Meta:
        model = Posts
        exclude = ()


class CommentSerializer(ModelSerializer):
    # text = CharField(max_length=15, required=False)
    class Meta:
        model = Comment
        exclude = ()


class FormSerializers(Serializer):
    name = CharField(max_length=255)
    phone = CharField(max_length=25, required=False)
    image = ImageField(required=False)
    email = EmailField(max_length=15)
    address = CharField(max_length=150, min_length=10, allow_blank=True)

    def validate_name(self, attrs):
        if not attrs.isalpha():
            raise ValidationError('ism yuboring')
        return attrs

    def validate_phone(self, attrs):
        if not attrs.isnumeric():
            raise ValidationError('nomerni togri yozing')
        return attrs

    def validate(self, attrs):
        return super().validate(attrs)
