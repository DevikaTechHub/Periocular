from django.db import models

# Create your models here.
class Organisation(models.Model):
    organisation_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=20)
    address = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'organisation'
