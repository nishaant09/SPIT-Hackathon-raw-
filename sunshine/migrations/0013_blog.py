
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunshine', '0012_auto_20191114_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True)),
                ('author', models.CharField(max_length=32)),
                ('content', models.TextField()),
                ('slug', models.SlugField(max_length=128)),
                ('updated_on', models.DateField(auto_now=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('publish_on', models.DateField()),
            ],
        ),
    ]
