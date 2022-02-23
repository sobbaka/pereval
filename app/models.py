# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class PerevalAdded(models.Model):
    date_added = models.DateTimeField(blank=True, null=True)
    raw_data = models.TextField(blank=True, null=True)  # This field type is a guess. JSON
    images = models.TextField(blank=True, null=True)  # This field type is a guess. M2M

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
