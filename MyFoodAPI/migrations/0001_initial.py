# Generated by Django 4.1.2 on 2023-07-04 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('Desc', models.TextField()),
                ('delivery', models.CharField(max_length=300)),
                ('payment', models.CharField(max_length=300)),
                ('service', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='contacModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.IntegerField(default=0)),
                ('address', models.TextField()),
                ('Query', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HomeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('Desc', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='MenuModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('Desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.IntegerField(default=0)),
                ('foodName', models.CharField(max_length=200)),
                ('AdditionalFood', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=0)),
                ('myDate', models.DateTimeField(auto_now=True)),
                ('address', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
    ]
