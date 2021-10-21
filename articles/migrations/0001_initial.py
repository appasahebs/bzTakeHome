# Generated by Django 3.2.8 on 2021-10-20 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('publish_date', models.CharField(max_length=255)),
                ('authors', models.CharField(max_length=255)),
                ('section', models.CharField(max_length=255)),
                ('tags', models.CharField(max_length=255)),
                ('sort', models.TextField()),
            ],
        ),
    ]