# Generated by Django 5.0.6 on 2024-06-05 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_order_book_select_book_and_place_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order_book',
            old_name='Select_Book_and_Place_Order',
            new_name='Select_Book',
        ),
        migrations.AddField(
            model_name='order_book',
            name='Select_Quantity',
            field=models.CharField(choices=[('01', '1'), ('02', '2'), ('03', '3'), ('04', '4'), ('05', '5'), ('06', '6'), ('07', '7'), ('08', '8')], default='01', max_length=2),
        ),
    ]
