# Generated by Django 3.2.13 on 2022-06-30 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimoni',
            name='nama',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
