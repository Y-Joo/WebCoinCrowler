# Generated by Django 3.1.7 on 2021-04-02 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsed_data', '0002_auto_20210402_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdata',
            name='content',
            field=models.JSONField(default=dict),
        ),
    ]