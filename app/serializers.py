from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, ImageField, EmailField, IntegerField, CurrentUserDefault, HiddenField
from rest_framework.serializers import ModelSerializer, Serializer

from app.models import Posts, Comment
User = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class PostSerializers(ModelSerializer):
    author = HiddenField(default=CurrentUserDefault())

    # def save(self, **kwargs):
    #     request = self.context.get('request')
    #     kwargs['author'] = request.user
    #     return super().save(**kwargs)

    # age = IntegerField(required=False, read_only=True)

    # def validate(self, attrs):
    #     print(attrs.get('age'))
    #     if age := attrs.pop('age'):
    #         attrs['title'] = f"{attrs['title']}-{age}"
    #     return super().validate(attrs)

    class Meta:
        model = Posts
        fields = ('title', 'author', 'description')

        # read_only_fields = ['author']
        # write_only_fields = ['title']
        #
        # extra_kwargs = {
        #     'author': {'read_only': True},
        #     'description': {'write_only': True},
        # }

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['author'] = UserSerializer(instance.author).data
        repr['example'] = 'test 3232'

        return repr


class CommentSerializer(ModelSerializer):
    # text = CharField(max_length=15, required=False)
    class Meta:
        model = Comment
        exclude = ()


class FormSerializers(Serializer):
    name = CharField(max_length=255)
    phone = CharField(max_length=25, required=False)
    image = ImageField(required=False)
    email = EmailField(max_length=15, write_only=True)
    address = CharField(max_length=150, min_length=10, allow_blank=True)

    def validate_name(self, attrs):
        if not attrs.isalpha():
            raise ValidationError('ism yuboring')
        return attrs

    def validate_phone(self, attrs):
        if not attrs.isnumeric():
            raise ValidationError('nomerni togri yozing')
        return attrs

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        return repr

