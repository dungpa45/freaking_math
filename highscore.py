from mongoengine import Document, StringField, IntField


class Highscore(Document):
    name = StringField()
    diem = IntField()
