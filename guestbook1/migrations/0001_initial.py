# Generated by Django 3.0.3 on 2020-05-01 02:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog_v2', '0002_auto_20200420_0818'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Visitors', max_length=15)),
                ('email', models.EmailField(blank=True, default='', max_length=254)),
                ('text', models.TextField()),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comment', to='blog_v2.Post')),
            ],
            options={
                'db_table': 'Comment_1',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Comment_reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Visitors', max_length=15)),
                ('email', models.EmailField(blank=True, default='', max_length=254)),
                ('text', models.TextField()),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_reply', to='guestbook1.Comment')),
            ],
            options={
                'db_table': 'Comment_reply_1',
                'ordering': ['-create_time'],
            },
        ),
    ]