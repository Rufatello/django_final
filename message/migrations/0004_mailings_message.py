# Generated by Django 5.0 on 2023-12-26 09:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_alter_mailings_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailings',
            name='message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='message.message', verbose_name='Письмо'),
        ),
    ]
