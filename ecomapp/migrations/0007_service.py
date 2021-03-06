# Generated by Django 3.2.12 on 2022-04-29 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0006_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('contact', models.TextField(max_length=25)),
                ('email', models.EmailField(max_length=25)),
                ('message', models.TextField(max_length=255)),
            ],
        ),
    ]
