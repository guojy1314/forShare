from django.db import models

# Create your models here.


class User(models.Model):

    gender = (
        ('male', '男'),
        ('female', '女'),
    )
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    wxopenid = models.CharField(db_column='wxOpenid', max_length=25, blank=True, null=True)
    create_time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'user'
