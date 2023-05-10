# Generated by Django 4.2.1 on 2023-05-10 21:27

import client.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=16, unique=True, validators=[client.validators.validate_phone], verbose_name='phone')),
                ('tag', models.CharField(max_length=64, verbose_name='tag')),
                ('location', models.CharField(choices=[('Russia, Anadyr - Asia/Anadyr', 'Russia, Anadyr'), ('Russia, Astrakhan - Europe/Astrakhan', 'Russia, Astrakhan'), ('Russia, Barnaul - Asia/Barnaul', 'Russia, Barnaul'), ('Russia, Chita - Asia/Chita', 'Russia, Chita'), ('Russia, Irkutsk - Asia/Irkutsk', 'Russia, Irkutsk'), ('Russia, Kaliningrad - Europe/Kaliningrad', 'Russia, Kaliningrad'), ('Russia, Kamchatka - Asia/Kamchatka', 'Russia, Kamchatka'), ('Russia, Khandyga - Asia/Khandyga', 'Russia, Khandyga'), ('Russia, Kirov - Europe/Kirov', 'Russia, Kirov'), ('Russia, Krasnoyarsk - Asia/Krasnoyarsk', 'Russia, Krasnoyarsk'), ('Russia, Magadan - Asia/Magadan', 'Russia, Magadan'), ('Russia, Moscow - Europe/Moscow', 'Russia, Moscow'), ('Russia, Novokuznetsk - Asia/Novokuznetsk', 'Russia, Novokuznetsk'), ('Russia, Novosibirsk - Asia/Novosibirsk', 'Russia, Novosibirsk'), ('Russia, Omsk - Asia/Omsk', 'Russia, Omsk'), ('Russia, Sakhalin - Asia/Sakhalin', 'Russia, Sakhalin'), ('Russia, Samara - Europe/Samara', 'Russia, Samara'), ('Russia, Saratov - Europe/Saratov', 'Russia, Saratov'), ('Russia, Srednekolymsk - Asia/Srednekolymsk', 'Russia, Srednekolymsk'), ('Russia, Tomsk - Asia/Tomsk', 'Russia, Tomsk'), ('Russia, Ulyanovsk - Europe/Ulyanovsk', 'Russia, Ulyanovsk'), ('Russia, Ust-Nera - Asia/Ust-Nera', 'Russia, Ust-Nera'), ('Russia, Vladivostok - Asia/Vladivostok', 'Russia, Vladivostok'), ('Russia, Volgograd - Europe/Volgograd', 'Russia, Volgograd'), ('Russia, Yakutsk - Asia/Yakutsk', 'Russia, Yakutsk'), ('Russia, Yekaterinburg - Asia/Yekaterinburg', 'Russia, Yekaterinburg')], max_length=128, verbose_name='location')),
            ],
            options={
                'verbose_name': 'client',
                'verbose_name_plural': 'clients',
            },
        ),
    ]
