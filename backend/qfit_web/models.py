from django.db import models

# Create your models here.

class Data(models.Model):
    
    title = models.CharField(max_length = 200)

    def __str__(self):
        return self.title


class Feature(models.Model):
    title = models.CharField(max_length=200)
    values= models.JSONField()
    data = models.ForeignKey(Data, on_delete = models.CASCADE)

    def __str__(self):
        return self.title




    

