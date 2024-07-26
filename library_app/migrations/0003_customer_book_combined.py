# Generated by Django 5.0.3 on 2024-04-16 17:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0002_delete_customer_book_combined'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Book_Combined',
            fields=[
                ('customer_book_id', models.AutoField(primary_key=True, serialize=False)),
                ('book_issuance_date', models.DateField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.book')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.customer_library')),
            ],
        ),
    ]
