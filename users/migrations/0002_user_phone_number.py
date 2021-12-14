# Generated by Django 2.2.25 on 2021-12-14 15:59

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=phone_field.models.PhoneField(blank=True, help_text='Número de telefone', max_length=31),
        ),
    ]
