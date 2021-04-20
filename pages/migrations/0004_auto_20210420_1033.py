# Generated by Django 3.2 on 2021-04-20 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_friendrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendrequest',
            name='from_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coming_from_profile', to='pages.profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='user.png', null=True, upload_to='photos/%Y/%m'),
        ),
    ]
