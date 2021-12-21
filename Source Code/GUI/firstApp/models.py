from django.db import models

# Create your models here.
class FeedBacks(models.Model):
    name = models.CharField(max_length=50)
    email =  models.CharField(max_length=50)
    desc =  models.CharField(max_length=122)
    


    def __str__(self):
        return self.name


class RadioFeedBacks(models.Model):
    rname = models.CharField(max_length=50)
    rdesc =  models.CharField(max_length=122)
    


    def __str__(self):
        return self.rname