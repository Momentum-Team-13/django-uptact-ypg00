# Generated by Django 4.0.3 on 2022-06-29 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0008_rename_note_note_text_field'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='text_field',
            new_name='notes',
        ),
    ]