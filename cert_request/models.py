from django.db import models
from cert_details.models import CertDetails
from user.models import User
# Create your models here.

class CertRequest(models.Model):
    cert_request_id = models.AutoField(primary_key=True)
    # cert_details_id = models.IntegerField()
    cert_details=models.ForeignKey(CertDetails,on_delete=models.CASCADE)
    # user_id = models.IntegerField()
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    time = models.DateTimeField()
    status = models.CharField(max_length=45)
    proof = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'cert_request'

