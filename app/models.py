from django.db import models

# Create your models here.
class Catagery(models.Model):
    title = models.CharField( max_length=50)
    
    def __str__(self):
        return self.title
    
class Subcatagery(models.Model):
    catagery= models.ForeignKey(Catagery,  on_delete=models.CASCADE)
    name = models.CharField( max_length=50)
    amount = models.IntegerField()

    def __str__(self):
        return self.name
    
    