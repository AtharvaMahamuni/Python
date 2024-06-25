from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'Masala'),
        ('KL', 'Kiwi'),
        ('GR', 'Ginger'),
        ('PL', 'Plain'),
        ('EL', 'Elaichi'),
    ]
    name = models.CharField(max_length=50)   
    image = models.ImageField(upload_to='chais/') 
    date_added = models.DateField(default=timezone.now)
    chai_type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    
    def __str__(self):
        return self.name

    
    
