# Generated by Django 4.1 on 2022-09-07 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='weather',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
