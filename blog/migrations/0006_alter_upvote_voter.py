# Generated by Django 4.0.1 on 2022-01-11 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_upvote_remove_post_upvote_delete_vote_upvote_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upvote',
            name='voter',
            field=models.IntegerField(),
        ),
    ]
