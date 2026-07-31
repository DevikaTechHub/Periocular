from django.db import models
from authority.models import Authority

# Create your models here.
class Feature(models.Model):
    feature_id = models.AutoField(primary_key=True)
    features = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    # authority_id = models.IntegerField()
    authority=  models.ForeignKey(Authority,on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'feature'
