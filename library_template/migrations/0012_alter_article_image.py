# Generated by Django 3.2.19 on 2023-06-14 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_template', '0011_remove_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='articles_images/'),
        ),
    ]