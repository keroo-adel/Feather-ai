# Generated by Django 3.2.19 on 2023-06-17 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library_template', '0035_remove_socialmediapost_product_name'),
        ('long_form_editor', '0004_auto_20230617_0513'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='library_article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='editor_articles', to='library_template.article'),
        ),
    ]