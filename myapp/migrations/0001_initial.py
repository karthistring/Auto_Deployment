# Generated by Django 4.1.1 on 2022-09-15 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblEmp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('age', models.IntegerField(blank=True)),
            ],
            options={
                'db_table': 'tbl_emp',
                'managed': True,
            },
        ),
    ]