# Generated by Django 4.1.2 on 2023-05-26 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_ontology', '0002_collection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='description',
        ),
    ]
