# Generated by Django 4.2.2 on 2023-07-03 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(null=True)),
                ('ref_id', models.CharField(max_length=50)),
                ('trn_type', models.CharField(max_length=50)),
                ('amount', models.IntegerField(null=True)),
                ('trn_date', models.DateField(null=True)),
                ('owner', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Uploads',
        ),
    ]
