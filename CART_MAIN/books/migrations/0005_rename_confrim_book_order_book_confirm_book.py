# Generated by Django 5.0.6 on 2024-06-06 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_order_book_confrim_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order_book',
            old_name='Confrim_book',
            new_name='Confirm_book',
        ),
    ]
