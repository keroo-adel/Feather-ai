# Generated by Django 3.2.19 on 2023-06-12 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_template', '0004_auto_20230611_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outline',
            name='sub_topic',
            field=models.CharField(max_length=100, null=True),
        ),
    ]