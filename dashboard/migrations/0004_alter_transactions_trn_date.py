# Generated by Django 4.2.2 on 2023-06-28 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_transactions_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='trn_date',
            field=models.DateField(null=True),
        ),
    ]
