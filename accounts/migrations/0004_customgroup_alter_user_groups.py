# Generated by Django 4.2.5 on 2023-10-08 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0003_alter_user_groups_alter_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True, verbose_name='Name')),
                ('permissions', models.ManyToManyField(blank=True, related_name='custom_group_set', related_query_name='group', to='auth.permission', verbose_name='Uprawnienia')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='custom_user_set', related_query_name='user', to='accounts.customgroup', verbose_name='Grupy'),
        ),
    ]
