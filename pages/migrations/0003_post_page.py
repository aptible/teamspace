# Generated by Django 4.1.7 on 2023-05-08 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='page',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pages.page'),
            preserve_default=False,
        ),
    ]
