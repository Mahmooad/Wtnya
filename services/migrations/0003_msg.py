# Generated by Django 4.0.4 on 2022-04-29 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_service_otherbank'),
    ]

    operations = [
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approveMsg', models.TextField(null=True)),
                ('regMsg', models.TextField(null=True)),
            ],
        ),
    ]
