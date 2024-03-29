# Generated by Django 4.2.1 on 2023-05-11 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_client_mobile_code'),
        ('main', '0002_mailing_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskMailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=128, verbose_name='task_id')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_client', to='client.client', verbose_name='client')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_mailing', to='main.mailing', verbose_name='mailing')),
            ],
            options={
                'verbose_name': 'task mailing',
                'verbose_name_plural': 'tasks mailing',
            },
        ),
    ]
