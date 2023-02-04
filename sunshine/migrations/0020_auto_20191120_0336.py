
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunshine', '0019_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='Audio',
            field=models.FileField(max_length=254, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='media',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
