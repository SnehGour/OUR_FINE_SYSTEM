from django.db import models
# Create your models here.

class login(models.Model):
    Username=models.CharField(max_length=100 ,primary_key=True)
    Password=models.CharField(max_length=100)

    def __str__(self):
        return self.Username


class RULEs(models.Model):
    Rule=models.CharField(max_length=500)
    Fine_amount=models.IntegerField()
    def __str__(self):
        return self.Rule

class Apply_Fine(models.Model):
    Username = models.ForeignKey(login,on_delete=models.CASCADE)
    Rule =models.ForeignKey(RULEs,on_delete=models.CASCADE)
    id=models.IntegerField(primary_key=True)
    Fine_Amount =models.IntegerField()
    Date=models.DateTimeField()
    
    def __str__(self):
        return self.Username

