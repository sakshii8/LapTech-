# Generated by Django 3.2.12 on 2022-04-29 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0007_service'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Service',
            new_name='Enquiry',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
