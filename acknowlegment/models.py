from django.db import models
from user.models import User

# Create your models here.
class Acknowledgment(models.Model):
    acknowledgment_id = models.AutoField(primary_key=True)
    # user_id = models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    acknowledgment = models.CharField(max_length=100)
    date = models.DateTimeField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'acknowledgment'
