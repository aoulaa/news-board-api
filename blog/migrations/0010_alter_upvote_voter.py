# Generated by Django 4.0.1 on 2022-01-12 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_upvote_voter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upvote',
            name='voter',
            field=models.CharField(max_length=50),
        ),
    ]