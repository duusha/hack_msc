from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    work_rate = models.FloatField(default=1.0)
    primary_modality = models.CharField(max_length=100)
    additional_modalities = models.ManyToManyField('Modality', blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

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

