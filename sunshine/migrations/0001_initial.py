
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('body', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='carousels')),
                ('slug', models.SlugField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventname', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('eventinfo', models.CharField(max_length=850, null=True)),
                ('coodinator', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Head',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leader', models.CharField(max_length=70, null=True)),
                ('department', models.CharField(max_length=100)),
                ('departmentaim', models.CharField(max_length=100)),
            ],
        ),
    ]
