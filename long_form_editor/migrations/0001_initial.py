# Generated by Django 3.2.19 on 2023-06-01 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('html', models.TextField()),
                ('tag', models.CharField(default='p', max_length=10)),
            ],
        ),
    ]