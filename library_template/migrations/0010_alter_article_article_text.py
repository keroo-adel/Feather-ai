# Generated by Django 3.2.19 on 2023-06-14 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_template', '0009_auto_20230614_0444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
