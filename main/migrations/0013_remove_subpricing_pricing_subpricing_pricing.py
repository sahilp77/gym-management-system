# Generated by Django 5.1.2 on 2024-10-16 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_pricing_highlight_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subpricing',
            name='pricing',
        ),
        migrations.AddField(
            model_name='subpricing',
            name='pricing',
            field=models.ManyToManyField(to='main.pricing'),
        ),
    ]
