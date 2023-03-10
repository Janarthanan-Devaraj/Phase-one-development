# Generated by Django 4.1.7 on 2023-03-07 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_profile_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicsinfo',
            name='department',
            field=models.CharField(blank=True, choices=[('IT', 'Information Technology'), ('CSE', 'Computer Science and Engineering'), ('ECE', 'Electronics and Communication Engineering'), ('ME', 'Mechanical Engineering'), ('CE', 'Civil Engineering')], max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_cover',
            field=models.ImageField(blank=True, default='profile-cover/default-profile-cover.jpg', null=True, upload_to='profile-cover'),
        ),
    ]
