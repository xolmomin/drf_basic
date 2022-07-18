from django.db import models
from django.db.models import Model, DateTimeField, CharField, TextField, ForeignKey, CASCADE, FileField


class BaseModel(Model):
    updated_at = DateTimeField(auto_now_add=True)
    created_at = DateTimeField(auto_now=True)


class Posts(BaseModel):
    title = CharField(max_length=255)
    description = TextField()
    author = ForeignKey('auth.User', CASCADE)


class Comment(BaseModel):
    post = ForeignKey('app.Posts', CASCADE)
    text = CharField(max_length=255)
    file = FileField(upload_to='comment/file/')
    author = ForeignKey('auth.User', CASCADE)


