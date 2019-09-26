from django.db import models
from datetimeutc.fields import DateTimeUTCField

# Create your models here.
'''
CREATE TABLE user(
   user_id serial PRIMARY KEY,
   email VARCHAR (128) UNIQUE NOT NULL,
   username VARCHAR (50) NOT NULL,
   pass VARCHAR (50) NOT NULL,
   firstname VARCHAR (50) NOT NULL,
   animal VARCHAR (50) NOT NULL,
   created_on TIMESTAMP NOT NULL
);
'''
class User(models.Model):
    user_id = models.AutoField(primary_key=True, blank=True, default=None)
    email = models.CharField(max_length=128, unique=True, null=False)
    username = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False, db_column='pass')
    firstname = models.CharField(max_length=50, null=False)
    animal = models.CharField(max_length=50, null=False)
    created_on = DateTimeUTCField(auto_now_add=True)

    class Meta:
        db_table = "user"