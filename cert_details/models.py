from django.db import models

# Create your models here.

class CertDetails(models.Model):
    cert_details_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=150)
    type = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'cert_details'
