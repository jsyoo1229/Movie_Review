# Generated by Django 5.0.3 on 2024-03-12 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_comment_email_comment_website_alter_post_file_upload_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genres',
        ),
        migrations.AddField(
            model_name='post',
            name='overview',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='poster_path',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='release_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='trailer_url',
            field=models.URLField(null=True),
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]