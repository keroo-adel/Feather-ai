# Generated by Django 3.2.19 on 2023-06-19 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_template', '0038_alter_article_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
