# Generated by Django 3.2.16 on 2024-06-29 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='text',
            new_name='description',
        ),
    ]
