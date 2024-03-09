# Generated by Django 5.0.3 on 2024-03-08 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='book_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='sale',
            name='number_of_books',
            field=models.IntegerField(default=0),
        ),
    ]