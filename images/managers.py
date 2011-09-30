# portfolio/managers.py

from datetime import datetime

from django.db import models
from django.db.models.query import QuerySet

class ImageMixin(object):
    def public(self):
        return self.get_query_set().filter(public=True)

class ImageQuerySet(QuerySet, ProjectMixin):
    pass

class ImageManager(models.Manager, ProjectMixin):
    def get_query_set(self):
        return ProjectQuerySet(self.model, using=self._db)