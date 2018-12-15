from mongoengine import Document, StringField, IntField


class Highscore(Document):
    level = StringField()
    name = StringField()
    diem = IntField()
