# Generated by Django 5.0.2 on 2024-02-23 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rmd_web', '0004_remove_post_joined_date_post_created_at_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]