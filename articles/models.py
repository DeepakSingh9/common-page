# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    describe=models.CharField(max_length=200)
    title=models.CharField(max_length=200,blank=True,null=True)
    publish=models.DateTimeField(default=timezone.now())
    link=models.URLField(max_length=200)
    name=models.ForeignKey(User)

    def __str__(self):
        return self.link

    class Meta:
        ordering=('-publish',)


