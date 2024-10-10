# Generated by Django 5.0.1 on 2024-03-02 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fullname', models.CharField(max_length=25)),
                ('Email', models.EmailField(max_length=254)),
                ('Gender', models.CharField(max_length=25)),
                ('Phonenumer', models.CharField(max_length=12)),
                ('DOB', models.CharField(max_length=50)),
                ('Selectmembershipplan', models.CharField(max_length=55)),
                ('Selecttrainer', models.CharField(max_length=55)),
                ('Reference', models.CharField(max_length=55)),
                ('Address', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MembershipPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(max_length=185)),
                ('price', models.IntegerField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('gender', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=25)),
                ('salary', models.IntegerField(max_length=25)),
            ],
        ),
    ]