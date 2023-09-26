from django.db import models

# Create your models here.

class Tasks(models.Model):
    Task=models.CharField(max_length=500)
    Date=models.DateTimeField()
    IsActive=models.BooleanField(default=True)
    CreatedDate=models.DateTimeField(auto_now=True)
    CreatedBy=models.TextField()
    IsDelete=models.IntegerField(default='0')

    def __str__(self):
        return self.Task