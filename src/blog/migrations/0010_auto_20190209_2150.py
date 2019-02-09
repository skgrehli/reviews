# Generated by Django 2.1.5 on 2019-02-09 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_userreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.STAR_RATINGS_RATING_MODEL),
        ),
    ]