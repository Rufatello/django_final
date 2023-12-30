# Generated by Django 4.2.7 on 2023-12-30 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0010_mailings_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(blank=True, null=True, verbose_name='дата')),
                ('state', models.CharField(choices=[('start', 'Запущена'), ('finish', 'Завершена'), ('created', 'Создана')], default='start', max_length=10, verbose_name='Статус')),
                ('email_answer', models.BooleanField(default=False, verbose_name='ответ от почты')),
            ],
        ),
    ]
