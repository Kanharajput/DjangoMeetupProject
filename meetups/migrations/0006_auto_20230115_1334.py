# Generated by Django 3.2.16 on 2023-01-15 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0005_alter_meetup_participants'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterModelOptions(
            name='participants',
            options={'verbose_name_plural': 'Participants'},
        ),
        migrations.AddField(
            model_name='meetup',
            name='organizer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='meetups.organizer'),
        ),
    ]
