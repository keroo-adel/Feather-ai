# Generated by Django 3.2.19 on 2023-06-16 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library_template', '0029_emailtools'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_purpose', models.CharField(max_length=255)),
                ('tone_of_voice', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
                ('num_generated_emails', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='EmailTools',
        ),
        migrations.AddField(
            model_name='emailsubject',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_template.project'),
        ),
    ]
