# Generated by Django 5.0.2 on 2024-02-25 08:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rmd_web', '0005_rename_comments_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rmd_web.post'),
        ),
    ]
