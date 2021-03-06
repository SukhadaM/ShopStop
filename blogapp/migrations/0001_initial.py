# Generated by Django 3.1.3 on 2021-04-18 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('blog_title', models.CharField(max_length=20)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('category1', models.IntegerField(choices=[(0, 'None'), (1, 'Creative'), (2, 'Design'), (3, 'News'), (4, 'Photography'), (5, 'Corporate')], default=0)),
                ('about_keyword1', models.CharField(max_length=20, null=True)),
                ('about_keyword2', models.CharField(max_length=20, null=True)),
                ('about_keyword3', models.CharField(max_length=20, null=True)),
                ('blog', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_name', models.CharField(max_length=20)),
                ('comment_text', models.TextField()),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.blogmodel')),
            ],
        ),
    ]
