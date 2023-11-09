# Generated by Django 3.0.2 on 2020-06-01 07:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('passwords', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='passwords',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='passwords', to=settings.AUTH_USER_MODEL),
        ),
    ]
