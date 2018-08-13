# Generated by Django 2.0.4 on 2018-08-13 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkId', models.CharField(max_length=32)),
            ],
        ),
        migrations.RenameField(
            model_name='feed',
            old_name='link',
            new_name='linkFile',
        ),
        migrations.AddField(
            model_name='link',
            name='parentFeed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Feed'),
        ),
    ]