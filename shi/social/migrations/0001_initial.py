# Generated by Django 5.1.3 on 2024-11-28 22:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('media', '0002_remove_media_name_af_remove_media_name_ar_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('name_en', models.CharField(max_length=255, null=True)),
                ('name_az', models.CharField(max_length=255, null=True)),
                ('name_ru', models.CharField(max_length=255, null=True)),
                ('icon', models.ForeignKey(blank=True, limit_choices_to={'type': 'icon'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='social_media_icons', to='media.media')),
            ],
        ),
    ]
