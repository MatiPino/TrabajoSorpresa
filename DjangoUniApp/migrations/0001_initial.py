# Generated by Django 3.2.3 on 2021-06-01 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recordatorios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(max_length=10)),
                ('asunto', models.CharField(max_length=100)),
                ('texto', models.CharField(max_length=200)),
            ],
        ),
    ]
