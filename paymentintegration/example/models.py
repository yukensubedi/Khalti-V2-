from django.db import models

# Create your models here.
class verification(models.Model):
    pidx = models.CharField(max_length=200)
    def  __str__(self):
        return self.pidx
    class Meta:
        verbose_name = "verification"
        verbose_name_plural = "verification"

class payment_status(models.Model):
    details = models.JSONField()
   
    
        