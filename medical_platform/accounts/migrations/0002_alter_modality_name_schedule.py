# Generated by Django 4.2 on 2024-06-14 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modality',
            name='name',
            field=models.CharField(choices=[('КТ', 'КТ'), ('ММГ', 'ММГ'), ('ФЛГ', 'ФЛГ'), ('Денситометрия', 'Денситометрия'), ('РГ', 'РГ')], max_length=100, unique=True),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time_from', models.TimeField()),
                ('time_to', models.TimeField()),
                ('description', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
