# Generated by Django 5.0.4 on 2024-05-31 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0002_registration_db'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(blank=True, max_length=100, null=True)),
                ('Product_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Total_Price', models.IntegerField(blank=True, null=True)),
                ('Quantity', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]