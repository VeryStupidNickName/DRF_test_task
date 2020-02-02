# Generated by Django 3.0.2 on 2020-02-01 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadmodel',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='uploadmodel',
            name='date',
        ),
        migrations.RemoveField(
            model_name='uploadmodel',
            name='item',
        ),
        migrations.RemoveField(
            model_name='uploadmodel',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='uploadmodel',
            name='total',
        ),
        migrations.AddField(
            model_name='uploadmodel',
            name='choice',
            field=models.FileField(default=0, upload_to='uploads/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploadmodel',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='DealsModel',
            fields=[
                ('total', models.IntegerField(null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('date', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Customer')),
                ('item', models.ManyToManyField(to='app.Gem')),
            ],
        ),
    ]
