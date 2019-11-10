# Generated by Django 2.0.6 on 2019-11-08 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_admin_sex'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('salary', models.SmallIntegerField()),
                ('age', models.SmallIntegerField()),
                ('head', models.FileField(upload_to='imgs')),
            ],
        ),
    ]