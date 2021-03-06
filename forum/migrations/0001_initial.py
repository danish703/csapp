# Generated by Django 3.0.2 on 2020-06-05 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_image_url', models.ImageField(blank=True, null=True, upload_to='')),
                ('post_status', models.TextField()),
                ('posted_by_userId', models.CharField(max_length=255)),
                ('posted_by_semester', models.CharField(max_length=15)),
                ('posted_by_userImage', models.CharField(blank=True, max_length=255, null=True, verbose_name='Image url')),
                ('posted_by_username', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('comment_user_id', models.CharField(max_length=255)),
                ('comment_user_photo', models.CharField(blank=True, max_length=255, null=True, verbose_name='Image url')),
                ('comment_username', models.CharField(max_length=255, verbose_name='username')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Post')),
            ],
        ),
    ]
