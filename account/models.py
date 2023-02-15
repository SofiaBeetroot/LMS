from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    POSITION_LIST = [
        ('BD', 'Back-end developer'),
        ('DS', 'Data scientist'),
        ('PD', 'Python developer')
    ]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    position = models.CharField(max_length=2, choices=POSITION_LIST)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
