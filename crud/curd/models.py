# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Register(models.Model):
    eid = models.CharField(max_length=10)
    ename = models.CharField(max_length=20)
    eaddress = models.CharField(max_length=30)
