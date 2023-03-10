# Generated by Django 4.1.7 on 2023-03-10 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0004_feed_remove_post_author_remove_post_likes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='shares',
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField()),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feeds.feed')),
            ],
        ),
    ]
