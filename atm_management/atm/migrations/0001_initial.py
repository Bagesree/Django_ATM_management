# Generated by Django 4.1.7 on 2023-03-23 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('IFSC', models.CharField(max_length=250)),
                ('Ac_NO', models.IntegerField(default=None, primary_key=True, serialize=False)),
                ('Ac_type', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=150)),
                ('Balance', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('IFSC', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('Branch_Name', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ac_NO', models.IntegerField(default=None)),
                ('Date_and_time', models.DateTimeField(auto_now_add=True)),
                ('Debit', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('Credit', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('Balance', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
            ],
        ),
    ]
