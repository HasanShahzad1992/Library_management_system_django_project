# Generated by Django 5.0.3 on 2024-04-14 18:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=40)),
                ('author_name', models.CharField(max_length=35)),
                ('publishing_year', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Customer_Library',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=35)),
                ('age', models.IntegerField()),
                ('cnic', models.CharField(max_length=20)),
            ],
        ),
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
