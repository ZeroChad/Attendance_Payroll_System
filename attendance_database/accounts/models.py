from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now, localdate
from datetime import datetime, date, time , timedelta

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('employee', 'Employee'),
        ('manager', 'Manager'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='employee')

    SEX_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    )
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, default='male')
    birthday = models.DateField(default=now)
    date_joined = models.DateField(default=now, editable=False)

    @property
    def age(self):
        date_now = localdate(now())
        age = (
            date_now.year
            - self.birthday.year
            - ((date_now.month, date_now.day) < (self.birthday.month, self.birthday.day))
        )
        return age

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        super().save(*args, **kwargs)


