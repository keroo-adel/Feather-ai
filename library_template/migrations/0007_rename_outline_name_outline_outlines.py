# Generated by Django 3.2.19 on 2023-06-12 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_template', '0006_alter_outline_outline_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='outline',
            old_name='outline_name',
            new_name='Outlines',
        ),
    ]