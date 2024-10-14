from django.db import models
from django.utils import timezone

# Create your models here.
class ChaVarity(models.Model):
    CHA_TYPE_CHOICES = [
        ('ML', 'Milk Tea'),
        ('BL', 'Black Tea'),
        ('GR', 'Green Tea'),
        ('EL', 'Earl Grey Tea'),
    ] # This is a list of tuples. (Enum)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/') # upload_to is the directory where the image will be uploaded.
        ## If the directory does not exist, it will be created automatically. (media/images/)
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=5, decimal_places=2, default=20.00)
    date_created = models.DateTimeField(default=timezone.now)
    cha_type = models.CharField(max_length=2, choices=CHA_TYPE_CHOICES, default='ML')

    def __str__(self):
        return self.name # This will be the name of the object in the admin panel.
