from django.db import models

# Create your models here.

class Login(models.Model):
    login_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=45)
    password = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    u_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'login'

