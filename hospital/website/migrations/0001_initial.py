# Generated by Django 4.2.7 on 2023-11-15 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=50)),
                ('peso', models.FloatField()),
                ('edad', models.IntegerField()),
                ('fechacumple', models.DateTimeField()),
            ],
        ),
    ]
