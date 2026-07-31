from django.db import models

# Create your models here.
class JobVacancy(models.Model):
    job_vacancy_id = models.AutoField(primary_key=True)
    company = models.CharField(max_length=45)
    designation = models.CharField(max_length=45)
    qualification = models.CharField(max_length=45)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'job_vacancy'

