# Generated by Django 4.2.7 on 2023-11-23 19:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='event',
            name='Please check date event',
        ),
        migrations.AlterField(
            model_name='participants',
            name='participation_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 11, 23, 20, 2, 0, 462527)),
        ),
        migrations.AddConstraint(
            model_name='event',
            constraint=models.CheckConstraint(check=models.Q(('evt_date__gte', datetime.datetime(2023, 11, 23, 20, 2, 0, 461527))), name='Please check date event'),
        ),
    ]
