# Generated by Django 4.2.5 on 2023-10-31 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_mynotes_comments_alter_mynotes_file_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=20)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('msg', models.TextField()),
            ],
        ),
    ]
