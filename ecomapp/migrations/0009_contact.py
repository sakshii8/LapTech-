# Generated by Django 3.2.12 on 2022-04-29 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0008_auto_20220429_1050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=25)),
                ('message', models.TextField(max_length=255)),
            ],
        ),
    ]
