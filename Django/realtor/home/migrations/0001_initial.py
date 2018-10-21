# Generated by Django 2.1.2 on 2018-10-19 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Builder',
            fields=[
                ('email_id', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(blank=True, max_length=10, null=True)),
                ('office_address', models.CharField(max_length=100)),
                ('builder_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'builder',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Buyers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_id', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'buyers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Develop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completion_date', models.DateField()),
            ],
            options={
                'db_table': 'develop',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HomeBuyers',
            fields=[
                ('email_id', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('buyer_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'home_buyers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Land',
            fields=[
                ('price', models.FloatField()),
                ('size', models.FloatField()),
                ('address', models.CharField(max_length=100)),
                ('land_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'land',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Landlords',
            fields=[
                ('email_id', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(max_length=100)),
                ('landlord_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'landlords',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('description', models.CharField(blank=True, max_length=10000, null=True)),
                ('name', models.CharField(max_length=100)),
                ('number_of_bedrooms', models.IntegerField()),
                ('project_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('price', models.FloatField()),
                ('address', models.CharField(max_length=100)),
                ('size', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'project',
                'managed': False,
            },
        ),
    ]