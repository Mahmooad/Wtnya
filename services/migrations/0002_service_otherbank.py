# Generated by Django 4.0.4 on 2022-04-29 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='otherBank',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
