# Generated by Django 3.2.19 on 2023-06-18 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_template', '0036_alter_article_outlines'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='outlines',
            field=models.ManyToManyField(blank=True, to='library_template.Outline'),
        ),
    ]