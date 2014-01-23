# -*- coding: utf-8 -*-
from django.db import models


class Estado(models.Model):
    estado = models.CharField(max_length=50)

    def __unicode__(self):
        return self.estado

    class Meta:
        verbose_name = u'Estado'
        verbose_name_plural = u'Estados'