# Generated by Django 4.0.1 on 2022-01-11 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='upvotes',
            new_name='upvote',
        ),
    ]
