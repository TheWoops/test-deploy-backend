# Generated by Django 3.1.7 on 2021-03-24 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0004_system_protocol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='system',
            name='password',
            field=models.CharField(default='pw', help_text='password to access system', max_length=30),
        ),
        migrations.AlterField(
            model_name='system',
            name='token',
            field=models.CharField(default='pw', help_text='OATH Token to access system', max_length=255),
        ),
        migrations.AlterField(
            model_name='system',
            name='user',
            field=models.CharField(default='pw', help_text='username to access system', max_length=20),
        ),
    ]
