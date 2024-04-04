# Generated by Django 5.0.1 on 2024-04-01 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_test',
            name='test_status',
            field=models.CharField(default=0, max_length=25),
        ),
        migrations.AlterField(
            model_name='tbl_test',
            name='test_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='tbl_test',
            name='test_end_time',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='tbl_test',
            name='test_score',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='tbl_test',
            name='test_start_time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]