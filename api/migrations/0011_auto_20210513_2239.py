# Generated by Django 3.1.7 on 2021-05-13 16:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='rate_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='anime',
            name='rating',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]