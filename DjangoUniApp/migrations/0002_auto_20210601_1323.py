# Generated by Django 3.2.3 on 2021-06-01 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoUniApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recordatorios',
            name='fecha',
        ),
        migrations.AddField(
            model_name='recordatorios',
            name='estado',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='recordatorios',
            name='fechafinal',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='recordatorios',
            name='fechainicio',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
