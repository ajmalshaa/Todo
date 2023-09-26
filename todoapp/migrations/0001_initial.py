# Generated by Django 4.2.4 on 2023-09-02 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Task', models.CharField(max_length=500)),
                ('Date', models.DateTimeField()),
                ('IsActive', models.IntegerField()),
            ],
        ),
    ]
