# Generated by Django 3.2.19 on 2023-06-18 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_template', '0035_remove_socialmediapost_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='outlines',
            field=models.ManyToManyField(blank=True, null=True, to='library_template.Outline'),
        ),
    ]
