# Generated by Django 5.0.3 on 2024-03-19 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0004_alter_post_number_of_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_user',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]