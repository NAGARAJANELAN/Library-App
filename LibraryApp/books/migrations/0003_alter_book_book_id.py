# Generated by Django 5.0 on 2023-12-08 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_remove_book_id_alter_book_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
