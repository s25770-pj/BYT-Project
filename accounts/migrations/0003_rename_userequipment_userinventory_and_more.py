# Generated by Django 5.0.1 on 2024-01-29 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserEquipment',
            new_name='UserInventory',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='equipment',
            new_name='inventory',
        ),
    ]