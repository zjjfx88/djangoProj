# Generated by Django 2.0.1 on 2018-03-01 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='code',
            field=models.CharField(default='sa', max_length=32),
            preserve_default=False,
        ),
    ]
