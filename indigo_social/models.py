# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=1024, help_text="A short bio")
    qualifications = models.TextField(max_length=512, help_text="Qualifications")
    skills = models.CharField(max_length=256, help_text="Skills")
    organisations = models.CharField(max_length=256, help_text="Organisation(s)")
    specialisations = models.CharField(max_length=256, help_text="Specialisation(s)")
    areas_of_law = models.CharField(max_length=256, help_text="Area(s) of law")
    profile_photo = models.ImageField()
    twitter_profile = models.URLField()
    linkedin_profile = models.URLField()

