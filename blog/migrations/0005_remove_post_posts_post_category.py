# Generated by Django 5.0.6 on 2024-06-05 06:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_category_options_post_posts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='posts',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.category'),
            preserve_default=False,
        ),
    ]
