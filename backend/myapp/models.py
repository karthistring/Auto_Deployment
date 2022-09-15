from django.db import models

class TblEmp(models.Model):
    name=models.CharField(max_length=255,blank=True)
    age=models.IntegerField(blank=True)

    class Meta:
        managed = True
        db_table = 'tbl_emp'


