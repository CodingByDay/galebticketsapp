# Generated by Django 3.0.7 on 2020-08-03 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200803_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tickets',
            name='email_as_send',
        ),
    ]