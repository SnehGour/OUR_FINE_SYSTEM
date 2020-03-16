from django.db import models
# Create your models here.

class login(models.Model):
    Username=models.CharField(max_length=100 ,primary_key=True)
    Password=models.CharField(max_length=100)

    def __str__(self):
        return self.Username
class Fine_apply(models.Model):
    Username = models.ForeignKey(login,on_delete=models.CASCADE)
    Rule =models.CharField(max_length=265)
    Fine_Amount =models.IntegerField()
    Date=models.DateTimeField()

    def __str__(self):
        a=self.Username
        b=str(self.Fine_Amount)
        return a+b