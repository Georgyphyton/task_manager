# Generated by Django 4.2.4 on 2023-08-28 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0004_alter_statuses_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statuses',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Name'),
        ),
    ]
