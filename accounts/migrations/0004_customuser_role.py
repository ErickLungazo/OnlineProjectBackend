# Generated by Django 5.1.3 on 2024-11-15 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_customuser_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('superadmin', 'Superadmin'), ('admin', 'Admin'), ('lecturer', 'Lecturer'), ('student', 'Student')], default='student', max_length=20),
        ),
    ]
