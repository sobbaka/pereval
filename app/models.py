from django.db import models


class PerevalAdded(models.Model):
    date_added = models.DateTimeField()
    raw_data = models.TextField()  # This field type is a guess. JSON
    images = models.TextField()  # This field type is a guess. M2M

    class Meta:
        managed = False
        db_table = 'pereval_added'


class PerevalImages(models.Model):
    date_added = models.DateTimeField(blank=True, null=True)
    img = models.TextField(blank=True, null=True) # URL

    class Meta:
        managed = False
        db_table = 'pereval_images'


class PerevalAreas(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_parent = models.BigIntegerField()
    title = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pereval_areas'


class SprActivitiesTypes(models.Model):
    title = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spr_activities_types'
