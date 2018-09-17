# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class vreg(models.Model):

    name = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    city = models.CharField(max_length=200)
    types = models.TextField()
