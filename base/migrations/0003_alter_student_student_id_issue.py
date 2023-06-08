# Generated by Django 4.0.3 on 2023-05-28 05:22

import base.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_student_phone_number_delete_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(max_length=64, primary_key=True, serialize=False, unique=True),
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateField(auto_now_add=True)),
                ('expiry_date', models.DateField(default=base.models.expiry)),
                ('fine', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('status', models.CharField(choices=[('issued', 'Issued'), ('returned', 'Returned')], default='issued', max_length=10)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='base.book')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='base.student')),
            ],
        ),
    ]
