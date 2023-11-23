# Generated by Django 4.2.6 on 2023-11-17 10:10

from django.db import migrations, models
from cvat.apps.engine.models import Location


def manually_remove_outdated_relations(apps, schema_editor):
    Storage = apps.get_model("engine", "Storage")
    CloudStorage = apps.get_model("engine", "CloudStorage")
    Storage.objects.filter(location=Location.LOCAL, cloud_storage_id__isnull=False).update(cloud_storage_id=None)
    Storage.objects.filter(
        ~models.Exists(
            CloudStorage.objects.filter(pk=models.OuterRef("cloud_storage_id"))
        ),
        location=Location.CLOUD_STORAGE,
    ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("engine", "0075_annotationguide_is_public"),
    ]

    operations = [
        migrations.RunPython(manually_remove_outdated_relations),
    ]