# Generated by Django 4.1 on 2022-09-26 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='summary',
            field=models.TextField(),
        ),
    ]