from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    work_rate = models.FloatField(default=1.0)
    primary_modality = models.CharField(max_length=100)
    additional_modalities = models.ManyToManyField('Modality', blank=True)
    admin = models.BooleanField(default=False)

    # Удаление переопределенных полей groups и user_permissions для устранения конфликтов
    # groups = models.ManyToManyField('auth.Group', related_name='custom_user_set', blank=True)
    # user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_set', blank=True)

class Modality(models.Model):
    MODALITY_CHOICES = [
        ('КТ', 'КТ'),
        ('ММГ', 'ММГ'),
        ('ФЛГ', 'ФЛГ'),
        ('Денситометрия', 'Денситометрия'),
        ('РГ', 'РГ'),
    ]

    name = models.CharField(max_length=100, choices=MODALITY_CHOICES, unique=True)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='schedules')
    date = models.DateField()
    time_from = models.TimeField()
    time_to = models.TimeField()
    description = models.TextField()

    def __str__(self):
        return f"{self.date} {self.time_from}-{self.time_to}: {self.user.username}"

