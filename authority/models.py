from django.db import models

# Create your models here.
class Authority(models.Model):
    authority_id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=20)
    phone_no = models.CharField(unique=True, max_length=20, blank=True, null=True)
    name = models.CharField(max_length=45)
    location = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'authority'

