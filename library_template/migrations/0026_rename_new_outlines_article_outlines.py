# Generated by Django 3.2.19 on 2023-06-14 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_template', '0025_auto_20230615_0240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='new_outlines',
            new_name='outlines',
        ),
    ]
