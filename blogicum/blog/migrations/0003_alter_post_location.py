# Generated by Django 3.2.16 on 2024-06-29 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_text_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.location', verbose_name='Местоположение'),
        ),
    ]