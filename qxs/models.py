# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class QianxuesenQianxuesenChengji(models.Model):
    st_id = models.CharField(max_length=200, blank=True, null=True)
    st_name = models.CharField(max_length=200, blank=True, null=True)
    class_num = models.IntegerField(blank=True, null=True)
    cl_name = models.CharField(max_length=200, blank=True, null=True)
    cl_credit = models.CharField(max_length=200, blank=True, null=True)
    cl_performance = models.CharField(max_length=200, blank=True, null=True)
    cl_type = models.CharField(max_length=200, blank=True, null=True)
    cl_attribute = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qianxuesen_qianxuesen_chengji'


class QianxuesenQianxuesenKebiao(models.Model):
    cl_school = models.CharField(max_length=100, blank=True, null=True)
    cl_cid = models.CharField(max_length=100, blank=True, null=True)
    cl_id = models.CharField(max_length=100, blank=True, null=True)
    teacher_id = models.CharField(max_length=100, blank=True, null=True)
    teacher = models.CharField(max_length=100, blank=True, null=True)
    teacher_title = models.CharField(max_length=100, blank=True, null=True)
    teacher_school = models.CharField(max_length=100, blank=True, null=True)
    cl_name = models.CharField(max_length=100, blank=True, null=True)
    st_class = models.CharField(max_length=500, blank=True, null=True)
    cl_credit = models.FloatField(blank=True, null=True)
    classroom = models.CharField(max_length=100, blank=True, null=True)
    cl_date = models.CharField(max_length=100, blank=True, null=True)
    jieci_1 = models.CharField(max_length=100, blank=True, null=True)
    jieci_2 = models.CharField(max_length=100, blank=True, null=True)
    jieci_3 = models.CharField(max_length=100, blank=True, null=True)
    jieci_4 = models.CharField(max_length=100, blank=True, null=True)
    jieci_5 = models.CharField(max_length=100, blank=True, null=True)
    jieci_6 = models.CharField(max_length=100, blank=True, null=True)
    jieci_7 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qianxuesen_qianxuesen_kebiao'


class QianxuesenQianxuesenProject19(models.Model):
    st_id = models.CharField(max_length=30, blank=True, null=True)
    st_name = models.CharField(max_length=30, blank=True, null=True)
    st_school = models.CharField(max_length=30, blank=True, null=True)
    st_major = models.CharField(max_length=30, blank=True, null=True)
    major_2 = models.CharField(max_length=30, blank=True, null=True)
    st_class = models.CharField(max_length=30, blank=True, null=True)
    st_grade = models.CharField(max_length=30, blank=True, null=True)
    schoolyear = models.CharField(max_length=30, blank=True, null=True)
    cl_cid = models.CharField(max_length=30, blank=True, null=True)
    cl_name = models.CharField(max_length=30, blank=True, null=True)
    cl_credit = models.FloatField(blank=True, null=True)
    cl_type = models.CharField(max_length=30, blank=True, null=True)
    cl_attribute = models.CharField(max_length=30, blank=True, null=True)
    cl_school = models.CharField(max_length=30, blank=True, null=True)
    cl_lanuage = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qianxuesen_qianxuesen_project19'


class QianxuesenQianxuesenQianxuesen(models.Model):
    st_id = models.CharField(max_length=20)
    st_name = models.CharField(max_length=20)
    st_school = models.CharField(max_length=20)
    st_class = models.CharField(max_length=20)
    cl_name = models.CharField(max_length=30)
    cl_cid = models.CharField(max_length=30)
    cl_credit = models.FloatField()
    cl_id = models.CharField(max_length=20)
    teacher = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'qianxuesen_qianxuesen_qianxuesen'


class QianxuesenQianxuesenQianxuesenst(models.Model):
    st_id = models.CharField(max_length=200, blank=True, null=True)
    st_major = models.CharField(max_length=200, blank=True, null=True)
    major_2 = models.CharField(max_length=200, blank=True, null=True)
    st_grade = models.CharField(max_length=200, blank=True, null=True)
    st_name = models.CharField(max_length=200, blank=True, null=True)
    st_class = models.CharField(max_length=200, blank=True, null=True)
    st_school = models.CharField(max_length=200, blank=True, null=True)
    total_credit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qianxuesen_qianxuesen_qianxuesenst'


class QxsTeaRate(models.Model):
    id = models.BigAutoField(primary_key=True)
    cl_name = models.CharField(max_length=30)
    cl_cid = models.CharField(max_length=30)
    cl_id = models.CharField(max_length=30)
    teacher = models.CharField(max_length=20)
    point = models.IntegerField()
    adv = models.CharField(max_length=300, blank=True, null=True)
    st_id = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qxs_tea_rate'


class QxsUsers(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    role = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'qxs_users'

class QxsRatedetils(models.Model):
    id = models.IntegerField(primary_key=True)
    cl_school = models.CharField(max_length=100, blank=True, null=True)
    cl_cid = models.CharField(max_length=100, blank=True, null=True)
    cl_id = models.CharField(max_length=100, blank=True, null=True)
    teacher_id = models.CharField(max_length=100, blank=True, null=True)
    teacher = models.CharField(max_length=100, blank=True, null=True)
    cl_name = models.CharField(max_length=100, blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)
    nopass = models.IntegerField(blank=True, null=True)
    passed = models.IntegerField(blank=True, null=True)
    common = models.IntegerField(blank=True, null=True)
    good = models.IntegerField(blank=True, null=True)
    excellent = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qxs_ratedetils'
