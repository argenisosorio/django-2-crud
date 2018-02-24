# -*- coding: utf-8 -*-
from django.db import models


class Person(models.Model):
    """
    Class that manages the person model fields
    """
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name
