from peewee import *
from datetime import datetime

db = PostgresqlDatabase(
    'second_flask_db1',
    host = 'localhost',
    port = 5432,
    user = 'second_flask_user',
    password = 'qwe123'
)
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Post(BaseModel):
    login = CharField(max_length=255, null=False)
    password = CharField(max_length=255, null=False)
    date = DateField(default=datetime.now)

    def __repr__(self):
        return self.login

db.create_tables([Post])

db.close()