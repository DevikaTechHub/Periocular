from django.db import models
from job_vacancy.models import JobVacancy
from user.models import User
# Create your models here.
class JobApplication(models.Model):
    job_application_id = models.AutoField(primary_key=True)
    # job_vacancy_id = models.IntegerField()
    job_vacancy=models.ForeignKey(JobVacancy,on_delete=models.CASCADE)
    # user_id = models.IntegerField()
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    resume = models.CharField(max_length=200)
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'job_application'
