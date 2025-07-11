from django.db import models
# Create your models here.
class tips(models.Model):
    tip_id=models.CharField(max_length=50)
    tip_name=models.CharField(max_length=100)
    tip_desc=models.CharField(max_length=500)
    tip_img=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.tip_id