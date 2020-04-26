from django.db import models


class Tours(models.Model):
    title=models.CharField(max_length=100,null=True)
    pershkrim=models.CharField(max_length=300)
    dataNisjes=models.CharField(max_length=30)
    dataKthimit=models.CharField(max_length=30)
    cmimi=models.CharField(max_length=30)
    nrDitesh=models.CharField(max_length=30)
    foto=models.ImageField(upload_to="images/", null=True)

    def __str__(self):
        return self.title

class FavTours(models.Model):
    title=models.CharField(max_length=100,null=True)
    pershkrim = models.CharField(max_length=300)
    dataNisjes = models.CharField(max_length=30)
    dataKthimit = models.CharField(max_length=30)
    cmimi = models.CharField(max_length=30)
    nrDitesh = models.CharField(max_length=30)
    foto = models.ImageField(upload_to="images/", null=True)


    def __str__(self):
        return self.title

class Kontakt(models.Model):
    first_name=models.CharField(max_length=200,null=True)
    last_name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200)
    message=models.CharField(max_length=1000)
    tel=models.CharField(max_length=30)
    select=models.CharField(max_length=100)


    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)