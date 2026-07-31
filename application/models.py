from django.db import models
from cert_details.models import CertDetails
from user.models import User

# Create your models here.
class Application(models.Model):
    application_id = models.AutoField(primary_key=True)
    # user_id = models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # cert_details_id = models.IntegerField()
    cert_details=models.ForeignKey(CertDetails,on_delete=models.CASCADE)
    rules = models.CharField(max_length=45)
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'application'
