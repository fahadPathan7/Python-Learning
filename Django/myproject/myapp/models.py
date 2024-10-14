from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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

# One to Many Relationship
class ChaReview(models.Model):
    cha = models.ForeignKey(ChaVarity, on_delete=models.CASCADE, related_name='reviews') # related_name is used to access the reviews of a particular cha.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} review for {self.cha.name}" # This will be the name of the object in the admin panel.

# Many to Many Relationship
class Store(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    cha_variety = models.ManyToManyField(ChaVarity, related_name='stores')

    def __str__(self):
        return self.name # This will be the name of the object in the admin panel.

# One to One Relationship
class ChaCertificate(models.Model):
    cha = models.OneToOneField(ChaVarity, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.cha.name} certificate" # This will be the name of the object in the admin panel.