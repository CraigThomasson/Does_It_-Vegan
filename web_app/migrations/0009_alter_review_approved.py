# Generated by Django 3.2 on 2022-04-25 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0008_dish_posted_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='approved',
            field=models.CharField(choices=[('approved', 'Apprroved'), ('not approved', 'Not Approved')], default='not approved', max_length=100),
        ),
    ]