# Generated by Django 4.2.16 on 2024-10-20 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_rename_contatc_contatct'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contatct',
            new_name='Contact',
        ),
    ]
