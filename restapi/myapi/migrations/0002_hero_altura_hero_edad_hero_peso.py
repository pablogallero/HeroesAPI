# Generated by Django 4.1.2 on 2023-01-02 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='altura',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hero',
            name='edad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hero',
            name='peso',
            field=models.IntegerField(default=0),
        ),
    ]
