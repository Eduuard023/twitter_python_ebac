# Generated by Django 5.0.6 on 2024-05-27 19:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("twitter", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tweet",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AddField(
            model_name="tweet",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="tweet_like", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="tweet",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="tweets",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="tweet",
            name="deadline",
            field=models.DateTimeField(verbose_name="Data de entrega"),
        ),
        migrations.AlterField(
            model_name="tweet",
            name="title",
            field=models.CharField(max_length=100, verbose_name="Escreva aqui"),
        ),
    ]