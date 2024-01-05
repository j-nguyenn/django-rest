# Generated by Django 3.1.8 on 2023-12-13 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('type', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('cast', models.CharField(max_length=700)),
                ('country', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('listed_in', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1500)),
                ('release_year', models.CharField(max_length=100)),
                ('date_added', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
