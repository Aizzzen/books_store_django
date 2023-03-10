# Generated by Django 4.1.5 on 2023-01-13 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0003_books_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBookRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False)),
                ('in_bookmarks', models.BooleanField(default=False)),
                ('rate', models.PositiveSmallIntegerField(choices=[(1, 'Ok'), (2, 'Not bad'), (3, 'Good'), (4, 'Amazing'), (5, 'Incredible')])),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.books')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
