# Generated by Django 3.2.5 on 2021-07-04 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_alter_user_activation_key_expires'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='vksite',
            field=models.CharField(blank=True, max_length=128, verbose_name='vk url'),
        ),
    ]