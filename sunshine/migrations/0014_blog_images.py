
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunshine', '0013_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='images',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
