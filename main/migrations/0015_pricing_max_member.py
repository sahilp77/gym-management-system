# Generated by Django 5.1.2 on 2024-10-20 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_subpricing_pricing'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricing',
            name='max_member',
            field=models.IntegerField(null=True),
        ),
    ]