# Generated by Django 4.1.5 on 2023-01-13 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='author',
            field=models.CharField(default='Author', max_length=255),
            preserve_default=False,
        ),
    ]