# Generated by Django 3.0.5 on 2020-11-07 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=70)),
                ('description', models.CharField(default='', max_length=200)),
                ('published', models.BooleanField(default=False)),
            ],
        ),
    ]
