# Generated by Django 3.2.19 on 2023-06-17 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('long_form_editor', '0002_alter_block_html'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('block_type', models.CharField(choices=[('h1Style', 'Heading 1'), ('h2Style', 'Heading 2'), ('h3Style', 'Heading 3'), ('paragraphStyle', 'Paragraph'), ('listStyle', 'Bullet List')], max_length=20)),
                ('position', models.TextField()),
            ],
        ),
    ]
