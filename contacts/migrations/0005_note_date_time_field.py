# Generated by Django 4.0.3 on 2022-06-28 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_contact_note_note_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='date_time_field',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
