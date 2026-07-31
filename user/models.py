from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=20)
    house_name = models.CharField(max_length=45)
    place = models.CharField(max_length=45)
    pin_code = models.CharField(max_length=45)
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'user'

