from mongoengine import Document, StringField, DateTimeField, IntField, BooleanField
import datetime


class User(Document):
    _id = IntField()
    username = StringField(max_length=250, required=True)
    password = StringField(max_length=250, required=True)
    disabled = BooleanField(default=False)
    date_created = DateTimeField(default=datetime.datetime.utcnow)
    date_modified = DateTimeField(default=datetime.datetime.utcnow)
